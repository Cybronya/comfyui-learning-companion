---
key: 图片生成/图生图/Super Upscale _ High Resolution_1925848175574208513.json
name: Super Upscale _ High Resolution_1925848175574208513
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Super Upscale _ High Resolution_1925848175574208513.json
hash: fd1ed0336c258a1c
coverage: 0.515152
learned_at: 2026-10-23 11:26:18
nodes: [Florence2ModelLoader, easy imageSize, easy cleanGpuUsed, EmptySD3LatentImage, BasicScheduler, KSamplerSelect, BasicGuider, RandomNoise, Reroute, Reroute, Reroute, FluxGuidance, Reroute, Reroute, Reroute, ConditioningZeroOut, Reroute, KSampler, Reroute, VAEEncode, Reroute, Reroute, ImageUpscaleWithModel, Reroute, Reroute, Reroute, FluxGuidance, ConditioningZeroOut, DualCLIPLoader, Reroute, Reroute, Reroute, Reroute, Reroute, UpscaleModelLoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, easy cleanGpuUsed, Reroute, ConstrainImage|pysssss, SamplerCustomAdvanced, Reroute, Reroute, Reroute, Reroute, ControlNetLoader, Reroute, ControlNetLoader, ConstrainImage|pysssss, easy cleanGpuUsed, easy imageSize, Reroute, Reroute, FluxGuidance, LoraLoaderModelOnly, LoraLoaderModelOnly, ControlNetApplySD3, PreviewImage, FluxUnionControlNetApply, LoraLoaderModelOnly, easy cleanGpuUsed, easy cleanGpuUsed, UltimateSDUpscale, Reroute, Reroute, SaveImage, PrimitiveFloat, ImageScaleBy, Reroute, ImageUpscaleWithModel, ConstrainImage|pysssss, easy imageSizeBySide, Reroute, LoadImage, Reroute, Reroute, VAEDecode, easy cleanGpuUsed, Image Comparer (rgthree), Image Comparer (rgthree), PreviewImage, PreviewImage, PreviewImage, PreviewImage, Florence2Run, CR Text Concatenate, easy showAnything, TextBox, CheckpointLoaderSimple, VAELoader, CLIPTextEncode, VAEDecode, ColorMatch, ColorMatch, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "STOIQONewrealityFLUXSD_F1DAlpha.safetensors", "controlnet_strength": "tile", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 686012002925834, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Super Upscale _ High Resolution_1925848175574208513.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Super Upscale _ High Resolution_1925848175574208513.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（99 个）：
- `Florence2ModelLoader`
- `easy imageSize`
- `easy cleanGpuUsed`
- `EmptySD3LatentImage`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `Reroute`
- `Reroute`
- `Reroute`
- `FluxGuidance`
- `Reroute`
- `Reroute`
- `Reroute`
- `ConditioningZeroOut`
- `Reroute`
- `KSampler` ★核心
- `Reroute`
- `VAEEncode` ★核心
- `Reroute`
- `Reroute`
- `ImageUpscaleWithModel`
- `Reroute`
- `Reroute`
- `Reroute`
- `FluxGuidance`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `UpscaleModelLoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `ConstrainImage|pysssss`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ControlNetLoader`
- `Reroute`
- `ControlNetLoader`
- `ConstrainImage|pysssss`
- `easy cleanGpuUsed`
- `easy imageSize`
- `Reroute`
- `Reroute`
- `FluxGuidance`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ControlNetApplySD3` ★核心
- `PreviewImage`
- `FluxUnionControlNetApply` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `UltimateSDUpscale`
- `Reroute`
- `Reroute`
- `SaveImage`
- `PrimitiveFloat`
- `ImageScaleBy`
- `Reroute`
- `ImageUpscaleWithModel`
- `ConstrainImage|pysssss`
- `easy imageSizeBySide`
- `Reroute`
- `LoadImage`
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `Florence2Run`
- `CR Text Concatenate`
- `easy showAnything`
- `TextBox`
- `CheckpointLoaderSimple` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ColorMatch`
- `ColorMatch`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `686012002925834`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `tile`
- `checkpoint` = `STOIQONewrealityFLUXSD_F1DAlpha.safetensors`

## 知识

覆盖率 **52%**（51/99）

**有卡**：`Florence2ModelLoader`、`easy imageSize`、`easy cleanGpuUsed`、`EmptySD3LatentImage`、`BasicScheduler`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`FluxGuidance`、`ConditioningZeroOut`、`KSampler`、`VAEEncode`、`ImageUpscaleWithModel`、`DualCLIPLoader`、`UpscaleModelLoader`、`ConstrainImage|pysssss`、`SamplerCustomAdvanced`、`ControlNetLoader`、`LoraLoaderModelOnly`、`ControlNetApplySD3`、`FluxUnionControlNetApply`、`UltimateSDUpscale`、`SaveImage`、`ImageScaleBy`、`easy imageSizeBySide`、`LoadImage`、`VAEDecode`、`Florence2Run`、`CR Text Concatenate`、`TextBox`、`CheckpointLoaderSimple`、`VAELoader`、`CLIPTextEncode`、`ColorMatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
