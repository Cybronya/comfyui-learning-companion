from response_generator.generator import (
    ResponseGenerator
)

from workflow_parser.knowledge_loader import (
    NodeKnowledgeLoader
)

from pathlib import Path



# 1. 无知识库的基础用法
generator=ResponseGenerator()



context={


"workflow":{

"nodes":[

"KSampler"

],

"parameters":{

"steps":10,

"cfg":12

}

},


"conversation":{

"active_topic":

"KSampler"

}

}



result=generator.generate(

"为什么我的图片很模糊？",

context

)



print(
result["prompt"]
)



print("analysis:", result["analysis"])



# 2. 接入知识库：知识卡内容注入 prompt
root = Path(__file__).resolve().parent.parent

loader = NodeKnowledgeLoader(
    root
    / "comfyui_library"
    / "knowledge"
)


generator_with_knowledge = ResponseGenerator(
    knowledge_loader=loader
)


result = generator_with_knowledge.generate(
    "KSampler 的 steps 怎么设置？",
    context
)


print()

print("=== 注入知识后 prompt 的知识部分 ===")

prompt = result["prompt"]

start = prompt.find("相关知识:")

print(prompt[start:start + 200])
