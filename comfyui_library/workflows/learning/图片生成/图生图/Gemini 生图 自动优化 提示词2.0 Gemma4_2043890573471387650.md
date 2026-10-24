---
key: 图片生成/图生图/Gemini 生图 自动优化 提示词2.0 Gemma4_2043890573471387650.json
name: Gemini 生图 自动优化 提示词2.0 Gemma4_2043890573471387650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Gemini 生图 自动优化 提示词2.0 Gemma4_2043890573471387650.json
hash: 6e708006a35759dd
coverage: 0.8125
learned_at: 2026-10-23 11:02:46
nodes: [easy cleanGpuUsed, LoadImage, llama_cpp_instruct_adv, LoadImage, ImageBatchMulti, llama_cpp_parameters, llama_cpp_model_loader, RH_RhartImageNG31FlashImageToImage, PrimitiveNode, PreviewImage, SaveImage, RHHiddenNodes, LoadImage, LoadImage, PreviewAny, CR Text]
patterns: []
missing: []
---

# 图片生成/图生图/Gemini 生图 自动优化 提示词2.0 Gemma4_2043890573471387650.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Gemini 生图 自动优化 提示词2.0 Gemma4_2043890573471387650.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（16 个）：
- `easy cleanGpuUsed`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `ImageBatchMulti`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `RH_RhartImageNG31FlashImageToImage`
- `PrimitiveNode`
- `PreviewImage`
- `SaveImage`
- `RHHiddenNodes`
- `LoadImage`
- `LoadImage`
- `PreviewAny`
- `CR Text`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`easy cleanGpuUsed`、`LoadImage`、`llama_cpp_instruct_adv`、`ImageBatchMulti`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`RH_RhartImageNG31FlashImageToImage`、`SaveImage`、`RHHiddenNodes`、`CR Text`

**用到的条目**：LoadImage、SaveImage、ImageBatchMulti、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、RHHiddenNodes、RH_RhartImageNG31FlashImageToImage
