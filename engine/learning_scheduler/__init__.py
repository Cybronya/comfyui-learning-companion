"""
Learning Scheduler - 工作流学习调度系统

回答三个问题：**先学什么**、**学到哪了**、**哪些学不了**。

它本身不做学习，只负责排队与状态：
    学习怎么执行 → workflow_learning.WorkflowLearner
    学没学过     → workflow_learning.LearningStore

    WorkflowScanner
          ↓
    build_schedule()
      ├─ LearningStore.exists(key, hash)   跳过已学且内容未变
      ├─ 读节点清单
      ├─ PriorityCalculator                 打分
      └─ TaskQueue                          优先级降序
          ↓
    run()   循环：pop_next → learner.learn() → 更新状态
          ↓
    ScheduleStore（Markdown，可续跑）

优先级以**内容信号**为主：

    节点数           每个节点 1 分      流程越复杂越该先学
    缺卡节点数       每个 8 分        缺口越大，学完收益越高
    未见过的节点类型 每个 4 分        新颖
    曾失败           每次 2 分        可能是已修好的偶发问题
    内容已变更        5 分            用户改过，更该重学
    文件名关键词      缩放到 1 倍      仅作同分 tie-break

**为什么文件名权重这么低**：文件名是用户随手取的。`img_20240312.png`
得 0 分，而一个真用了 ControlNet 但叫 `a.json` 的 workflow 若只看名字
也拿不到分 —— 名字里的关键词和实际节点结构没有必然关系。

**为什么必须有重试上限**：永久损坏的文件（JSON 语法错误、引用不存在的
节点）重试再多遍也不会成功。不隔离的话队列会永远卡在同一批文件上，
调度器等于死锁。用尽重试的任务转 abandoned，需人工处理。

主入口：LearningScheduler.build_schedule() / run() / resume()
"""

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
from .task_queue import TaskQueue
from .priority import (
    PriorityCalculator,
    FILENAME_HINTS,
    WEIGHT_PER_NODE,
    WEIGHT_PER_UNKNOWN_NODE,
    WEIGHT_NOVEL_NODE_TYPE,
)
from .scheduler_state import SchedulerState
from .schedule_store import ScheduleStore, DEFAULT_PATH
from .scheduler import LearningScheduler, build_scheduler


def create_scheduler(
    learner=None,
    max_retries: int = 3,
    verbose: bool = True,
    **extra
) -> LearningScheduler:
    """
    便捷构造

    Args:
        learner: WorkflowLearner；不传则只能 build_schedule，不能 run
        max_retries: 单任务重试上限
        verbose: run() 时是否打印每个任务的结果
        **extra: scanner / store / priority / queue / schedule_store

    Returns:
        LearningScheduler 实例
    """
    return build_scheduler(
        learner=learner,
        max_retries=max_retries,
        verbose=verbose,
        **extra,
    )


__all__ = [
    "LearningTask",
    "STATUS_PENDING",
    "STATUS_RUNNING",
    "STATUS_COMPLETED",
    "STATUS_FAILED",
    "STATUS_SKIPPED",
    "STATUS_ABANDONED",
    "FINAL_STATUSES",
    "TaskQueue",
    "PriorityCalculator",
    "FILENAME_HINTS",
    "WEIGHT_PER_NODE",
    "WEIGHT_PER_UNKNOWN_NODE",
    "WEIGHT_NOVEL_NODE_TYPE",
    "SchedulerState",
    "ScheduleStore",
    "DEFAULT_PATH",
    "LearningScheduler",
    "build_scheduler",
    "create_scheduler",
]
