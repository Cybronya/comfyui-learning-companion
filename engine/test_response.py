from workflow_parser.parser import (
    WorkflowParser
)

from workflow_parser.knowledge_loader import (
    NodeKnowledgeLoader
)

from context.context_manager import (
    ContextManager
)

from teaching.response_generator import (
    TeachingResponseGenerator
)

from pathlib import Path

import json

# 用 __file__ 定位项目根目录，保证从任意工作目录运行都能找到文件。
root = Path(__file__).resolve().parent.parent



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



# 模拟用户已打开工作流（解析自动写入上下文）
parser = WorkflowParser(

    loader,

    context=context

)


parser.parse(
    str(
        root
        / "comfyui_library"
        / "workflows"
        / "sd1.5"
        / "basic.json"
    )
)



# 用户提问
question = "KSampler 的 CFG 怎么设置？"

context.update_question(question)


context_data = context.get_context()


print("Question:")

print("-", question)

print()

print("Context:")

print(json.dumps(
    context_data,
    ensure_ascii=False,
    indent=4
))

print()

print("Response:")

print(
    TeachingResponseGenerator(loader).answer(
        question,
        context_data
    )
)


# 结束后清空状态
context.clear()
