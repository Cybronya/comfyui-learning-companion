---
key: Z_image-文生图高清放大(Qwen2.1提示词)_2094731166896189441.json
name: Z_image-文生图高清放大(Qwen2.1提示词)_2094731166896189441
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z_image-文生图高清放大(Qwen2.1提示词)_2094731166896189441.json
hash: 85f7e3c0191f6321
coverage: 0.733333
learned_at: 2026-10-10 20:59:17
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, CLIPLoader, VAELoader, CLIPTextEncode, TTResolutionSelector, KSampler, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, Switch any [Crystools], ConditioningZeroOut, ReferenceLatent, ReferenceLatent, KSampler, Image Comparer (rgthree), PreviewImage, ImageScaleToTotalPixels, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2, 忽略多组孤海, PrimitiveStringMultiline, CLIPLoader, CLIPTextEncode, 忽略多组孤海, TextConcatenator, TextGenerate, CR Text Concatenate, JsonExtractString, PreviewAny, PreviewImage, VAEDecode, VAEDecode, Image Comparer (rgthree), SaveImage, PrimitiveStringMultiline, YC Color Match, VAEEncode]
patterns: [text_to_image]
missing: [CR Text Concatenate, Switch any [Crystools], YC Color Match, 忽略多组孤海, 忽略多组孤海]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 417829131030824, "steps": 4, "width": 1920}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Switch any [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `YC Color Match` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Z_image-文生图高清放大(Qwen2.1提示词)_2094731166896189441.json

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

覆盖率 **73%**（33/45）

**有卡**：`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`CLIPTextEncode`、`TTResolutionSelector`、`KSampler`、`ConditioningZeroOut`、`ReferenceLatent`、`ImageScaleToTotalPixels`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SeedVR2`、`TextConcatenator`、`TextGenerate`、`JsonExtractString`、`VAEDecode`、`SaveImage`、`VAEEncode`

**缺卡**（5）：`CR Text Concatenate`、`Switch any [Crystools]`、`YC Color Match`、`忽略多组孤海`、`忽略多组孤海`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Switch any [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `YC Color Match` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
