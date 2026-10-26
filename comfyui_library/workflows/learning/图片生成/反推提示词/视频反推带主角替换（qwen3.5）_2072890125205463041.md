---
key: 图片生成/反推提示词/视频反推带主角替换（qwen3.5）_2072890125205463041.json
name: 视频反推带主角替换（qwen3.5）_2072890125205463041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/视频反推带主角替换（qwen3.5）_2072890125205463041.json
hash: 619965790a7ebed2
coverage: 0.764706
learned_at: 2026-10-26 01:48:46
nodes: [PreviewAny, Note, RH_LLMAPI_Pro_Node, LoadVideo, easy saveText, llama_cpp_parameters, llama_cpp_model_loader, LoadImage, PreviewAny, llama_cpp_model_loader, llama_cpp_parameters, PreviewAny, easy saveText, llama_cpp_instruct_adv, llama_cpp_instruct_adv, Text, VHS_LoadVideo]
patterns: []
missing: []
---

# 图片生成/反推提示词/视频反推带主角替换（qwen3.5）_2072890125205463041.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/视频反推带主角替换（qwen3.5）_2072890125205463041.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（17 个）：
- `PreviewAny`
- `Note`
- `RH_LLMAPI_Pro_Node`
- `LoadVideo`
- `easy saveText`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `LoadImage`
- `PreviewAny`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `PreviewAny`
- `easy saveText`
- `llama_cpp_instruct_adv`
- `llama_cpp_instruct_adv`
- `Text`
- `VHS_LoadVideo`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`RH_LLMAPI_Pro_Node`、`LoadVideo`、`easy saveText`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`LoadImage`、`llama_cpp_instruct_adv`、`Text`、`VHS_LoadVideo`

**用到的条目**：LoadImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、LoadVideo、RH_LLMAPI_Pro_Node、Text
