---
key: 图片生成/文生图/Z_image-文生图高清放大(Qwen2.1提示词)_2094731166896189441.json
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

# 图片生成/文生图/Z_image-文生图高清放大(Qwen2.1提示词)_2094731166896189441.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z_image-文生图高清放大(Qwen2.1提示词)_2094731166896189441.json`

## 结构

**节点**（45 个）：
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `TTResolutionSelector`
- `KSampler`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `Switch any [Crystools]`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `KSampler`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2`
- `忽略多组孤海`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `CLIPTextEncode`
- `忽略多组孤海`
- `TextConcatenator`
- `TextGenerate`
- `CR Text Concatenate`
- `JsonExtractString`
- `PreviewAny`
- `PreviewImage`
- `VAEDecode`
- `VAEDecode`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PrimitiveStringMultiline`
- `YC Color Match`
- `VAEEncode`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1080`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `417829131030824`
- `steps` = `4`
- `width` = `1920`

## 知识

覆盖率 **73%**（33/45）

**有卡**：`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`CLIPTextEncode`、`TTResolutionSelector`、`KSampler`、`Switch any [Crystools]`、`ConditioningZeroOut`、`ReferenceLatent`、`Image Comparer (rgthree)`、`PreviewImage`、`ImageScaleToTotalPixels`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SeedVR2`、`忽略多组孤海`、`PrimitiveStringMultiline`、`TextConcatenator`

**缺卡**（5）：`CR Text Concatenate`、`Switch any [Crystools]`、`YC Color Match`、`忽略多组孤海`、`忽略多组孤海`

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
