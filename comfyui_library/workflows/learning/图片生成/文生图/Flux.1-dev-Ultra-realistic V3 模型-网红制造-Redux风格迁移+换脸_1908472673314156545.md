---
key: 图片生成/文生图/Flux.1-dev-Ultra-realistic V3 模型-网红制造-Redux风格迁移+换脸_1908472673314156545.json
name: Flux.1-dev-Ultra-realistic V3 模型-网红制造-Redux风格迁移+换脸_1908472673314156545
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-dev-Ultra-realistic V3 模型-网红制造-Redux风格迁移+换脸_1908472673314156545.json
hash: df8a0c96830b5556
coverage: 0.574074
learned_at: 2026-10-10 20:58:36
nodes: [Anything Everywhere, Anything Everywhere, EmptyLatentImagePresets, SetNode, SetNode, SetNode, LoadImage, SetNode, LoadImage, CLIPTextEncode, StyleModelLoader, CLIPVisionLoader, GetNode, CLIPTextEncode, SetNode, CLIPVisionEncode, StyleModelApplySimple, FluxGuidance, SetNode, ImageUpscaleWithModel, SamplerCustom, GetNode, KSamplerSelect, BasicScheduler, ApplyPulidFlux, SetNode, GetNode, VAEDecode, SetNode, EmptySD3LatentImage, GetNode, GetNode, ModelSamplingFlux, GetNode, PulidFluxInsightFaceLoader, PulidFluxModelLoader, PulidFluxEvaClipLoader, GetNode, GetNode, GetNode, SaveImage, UltimateSDUpscale, UpscaleModelLoader, ImageScaleBy, VAEEncode, KSampler, GetNode, PreviewImage, VAEDecode, GetNode, DualCLIPLoader, VAELoader, CheckpointLoaderSimple, SetNode]
patterns: [image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Flux.1-dev-fp8-Ultra-realistic_V3超写实艺术增强.safetensors", "denoise": 0.6000000000000001, "height": true, "sampler_name": "euler", "scheduler": "simple", "seed": 724594132749584, "steps": 10, "width": "1344 x 768 (1.75:1)"}
---

# 图片生成/文生图/Flux.1-dev-Ultra-realistic V3 模型-网红制造-Redux风格迁移+换脸_1908472673314156545.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1-dev-Ultra-realistic V3 模型-网红制造-Redux风格迁移+换脸_1908472673314156545.json`

## 结构

**节点**（54 个）：
- `Anything Everywhere`
- `Anything Everywhere`
- `EmptyLatentImagePresets`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `CLIPTextEncode`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `GetNode`
- `CLIPTextEncode`
- `SetNode`
- `CLIPVisionEncode`
- `StyleModelApplySimple`
- `FluxGuidance`
- `SetNode`
- `ImageUpscaleWithModel`
- `SamplerCustom`
- `GetNode`
- `KSamplerSelect`
- `BasicScheduler`
- `ApplyPulidFlux`
- `SetNode`
- `GetNode`
- `VAEDecode`
- `SetNode`
- `EmptySD3LatentImage`
- `GetNode`
- `GetNode`
- `ModelSamplingFlux`
- `GetNode`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `PulidFluxEvaClipLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `SaveImage`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `ImageScaleBy`
- `VAEEncode`
- `KSampler`
- `GetNode`
- `PreviewImage`
- `VAEDecode`
- `GetNode`
- `DualCLIPLoader`
- `VAELoader`
- `CheckpointLoaderSimple`
- `SetNode`

**识别到的模式**：image_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `checkpoint` = `Flux.1-dev-fp8-Ultra-realistic_V3超写实艺术增强.safetensors`
- `denoise` = `0.6000000000000001`
- `height` = `True`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `724594132749584`
- `steps` = `10`
- `width` = `1344 x 768 (1.75:1)`

## 知识

覆盖率 **57%**（31/54）

**有卡**：`Anything Everywhere`、`EmptyLatentImagePresets`、`SetNode`、`LoadImage`、`CLIPTextEncode`、`StyleModelLoader`、`CLIPVisionLoader`、`GetNode`、`CLIPVisionEncode`、`StyleModelApplySimple`、`FluxGuidance`、`ImageUpscaleWithModel`、`SamplerCustom`、`KSamplerSelect`、`BasicScheduler`、`ApplyPulidFlux`、`VAEDecode`、`EmptySD3LatentImage`
