---
key: Qwen_image2.1+Z_image+Krea2三模型文生图合集工作流_2104673944501575681.json
name: Qwen_image2.1+Z_image+Krea2三模型文生图合集工作流_2104673944501575681
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen_image2.1+Z_image+Krea2三模型文生图合集工作流_2104673944501575681.json
hash: 713fe69439d82cbf
coverage: 0.857143
learned_at: 2026-10-10 20:59:08
nodes: [JsonExtractString, TextGenerate, PrimitiveStringMultiline, UNETLoader, PrimitiveStringMultiline, TextConcatenator, CLIPLoader, UNETLoader, JsonExtractString, PrimitiveStringMultiline, TextConcatenator, CLIPLoader, VAELoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, UNETLoader, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, VAEDecode, ColorMatch, CLIPTextEncode, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, SeedVR2ExtraArgs, SeedVR2BlockSwap, VAEEncode, GetImageSize, ImageScaleToTotalPixels, CLIPLoader, VAELoader, UNETLoader, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, CLIPTextEncode, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, VAEEncode, GetImageSize, ImageScaleToTotalPixels, EmptyLatentImage, ModelSamplingAuraFlow, SeedVR2BlockSwap, SeedVR2, VAEDecode, ColorMatch, Seed (rgthree), VAEDecode, TextGenerate, KSampler, PreviewAny, GH_ImageVideoComparer, ImageSharpen, CLIPLoader, VAELoader, UNETLoader, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, CLIPTextEncode, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, VAEEncode, GetImageSize, ImageScaleToTotalPixels, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2, ColorMatch, GH_ImageVideoComparer, ImageSharpen, VAELoader, CLIPLoader, EmptyLatentImage, ConditioningZeroOut, CLIPTextEncode, CLIPTextEncode, TextEncodeQwenImage21, EmptyLatentImage, Seed (rgthree), PreviewAny, VAEDecode, KSampler, GH_ImageVideoComparer, CLIPLoader, UNETLoader, VAELoader, VAEDecode, CLIPLoader, KSampler, TextConcatenator, CLIPLoader, JsonExtractString, TextGenerate, PreviewAny, PrimitiveStringMultiline, PrimitiveStringMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveStringMultiline, LoraLoaderModelOnly, Any Switch (rgthree), CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, TTResolutionSelector, CR Text Concatenate, CR Text Concatenate, PreviewImage, SeedVR2, SaveImage, GH_ImageVideoComparer, GH_ImageVideoComparer, PreviewImage, ImageSharpen, PreviewImage, SaveImage, PreviewImage, GH_ImageVideoComparer, PreviewImage, SaveImage, SeedVR2ExtraArgs, VAEDecode, PreviewImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CR Text Concatenate, CR Text Concatenate, Seed (rgthree), Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen_image2.1+Z_image+Krea2三模型文生图合集工作流_2104673944501575681.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen_image2.1+Z_image+Krea2三模型文生图合集工作流_2104673944501575681.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（168 个）：
- `JsonExtractString`
- `TextGenerate`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `TextConcatenator`
- `CLIPLoader`
- `UNETLoader` ★核心
- `JsonExtractString`
- `PrimitiveStringMultiline`
- `TextConcatenator`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ColorMatch`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `VAEEncode` ★核心
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `EmptyLatentImage` ★核心
- `ModelSamplingAuraFlow`
- `SeedVR2BlockSwap`
- `SeedVR2`
- `VAEDecode` ★核心
- `ColorMatch`
- `Seed (rgthree)`
- `VAEDecode` ★核心
- `TextGenerate`
- `KSampler` ★核心
- `PreviewAny`
- `GH_ImageVideoComparer`
- `ImageSharpen`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEEncode` ★核心
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
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `Seed (rgthree)`
- `PreviewAny`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `GH_ImageVideoComparer`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `TextConcatenator`
- `CLIPLoader`
- `JsonExtractString`
- `TextGenerate`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `Any Switch (rgthree)`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `TTResolutionSelector`
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
- `VAEDecode` ★核心
- `PreviewImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **86%**（144/168）

**有卡**：`JsonExtractString`、`TextGenerate`、`UNETLoader`、`TextConcatenator`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`VAEDecode`、`ColorMatch`、`CLIPTextEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`VAEEncode`、`GetImageSize`、`ImageScaleToTotalPixels`、`EmptyLatentImage`、`ModelSamplingAuraFlow`、`SeedVR2`、`KSampler`、`GH_ImageVideoComparer`、`ImageSharpen`、`TextEncodeQwenImage21`、`TTResolutionSelector`、`SaveImage`、`solarL_SaveImagesToZip`

**缺卡**（4）：`CR Text Concatenate`、`CR Text Concatenate`、`Seed (rgthree)`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
