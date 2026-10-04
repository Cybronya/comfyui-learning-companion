from workflow_parser.parser import (
    WorkflowParser
)

from workflow_parser.analyzer import (
    WorkflowAnalyzer
)

from pathlib import Path

# 用项目内真实存在的 SD1.5 默认文生图工作流（UI 格式 JSON）作为测试样本；
# 用 __file__ 定位，保证从任意工作目录运行都能找到文件。
workflow = str(
    Path(__file__).resolve().parent.parent
    / "comfyui_library"
    / "workflows"
    / "sd1.5"
    / "_workflow.json"
)


parser=WorkflowParser()


knowledge=parser.parse(
    workflow
)


knowledge=WorkflowAnalyzer().analyze(
    knowledge
)


print(
    knowledge
)
