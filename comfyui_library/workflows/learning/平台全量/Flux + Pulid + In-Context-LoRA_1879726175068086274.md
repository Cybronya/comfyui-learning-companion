---
key: 平台全量/Flux + Pulid + In-Context-LoRA_1879726175068086274.json
name: Flux + Pulid + In-Context-LoRA_1879726175068086274
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux + Pulid + In-Context-LoRA_1879726175068086274.json
hash: 94876e4686fdde07
coverage: 0.746479
learned_at: 2026-11-14 00:27:27
nodes: [Reroute, CheckpointLoaderSimple, PreviewImage, PreviewImage, PreviewImage, ModelSamplingFlux, Reroute, Reroute, PreviewImage, PreviewImage, ApplyPulidFlux, PreviewImage, PulidFluxInsightFaceLoader, PulidFluxModelLoader, PulidFluxEvaClipLoader, EmptySD3LatentImage, PrimitiveNode, PrimitiveNode, CLIPTextEncode, VAEDecode, GetImageSize+, LoadImage, FloatConstant, FloatConstant, FloatConstant, VAEEncode, ControlNetApplySD3, UpscaleModelLoader, easy mathInt, easy mathInt, PreviewImage, Text Multiline, CLIPTextEncode, CLIPTextEncode, ImageCrop, PreviewImage, CLIPTextEncode, CLIPTextEncode, ImageCrop, Reroute, Text Multiline, PreviewImage, Text Multiline, CLIPTextEncode, CLIPTextEncode, ImageCrop, Reroute, PreviewImage, Text Multiline, CLIPTextEncode, CLIPTextEncode, ImageCrop, Text Multiline, FloatConstant, CLIPTextEncode, KSampler, KSampler, UltimateSDUpscale, VAEDecode, PreviewImage, LoraLoader, ControlNetLoader, UltimateSDUpscale, UltimateSDUpscale, UltimateSDUpscale, UltimateSDUpscale, SaveImage, SaveImage, SaveImage, SaveImage, Text Multiline]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "fluxFusionDSSmoothMerge4StepsAIO_v0Fp8E4m3fnAIO.safetensors", "controlnet_strength": 0.4, "denoise": 0.6, "lora_name": "sdxl_lightning_4step_lora.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 88888888, "steps": 4, "strength_clip": 1, "strength_model": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Flux + Pulid + In-Context-LoRA_1879726175068086274.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux + Pulid + In-Context-LoRA_1879726175068086274.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `Reroute`
- `CheckpointLoaderSimple` ★核心
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `ModelSamplingFlux`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `PreviewImage`
- `ApplyPulidFlux`
- `PreviewImage`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `PulidFluxEvaClipLoader`
- `EmptySD3LatentImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `GetImageSize+`
- `LoadImage`
- `FloatConstant`
- `FloatConstant`
- `FloatConstant`
- `VAEEncode` ★核心
- `ControlNetApplySD3` ★核心
- `UpscaleModelLoader`
- `easy mathInt`
- `easy mathInt`
- `PreviewImage`
- `Text Multiline`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageCrop`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageCrop`
- `Reroute`
- `Text Multiline`
- `PreviewImage`
- `Text Multiline`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageCrop`
- `Reroute`
- `PreviewImage`
- `Text Multiline`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageCrop`
- `Text Multiline`
- `FloatConstant`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `UltimateSDUpscale`
- `VAEDecode` ★核心
- `PreviewImage`
- `LoraLoader` ★核心
- `ControlNetLoader`
- `UltimateSDUpscale`
- `UltimateSDUpscale`
- `UltimateSDUpscale`
- `UltimateSDUpscale`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `Text Multiline`

**识别到的模式**：image_to_image、lora

## 关键参数

- `checkpoint` = `fluxFusionDSSmoothMerge4StepsAIO_v0Fp8E4m3fnAIO.safetensors`
- `controlnet_strength` = `0.4`
- `seed` = `88888888`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.6`
- `lora_name` = `sdxl_lightning_4step_lora.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **75%**（53/71）

**有卡**：`CheckpointLoaderSimple`、`ModelSamplingFlux`、`ApplyPulidFlux`、`PulidFluxInsightFaceLoader`、`PulidFluxModelLoader`、`PulidFluxEvaClipLoader`、`EmptySD3LatentImage`、`CLIPTextEncode`、`VAEDecode`、`GetImageSize+`、`LoadImage`、`FloatConstant`、`VAEEncode`、`ControlNetApplySD3`、`UpscaleModelLoader`、`easy mathInt`、`Text Multiline`、`ImageCrop`、`KSampler`、`UltimateSDUpscale`、`LoraLoader`、`ControlNetLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetApplySD3、ControlNetLoader、VAEEncode

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
