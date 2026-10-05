"""
任务模型

一次待执行的 workflow 学习任务。

与 workflow_learning.LearningRecord 的区别：
    LearningRecord  是「学完了的结论」
    LearningTask    是「排队等学 / 学到哪了」
前者是结果，后者是过程状态。调度器只管后者。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime


# 任务状态
STATUS_PENDING = "pending"
STATUS_RUNNING = "running"
STATUS_COMPLETED = "completed"
STATUS_FAILED = "failed"
STATUS_SKIPPED = "skipped"
STATUS_ABANDONED = "abandoned"     # 重试用尽，永久放弃

# 终态：不会再被调度
FINAL_STATUSES = {
    STATUS_COMPLETED,
    STATUS_SKIPPED,
    STATUS_ABANDONED,
}


@dataclass
class LearningTask:
    """
    一个待学习的 workflow
    """

    workflow_path: str
    workflow_name: str

    # 与 workflow_learning.LearningStore 保持一致的标识：
    # 用相对路径而非文件名，否则 a/x.json 与 b/x.json 会互相覆盖
    key: str = ""

    priority: int = 0
    status: str = STATUS_PENDING
    retry_count: int = 0
    result: str = ""

    # 调度依据（写进记录，便于事后解释「为什么先学它」）
    priority_reasons: List[str] = field(default_factory=list)
    node_count: int = 0
    # 没有知识卡的节点数 —— 缺口越大越该先学
    unknown_node_count: int = 0
    # 相对上次学习，节点是否变化（变了说明用户改过，更该重学）
    content_changed: bool = False

    content_hash: str = ""
    last_error: str = ""
    created_at: str = ""
    started_at: str = ""
    finished_at: str = ""

    def __post_init__(self):
        if not self.key:
            self.key = self.workflow_name
        if not self.created_at:
            self.created_at = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

    # ---------- 状态判断 ----------

    @property
    def is_final(self) -> bool:
        """是否已到终态"""
        return self.status in FINAL_STATUSES

    @property
    def is_runnable(self) -> bool:
        """是否可被调度（待执行，或失败待重试）"""
        return self.status in (STATUS_PENDING, STATUS_FAILED)

    def can_retry(self, max_retries: int) -> bool:
        """
        是否还能重试

        没有这个判断，一个永久损坏的文件（JSON 语法错误、
        引用了不存在的模型路径）会被无限重试，
        队列永远卡在同一批文件上。
        """
        if self.status == STATUS_FAILED:
            return self.retry_count < max_retries
        return True

    # ---------- 状态迁移 ----------

    def start(self) -> None:
        """标记开始执行"""
        self.status = STATUS_RUNNING
        self.started_at = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    def complete(self, result: str = "") -> None:
        """标记完成"""
        self.status = STATUS_COMPLETED
        self.result = result
        self.finished_at = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        self.last_error = ""

    def fail(self, error: str, max_retries: int = 3) -> None:
        """
        标记失败

        Args:
            error: 错误信息
            max_retries: 重试上限，用尽则转 abandoned
        """
        self.status = STATUS_FAILED
        self.last_error = error
        self.result = ""
        self.finished_at = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        self.retry_count += 1

        if self.retry_count >= max_retries:
            self.status = STATUS_ABANDONED

    # ---------- 序列化 ----------

    def to_dict(self) -> Dict:
        return {
            "key": self.key,
            "name": self.workflow_name,
            "path": self.workflow_path,
            "priority": self.priority,
            "status": self.status,
            "retry_count": self.retry_count,
            "result": self.result,
            "priority_reasons": list(self.priority_reasons),
            "node_count": self.node_count,
            "unknown_node_count": self.unknown_node_count,
            "content_changed": self.content_changed,
            "hash": self.content_hash,
            "last_error": self.last_error,
            "created_at": self.created_at,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "LearningTask":
        return cls(
            workflow_path=data.get("path", ""),
            workflow_name=data.get("name", ""),
            key=data.get("key", ""),
            priority=data.get("priority", 0),
            status=data.get("status", STATUS_PENDING),
            retry_count=data.get("retry_count", 0),
            result=data.get("result", ""),
            priority_reasons=data.get("priority_reasons", []),
            node_count=data.get("node_count", 0),
            unknown_node_count=data.get("unknown_node_count", 0),
            content_changed=data.get("content_changed", False),
            content_hash=data.get("hash", ""),
            last_error=data.get("last_error", ""),
            created_at=data.get("created_at", ""),
            started_at=data.get("started_at", ""),
            finished_at=data.get("finished_at", ""),
        )

    def __repr__(self) -> str:
        return (
            f"<LearningTask {self.key} "
            f"p={self.priority} {self.status} "
            f"retry={self.retry_count}>"
        )
