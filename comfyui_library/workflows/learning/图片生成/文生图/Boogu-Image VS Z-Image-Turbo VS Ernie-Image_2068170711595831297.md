---
key: 图片生成/文生图/Boogu-Image VS Z-Image-Turbo VS Ernie-Image_2068170711595831297.json
name: Boogu-Image VS Z-Image-Turbo VS Ernie-Image_2068170711595831297
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Boogu-Image VS Z-Image-Turbo VS Ernie-Image_2068170711595831297.json
hash: 9f761f38d5bde3a3
coverage: 0.953488
learned_at: 2026-10-19 23:21:17
nodes: [UNETLoader, CLIPLoader, CLIPTextEncode, CLIPLoader, CLIPTextEncode, VAELoader, CLIPTextEncode, KSampler, UNETLoader, CLIPLoader, LayerUtility: ImageReelComposit, SaveImage, VAEDecode, VAEDecode, VAEDecode, VAELoader, VAELoader, VAELoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, UNETLoader, LoraLoaderModelOnly, EmptyLatentImage, VAEDecode, LayerUtility: ImageReel, UNETLoader, KSampler, CLIPTextEncode, CLIPTextEncode, KSampler, SaveImage, SaveImage, SaveImage, SaveImage, Seed (rgthree), CLIPTextEncode, KSampler, PrimitiveStringMultiline, easy promptList, easy promptList, Fast Groups Bypasser (rgthree), ResolutionSelector]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 5, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 50, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Boogu-Image VS Z-Image-Turbo VS Ernie-Image_2068170711595831297.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Boogu-Image VS Z-Image-Turbo VS Ernie-Image_2068170711595831297.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `PrimitiveStringMultiline`
- `easy promptList`
- `easy promptList`
- `Fast Groups Bypasser (rgthree)`
- `ResolutionSelector`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `0`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（41/43）

**有卡**：`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`KSampler`、`LayerUtility: ImageReelComposit`、`SaveImage`、`VAEDecode`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`LayerUtility: ImageReel`、`Seed (rgthree)`、`easy promptList`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
