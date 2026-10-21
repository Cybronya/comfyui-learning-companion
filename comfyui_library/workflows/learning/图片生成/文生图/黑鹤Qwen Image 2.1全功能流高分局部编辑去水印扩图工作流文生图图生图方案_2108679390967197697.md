---
key: 图片生成/文生图/黑鹤Qwen Image 2.1全功能流高分局部编辑去水印扩图工作流文生图图生图方案_2108679390967197697.json
name: 黑鹤Qwen Image 2.1全功能流高分局部编辑去水印扩图工作流文生图图生图方案_2108679390967197697
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/黑鹤Qwen Image 2.1全功能流高分局部编辑去水印扩图工作流文生图图生图方案_2108679390967197697.json
hash: 46063bb84f151281
coverage: 0.828767
learned_at: 2026-10-21 03:03:28
nodes: [ResolutionSelector, LoadImage, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, PrimitiveStringMultiline, Seed (rgthree), ImageScaleToTotalPixels, PreviewImage, InpaintStitchImproved, Image Comparer (rgthree), CLIPLoader, VAELoader, KSampler, Seed (rgthree), LoadImage, ImageScaleToTotalPixels, Fast Groups Bypasser (rgthree), VAEEncode, SetLatentNoiseMask, Image Comparer (rgthree), TextEncodeQwenImage21, DrawMaskOnImage, PreviewImage, ComfySwitchNode, INTConstant, InpaintCropImproved, ImageScaleToTotalPixels, LoadImage, Fast Groups Bypasser (rgthree), SimpleMath+, Fast Groups Bypasser (rgthree), KSampler, TextEncodeQwenImage21, LoadImage, CLIPLoader, VAELoader, VAEDecode, QwenImage21Cache, PrimitiveStringMultiline, Seed (rgthree), PreviewImage, ImagePadForOutpaint, ImageScaleToTotalPixels, ImageScaleToTotalPixels, DrawMaskOnImage, VAEDecode, EmptyLatentImage, VAELoader, CLIPLoader, SplitImageWithAlpha, JoinImageWithAlpha, easy imageColorMatch, ComfySwitchNode, UNETLoader, QwenImage21Cache, VAEDecode, UNETLoader, UNETLoader, UNETLoader, LoadImage, PrimitiveStringMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage, Fast Groups Bypasser (rgthree), Seed (rgthree), KSampler, SaveImage, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, ResolutionSelector, TextEncodeQwenImage21, Image Comparer (rgthree), SaveImage, Fast Groups Bypasser (rgthree), UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/黑鹤Qwen Image 2.1全功能流高分局部编辑去水印扩图工作流文生图图生图方案_2108679390967197697.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/黑鹤Qwen Image 2.1全功能流高分局部编辑去水印扩图工作流文生图图生图方案_2108679390967197697.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（146 个）：
- `ResolutionSelector`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `PrimitiveStringMultiline`
- `Seed (rgthree)`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `InpaintStitchImproved`
- `Image Comparer (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `Seed (rgthree)`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `Fast Groups Bypasser (rgthree)`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `DrawMaskOnImage`
- `PreviewImage`
- `ComfySwitchNode`
- `INTConstant`
- `InpaintCropImproved`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `SimpleMath+`
- `Fast Groups Bypasser (rgthree)`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `PrimitiveStringMultiline`
- `Seed (rgthree)`
- `PreviewImage`
- `ImagePadForOutpaint`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `DrawMaskOnImage`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `CLIPLoader`
- `SplitImageWithAlpha`
- `JoinImageWithAlpha`
- `easy imageColorMatch`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`
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
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Seed (rgthree)`
- `KSampler` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
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

覆盖率 **83%**（121/146）

**有卡**：`ResolutionSelector`、`LoadImage`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`SaveImage`、`TextEncodeQwenImage21`、`Seed (rgthree)`、`ImageScaleToTotalPixels`、`InpaintStitchImproved`、`VAEEncode`、`SetLatentNoiseMask`、`DrawMaskOnImage`、`INTConstant`、`InpaintCropImproved`、`SimpleMath+`、`ImagePadForOutpaint`、`SplitImageWithAlpha`、`JoinImageWithAlpha`、`easy imageColorMatch`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
