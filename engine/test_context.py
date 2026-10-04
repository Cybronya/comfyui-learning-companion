from workflow_parser.parser import (
    WorkflowParser
)

from workflow_parser.analyzer import (
    WorkflowAnalyzer
)

from workflow_parser.knowledge_loader import (
    NodeKnowledgeLoader
)

from context.context_manager import (
    ContextManager
)

from pathlib import Path

# 用 __file__ 定位项目根目录，保证从任意工作目录运行都能找到文件。
root = Path(__file__).resolve().parent.parent



# 1. 初始化知识加载器与上下文管理器
loader = NodeKnowledgeLoader(

    root
    / "comfyui_library"
    / "knowledge"

)


context = ContextManager(

    root
    / "engine"
    / "context"
    / "context_store.json",

    known_node_types=list(
        loader.index.keys()
    )

)



# 2. 解析工作流（自动写入 WorkflowContext）
parser = WorkflowParser(

    loader,

    context=context

)


workflow = parser.parse(

    str(
        root
        / "comfyui_library"
        / "workflows"
        / "sd1.5"
        / "basic.json"
    )

)


workflow = WorkflowAnalyzer().analyze(

    workflow

)



# 3. 模拟用户提问
context.update_question(
    "KSampler 的 CFG 怎么设置？"
)


print("=== 当前上下文 ===")

import json

print(
    json.dumps(
        context.get_context(),
        ensure_ascii=False,
        indent=4
    )
)


# 4. 结束后清空状态
context.clear()

print()

print("上下文已清空:", context.get_context())
