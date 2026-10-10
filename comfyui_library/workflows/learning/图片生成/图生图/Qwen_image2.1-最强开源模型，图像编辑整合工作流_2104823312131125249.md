---
key: 图片生成/图生图/Qwen_image2.1-最强开源模型，图像编辑整合工作流_2104823312131125249.json
name: Qwen_image2.1-最强开源模型，图像编辑整合工作流_2104823312131125249
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_image2.1-最强开源模型，图像编辑整合工作流_2104823312131125249.json
hash: 21a4fa683f9d5322
coverage: 0.659091
learned_at: 2026-10-10 20:48:10
nodes: [CLIPLoader, VAELoader, UNETLoader, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, CLIPTextEncode, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, Image Compare (mtb), TextConcatenator, LoadImage, LoadImage, LoadImage, LoadImage, PreviewImage, LoadImage, LoadImage, VAEEncode, VAEDecode, GetImageSize, ImageSharpen, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ColorMatch, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, SetNode, SetNode, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, SetNode, SaveImage, SDPoseOODProcessor, SDPoseOODLoader, GetNode, YOLOModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, 孤海注释, 忽略多组孤海, LoadImage, GetNode, SetNode, SetNode, 孤海注释, PrimitiveStringMultiline, ImageScaleToTotalPixels, SeedVR2BlockSwap, SaveImageAdvanced, SeedVR2, SeedVR2ExtraArgs, LoadImage, LoadImage, GH_ImageVideoComparer, PreviewImage, LoadImage, SetNode, GetNode, TextGenerate, ImageConcanate, DrawMaskOnImage, SimpleMath+, SetLatentNoiseMask, InpaintStitchImproved, PrimitiveStringMultiline, CLIPLoader, JsonExtractString, CR Text Concatenate, SaveImage, LoadImage, PreviewAny, INTConstant, PreviewImage, PreviewImage, UNETLoader, CLIPLoader, VAELoader, 忽略多组孤海, ImageScaleToTotalPixels, InpaintCropImproved, VAEEncode, 孤海注释, LoadImage, 孤海注释, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, 孤海注释, Any Switch (rgthree), EmptyLatentImage, ResolutionSelector, TextEncodeQwenImage21, VAEDecode, Seed (rgthree), 孤海注释, ComfySwitchNode, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), LoadImage, LoraLoaderModelOnly, Note, PrimitiveStringMultiline, KSampler, ComfySwitchNode]
patterns: [text_to_image, image_to_image]
missing: [CR Text Concatenate, Image Compare (mtb), LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, 忽略多组孤海, 忽略多组孤海, Seed (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 971075361831478, "steps": 30, "width": 1024}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Image Compare (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Qwen_image2.1-最强开源模型，图像编辑整合工作流_2104823312131125249.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_image2.1-最强开源模型，图像编辑整合工作流_2104823312131125249.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（132 个）：
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
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `GetImageSize`
- `ImageSharpen`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ColorMatch`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
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
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `孤海注释`
- `忽略多组孤海`
- `LoadImage`
- `GetNode`
- `SetNode`
- `SetNode`
- `孤海注释`
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
- `LoadImage`
- `PreviewAny`
- `INTConstant`
- `PreviewImage`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `忽略多组孤海`
- `ImageScaleToTotalPixels`
- `InpaintCropImproved`
- `VAEEncode` ★核心
- `孤海注释`
- `LoadImage`
- `孤海注释`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `孤海注释`
- `Any Switch (rgthree)`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `Seed (rgthree)`
- `孤海注释`
- `ComfySwitchNode`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `PrimitiveStringMultiline`
- `KSampler` ★核心
- `ComfySwitchNode`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `971075361831478`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **66%**（87/132）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`TextConcatenator`、`LoadImage`、`VAEEncode`、`VAEDecode`、`GetImageSize`、`ImageSharpen`、`ColorMatch`、`SaveImage`、`ImageScaleToTotalPixels`、`SDPoseOODProcessor`、`SDPoseOODLoader`、`YOLOModelLoader`、`SeedVR2BlockSwap`、`SaveImageAdvanced`、`SeedVR2`、`SeedVR2ExtraArgs`、`GH_ImageVideoComparer`、`TextGenerate`、`ImageConcanate`、`DrawMaskOnImage`、`SetLatentNoiseMask`、`InpaintStitchImproved`、`JsonExtractString`、`INTConstant`、`InpaintCropImproved`、`EmptyLatentImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`KSampler`

**缺卡**（7）：`CR Text Concatenate`、`Image Compare (mtb)`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`忽略多组孤海`、`忽略多组孤海`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Image Compare (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
