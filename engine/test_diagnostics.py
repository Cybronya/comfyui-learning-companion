from workflow_parser.parser import (
    WorkflowParser
)

from workflow_parser.knowledge_loader import (
    NodeKnowledgeLoader
)

from workflow_analyzer.graph_builder import (
    GraphBuilder
)

from diagnostics import (
    DiagnosticEngine
)

from pathlib import Path

import json

# 用 __file__ 定位项目根目录，保证从任意工作目录运行都能找到文件。
root = Path(__file__).resolve().parent.parent



# 构造一个有问题的工作流：
# KSampler steps=8, cfg=18；且缺少 VAEDecode
workflow_json = {

    "nodes": [
        {"id": 4, "type": "CheckpointLoaderSimple",
         "inputs": [], "widgets_values": ["sd15_base_model.safetensors"]},
        {"id": 6, "type": "CLIPTextEncode",
         "inputs": [{"name": "clip", "type": "CLIP", "link": 18}],
         "widgets_values": ["a portrait photo"]},
        {"id": 5, "type": "EmptyLatentImage",
         "inputs": [], "widgets_values": [512, 512, 1]},
        {"id": 3, "type": "KSampler",
         "inputs": [
             {"name": "model", "type": "MODEL", "link": 17},
             {"name": "positive", "type": "CONDITIONING", "link": 4}
         ],
         "widgets_values": [123, "fixed", 8, 18, "euler", "normal", 1]},
        {"id": 9, "type": "SaveImage",
         "inputs": [{"name": "images", "type": "IMAGE", "link": 9}],
         "widgets_values": ["test_"]}
    ],

    "links": [
        [17, 4, 0, 3, 0, "MODEL"],
        [18, 4, 1, 6, 0, "CLIP"],
        [4, 6, 0, 3, 1, "CONDITIONING"],
        [9, 3, 0, 9, 0, "IMAGE"]
    ]

}



# 1. WorkflowKnowledge（参数值在 widgets 里）
loader = NodeKnowledgeLoader(
    root
    / "comfyui_library"
    / "knowledge"
)

workflow = WorkflowParser(loader).parse_data(workflow_json)



# 2. WorkflowGraph
graph = GraphBuilder().build(
    workflow_json
)



# 3. 诊断
engine=DiagnosticEngine()

report=engine.analyze(
    workflow,
    graph
)



print("workflow_type:", report.workflow_type)

print()

print("issues:")

for issue in report.issues:

    print(
        "-",
        issue.issue_type,
        "|",
        issue.node,
        issue.parameter,
        "=",
        issue.value,
        "|",
        issue.severity
    )

    print("  ", issue.message)

    print("  ", issue.suggestion)

print()

print("recommendations:")

for s in report.suggestions:

    print("-", s)
