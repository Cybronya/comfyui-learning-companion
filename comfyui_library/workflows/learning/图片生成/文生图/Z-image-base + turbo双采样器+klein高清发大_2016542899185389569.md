---
key: 图片生成/文生图/Z-image-base + turbo双采样器+klein高清发大_2016542899185389569.json
name: Z-image-base + turbo双采样器+klein高清发大_2016542899185389569
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image-base + turbo双采样器+klein高清发大_2016542899185389569.json
hash: a9fadcefdafce8f8
coverage: 0.941176
learned_at: 2026-10-19 22:15:30
nodes: [VAELoader, CLIPLoader, UNETLoader, ModelSamplingAuraFlow, ModelSamplingAuraFlow, UNETLoader, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, VAELoader, UNETLoader, ConditioningZeroOut, LoraLoaderModelOnly, EmptyFlux2LatentImage, GetImageSize, VAEEncode, ReferenceLatent, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text, KSampler, PreviewImage, EmptyLatentImage, Int, Int, ConditioningZeroOut, VAEDecode, LayerUtility: ImageReelComposit, PreviewImage, VAEDecode, SaveImage, LayerUtility: ImageReel, CLIPTextEncode]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1664, "sampler_name": "euler", "scheduler": "simple", "seed": 13244427768246, "steps": 4, "width": 928}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-image-base + turbo双采样器+klein高清发大_2016542899185389569.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image-base + turbo双采样器+klein高清发大_2016542899185389569.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Prompt Text`
- `KSampler` ★核心
- `PreviewImage`
- `EmptyLatentImage` ★核心
- `Int`
- `Int`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `LayerUtility: ImageReel`
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `13244427768246`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `928`
- `height` = `1664`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（32/34）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`KSamplerAdvanced`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`EmptyFlux2LatentImage`、`GetImageSize`、`VAEEncode`、`ReferenceLatent`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`、`KSampler`、`EmptyLatentImage`、`Int`、`VAEDecode`、`LayerUtility: ImageReelComposit`、`SaveImage`、`LayerUtility: ImageReel`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
