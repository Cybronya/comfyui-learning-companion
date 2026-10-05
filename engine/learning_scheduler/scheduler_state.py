"""
调度状态

一次调度运行的统计与进度。

设计稿里 SchedulerState 的字段（total_tasks / completed / failed /
current_task）没有任何代码去填 —— 声明了但没人写。
这里改成从队列**计算**出来的视图，避免两处状态各自漂移：
队列是唯一事实来源，状态对象只是它的投影。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional

from .models import LearningTask


@dataclass
class SchedulerState:
    """
    调度运行状态
    """

    total_tasks: int = 0
    completed: int = 0
    failed: int = 0
    abandoned: int = 0
    skipped: int = 0
    pending: int = 0
    current_task: str = ""
    current_key: str = ""

    # 已完成 / 失败的任务 key，便于续跑时判断做过哪些
    completed_keys: List[str] = field(default_factory=list)
    failed_keys: List[str] = field(default_factory=list)
    abandoned_keys: List[str] = field(default_factory=list)

    # 本次运行的耗时与统计
    elapsed_ms: float = 0.0
    started_at: str = ""
    finished_at: str = ""

    @classmethod
    def from_queue(
        cls,
        queue,
        current_task: str = "",
        current_key: str = "",
        elapsed_ms: float = 0.0
    ) -> "SchedulerState":
        """
        从队列计算状态

        Args:
            queue: TaskQueue
            current_task: 当前正在执行的任务名
            current_key: 当前正在执行的任务 key
            elapsed_ms: 本次运行耗时

        Returns:
            SchedulerState
        """
        stats = queue.progress()

        return cls(
            total_tasks=stats["total"],
            completed=stats["completed"],
            failed=stats["failed"],
            abandoned=stats["abandoned"],
            skipped=stats["skipped"],
            pending=stats["pending"],
            current_task=current_task,
            current_key=current_key,
            completed_keys=[t.key for t in queue.completed()],
            failed_keys=[t.key for t in queue.failed()],
            abandoned_keys=[t.key for t in queue.abandoned()],
            elapsed_ms=round(elapsed_ms, 1),
        )

    @property
    def is_done(self) -> bool:
        """队列是否已无待处理任务"""
        return self.pending == 0 and self.current_task == ""

    @property
    def success_rate(self) -> float:
        """
        成功率（已结束的任务中成功的比例）

        分母用 completed + skipped + failed + abandoned ——
        只算 completed 会把失败和跳过都排除在分母外，
        数字会虚高。
        """
        finished = (
            self.completed + self.skipped
            + self.failed + self.abandoned
        )
        if not finished:
            return 0.0
        return self.completed / finished

    def summary(self) -> str:
        """
        一行进度摘要
        """
        parts = [
            f"共 {self.total_tasks}",
            f"完成 {self.completed}",
        ]
        if self.skipped:
            parts.append(f"跳过 {self.skipped}")
        if self.failed:
            parts.append(f"失败待重试 {self.failed}")
        if self.abandoned:
            parts.append(f"已放弃 {self.abandoned}")
        parts.append(f"待学 {self.pending}")

        if self.current_task:
            parts.append(f"当前 {self.current_task}")

        return "，".join(parts)

    def to_dict(self) -> Dict:
        return {
            "total_tasks": self.total_tasks,
            "completed": self.completed,
            "failed": self.failed,
            "abandoned": self.abandoned,
            "skipped": self.skipped,
            "pending": self.pending,
            "current_task": self.current_task,
            "current_key": self.current_key,
            "completed_keys": list(self.completed_keys),
            "failed_keys": list(self.failed_keys),
            "abandoned_keys": list(self.abandoned_keys),
            "success_rate": round(self.success_rate, 3),
            "elapsed_ms": self.elapsed_ms,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
        }
