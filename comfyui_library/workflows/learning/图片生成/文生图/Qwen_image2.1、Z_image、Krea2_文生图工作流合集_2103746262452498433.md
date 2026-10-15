---
key: 图片生成/文生图/Qwen_image2.1、Z_image、Krea2_文生图工作流合集_2103746262452498433.json
name: Qwen_image2.1、Z_image、Krea2_文生图工作流合集_2103746262452498433
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen_image2.1、Z_image、Krea2_文生图工作流合集_2103746262452498433.json
hash: ecf09fa46cc86617
coverage: 0.815068
learned_at: 2026-10-10 20:59:08
nodes: [JsonExtractString, TextGenerate, PrimitiveStringMultiline, UNETLoader, PrimitiveStringMultiline, TextConcatenator, CLIPLoader, UNETLoader, JsonExtractString, PrimitiveStringMultiline, TextConcatenator, CLIPLoader, VAELoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, UNETLoader, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, VAEDecode, ColorMatch, CLIPTextEncode, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, SeedVR2ExtraArgs, SeedVR2BlockSwap, VAEEncode, GetImageSize, ImageScaleToTotalPixels, CLIPLoader, VAELoader, UNETLoader, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, CLIPTextEncode, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, VAEEncode, GetImageSize, ImageScaleToTotalPixels, EmptyLatentImage, ModelSamplingAuraFlow, SeedVR2BlockSwap, SeedVR2, VAEDecode, ColorMatch, Seed (rgthree), VAEDecode, TextGenerate, KSampler, PreviewAny, GH_ImageVideoComparer, ImageSharpen, CLIPLoader, VAELoader, UNETLoader, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, CLIPTextEncode, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, VAEEncode, GetImageSize, ImageScaleToTotalPixels, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2, ColorMatch, GH_ImageVideoComparer, ImageSharpen, VAELoader, CLIPLoader, 孤海注释, EmptyLatentImage, ConditioningZeroOut, CLIPTextEncode, CLIPTextEncode, TextEncodeQwenImage21, EmptyLatentImage, Seed (rgthree), PreviewAny, VAEDecode, KSampler, GH_ImageVideoComparer, CLIPLoader, UNETLoader, VAELoader, 忽略多组孤海, 忽略多组孤海, VAEDecode, 孤海注释, CLIPLoader, KSampler, TextConcatenator, CLIPLoader, JsonExtractString, TextGenerate, PreviewAny, PrimitiveStringMultiline, PrimitiveStringMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveStringMultiline, LoraLoaderModelOnly, Any Switch (rgthree), CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, 忽略多组孤海, TTResolutionSelector, 孤海注释, 孤海注释, CR Text Concatenate, CR Text Concatenate, PreviewImage, SeedVR2, SaveImage, GH_ImageVideoComparer, GH_ImageVideoComparer, PreviewImage, ImageSharpen, PreviewImage, SaveImage, PreviewImage, GH_ImageVideoComparer, PreviewImage, SaveImage, SeedVR2ExtraArgs, VAEDecode, PreviewImage]
patterns: [text_to_image]
missing: [CR Text Concatenate, CR Text Concatenate, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, Seed (rgthree), Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler_ancestral", "scheduler": "beta57", "seed": 407210112866857, "steps": 8, "width": 1024}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen_image2.1、Z_image、Krea2_文生图工作流合集_2103746262452498433.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen_image2.1、Z_image、Krea2_文生图工作流合集_2103746262452498433.json`

## 结构

**节点**（146 个）：
- `JsonExtractString`
- `TextGenerate`
- `PrimitiveStringMultiline`
- `UNETLoader`
- `PrimitiveStringMultiline`
- `TextConcatenator`
- `CLIPLoader`
- `UNETLoader`
- `JsonExtractString`
- `PrimitiveStringMultiline`
- `TextConcatenator`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `ColorMatch`
- `CLIPTextEncode`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `VAEEncode`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced`
- `CLIPTextEncode`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEEncode`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `EmptyLatentImage`
- `ModelSamplingAuraFlow`
- `SeedVR2BlockSwap`
- `SeedVR2`
- `VAEDecode`
- `ColorMatch`
- `Seed (rgthree)`
- `VAEDecode`
- `TextGenerate`
- `KSampler`
- `PreviewAny`
- `GH_ImageVideoComparer`
- `ImageSharpen`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced`
- `CLIPTextEncode`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEEncode`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2`
- `ColorMatch`
- `GH_ImageVideoComparer`
- `ImageSharpen`
- `VAELoader`
- `CLIPLoader`
- `孤海注释`
- `EmptyLatentImage`
- `ConditioningZeroOut`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `TextEncodeQwenImage21`
- `EmptyLatentImage`
- `Seed (rgthree)`
- `PreviewAny`
- `VAEDecode`
- `KSampler`
- `GH_ImageVideoComparer`
- `CLIPLoader`
- `UNETLoader`
- `VAELoader`
- `忽略多组孤海`
- `忽略多组孤海`
- `VAEDecode`
- `孤海注释`
- `CLIPLoader`
- `KSampler`
- `TextConcatenator`
- `CLIPLoader`
- `JsonExtractString`
- `TextGenerate`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly`
- `Any Switch (rgthree)`
- `CLIPTextEncode`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `忽略多组孤海`
- `TTResolutionSelector`
- `孤海注释`
- `孤海注释`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `PreviewImage`
- `SeedVR2`
- `SaveImage`
- `GH_ImageVideoComparer`
- `GH_ImageVideoComparer`
- `PreviewImage`
- `ImageSharpen`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `GH_ImageVideoComparer`
- `PreviewImage`
- `SaveImage`
- `SeedVR2ExtraArgs`
- `VAEDecode`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta57`
- `seed` = `407210112866857`
- `steps` = `8`
- `width` = `1024`

## 知识

覆盖率 **82%**（119/146）

**有卡**：`JsonExtractString`、`TextGenerate`、`PrimitiveStringMultiline`、`UNETLoader`、`TextConcatenator`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`VAEDecode`、`ColorMatch`、`CLIPTextEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`VAEEncode`、`GetImageSize`、`ImageScaleToTotalPixels`、`EmptyLatentImage`、`ModelSamplingAuraFlow`、`SeedVR2`、`Seed (rgthree)`、`KSampler`、`PreviewAny`、`GH_ImageVideoComparer`、`ImageSharpen`、`孤海注释`、`TextEncodeQwenImage21`、`忽略多组孤海`

**缺卡**（7）：`CR Text Concatenate`、`CR Text Concatenate`、`忽略多组孤海`、`忽略多组孤海`、`忽略多组孤海`、`Seed (rgthree)`、`Seed (rgthree)`

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
