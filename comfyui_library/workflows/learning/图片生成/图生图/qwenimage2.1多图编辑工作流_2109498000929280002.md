---
key: 图片生成/图生图/qwenimage2.1多图编辑工作流_2109498000929280002.json
name: qwenimage2.1多图编辑工作流_2109498000929280002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwenimage2.1多图编辑工作流_2109498000929280002.json
hash: 5e9e3f7b76ec3432
coverage: 0.8
learned_at: 2026-10-23 11:44:20
nodes: [ComfySwitchNode, QwenImage21Cache, EmptyLatentImage, ImageRemoveAlpha+, ImageUpscaleWithModel, VAEDecode, PreviewAny, TextEncodeQwenImage21, llama_cpp_instruct_adv, PrimitiveStringMultiline, PrimitiveStringMultiline, XB_BatchImages, LoadImage, LoadImage, LoadImage, LoadImage, SaveImage, UNETLoader, CLIPLoader, VAELoader, PrimitiveStringMultiline, UpscaleModelLoader, llama_cpp_parameters, llama_cpp_model_loader, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1376, "sampler_name": "euler", "scheduler": "simple", "seed": 238390854083009, "steps": 25, "width": 1184}
---

# 图片生成/图生图/qwenimage2.1多图编辑工作流_2109498000929280002.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwenimage2.1多图编辑工作流_2109498000929280002.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `ComfySwitchNode`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `ImageRemoveAlpha+`
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `PreviewAny`
- `TextEncodeQwenImage21`
- `llama_cpp_instruct_adv`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `XB_BatchImages`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveStringMultiline`
- `UpscaleModelLoader`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `KSampler` ★核心

## 关键参数

- `width` = `1184`
- `height` = `1376`
- `batch_size` = `1`
- `seed` = `238390854083009`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（20/25）

**有卡**：`QwenImage21Cache`、`EmptyLatentImage`、`ImageRemoveAlpha+`、`ImageUpscaleWithModel`、`VAEDecode`、`TextEncodeQwenImage21`、`llama_cpp_instruct_adv`、`XB_BatchImages`、`LoadImage`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`UpscaleModelLoader`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
