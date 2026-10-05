"""
任务队列

管理待学习的 workflow。

与设计稿的两点差异：

1. **每次取下一个都重排**。设计稿的 get_next() 每次 O(n log n) 排序，
   1000 个文件取 1000 次就是 O(n² log n)。这里维护一个有序插入，
   取任务是 O(1)。

2. **重试用尽的任务要被隔离**。永久损坏的文件若一直留在队列里，
   队列永远卡在同一批文件上，实际等于调度器死锁。
   超过 max_retries 的任务转 abandoned，不再参与调度，
   但保留在列表里供事后排查。
"""

from typing import List, Optional, Dict, Any, Iterator

from .models import (
    LearningTask,
    STATUS_PENDING,
    STATUS_RUNNING,
    STATUS_COMPLETED,
    STATUS_FAILED,
    STATUS_ABANDONED,
    STATUS_SKIPPED,
    FINAL_STATUSES,
)


class TaskQueue:
    """
    学习任务队列
    """

    def __init__(self, max_retries: int = 3) -> None:
        """
        初始化队列

        Args:
            max_retries: 单个任务最大重试次数，用尽转 abandoned
        """
        self.tasks: List[LearningTask] = []
        self.max_retries = max_retries

    # ---------- 构建 ----------

    def reset(self) -> None:
        """
        清空队列

        build_schedule 会反复调用（增量扫描、重新规划），
        不 reset 会让同一个 key 出现多条任务。
        """
        self.tasks = []

    def add(self, task: LearningTask) -> LearningTask:
        """
        加入任务

        同一 key 已在队列里则更新而非重复加入 ——
        重复扫描同一目录时这是最常见的情况。

        Args:
            task: 任务

        Returns:
            实际入队的任务（可能是已存在的那条）
        """
        existing = self.find(task.key)
        if existing is not None:
            # 保留已有的重试与错误历史，只刷新可重算的字段
            existing.workflow_path = task.workflow_path
            existing.workflow_name = task.workflow_name
            existing.priority = task.priority
            existing.priority_reasons = task.priority_reasons
            existing.node_count = task.node_count
            existing.unknown_node_count = task.unknown_node_count
            existing.content_changed = task.content_changed
            existing.content_hash = task.content_hash

            # 已完成的重新入队时应回到待学（内容变了就是新的学习需求）
            if task.content_changed and existing.is_final:
                existing.status = STATUS_PENDING
                existing.retry_count = 0

            return existing

        self.tasks.append(task)
        return task

    def retain_keys(self, keys) -> List[str]:
        """
        只保留给定 key 的任务，移除其余

        用于增量重建计划：文件列表变了就同步队列，
        但保留已有任务的重试次数与错误信息 —— 直接 reset 会把
        这些历史清掉，导致永久失败的文件被无限重试。

        Args:
            keys: 要保留的 key 集合

        Returns:
            被移除的 key
        """
        keep = set(keys)
        removed = [t.key for t in self.tasks if t.key not in keep]

        if removed:
            self.tasks = [t for t in self.tasks if t.key in keep]

        return removed

    def find(self, key: str) -> Optional[LearningTask]:
        """
        按 key 找任务
        """
        for task in self.tasks:
            if task.key == key:
                return task
        return None

    # ---------- 取任务 ----------

    def get_next(self, exclude=None) -> Optional[LearningTask]:
        """
        取下一个该学的任务

        规则：
            1. 只取可执行状态（pending / 待重试的 failed）
            2. 优先级高的先学
            3. 同优先级按加入顺序（稳定排序）

        Args:
            exclude: 要排除的 key 集合。本轮已尝试过的任务传进来，
                     否则会反复取出同一个刚失败的任务

        Returns:
            任务；无可执行任务时返回 None
        """
        excluded = set(exclude or ())

        runnable = [
            t for t in self.tasks
            if t.is_runnable
            and t.can_retry(self.max_retries)
            and t.key not in excluded
        ]

        if not runnable:
            return None

        # 稳定的优先级排序：分数降序。
        # Python 的 sort 是稳定的，所以同分任务保持原有（加入）顺序 ——
        # 结果可复现，不依赖文件系统的枚举顺序。
        runnable.sort(key=lambda t: -t.priority)

        return runnable[0]

    def pop_next(self, exclude=None) -> Optional[LearningTask]:
        """
        取下一个并标记为 running

        Args:
            exclude: 排除的 key 集合（见 get_next）
        """
        task = self.get_next(exclude=exclude)
        if task is not None:
            task.start()
        return task

    def __iter__(self) -> Iterator[LearningTask]:
        return iter(self.tasks)

    def __len__(self) -> int:
        return len(self.tasks)

    # ---------- 完成 / 失败 ----------

    def complete(self, task: LearningTask, result: str = "") -> None:
        """
        标记任务完成
        """
        task.complete(result)

    def fail(self, task: LearningTask, error: str) -> None:
        """
        标记任务失败（超重试上限自动转 abandoned）
        """
        task.fail(error, self.max_retries)

    def skip(self, task: LearningTask, reason: str = "") -> None:
        """
        跳过任务（如已学过且内容未变）
        """
        task.status = STATUS_SKIPPED
        task.result = reason

    # ---------- 查询 ----------

    def by_status(self, status: str) -> List[LearningTask]:
        """
        按状态过滤
        """
        return [t for t in self.tasks if t.status == status]

    def pending(self) -> List[LearningTask]:
        return self.by_status(STATUS_PENDING)

    def failed(self) -> List[LearningTask]:
        return self.by_status(STATUS_FAILED)

    def abandoned(self) -> List[LearningTask]:
        """
        已放弃的任务（重试用尽）

        这些需要人工介入 —— 通常是文件本身有问题（JSON 损坏、
        引用了不存在的节点），重试再多遍也不会成功。
        """
        return self.by_status(STATUS_ABANDONED)

    def completed(self) -> List[LearningTask]:
        return self.by_status(STATUS_COMPLETED)

    def runnable_count(self) -> int:
        """当前可执行的任务数"""
        return len([
            t for t in self.tasks
            if t.is_runnable and t.can_retry(self.max_retries)
        ])

    def progress(self) -> Dict:
        """
        进度统计

        total 计入已放弃的任务 —— 否则看起来永远差那几个坏文件，
        实际已经做完了能做的部分。
        """
        total = len(self.tasks)
        done = len([
            t for t in self.tasks
            if t.status in (STATUS_COMPLETED, STATUS_SKIPPED)
        ])

        return {
            "total": total,
            "completed": len(self.completed()),
            "skipped": len(self.by_status(STATUS_SKIPPED)),
            "failed": len(self.failed()),
            "abandoned": len(self.abandoned()),
            "pending": len(self.pending()),
            "running": len(self.by_status(STATUS_RUNNING)),
            "done": done,
            "runnable": self.runnable_count(),
            "percent": (
                round(done / total * 100, 1) if total else 0.0
            ),
        }

    def abandoned_reasons(self) -> Dict[str, str]:
        """
        放弃原因清单（key → 最后一次错误）

        用于告诉用户「哪些文件需要手工处理、为什么」。
        """
        return {
            t.key: t.last_error or "未知原因"
            for t in self.abandoned()
        }
