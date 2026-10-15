---
key: 图片生成/文生图/Z_image-文生图高清放大(Qwen2.1提示词)_2094731166896189441.json
name: Z_image-文生图高清放大(Qwen2.1提示词)_2094731166896189441
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z_image-文生图高清放大(Qwen2.1提示词)_2094731166896189441.json
hash: 85f7e3c0191f6321
coverage: 0.844444
learned_at: 2026-10-15 22:27:41
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, CLIPLoader, VAELoader, CLIPTextEncode, TTResolutionSelector, KSampler, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, Switch any [Crystools], ConditioningZeroOut, ReferenceLatent, ReferenceLatent, KSampler, Image Comparer (rgthree), PreviewImage, ImageScaleToTotalPixels, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2, 忽略多组孤海, PrimitiveStringMultiline, CLIPLoader, CLIPTextEncode, 忽略多组孤海, TextConcatenator, TextGenerate, CR Text Concatenate, JsonExtractString, PreviewAny, PreviewImage, VAEDecode, VAEDecode, Image Comparer (rgthree), SaveImage, PrimitiveStringMultiline, YC Color Match, VAEEncode]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 417829131030824, "steps": 4, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z_image-文生图高清放大(Qwen2.1提示词)_2094731166896189441.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z_image-文生图高清放大(Qwen2.1提示词)_2094731166896189441.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `TTResolutionSelector`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Switch any [Crystools]`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2`
- `忽略多组孤海`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `忽略多组孤海`
- `TextConcatenator`
- `TextGenerate`
- `CR Text Concatenate`
- `JsonExtractString`
- `PreviewAny`
- `PreviewImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `PrimitiveStringMultiline`
- `YC Color Match`
- `VAEEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `417829131030824`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（38/45）

**有卡**：`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`CLIPTextEncode`、`TTResolutionSelector`、`KSampler`、`Switch any [Crystools]`、`ConditioningZeroOut`、`ReferenceLatent`、`ImageScaleToTotalPixels`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SeedVR2`、`忽略多组孤海`、`TextConcatenator`、`TextGenerate`、`CR Text Concatenate`、`JsonExtractString`、`VAEDecode`、`SaveImage`、`YC Color Match`、`VAEEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
