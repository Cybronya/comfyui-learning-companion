---
key: 图片生成/文生图/Ernie-Image-Turbo 4_8steps VS ErnieTurbo_extracted_lora VS Z-Image-Turbo_2045838209761939457.json
name: Ernie-Image-Turbo 4_8steps VS ErnieTurbo_extracted_lora VS Z-Image-Turbo_2045838209761939457
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Ernie-Image-Turbo 4_8steps VS ErnieTurbo_extracted_lora VS Z-Image-Turbo_2045838209761939457.json
hash: bec5e2c13b656bf2
coverage: 0.869565
learned_at: 2026-10-21 02:51:41
nodes: [CLIPLoader, CLIPTextEncode, VAELoader, LayerUtility: ImageReelComposit, KSamplerAdvanced, PreviewImage, Fast Groups Bypasser (rgthree), VAELoader, CLIPLoader, CLIPTextEncode, UNETLoader, UNETLoader, VAELoader, CLIPLoader, UNETLoader, VAELoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, SaveImage, PreviewImage, KSampler, ConditioningZeroOut, PreviewImage, KSampler, VAEDecode, ConditioningZeroOut, LoraLoaderModelOnly, PreviewImage, LayerUtility: ImageReel, VAEDecode, VAEDecode, VAEDecode, UNETLoader, KSampler, easy promptList, EmptyLatentImage, PrimitiveStringMultiline, SaveImage, easy promptList, CLIPTextEncode, ConditioningZeroOut, SaveImage, SaveImage, SaveImage, Seed (rgthree)]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1376, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 8, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Ernie-Image-Turbo 4_8steps VS ErnieTurbo_extracted_lora VS Z-Image-Turbo_2045838209761939457.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Ernie-Image-Turbo 4_8steps VS ErnieTurbo_extracted_lora VS Z-Image-Turbo_2045838209761939457.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LayerUtility: ImageReelComposit`
- `KSamplerAdvanced` ★核心
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `PreviewImage`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `LayerUtility: ImageReel`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `easy promptList`
- `EmptyLatentImage` ★核心
- `PrimitiveStringMultiline`
- `SaveImage`
- `easy promptList`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `Seed (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `768`
- `height` = `1376`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（40/46）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`LayerUtility: ImageReelComposit`、`KSamplerAdvanced`、`UNETLoader`、`ConditioningZeroOut`、`SaveImage`、`KSampler`、`VAEDecode`、`LoraLoaderModelOnly`、`LayerUtility: ImageReel`、`easy promptList`、`EmptyLatentImage`、`Seed (rgthree)`

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
