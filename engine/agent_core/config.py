"""
Agent 配置

控制链路里各阶段是否启用、召回条数上限、存储路径等。
"""

from typing import Dict, Any


# 完整链路：解析 → 分析 → 诊断 → 检索 → 回答
DEFAULT_CONFIG: Dict[str, Any] = {
    # 阶段开关
    "enable_context": True,
    "enable_parse": True,
    "enable_analyze": True,
    "enable_diagnostics": True,
    "enable_retrieval": True,
    "enable_learning": True,      # 知识演化（离线，不在 ask() 链路上）
    "enable_response": True,

    # 各阶段是否容错：单阶段失败记 error 并继续，而不是让整条链路崩
    "continue_on_error": True,

    # 检索
    "retrieval_limit": 0,          # 0 = 不限
    "retrieval_index_path": "engine/retrieval/retrieval_store.json",
    "retrieval_rebuild": "if_missing",  # if_missing=索引存在且非空就复用；
                                        # always=每次全量重建；never=只读不建

    # 知识图谱（跨条目查询：哪些流程用了 X / 节点常与谁共现）
    "enable_graph": True,
    "graph_json_path": "engine/knowledge_graph/knowledge_graph.json",

    # 上下文
    "context_store_path": "engine/context/context_store.json",
    "update_context": True,

    # 知识库
    "knowledge_dir": "comfyui_library/knowledge",
    "experience_store": "engine/learning_loop/experience_store.json",
    "evolution_store": "engine/knowledge_evolution/evolution_store.json",
}


def merge_config(overrides: Dict = None) -> Dict:
    """
    合并用户配置与默认配置

    Args:
        overrides: 覆盖项

    Returns:
        完整配置
    """
    config = dict(DEFAULT_CONFIG)

    if overrides:
        # 只接受已知键，避免拼错静默失效
        unknown = [k for k in overrides if k not in DEFAULT_CONFIG]
        if unknown:
            raise ValueError(f"未知配置项: {unknown}")

        config.update(overrides)

    return config


def stages_of(config: Dict) -> list:
    """
    按配置得出要执行的阶段顺序

    Args:
        config: 配置

    Returns:
        阶段名列表
    """
    stages = []

    if config.get("enable_context"):
        stages.append("context")
    if config.get("enable_parse"):
        stages.append("parse")
    if config.get("enable_analyze"):
        stages.append("analyze")
    if config.get("enable_diagnostics"):
        stages.append("diagnose")
    if config.get("enable_retrieval"):
        stages.append("retrieve")
    if config.get("enable_response"):
        stages.append("respond")

    return stages
