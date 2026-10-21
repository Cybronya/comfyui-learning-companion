---
key: 图片生成/文生图/黑鹤 Qwen-image2.1-全功能流(高分局部编辑_去水印_扩图)_2107329132018364417.json
name: 黑鹤 Qwen-image2.1-全功能流(高分局部编辑_去水印_扩图)_2107329132018364417
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/黑鹤 Qwen-image2.1-全功能流(高分局部编辑_去水印_扩图)_2107329132018364417.json
hash: c701b737fda0a183
coverage: 0.760417
learned_at: 2026-10-20 01:53:02
nodes: [ResolutionSelector, LoadImage, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, PrimitiveStringMultiline, Seed (rgthree), ImageScaleToTotalPixels, PreviewImage, InpaintStitchImproved, Image Comparer (rgthree), CLIPLoader, VAELoader, KSampler, Seed (rgthree), LoadImage, ImageScaleToTotalPixels, Fast Groups Bypasser (rgthree), VAEEncode, SetLatentNoiseMask, Image Comparer (rgthree), TextEncodeQwenImage21, DrawMaskOnImage, PreviewImage, ComfySwitchNode, INTConstant, InpaintCropImproved, ImageScaleToTotalPixels, LoadImage, Fast Groups Bypasser (rgthree), SimpleMath+, Fast Groups Bypasser (rgthree), KSampler, TextEncodeQwenImage21, LoadImage, CLIPLoader, VAELoader, VAEDecode, QwenImage21Cache, PrimitiveStringMultiline, Seed (rgthree), PreviewImage, ImagePadForOutpaint, Label (rgthree), ImageScaleToTotalPixels, ImageScaleToTotalPixels, DrawMaskOnImage, Note, VAEDecode, EmptyLatentImage, VAELoader, CLIPLoader, SplitImageWithAlpha, JoinImageWithAlpha, easy imageColorMatch, ComfySwitchNode, Label (rgthree), Note, UNETLoader, QwenImage21Cache, VAEDecode, UNETLoader, UNETLoader, UNETLoader, LoadImage, PrimitiveStringMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, SaveImage, Fast Groups Bypasser (rgthree), Seed (rgthree), KSampler, SaveImage, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, ResolutionSelector, TextEncodeQwenImage21, Image Comparer (rgthree), SaveImage, Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 677472079782450, "steps": 30, "width": 1024}
---

# 图片生成/文生图/黑鹤 Qwen-image2.1-全功能流(高分局部编辑_去水印_扩图)_2107329132018364417.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/黑鹤 Qwen-image2.1-全功能流(高分局部编辑_去水印_扩图)_2107329132018364417.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（96 个）：
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
- `Label (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `DrawMaskOnImage`
- `Note`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `CLIPLoader`
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
- `Note`
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

**识别到的模式**：image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `677472079782450`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（73/96）

**有卡**：`ResolutionSelector`、`LoadImage`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`SaveImage`、`TextEncodeQwenImage21`、`Seed (rgthree)`、`ImageScaleToTotalPixels`、`InpaintStitchImproved`、`VAEEncode`、`SetLatentNoiseMask`、`DrawMaskOnImage`、`INTConstant`、`InpaintCropImproved`、`SimpleMath+`、`ImagePadForOutpaint`、`Label (rgthree)`、`SplitImageWithAlpha`、`JoinImageWithAlpha`、`easy imageColorMatch`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
