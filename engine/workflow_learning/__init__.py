"""
Workflow Learning - 批量 workflow 学习管理

把「读不懂的 workflow」变成「学过的知识」。

    create_batch_learner(...).learn_folder()
        扫描目录（.json + .png）
          ↓
        查记录（比对内容指纹）
          ↓
        已学且内容未变 → 跳过
          ↓
        WorkflowLearner.learn(file)
          analyzer 结构分析
          explorer 流程链与核心节点（复用 autonomous_learning）
          retriever 知识召回
          gap_detector 缺口检测（别名感知，不会把同族节点误判为没知识）
          diagnostics 参数体检
          ↓
        LearningStore 写一条 Markdown 记录（frontmatter + 正文）
          ↓
        批次摘要 + 覆盖率统计

**存储格式：一个 workflow 一个 Markdown 文件**

    comfyui_library/workflows/learning/
      index.md          汇总索引（表格，一行一个 workflow，带链接）
      sd1.5/basic.md    该 workflow 的完整学习记录

不用 JSON 的理由：
    - Agent 直接可读可查，`grep -r "LoraLoader" learning/`
      就能查出「哪些 workflow 用了这个节点」—— JSON 做不到
    - git diff 可读：JSON 每次重写是整块变更，Markdown 只变改动的行
    - 与知识卡规范一致（comfyui_library/knowledge/**/*.md 已用 frontmatter）

原先的 registry.json + experience.json + reports/*.md 三份已合并：
    它们描述的是同一件事却分散在不同格式，「已学过了吗」和「学到了什么」
    可能不一致。现在「文件存在」即「已学过」，没有第二种可能。

**知识来源仅限本地**：workflow 文件（json / PNG 元数据）、已有节点知识卡、
analyzer 结构分析、diagnostics 体检。不联网、不抓外部资料。

幂等：反复跑同一目录，第二次全部跳过；文件内容改了会自动重学。

主入口：BatchWorkflowLearner.learn_folder()
"""

from .learning_record import (
    LearningRecord,
    STATUS_COMPLETED,
    STATUS_FAILED,
    STATUS_SKIPPED,
    STATUS_STALE,
)
from .workflow_scanner import (
    WorkflowScanner,
    extract_text_chunks,
    load_png_workflow,
)
from .workflow_learner import WorkflowLearner
from .learning_store import LearningStore
from .markdown_format import (
    to_markdown,
    from_markdown,
    parse_frontmatter,
    build_frontmatter,
    split_frontmatter,
)
from .batch_learner import BatchWorkflowLearner
from .database_bridge import (
    STATUS_LEARNED,
    workflow_record_of,
    experience_args_of,
    sync_record,
    sync_all,
    is_learned,
)
from .paths import (
    PROJECT_ROOT,
    WORKFLOWS_DIR,
    STATE_DIR,
    STATE_DIR_NAME,
    INDEX_PATH,
    RECORD_SUFFIX,
    record_path_for,
    index_link_for,
    relative_to_project,
    ensure_state_dir,
)


def create_batch_learner(
    store_root: str = None,
    verbose: bool = True,
    database=None,
    **modules
) -> BatchWorkflowLearner:
    """
    便捷构造

    Args:
        store_root: 记录根目录；None 时用统一位置
                     `comfyui_library/workflows/learning/`
                     （仅测试需要隔离时传）
        verbose: 是否打印进度
        database: WorkflowDatabase；传入则学习结果镜像进库
                  （WorkflowDatabase() 即默认库，测试传临时路径的库）
        **modules: analyzer / retriever / parser / diagnostics /
                   explorer / gap_detector / knowledge

    Returns:
        BatchWorkflowLearner 实例
    """
    learner = WorkflowLearner(**modules)

    return BatchWorkflowLearner(
        learner=learner,
        store=LearningStore(store_root),
        scanner=WorkflowScanner(),
        verbose=verbose,
        database=database,
    )


__all__ = [
    "LearningRecord",
    "STATUS_COMPLETED",
    "STATUS_FAILED",
    "STATUS_SKIPPED",
    "STATUS_STALE",
    "WorkflowScanner",
    "extract_text_chunks",
    "load_png_workflow",
    "WorkflowLearner",
    "LearningStore",
    "BatchWorkflowLearner",
    "create_batch_learner",
    "STATUS_LEARNED",
    "workflow_record_of",
    "experience_args_of",
    "sync_record",
    "sync_all",
    "is_learned",
    "to_markdown",
    "from_markdown",
    "parse_frontmatter",
    "build_frontmatter",
    "split_frontmatter",
    "PROJECT_ROOT",
    "WORKFLOWS_DIR",
    "STATE_DIR",
    "STATE_DIR_NAME",
    "INDEX_PATH",
    "RECORD_SUFFIX",
    "record_path_for",
    "index_link_for",
    "relative_to_project",
    "ensure_state_dir",
]
