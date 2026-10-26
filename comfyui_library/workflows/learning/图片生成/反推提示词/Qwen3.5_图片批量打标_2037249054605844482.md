---
key: 图片生成/反推提示词/Qwen3.5_图片批量打标_2037249054605844482.json
name: Qwen3.5_图片批量打标_2037249054605844482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen3.5_图片批量打标_2037249054605844482.json
hash: 943fe8712edf6211
coverage: 0.666667
learned_at: 2026-10-26 01:46:08
nodes: [HAIGC_LoadImagesFromZip, RHBatchImages:, easy imageCount, PreviewImage, easy showAnything, ImageScaleToTotalPixels, easy forLoopStart, easy forLoopEnd, easy saveText, PreviewAny, easy showAnything, easy showAnything, HAIGC_SaveImagesToZip, llama_cpp_parameters, easy showAnything, llama_cpp_model_loader, llama_cpp_instruct_adv, CR Text]
patterns: []
missing: []
---

# 图片生成/反推提示词/Qwen3.5_图片批量打标_2037249054605844482.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen3.5_图片批量打标_2037249054605844482.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（18 个）：
- `HAIGC_LoadImagesFromZip`
- `RHBatchImages:`
- `easy imageCount`
- `PreviewImage`
- `easy showAnything`
- `ImageScaleToTotalPixels`
- `easy forLoopStart`
- `easy forLoopEnd`
- `easy saveText`
- `PreviewAny`
- `easy showAnything`
- `easy showAnything`
- `HAIGC_SaveImagesToZip`
- `llama_cpp_parameters`
- `easy showAnything`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `CR Text`

## 知识

覆盖率 **67%**（12/18）

**有卡**：`HAIGC_LoadImagesFromZip`、`RHBatchImages:`、`easy imageCount`、`ImageScaleToTotalPixels`、`easy forLoopStart`、`easy forLoopEnd`、`easy saveText`、`HAIGC_SaveImagesToZip`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`CR Text`

**用到的条目**：HAIGC_SaveImagesToZip、easy saveText、ImageScaleToTotalPixels、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、HAIGC_LoadImagesFromZip、CR Text
