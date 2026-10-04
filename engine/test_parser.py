from workflow_parser.parser import (
    WorkflowParser
)

from workflow_parser.analyzer import (
    WorkflowAnalyzer
)

from workflow_parser.knowledge_loader import (
    NodeKnowledgeLoader
)

from pathlib import Path

# 用项目内真实存在的 SD1.5 默认文生图工作流（UI 格式 JSON）作为测试样本；
# 用 __file__ 定位，保证从任意工作目录运行都能找到文件。
root = Path(__file__).resolve().parent.parent

workflow = str(
    root
    / "comfyui_library"
    / "workflows"
    / "sd1.5"
    / "_workflow.json"
)

knowledge_path = str(
    root
    / "comfyui_library"
    / "knowledge"
)


# 1. 知识加载器独立使用：Node Type -> 知识卡
loader = NodeKnowledgeLoader(
    knowledge_path
)


node = loader.load(
    "KSampler"
)


print("=== 单节点知识 ===")

print("node_type:", node["node_type"])

print("category:", node["category"])

print("role:", node["role"])

print("difficulty:", node["difficulty"])

print("learning_topics:", node["learning_topics"])

print("content 开头:", node["content"].splitlines()[0])


# 2. 解析工作流：节点自动携带知识
parser = WorkflowParser(
    knowledge_path=knowledge_path
)


knowledge = parser.parse(
    workflow
)


knowledge = WorkflowAnalyzer().analyze(
    knowledge
)


print()

print("=== 工作流解析结果 ===")

print("task_type:", knowledge.task_type)

for n in knowledge.nodes:

    print(
        n.node_type,
        "| role:", n.role,
        "| category:", n.category,
        "| topics:", n.learning_topics
    )
