---
key: 图片生成/文生图/VividMuse Z-Image-Engineer-V6-Workflow_2065785395203362818.json
name: VividMuse Z-Image-Engineer-V6-Workflow_2065785395203362818
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image-Engineer-V6-Workflow_2065785395203362818.json
hash: 0093519a11b50e3a
coverage: 0.913043
learned_at: 2026-10-19 23:21:46
nodes: [VAEDecode, VAEDecode, CLIPTextEncode, VAEDecode, LoraLoaderModelOnly, PreviewImage, VAELoader, CLIPLoader, KSamplerAdvanced, ConditioningZeroOut, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAEDecode, CLIPTextEncode, VAEDecode, LoraLoaderModelOnly, PreviewImage, VAELoader, KSamplerAdvanced, ConditioningZeroOut, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPTextEncode, ConditioningZeroOut, VAELoader, KSampler, UNETLoader, UNETLoader, CLIPLoader, CLIPTextEncode, KSampler, VAELoader, ConditioningZeroOut, LayerUtility: ImageReelComposit, VAEDecode, VAEDecode, LayerColor: ColorAdapter, LayerColor: ColorAdapter, SaveImage, LayerUtility: ImageReel, EmptyLatentImage, UNETLoader, SaveImage, PreviewImage, PreviewImage, SaveImage, SaveImage, LoraLoaderModelOnly, SaveImage, Fast Groups Bypasser (rgthree), Seed (rgthree), ClipLoaderGGUF, ClipLoaderGGUF, easy promptList, PrimitiveStringMultiline, LoraLoaderModelOnly, easy promptList]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 11111, "steps": 8, "width": 1536}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/VividMuse Z-Image-Engineer-V6-Workflow_2065785395203362818.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image-Engineer-V6-Workflow_2065785395203362818.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `VAELoader`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `LayerUtility: ImageReelComposit`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LayerColor: ColorAdapter`
- `LayerColor: ColorAdapter`
- `SaveImage`
- `LayerUtility: ImageReel`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Seed (rgthree)`
- `ClipLoaderGGUF`
- `ClipLoaderGGUF`
- `easy promptList`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `easy promptList`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `11111`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`
- `width` = `1536`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（63/69）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`KSamplerAdvanced`、`ConditioningZeroOut`、`UNETLoader`、`KSampler`、`LayerUtility: ImageReelComposit`、`LayerColor: ColorAdapter`、`SaveImage`、`LayerUtility: ImageReel`、`EmptyLatentImage`、`Seed (rgthree)`、`ClipLoaderGGUF`、`easy promptList`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
