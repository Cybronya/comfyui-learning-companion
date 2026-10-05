"""
调度状态存储

保存任务队列，让「调度到一半被打断」能续跑。

格式沿用项目约定：**Markdown + frontmatter**，不是 JSON。
理由与 workflow_learning / knowledge_consolidation 一致 ——
Agent 要能直接读、能 grep，git diff 也要可读。

设计稿里 store 只存 name/path/status/priority，**不存 retry_count 和
result** —— 那意味着续跑时重试次数归零，永久失败的文件会被无限重试；
错误信息也没地方放，用户看不到「为什么这个文件学不了」。

这里把全部字段写进 frontmatter，错误与优先级理由都留档。

一个任务一行表格（读起来紧凑，一眼能看完整队列），
frontmatter 存整体状态，详情（错误、重试、理由）放在表格单元格里。
重试次数与优先级理由用 ` | ` 分隔，避免与表格分隔符冲突。
"""

from pathlib import Path
from typing import List, Dict, Any, Optional

from ..workflow_learning.markdown_format import (
    build_frontmatter,
    split_frontmatter,
    parse_frontmatter,
)
from ..workflow_learning.paths import relative_to_project
from .models import (
    LearningTask,
    STATUS_PENDING,
    STATUS_RUNNING,
    STATUS_COMPLETED,
    STATUS_FAILED,
    STATUS_SKIPPED,
    STATUS_ABANDONED,
    FINAL_STATUSES,
)
from .scheduler_state import SchedulerState


# 单元格内多值分隔符（不能用逗号，会与 Markdown 表格冲突）
CELL_SEP = " | "

DEFAULT_PATH = "engine/learning_scheduler/learning_queue.md"


class ScheduleStore:
    """
    队列持久化
    """

    def __init__(self, path: str = None) -> None:
        """
        初始化存储

        Args:
            path: 队列文件路径；None 时用默认
                  engine/learning_scheduler/learning_queue.md
        """
        self.path = Path(path) if path else Path(DEFAULT_PATH)

    # ---------- 写 ----------

    def save(
        self,
        tasks: List[LearningTask],
        state: SchedulerState = None,
        folder: str = ""
    ) -> str:
        """
        保存队列

        Args:
            tasks: 任务列表
            state: 调度状态（可选）
            folder: 扫描目录

        Returns:
            文件路径；失败返回空串
        """
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self.path.write_text(
                self.render(tasks, state, folder), encoding="utf-8"
            )
            return str(self.path)
        except Exception as e:
            print(f"保存学习队列失败: {e}")
            return ""

    def render(
        self,
        tasks: List[LearningTask],
        state: SchedulerState = None,
        folder: str = ""
    ) -> str:
        """
        渲染队列为 Markdown
        """
        state = state if state is not None else self._state_of(tasks)

        front = build_frontmatter({
            "source": folder,
            "total": state.total_tasks,
            "completed": state.completed,
            "skipped": state.skipped,
            "failed": state.failed,
            "abandoned": state.abandoned,
            "pending": state.pending,
            "generated_at": state.finished_at or state.started_at,
        })

        lines = [
            "# 学习队列",
            "",
            "> 本文件由 `engine/learning_scheduler/` 生成，"
            "记录学习顺序与状态。",
            "> 中断后可据此续跑 —— `retry` 与 `错误` 列是关键，"
            "删掉会导致失败任务被无限重试。",
            "",
        ]

        if folder:
            lines.insert(4, f"> 扫描目录：`{folder}`")
            lines.insert(5, "")

        lines.extend([
            f"## 进度：{state.summary()}",
            "",
        ])

        if not tasks:
            lines.append("队列为空。")
            return front + "\n" + "\n".join(lines)

        lines.extend([
            "## 任务",
            "",
            "| # | workflow | 优先级 | 状态 | 重试 | 节点 | 缺卡 | 错误 |",
            "|---|---|---|---|---|---|---|---|",
        ])

        # 按调度顺序展示：优先级降序，同分按加入顺序
        ordered = sorted(tasks, key=lambda t: -t.priority)

        for i, task in enumerate(ordered, 1):
            lines.append(
                f"| {i} "
                f"| `{task.key}` "
                f"| {task.priority} "
                f"| {self._status_label(task.status)} "
                f"| {task.retry_count} "
                f"| {task.node_count} "
                f"| {task.unknown_node_count} "
                f"| {self._cell(task.last_error)} |"
            )

        # 待重试：还没放弃，但上一轮失败了，用户需要知道是谁、为什么
        failed = [t for t in tasks if t.status == STATUS_FAILED]
        if failed:
            lines.extend([
                "",
                "## 失败待重试",
                "",
                "下一轮 `run()` 会自动重试；重试用尽后转入下方"
                "「需要人工处理」：",
                "",
            ])
            for task in failed:
                lines.append(
                    f"- `{task.key}`（已试 {task.retry_count} 次）"
                    f" —— {task.last_error or '未知原因'}"
                )

        # 已放弃的单独说明：这些需要人工处理
        abandoned = [t for t in tasks if t.status == STATUS_ABANDONED]
        if abandoned:
            lines.extend([
                "",
                "## 需要人工处理",
                "",
                "以下任务重试用尽，通常是文件本身有问题"
                "（JSON 损坏、引用不存在的节点），重试无用：",
                "",
            ])
            for task in abandoned:
                lines.append(
                    f"- `{task.key}` —— {task.last_error or '未知原因'}"
                )

        # 优先级理由：让「为什么先学它」可追溯
        with_reasons = [t for t in tasks if t.priority_reasons]
        if with_reasons:
            lines.extend(["", "## 排序依据", ""])
            for task in sorted(
                with_reasons, key=lambda t: -t.priority
            )[:10]:
                lines.append(f"- `{task.key}`（{task.priority} 分）")
                for reason in task.priority_reasons:
                    lines.append(f"    - {reason}")

        return front + "\n" + "\n".join(lines) + "\n"

    # ---------- 读 ----------

    def load(self) -> List[LearningTask]:
        """
        读回队列

        Returns:
            任务列表；文件不存在或格式不对时返回空列表
        """
        if not self.path.exists():
            return []

        try:
            text = self.path.read_text(encoding="utf-8-sig")
        except Exception as e:
            print(f"读取学习队列失败: {e}")
            return []

        tasks = []

        for line in text.split("\n"):
            if not line.startswith("| ") or "---" in line:
                continue

            cells = [
                c.strip() for c in line.strip("|").split("|")
            ]

            # 表头行与非法行跳过。表格共 8 列，
            # strip("|") 去掉首尾竖线后 split 出 8 格
            if len(cells) < 8 or not cells[0].isdigit():
                continue
            if not cells[1].startswith("`"):
                continue

            key = cells[1].strip("`")
            if not key:
                continue

            tasks.append(self._task_from_cells(key, cells))

        return tasks

    def _task_from_cells(
        self,
        key: str,
        cells: List[str]
    ) -> LearningTask:
        """
        从表格行还原任务
        """
        def as_int(text: str, default: int = 0) -> int:
            try:
                return int(text.strip())
            except ValueError:
                return default

        return LearningTask(
            workflow_path="",
            workflow_name=key.rsplit("/", 1)[-1],
            key=key,
            priority=as_int(cells[2]),
            status=self._status_from_label(cells[3]),
            retry_count=as_int(cells[4]),
            node_count=as_int(cells[5]),
            unknown_node_count=as_int(cells[6]),
            last_error=cells[7].strip() if len(cells) > 7 else "",
        )

    def load_meta(self) -> Dict:
        """
        读队列的 frontmatter（整体统计）
        """
        if not self.path.exists():
            return {}

        text = self.path.read_text(encoding="utf-8-sig")
        front, _body = split_frontmatter(text)

        return parse_frontmatter(front) if front else {}

    # ---------- 工具 ----------

    @staticmethod
    def _state_of(tasks: List[LearningTask]) -> SchedulerState:
        """
        没有 queue 对象时，直接从任务列表算状态
        """
        total = len(tasks)

        def by_status(status: str) -> int:
            return len([t for t in tasks if t.status == status])

        done = by_status(STATUS_COMPLETED) + by_status(STATUS_SKIPPED)

        return SchedulerState(
            total_tasks=total,
            completed=by_status(STATUS_COMPLETED),
            failed=by_status(STATUS_FAILED),
            abandoned=by_status(STATUS_ABANDONED),
            skipped=by_status(STATUS_SKIPPED),
            pending=by_status(STATUS_PENDING),
            completed_keys=[
                t.key for t in tasks
                if t.status == STATUS_COMPLETED
            ],
            failed_keys=[
                t.key for t in tasks if t.status == STATUS_FAILED
            ],
            abandoned_keys=[
                t.key for t in tasks
                if t.status == STATUS_ABANDONED
            ],
        )

    @staticmethod
    def _status_label(status: str) -> str:
        return {
            "pending": "⏳ 待学",
            "running": "▶️ 进行中",
            "completed": "✅ 完成",
            "failed": "❌ 失败待重试",
            "skipped": "⏭️ 跳过",
            "abandoned": "🚫 已放弃",
        }.get(status, status)

    @staticmethod
    def _status_from_label(label: str) -> str:
        label = label.strip()
        for key, text in {
            "pending": "⏳ 待学",
            "running": "▶️ 进行中",
            "completed": "✅ 完成",
            "failed": "❌ 失败待重试",
            "skipped": "⏭️ 跳过",
            "abandoned": "🚫 已放弃",
        }.items():
            if label == text or label == key:
                return key
        return "pending"

    @staticmethod
    def _cell(text: str) -> str:
        """
        转义表格单元格

        竖线会破坏表格结构，换行会破坏行结构。
        """
        if not text:
            return "-"

        cleaned = (
            text.replace("|", "/").replace("\n", " ").strip()
        )
        return cleaned if cleaned else "-"
