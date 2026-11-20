---
key: 平台全量/老照片修复Flux controlNet Upscale_1863501237047197698.json
name: 老照片修复Flux controlNet Upscale_1863501237047197698
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/老照片修复Flux controlNet Upscale_1863501237047197698.json
hash: d9b4e21371112d4b
coverage: 0.84
learned_at: 2026-11-14 02:30:06
nodes: [ConditioningZeroOut, CLIPTextEncode, Image Comparer (rgthree), PreviewImage, Molmo7BDbnb, ShowText|pysssss, FluxGuidance, LoadImage, ImageScaleBy, Note, LoraLoaderModelOnly, VAELoader, ControlNetLoader, DualCLIPLoader, UNETLoader, VAEEncode, ControlNetApplyAdvanced, LoraLoaderModelOnly, KSampler, easy cleanGpuUsed, easy cleanGpuUsed, ModelSamplingFlux, easy cleanGpuUsed, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 8, "controlnet_strength": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 213432112199377, "steps": 20}
---

# 平台全量/老照片修复Flux controlNet Upscale_1863501237047197698.json

> 来源文件 `comfyui_library/workflows/平台全量/老照片修复Flux controlNet Upscale_1863501237047197698.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `PreviewImage`
- `Molmo7BDbnb`
- `ShowText|pysssss`
- `FluxGuidance`
- `LoadImage`
- `ImageScaleBy`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `ControlNetLoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ModelSamplingFlux`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `1`
- `seed` = `213432112199377`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`ConditioningZeroOut`、`CLIPTextEncode`、`Molmo7BDbnb`、`FluxGuidance`、`LoadImage`、`ImageScaleBy`、`LoraLoaderModelOnly`、`VAELoader`、`ControlNetLoader`、`DualCLIPLoader`、`UNETLoader`、`VAEEncode`、`ControlNetApplyAdvanced`、`KSampler`、`easy cleanGpuUsed`、`ModelSamplingFlux`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
