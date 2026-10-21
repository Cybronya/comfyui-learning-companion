---
key: 图片生成/文生图/Qwen Image 2.1黑鹤全功能流｜高分局部编辑+去水印+扩图一板全搞定_2108006501402112001.json
name: Qwen Image 2.1黑鹤全功能流｜高分局部编辑+去水印+扩图一板全搞定_2108006501402112001
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1黑鹤全功能流｜高分局部编辑+去水印+扩图一板全搞定_2108006501402112001.json
hash: 68a64718d6990f81
coverage: 0.820896
learned_at: 2026-10-20 01:51:03
nodes: [ResolutionSelector, LoadImage, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, PrimitiveStringMultiline, Seed (rgthree), ImageScaleToTotalPixels, PreviewImage, InpaintStitchImproved, Image Comparer (rgthree), CLIPLoader, VAELoader, KSampler, Seed (rgthree), LoadImage, ImageScaleToTotalPixels, Fast Groups Bypasser (rgthree), VAEEncode, SetLatentNoiseMask, Image Comparer (rgthree), TextEncodeQwenImage21, DrawMaskOnImage, PreviewImage, ComfySwitchNode, INTConstant, InpaintCropImproved, ImageScaleToTotalPixels, LoadImage, Fast Groups Bypasser (rgthree), SimpleMath+, Fast Groups Bypasser (rgthree), KSampler, TextEncodeQwenImage21, LoadImage, CLIPLoader, VAELoader, VAEDecode, QwenImage21Cache, PrimitiveStringMultiline, Seed (rgthree), PreviewImage, ImagePadForOutpaint, ImageScaleToTotalPixels, ImageScaleToTotalPixels, DrawMaskOnImage, VAEDecode, EmptyLatentImage, VAELoader, CLIPLoader, SplitImageWithAlpha, JoinImageWithAlpha, easy imageColorMatch, ComfySwitchNode, UNETLoader, QwenImage21Cache, VAEDecode, UNETLoader, UNETLoader, UNETLoader, LoadImage, PrimitiveStringMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage, Fast Groups Bypasser (rgthree), Seed (rgthree), KSampler, SaveImage, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, ResolutionSelector, TextEncodeQwenImage21, Image Comparer (rgthree), SaveImage, Fast Groups Bypasser (rgthree), 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1黑鹤全功能流｜高分局部编辑+去水印+扩图一板全搞定_2108006501402112001.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1黑鹤全功能流｜高分局部编辑+去水印+扩图一板全搞定_2108006501402112001.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（134 个）：
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
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

覆盖率 **82%**（110/134）

**有卡**：`ResolutionSelector`、`LoadImage`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`SaveImage`、`TextEncodeQwenImage21`、`Seed (rgthree)`、`ImageScaleToTotalPixels`、`InpaintStitchImproved`、`VAEEncode`、`SetLatentNoiseMask`、`DrawMaskOnImage`、`INTConstant`、`InpaintCropImproved`、`SimpleMath+`、`ImagePadForOutpaint`、`SplitImageWithAlpha`、`JoinImageWithAlpha`、`easy imageColorMatch`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
