---
key: 图片生成/图生图/Qwen image2.1最强开源模型图像编辑整合工作流 全能改图_2105410925342846978.json
name: Qwen image2.1最强开源模型图像编辑整合工作流 全能改图_2105410925342846978
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image2.1最强开源模型图像编辑整合工作流 全能改图_2105410925342846978.json
hash: 87d99c68b03436de
coverage: 0.878505
learned_at: 2026-10-21 00:43:03
nodes: [CLIPLoader, VAELoader, UNETLoader, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, CLIPTextEncode, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, SeedVR2, SeedVR2ExtraArgs, SeedVR2BlockSwap, ImageScaleToTotalPixels, Image Compare (mtb), SaveImageAdvanced, TextGenerate, CLIPLoader, PrimitiveStringMultiline, CR Text Concatenate, JsonExtractString, TextConcatenator, LoadImage, SDPoseOODLoader, YOLOModelLoader, SDPoseOODProcessor, PreviewImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PreviewImage, GH_ImageVideoComparer, LoadImage, VAEEncode, VAEDecode, GetImageSize, ImageSharpen, Any Switch (rgthree), UNETLoader, CLIPLoader, LoadImage, PrimitiveStringMultiline, ColorMatch, SaveImage, VAELoader, TextEncodeQwenImage21, VAEEncode, KSampler, EmptyLatentImage, ResolutionSelector, Seed (rgthree), SaveImage, LoadImage, ComfySwitchNode, VAEDecode, LoraLoaderModelOnly, PreviewAny, PrimitiveStringMultiline, MaskFillHoles, LayerMask: MaskGrow, ImageAndMaskPreview, SetLatentNoiseMask, 孤海图像缩放按像素, Fast Groups Bypasser (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image2.1最强开源模型图像编辑整合工作流 全能改图_2105410925342846978.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image2.1最强开源模型图像编辑整合工作流 全能改图_2105410925342846978.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（107 个）：
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
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `SeedVR2`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `ImageScaleToTotalPixels`
- `Image Compare (mtb)`
- `SaveImageAdvanced`
- `TextGenerate`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `CR Text Concatenate`
- `JsonExtractString`
- `TextConcatenator`
- `LoadImage`
- `SDPoseOODLoader`
- `YOLOModelLoader`
- `SDPoseOODProcessor`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `GH_ImageVideoComparer`
- `LoadImage`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `GetImageSize`
- `ImageSharpen`
- `Any Switch (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ColorMatch`
- `SaveImage`
- `VAELoader`
- `TextEncodeQwenImage21`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `Seed (rgthree)`
- `SaveImage`
- `LoadImage`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewAny`
- `PrimitiveStringMultiline`
- `MaskFillHoles`
- `LayerMask: MaskGrow`
- `ImageAndMaskPreview`
- `SetLatentNoiseMask`
- `孤海图像缩放按像素`
- `Fast Groups Bypasser (rgthree)`
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

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（94/107）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`ImageScaleToTotalPixels`、`SeedVR2`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`Image Compare (mtb)`、`SaveImageAdvanced`、`TextGenerate`、`CR Text Concatenate`、`JsonExtractString`、`TextConcatenator`、`LoadImage`、`SDPoseOODLoader`、`YOLOModelLoader`、`SDPoseOODProcessor`、`GH_ImageVideoComparer`、`VAEEncode`、`VAEDecode`、`GetImageSize`、`ImageSharpen`、`ColorMatch`、`SaveImage`、`TextEncodeQwenImage21`、`KSampler`、`EmptyLatentImage`、`ResolutionSelector`、`Seed (rgthree)`、`LoraLoaderModelOnly`、`MaskFillHoles`、`LayerMask: MaskGrow`、`ImageAndMaskPreview`、`SetLatentNoiseMask`、`孤海图像缩放按像素`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
