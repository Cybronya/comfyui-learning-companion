---
key: 平台全量/ComfyUI In-Context Edit_1921752752244867074.json
name: ComfyUI In-Context Edit_1921752752244867074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ComfyUI In-Context Edit_1921752752244867074.json
hash: 45decdb7c03337bf
coverage: 0.8
learned_at: 2026-11-14 00:22:17
nodes: [ICEFConditioning, UNETLoader, VAEDecode, PreviewImage, DualCLIPLoader, VAELoader, FluxGuidance, MaskPreview, KSamplerAdvanced, UpscaleModelLoader, ImageUpscaleWithModel, ConditioningZeroOut, LoraLoaderModelOnly, ImageCrop, ImageCrop, PreviewImage, easy cleanGpuUsed, easy cleanGpuUsed, Note, Image Comparer (rgthree), ImageCrop, SaveImage, DiptychCreate, Note, InContextEditInstruction]
patterns: []
missing: []
parameters: {"cfg": 28, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 平台全量/ComfyUI In-Context Edit_1921752752244867074.json

> 来源文件 `comfyui_library/workflows/平台全量/ComfyUI In-Context Edit_1921752752244867074.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `ICEFConditioning`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `DualCLIPLoader`
- `VAELoader`
- `FluxGuidance`
- `MaskPreview`
- `KSamplerAdvanced` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `ImageCrop`
- `ImageCrop`
- `PreviewImage`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `Note`
- `Image Comparer (rgthree)`
- `ImageCrop`
- `SaveImage`
- `DiptychCreate`
- `Note`
- `InContextEditInstruction`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `28`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **80%**（20/25）

**有卡**：`ICEFConditioning`、`UNETLoader`、`VAEDecode`、`DualCLIPLoader`、`VAELoader`、`FluxGuidance`、`MaskPreview`、`KSamplerAdvanced`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`ImageCrop`、`easy cleanGpuUsed`、`SaveImage`、`DiptychCreate`、`InContextEditInstruction`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、ConditioningZeroOut、FluxGuidance、KSamplerAdvanced、DualCLIPLoader
