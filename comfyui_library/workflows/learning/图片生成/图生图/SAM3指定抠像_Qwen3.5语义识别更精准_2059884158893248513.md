---
key: 图片生成/图生图/SAM3指定抠像_Qwen3.5语义识别更精准_2059884158893248513.json
name: SAM3指定抠像_Qwen3.5语义识别更精准_2059884158893248513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SAM3指定抠像_Qwen3.5语义识别更精准_2059884158893248513.json
hash: 771feeb9151acb31
coverage: 0.846154
learned_at: 2026-10-23 11:23:29
nodes: [llama_cpp_model_loader, llama_cpp_parameters, RH_Translator, CR Text Concatenate, PreviewAny, SAM3Segment, PreviewImage, SaveImage, llama_cpp_instruct_adv, LoadImage, CR Text, LoadRembgByBiRefNetModel, RembgByBiRefNet]
patterns: []
missing: []
---

# 图片生成/图生图/SAM3指定抠像_Qwen3.5语义识别更精准_2059884158893248513.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SAM3指定抠像_Qwen3.5语义识别更精准_2059884158893248513.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（13 个）：
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `RH_Translator`
- `CR Text Concatenate`
- `PreviewAny`
- `SAM3Segment`
- `PreviewImage`
- `SaveImage`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `CR Text`
- `LoadRembgByBiRefNetModel`
- `RembgByBiRefNet`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`llama_cpp_model_loader`、`llama_cpp_parameters`、`RH_Translator`、`CR Text Concatenate`、`SAM3Segment`、`SaveImage`、`llama_cpp_instruct_adv`、`LoadImage`、`CR Text`、`LoadRembgByBiRefNetModel`、`RembgByBiRefNet`

**用到的条目**：LoadImage、SaveImage、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、RH_Translator、LoadRembgByBiRefNetModel、RembgByBiRefNet
