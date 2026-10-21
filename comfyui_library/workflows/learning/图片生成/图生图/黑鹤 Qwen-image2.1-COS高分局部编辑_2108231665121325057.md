---
key: 图片生成/图生图/黑鹤 Qwen-image2.1-COS高分局部编辑_2108231665121325057.json
name: 黑鹤 Qwen-image2.1-COS高分局部编辑_2108231665121325057
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/黑鹤 Qwen-image2.1-COS高分局部编辑_2108231665121325057.json
hash: 4750845bcd5afc6d
coverage: 0.730159
learned_at: 2026-10-21 00:57:08
nodes: [ResolutionSelector, LoadImage, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, PrimitiveStringMultiline, Seed (rgthree), ImageScaleToTotalPixels, InpaintStitchImproved, CLIPLoader, VAELoader, Seed (rgthree), ImageScaleToTotalPixels, VAEEncode, Image Comparer (rgthree), ImageScaleToTotalPixels, LoadImage, Fast Groups Bypasser (rgthree), SimpleMath+, Note, SplitImageWithAlpha, JoinImageWithAlpha, easy imageColorMatch, ComfySwitchNode, Label (rgthree), Note, UNETLoader, QwenImage21Cache, VAEDecode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, TextEncodeQwenImage21, PrimitiveStringMultiline, ComfySwitchNode, SetLatentNoiseMask, INTConstant, PreviewImage, SaveImage, InpaintCropImproved, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), KSampler, ImageToMask, PreviewImage, DrawMaskOnImage, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 321832901595703, "steps": 25, "width": 1024}
---

# 图片生成/图生图/黑鹤 Qwen-image2.1-COS高分局部编辑_2108231665121325057.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/黑鹤 Qwen-image2.1-COS高分局部编辑_2108231665121325057.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
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
- `InpaintStitchImproved`
- `CLIPLoader`
- `VAELoader`
- `Seed (rgthree)`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `SimpleMath+`
- `Note`
- `SplitImageWithAlpha`
- `JoinImageWithAlpha`
- `easy imageColorMatch`
- `ComfySwitchNode`
- `Label (rgthree)`
- `Note`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `SetLatentNoiseMask`
- `INTConstant`
- `PreviewImage`
- `SaveImage`
- `InpaintCropImproved`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `KSampler` ★核心
- `ImageToMask`
- `PreviewImage`
- `DrawMaskOnImage`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `321832901595703`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（46/63）

**有卡**：`ResolutionSelector`、`LoadImage`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`SaveImage`、`TextEncodeQwenImage21`、`Seed (rgthree)`、`ImageScaleToTotalPixels`、`InpaintStitchImproved`、`VAEEncode`、`SimpleMath+`、`SplitImageWithAlpha`、`JoinImageWithAlpha`、`easy imageColorMatch`、`Label (rgthree)`、`UNETLoader`、`LoraLoaderModelOnly`、`SetLatentNoiseMask`、`INTConstant`、`InpaintCropImproved`、`ImageToMask`、`DrawMaskOnImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
