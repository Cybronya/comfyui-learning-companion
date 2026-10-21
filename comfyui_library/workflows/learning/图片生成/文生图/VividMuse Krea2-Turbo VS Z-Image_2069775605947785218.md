---
key: 图片生成/文生图/VividMuse Krea2-Turbo VS Z-Image_2069775605947785218.json
name: VividMuse Krea2-Turbo VS Z-Image_2069775605947785218
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse Krea2-Turbo VS Z-Image_2069775605947785218.json
hash: 50bce3ec535c185c
coverage: 0.869565
learned_at: 2026-10-19 23:41:58
nodes: [CLIPLoader, UNETLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, VAEDecode, VAEDecode, VAELoader, CLIPLoader, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, UNETLoader, LoraLoaderModelOnly, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyLatentImage, PreviewImage, ConditioningZeroOut, CLIPTextEncode, easy promptConcat, PreviewImage, PreviewImage, LayerUtility: ImageReel, LayerColor: ColorAdapter, VAEDecode, ResolutionSelector, PrimitiveStringMultiline, Seed (rgthree), easy promptList, SaveImage, easy promptList, KSampler, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), easy promptList, SaveImage, SaveImage, SaveImage, LayerUtility: ImageReelComposit, easy promptList]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "er_sde", "scheduler": "simple", "seed": 0, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/VividMuse Krea2-Turbo VS Z-Image_2069775605947785218.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse Krea2-Turbo VS Z-Image_2069775605947785218.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `easy promptConcat`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: ImageReel`
- `LayerColor: ColorAdapter`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `Seed (rgthree)`
- `easy promptList`
- `SaveImage`
- `easy promptList`
- `KSampler` ★核心
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `easy promptList`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `LayerUtility: ImageReelComposit`
- `easy promptList`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（40/46）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAEDecode`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`easy promptConcat`、`LayerUtility: ImageReel`、`LayerColor: ColorAdapter`、`ResolutionSelector`、`Seed (rgthree)`、`easy promptList`、`SaveImage`、`KSampler`、`LayerUtility: ImageReelComposit`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
