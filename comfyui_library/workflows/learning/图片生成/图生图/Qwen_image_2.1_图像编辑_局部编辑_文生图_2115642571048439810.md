---
key: 图片生成/图生图/Qwen_image_2.1_图像编辑_局部编辑_文生图_2115642571048439810.json
name: Qwen_image_2.1_图像编辑_局部编辑_文生图_2115642571048439810
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1_图像编辑_局部编辑_文生图_2115642571048439810.json
hash: 8364fd572432afd9
coverage: 0.42446
learned_at: 2026-10-30 17:51:16
nodes: [EmptyLatentImage, PrimitiveBoolean, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, EmptyLatentImage, ResolutionSelector, GetNode, GetNode, SetNode, SetNode, CLIPLoader, UNETLoader, LoadImage, LoadImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, BatchImagesNode, SetNode, easy showAnything, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, GetNode, ComfySwitchNode, Seed (rgthree), GetNode, ImageScaleToTotalPixels, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, KSampler, SetLatentNoiseMask, GetNode, VAEDecode, SimpleMath+, DrawMaskOnImage, GetNode, ComfySwitchNode, VAEEncode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, Any Switch (rgthree), GetNode, GetNode, TextGenerateLTX2Prompt, GetNode, VAEDecode, SetNode, TextGenerateLTX2Prompt, SetNode, SetNode, easy showAnything, TextEncodeQwenImage21, PrimitiveStringMultiline, PrimitiveStringMultiline, KSampler, KSampler, ResolutionSelector, Any Switch (rgthree), SaveImage, GetNode, GetNode, PrimitiveStringMultiline, GetNode, Seed (rgthree), Any Switch (rgthree), CLIPLoader, QwenImage21Cache, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, CLIPLoader, VAELoader, SetNode, PreviewImage, PreviewImage, GetNode, SaveImage, GetNode, SaveImage, InpaintCropImproved, VAEDecode, Image Comparer (rgthree), InpaintStitchImproved, Image Comparer (rgthree), PrimitiveStringMultiline, Image Comparer (rgthree), Seed (rgthree), SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, INTConstant, MarkdownNote, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海]
patterns: [image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 643804720425800, "steps": 30, "width": 1024}
---

# 图片生成/图生图/Qwen_image_2.1_图像编辑_局部编辑_文生图_2115642571048439810.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1_图像编辑_局部编辑_文生图_2115642571048439810.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（139 个）：
- `EmptyLatentImage` ★核心
- `PrimitiveBoolean`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BatchImagesNode`
- `SetNode`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `GetNode`
- `ComfySwitchNode`
- `Seed (rgthree)`
- `GetNode`
- `ImageScaleToTotalPixels`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `SetLatentNoiseMask`
- `GetNode`
- `VAEDecode` ★核心
- `SimpleMath+`
- `DrawMaskOnImage`
- `GetNode`
- `ComfySwitchNode`
- `VAEEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `TextGenerateLTX2Prompt`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `KSampler` ★核心
- `KSampler` ★核心
- `ResolutionSelector`
- `Any Switch (rgthree)`
- `SaveImage`
- `GetNode`
- `GetNode`
- `PrimitiveStringMultiline`
- `GetNode`
- `Seed (rgthree)`
- `Any Switch (rgthree)`
- `CLIPLoader`
- `QwenImage21Cache`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `PreviewImage`
- `PreviewImage`
- `GetNode`
- `SaveImage`
- `GetNode`
- `SaveImage`
- `InpaintCropImproved`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `InpaintStitchImproved`
- `Image Comparer (rgthree)`
- `PrimitiveStringMultiline`
- `Image Comparer (rgthree)`
- `Seed (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `MarkdownNote`
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`

**识别到的模式**：image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `643804720425800`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **42%**（59/139）

**有卡**：`EmptyLatentImage`、`PrimitiveBoolean`、`LoadImage`、`ResolutionSelector`、`CLIPLoader`、`UNETLoader`、`ImageScaleToTotalPixels`、`BatchImagesNode`、`TextEncodeQwenImage21`、`Seed (rgthree)`、`KSampler`、`SetLatentNoiseMask`、`VAEDecode`、`SimpleMath+`、`DrawMaskOnImage`、`VAEEncode`、`TextGenerateLTX2Prompt`、`SaveImage`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`VAELoader`、`InpaintCropImproved`、`InpaintStitchImproved`、`INTConstant`、`忽略多组孤海`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
