"""
学习调度器

回答三个问题：**先学什么**、**学到哪了**、**哪些学不了**。

    WorkflowScanner  扫描目录
          ↓
    LearningScheduler.build_schedule()
          ├─ 查 LearningStore（按 key + 内容指纹）跳过已学
          ├─ 读每个 workflow 的节点清单
          ├─ PriorityCalculator 打分（内容信号为主，文件名为辅）
          └─ TaskQueue（优先级降序，同分保持加入顺序）
          ↓
    LearningScheduler.run()
          └─ 循环取任务 → WorkflowLearner.learn() → 记录状态
          ↓
    ScheduleStore  队列落盘（可续跑）

与既有模块的分工：
    workflow_learning.LearningStore  记录「学没学过 / 学到了什么」
    workflow_learning.WorkflowLearner 执行单文件学习
    learning_scheduler               **只管排队与状态**，不重复实现学习逻辑

与设计稿的三处修正：

1. `registry.exists(wf["name"])` → `store.exists(key, content_hash)`。
   用文件名会漏掉内容变更（改了参数永远不重学），
   也无法区分不同目录下的同名文件。

2. 补上执行循环。设计稿只有 build_schedule，
   第 11 节流程里的「Queue → Learner」没有代码。

3. 重试有上限。永久损坏的文件重试再多遍也不会成功，
   不隔离的话队列会永远卡在同一批文件上。
"""

import time
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Callable

from .models import (
    LearningTask,
    STATUS_PENDING,
    STATUS_COMPLETED,
    STATUS_FAILED,
    STATUS_ABANDONED,
)
from .task_queue import TaskQueue
from .priority import PriorityCalculator
from .scheduler_state import SchedulerState
from .schedule_store import ScheduleStore
from ..workflow_learning import LearningStore
from ..workflow_learning.paths import WORKFLOWS_DIR, relative_to_project


class LearningScheduler:
    """
    工作流学习调度器
    """

    def __init__(
        self,
        scanner=None,
        store=None,
        priority=None,
        queue=None,
        learner=None,
        schedule_store=None,
        max_retries: int = 3
    ) -> None:
        """
        初始化调度器

        Args:
            scanner: WorkflowScanner
            store: workflow_learning.LearningStore（判断是否已学）
            priority: PriorityCalculator
            queue: TaskQueue
            learner: WorkflowLearner（执行学习）；
                     不传则只能 build_schedule，不能 run
            schedule_store: ScheduleStore（队列持久化）
            max_retries: 单任务重试上限
        """
        from ..workflow_learning import WorkflowScanner

        # 一律用 `is None` 判断，不用 `or`。
        # TaskQueue 定义了 __len__，空队列是 falsy —— `queue or TaskQueue(...)`
        # 会把调用方传进来的队列连同 max_retries 一起悄悄顶掉，
        # 表现为「重试上限怎么设都不生效」。
        self.scanner = (
            scanner if scanner is not None
            else WorkflowScanner()
        )
        self.store = store if store is not None else LearningStore()
        self.queue = (
            queue if queue is not None
            else TaskQueue(max_retries=max_retries)
        )
        self.learner = learner
        self.schedule_store = (
            schedule_store if schedule_store is not None
            else ScheduleStore()
        )
        self.max_retries = max_retries

        # 「哪些节点已有知识卡」取自 node_index.json ——
        # 它精确列出了写过卡的节点，是判断知识缺口的权威依据
        self.priority = (
            priority if priority is not None
            else PriorityCalculator(
                known_node_types=self._known_card_nodes()
            )
        )

    # ---------- 建计划 ----------

    def build_schedule(
        self,
        folder: str = None,
        include_learned: bool = False,
        refresh_learner: Callable = None
    ) -> List[LearningTask]:
        """
        扫描目录并生成学习队列

        Args:
            folder: 目录；None 时用 comfyui_library/workflows/
            include_learned: 是否把已学的也放进队列（默认跳过）
            refresh_learner: 可选的钩子，在扫描后调用（如刷新检索索引）

        Returns:
            按优先级排序的任务列表
        """
        if folder is None:
            folder = WORKFLOWS_DIR

        if refresh_learner is not None:
            refresh_learner()

        files = self.scanner.scan(str(folder))

        # 注意：这里**不能** queue.reset()。
        # 重复调用 build_schedule（每次 run 都会调）是常态，
        # 清空会把 retry_count、last_error 等历史一起丢掉 ——
        # 永久失败的文件会因此被无限重试。
        # 正确做法是合并：保留已有任务的状态，只增删差异。
        self.queue.retain_keys({f["key"] for f in files})

        # 已学过的节点类型，用于算「新颖度」
        known_node_types = self._known_node_types()
        self.priority.known_node_types = known_node_types

        for item in files:
            key = item["key"]
            path = item["path"]

            content_hash = self._peek_hash(path)
            already = self.store.exists(key, content_hash)

            # 已学且内容未变 → 跳过
            if already and not include_learned:
                continue

            nodes = self._read_nodes(path)

            # 内容变了是更明确的学习需求，重试次数不继承
            previous = self.queue.find(key)
            retry_count = 0

            scored = self.priority.calculate(
                item,
                nodes=nodes,
                retry_count=retry_count,
                content_changed=already is False and content_hash != "",
            )

            task = LearningTask(
                workflow_path=path,
                workflow_name=item["name"],
                key=key,
                priority=scored["score"],
                status=STATUS_PENDING,
                priority_reasons=scored["reasons"],
                node_count=scored["node_count"],
                unknown_node_count=scored["unknown_node_count"],
                content_hash=content_hash,
            )

            self.queue.add(task)

        return self.ordered_tasks()

    def ordered_tasks(self) -> List[LearningTask]:
        """
        按调度顺序返回任务（优先级降序，同分保持加入顺序）
        """
        return sorted(self.queue.tasks, key=lambda t: -t.priority)

    def plan(
        self,
        folder: str = None
    ) -> List[Dict]:
        """
        生成可读的学习计划（对应设计稿第十节的输出形式）

        Args:
            folder: 目录

        Returns:
            [{"name", "key", "priority", "status", "reasons"}]
        """
        tasks = self.build_schedule(folder)

        return [
            {
                "name": t.workflow_name,
                "key": t.key,
                "priority": t.priority,
                "status": t.status,
                "reasons": t.priority_reasons,
            }
            for t in tasks
        ]

    # ---------- 执行 ----------

    def run(
        self,
        folder: str = None,
        limit: int = 0,
        save: bool = True
    ) -> SchedulerState:
        """
        执行队列

        Args:
            folder: 目录；None 时用默认
            limit: 最多执行多少个任务；0 表示不限
            save: 是否把队列状态落盘

        Returns:
            SchedulerState
        """
        if self.learner is None:
            raise RuntimeError(
                "未注入 learner，无法执行。"
                "只做调度请用 build_schedule()"
            )

        if folder is not None:
            self.build_schedule(folder)
        elif not self.queue.tasks:
            # 既没给目录也没建过计划 —— 建一次
            self.build_schedule()

        started = time.perf_counter()
        current = ""

        processed = 0
        # 一次 run 只对每个任务尝试一遍。
        # 若在这里就把失败任务重试到耗尽，一个坏文件会占掉全部
        # max_retries 并立刻转 abandoned —— 重试本该发生在多次 run 之间，
        # 给的是「稍后重试」的机会，而不是同一轮里连打三次。
        attempted = set()

        while True:
            if limit and processed >= limit:
                break

            # 排除本轮已尝试的任务：必须在 pop_next 之前过滤，
            # 否则 pop_next 会把刚失败的任务重新标记成 running，
            # 任务就卡在 running 状态了
            task = self.queue.pop_next(exclude=attempted)
            if task is None:
                break

            attempted.add(task.key)
            current = task.workflow_name
            processed += 1

            try:
                record = self.learner.learn(
                    task.workflow_path, key=task.key
                )

                if record.status == STATUS_COMPLETED:
                    # 记录落盘由 LearningStore 负责，这里只更新任务状态。
                    # 队列文件不写 LearningStore 避免两个存储互相污染 ——
                    # 真正的知识以 LearningStore 为准。
                    path = self.store.write(record)
                    self.queue.complete(
                        task,
                        result=relative_to_project(record.key),
                    )
                    if path:
                        task.result = relative_to_project(path)
                else:
                    self.queue.fail(task, record.error or "学习失败")

            except Exception as e:
                # 单个任务异常不能中断整批 —— 否则一个坏文件
                # 会让剩下的文件永远排不上
                self.queue.fail(
                    task, f"{type(e).__name__}: {e}"
                )

        state = SchedulerState.from_queue(
            self.queue,
            current_task=current,
            elapsed_ms=(time.perf_counter() - started) * 1000,
        )
        state.finished_at = _now()

        if save:
            self.schedule_store.save(
                self.queue.tasks, state,
                folder=relative_to_project(
                    folder or WORKFLOWS_DIR
                ),
            )

        return state


    def resume(
        self,
        folder: str = None
    ) -> SchedulerState:
        """
        续跑：读回上次的队列，从中断处继续

        重试次数从落盘记录里恢复 —— 这是设计稿里漏掉的：
        不恢复的话重试计数归零，永久失败的文件会被无限重试。

        Args:
            folder: 目录

        Returns:
            SchedulerState
        """
        saved = self.schedule_store.load()

        if not saved:
            return self.run(folder)

        # 恢复任务，保留重试历史
        for task in saved:
            fresh = LearningTask(
                workflow_path=self._path_of(task.key, folder),
                workflow_name=task.workflow_name,
                key=task.key,
                priority=task.priority,
                status=task.status,
                retry_count=task.retry_count,
                last_error=task.last_error,
                node_count=task.node_count,
                unknown_node_count=task.unknown_node_count,
                priority_reasons=task.priority_reasons,
            )
            self.queue.add(fresh)

        return self.run(folder, save=True)

    # ---------- 查询 ----------

    def progress(self) -> SchedulerState:
        """
        当前进度（不执行）
        """
        return SchedulerState.from_queue(self.queue)

    def pending(self, folder: str = None) -> List[Dict]:
        """
        哪些还没学（含需要重学的）
        """
        tasks = self.build_schedule(folder)

        return [
            {"key": t.key, "priority": t.priority,
             "reasons": t.priority_reasons}
            for t in tasks
        ]

    def abandoned(self) -> Dict[str, str]:
        """
        放弃的任务与原因（需人工处理）
        """
        return self.queue.abandoned_reasons()

    def render_plan(self, folder: str = None) -> str:
        """
        渲染可读的学习计划
        """
        tasks = self.build_schedule(folder)

        if not tasks:
            return (
                "没有待学习的 workflow —— "
                "要么都学过了，要么目录为空"
            )

        lines = [
            f"学习计划（{len(tasks)} 个待学）：",
            "",
        ]

        for i, task in enumerate(tasks, 1):
            lines.append(
                f"{i}. {task.key}（{task.priority} 分）"
            )
            for reason in task.priority_reasons:
                lines.append(f"     - {reason}")

        return "\n".join(lines)

    # ---------- 内部 ----------

    def _read_nodes(self, path: str) -> List[str]:
        """
        读 workflow 的节点清单（只为算优先级，尽量轻量）

        失败返回空列表 —— 读不了不该阻塞建计划，
        该文件会在真正执行时报错并计入失败。
        """
        path_obj = Path(path)

        try:
            if path_obj.suffix.lower() == ".png":
                from ..workflow_learning import load_png_workflow
                data = load_png_workflow(path) or {}
            else:
                with open(
                    path_obj, "r", encoding="utf-8-sig"
                ) as f:
                    data = json.load(f)
        except Exception:
            return []

        if not isinstance(data, dict):
            return []

        return [
            n.get("type", "") for n in data.get("nodes", [])
            if isinstance(n, dict) and n.get("type")
        ]

    def _known_card_nodes(self) -> set:
        """
        已有知识卡的节点类型集合

        读 comfyui_library/knowledge/node_index.json ——
        它的键就是写过卡的节点类型（如 KSampler、VAEDecode）。
        读不到就返回空集（此时不做缺口加权，只按节点数排序）。
        """
        from ..workflow_learning.paths import PROJECT_ROOT

        index_file = (
            PROJECT_ROOT / "comfyui_library" / "knowledge"
            / "node_index.json"
        )

        if not index_file.exists():
            return set()

        try:
            with open(
                index_file, "r", encoding="utf-8-sig"
            ) as f:
                data = json.load(f)
            return set(data.get("nodes", {}).keys())
        except Exception:
            return set()

    def _known_node_types(self) -> set:
        """
        已学过的节点类型集合（用于新颖度）
        """
        types = set()

        for record in self.store.completed_records():
            types.update(record.nodes)

        return types

    @staticmethod
    def _peek_hash(path: str) -> str:
        """
        取文件指纹
        """
        try:
            from ..workflow_learning import WorkflowLearner
            return WorkflowLearner._hash_file(Path(path))
        except Exception:
            return ""

    @staticmethod
    def _path_of(key: str, folder: str = None) -> str:
        """
        由 key 还原绝对路径（续跑时原文件仍在原处）
        """
        root = Path(folder or WORKFLOWS_DIR)
        return str(root / key)

    @staticmethod
    def _now() -> str:
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def build_scheduler(
    learner=None,
    folder: str = None,
    max_retries: int = 3,
    verbose: bool = True,
    **extra
) -> LearningScheduler:
    """
    便捷构造

    Args:
        learner: WorkflowLearner（不传则只能建计划不能执行）
        folder: 默认扫描目录
        max_retries: 重试上限
        verbose: run() 时是否打印进度
        **extra: scanner / store / priority / queue / schedule_store

    Returns:
        LearningScheduler 实例
    """
    scheduler = LearningScheduler(
        learner=learner,
        queue=TaskQueue(max_retries=max_retries),
        schedule_store=ScheduleStore(),
        **extra,
    )

    if verbose and learner is not None:
        # 包一层，打印每个任务的结果
        original = scheduler.learner.learn

        def logged(path, key=""):
            task = scheduler.queue.find(key)
            name = task.workflow_name if task else Path(path).stem
            print(f"  学习 {name} ...", end=" ")
            record = original(path, key=key)
            mark = "OK" if record.status == STATUS_COMPLETED else "FAIL"
            print(
                f"{mark}"
                + (f"（{len(record.nodes)} 节点）"
                   if record.status == STATUS_COMPLETED
                   else f"：{record.error}")
            )
            return record

        scheduler.learner.learn = logged

    return scheduler


def _now() -> str:
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
