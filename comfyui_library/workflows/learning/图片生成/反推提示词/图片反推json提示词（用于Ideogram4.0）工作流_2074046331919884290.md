---
key: 图片生成/反推提示词/图片反推json提示词（用于Ideogram4.0）工作流_2074046331919884290.json
name: 图片反推json提示词（用于Ideogram4.0）工作流_2074046331919884290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/图片反推json提示词（用于Ideogram4.0）工作流_2074046331919884290.json
hash: b7355b22edd033ea
coverage: 0.642857
learned_at: 2026-10-26 01:47:50
nodes: [PrimitiveStringMultiline, llama_cpp_instruct_adv, PreviewAny, StringReplace, StringReplace, GetImageSize, ComfyMathExpression, ComfyMathExpression, PreviewAny, PreviewAny, llama_cpp_model_loader, LoadImage, PreviewAny, easy saveText]
patterns: []
missing: []
---

# 图片生成/反推提示词/图片反推json提示词（用于Ideogram4.0）工作流_2074046331919884290.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/图片反推json提示词（用于Ideogram4.0）工作流_2074046331919884290.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（14 个）：
- `PrimitiveStringMultiline`
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `StringReplace`
- `StringReplace`
- `GetImageSize`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PreviewAny`
- `PreviewAny`
- `llama_cpp_model_loader`
- `LoadImage`
- `PreviewAny`
- `easy saveText`

## 知识

覆盖率 **64%**（9/14）

**有卡**：`llama_cpp_instruct_adv`、`StringReplace`、`GetImageSize`、`ComfyMathExpression`、`llama_cpp_model_loader`、`LoadImage`、`easy saveText`

**用到的条目**：LoadImage、GetImageSize、GetImageSize、easy saveText、ComfyMathExpression、llama_cpp_instruct_adv、llama_cpp_model_loader、StringReplace
