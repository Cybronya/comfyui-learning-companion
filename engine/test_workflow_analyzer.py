from workflow_analyzer.analyzer import (
    WorkflowAnalyzer
)

from pathlib import Path

import json

# 用 __file__ 定位项目根目录，保证从任意工作目录运行都能找到文件。
root = Path(__file__).resolve().parent.parent

analyzer = WorkflowAnalyzer()



# 1. 基础文生图工作流
with open(
    root
    / "comfyui_library"
    / "workflows"
    / "sd1.5"
    / "basic.json",
    "r",
    encoding="utf-8"
) as f:

    basic = json.load(f)



result = analyzer.analyze(basic)


print("=== basic.json ===")

print("workflow_type:", result["workflow_type"])

print("patterns:", result["patterns"])

print("nodes:", result["nodes"])

print("connections:")

for c in result["connections"]:

    print(
        " ",
        c["from"],
        "--",
        c["data"],
        "-->",
        c["to"]
    )



# 2. LoRA 工作流（含 LoraLoader + MarkdownNote）
with open(
    root
    / "comfyui_library"
    / "workflows"
    / "sd1.5"
    / "_workflow.json",
    "r",
    encoding="utf-8"
) as f:

    lora = json.load(f)



result = analyzer.analyze(lora)


print()

print("=== _workflow.json (LoRA) ===")

print("workflow_type:", result["workflow_type"])

print("patterns:", result["patterns"])
