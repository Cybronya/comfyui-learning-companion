---
key: 图片生成/图生图/Qwen image2.1最强开源模型 图像编辑整合处理工具_2114088484360245249.json
name: Qwen image2.1最强开源模型 图像编辑整合处理工具_2114088484360245249
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image2.1最强开源模型 图像编辑整合处理工具_2114088484360245249.json
hash: a06317d84c4ba66f
coverage: 0.736842
learned_at: 2026-10-26 22:03:17
nodes: [CLIPLoader, VAELoader, UNETLoader, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, CLIPTextEncode, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, Image Compare (mtb), TextConcatenator, LoadImage, LoadImage, PreviewImage, VAEEncode, VAEDecode, GetImageSize, ImageSharpen, LoadImage, ColorMatch, SaveImage, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, SetNode, SetNode, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, SetNode, SaveImage, SDPoseOODProcessor, SDPoseOODLoader, GetNode, YOLOModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, GetNode, SetNode, SetNode, PrimitiveStringMultiline, ImageScaleToTotalPixels, SeedVR2BlockSwap, SaveImageAdvanced, SeedVR2, SeedVR2ExtraArgs, LoadImage, LoadImage, GH_ImageVideoComparer, PreviewImage, LoadImage, SetNode, GetNode, TextGenerate, ImageConcanate, DrawMaskOnImage, SimpleMath+, SetLatentNoiseMask, InpaintStitchImproved, PrimitiveStringMultiline, CLIPLoader, JsonExtractString, CR Text Concatenate, SaveImage, PreviewAny, INTConstant, PreviewImage, PreviewImage, UNETLoader, CLIPLoader, VAELoader, ImageScaleToTotalPixels, InpaintCropImproved, VAEEncode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, Any Switch (rgthree), EmptyLatentImage, ResolutionSelector, TextEncodeQwenImage21, VAEDecode, Seed (rgthree), ComfySwitchNode, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, KSampler, ComfySwitchNode, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image2.1最强开源模型 图像编辑整合处理工具_2114088484360245249.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image2.1最强开源模型 图像编辑整合处理工具_2114088484360245249.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（133 个）：
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
- `Image Compare (mtb)`
- `TextConcatenator`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `GetImageSize`
- `ImageSharpen`
- `LoadImage`
- `ColorMatch`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `SetNode`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `SetNode`
- `SetNode`
- `ImageScaleToTotalPixels`
- `SetNode`
- `ImageScaleToTotalPixels`
- `SetNode`
- `ImageScaleToTotalPixels`
- `SetNode`
- `SaveImage`
- `SDPoseOODProcessor`
- `SDPoseOODLoader`
- `GetNode`
- `YOLOModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `GetNode`
- `SetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `ImageScaleToTotalPixels`
- `SeedVR2BlockSwap`
- `SaveImageAdvanced`
- `SeedVR2`
- `SeedVR2ExtraArgs`
- `LoadImage`
- `LoadImage`
- `GH_ImageVideoComparer`
- `PreviewImage`
- `LoadImage`
- `SetNode`
- `GetNode`
- `TextGenerate`
- `ImageConcanate`
- `DrawMaskOnImage`
- `SimpleMath+`
- `SetLatentNoiseMask`
- `InpaintStitchImproved`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `JsonExtractString`
- `CR Text Concatenate`
- `SaveImage`
- `PreviewAny`
- `INTConstant`
- `PreviewImage`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `InpaintCropImproved`
- `VAEEncode` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `Any Switch (rgthree)`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `Seed (rgthree)`
- `ComfySwitchNode`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `KSampler` ★核心
- `ComfySwitchNode`
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
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`

**识别到的模式**：text_to_image、image_to_image

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

覆盖率 **74%**（98/133）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`Image Compare (mtb)`、`TextConcatenator`、`LoadImage`、`VAEEncode`、`VAEDecode`、`GetImageSize`、`ImageSharpen`、`ColorMatch`、`SaveImage`、`ImageScaleToTotalPixels`、`SDPoseOODProcessor`、`SDPoseOODLoader`、`YOLOModelLoader`、`SeedVR2BlockSwap`、`SaveImageAdvanced`、`SeedVR2`、`SeedVR2ExtraArgs`、`GH_ImageVideoComparer`、`TextGenerate`、`ImageConcanate`、`DrawMaskOnImage`、`SimpleMath+`、`SetLatentNoiseMask`、`InpaintStitchImproved`、`JsonExtractString`、`CR Text Concatenate`、`INTConstant`、`InpaintCropImproved`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLatentImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`Seed (rgthree)`、`LoraLoaderModelOnly`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
