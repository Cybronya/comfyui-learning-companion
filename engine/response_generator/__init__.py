"""
Response Generator - 回答生成模块

两条产出路径，取决于是否接 LLM：

    generate(question, context, knowledge=None)
        → {"prompt": ..., "analysis": ...}
        给 LLM 的提示词。适合把本项目当 Agent 框架、后端接自有模型。

    answer(state)
        → Markdown 中文回答
        给人直接看。全规则拼装，不需要 LLM、不需要网络。

回答的事实来源（都不经过模型，所以不会编造参数）：
    diagnostics      实测参数值 + 阈值判定
    knowledge cards  参数说明、常见错误
    evolution store  多条历史经验统计出的区间
"""

from .generator import ResponseGenerator
from .answer_builder import (
    AnswerBuilder,
    SEVERITY_LABELS,
    ISSUE_CATEGORY,
)
from .knowledge_distiller import KnowledgeDistiller
from .analyzer import QuestionAnalyzer
from .prompt_builder import PromptBuilder

__all__ = [
    "ResponseGenerator",
    "AnswerBuilder",
    "KnowledgeDistiller",
    "QuestionAnalyzer",
    "PromptBuilder",
    "SEVERITY_LABELS",
    "ISSUE_CATEGORY",
]
