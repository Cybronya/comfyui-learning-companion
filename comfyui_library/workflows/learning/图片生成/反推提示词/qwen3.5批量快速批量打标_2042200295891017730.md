---
key: 图片生成/反推提示词/qwen3.5批量快速批量打标_2042200295891017730.json
name: qwen3.5批量快速批量打标_2042200295891017730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/qwen3.5批量快速批量打标_2042200295891017730.json
hash: c97e297d1d1ffc93
coverage: 0.916667
learned_at: 2026-10-26 01:47:00
nodes: [ImageScaleToTotalPixels, HAIGC_SaveImagesToZip, RH_BatchImages, easy imageCount, easy forLoopStart, easy forLoopEnd, easy saveText, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, HAIGC_LoadImagesFromZip, PreviewImage]
patterns: []
missing: []
---

# 图片生成/反推提示词/qwen3.5批量快速批量打标_2042200295891017730.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/qwen3.5批量快速批量打标_2042200295891017730.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（12 个）：
- `ImageScaleToTotalPixels`
- `HAIGC_SaveImagesToZip`
- `RH_BatchImages`
- `easy imageCount`
- `easy forLoopStart`
- `easy forLoopEnd`
- `easy saveText`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `HAIGC_LoadImagesFromZip`
- `PreviewImage`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`ImageScaleToTotalPixels`、`HAIGC_SaveImagesToZip`、`RH_BatchImages`、`easy imageCount`、`easy forLoopStart`、`easy forLoopEnd`、`easy saveText`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`HAIGC_LoadImagesFromZip`

**用到的条目**：HAIGC_SaveImagesToZip、easy saveText、ImageScaleToTotalPixels、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、RH_BatchImages、RH_BatchImages
