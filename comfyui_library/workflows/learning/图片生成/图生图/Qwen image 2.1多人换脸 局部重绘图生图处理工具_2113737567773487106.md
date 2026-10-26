---
key: 图片生成/图生图/Qwen image 2.1多人换脸 局部重绘图生图处理工具_2113737567773487106.json
name: Qwen image 2.1多人换脸 局部重绘图生图处理工具_2113737567773487106
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1多人换脸 局部重绘图生图处理工具_2113737567773487106.json
hash: 06519434f25daceb
coverage: 0.647059
learned_at: 2026-10-26 22:03:14
nodes: [TextGenerateLTX2Prompt, CLIPLoader, QwenImage21Cache, PrimitiveStringMultiline, GetNode, LayerUtility: ImageBlend, PreviewImage, 取色器_孤海, LayerMask: MaskGrow, LayerUtility: ColorImage, UNETLoader, KSampler, BatchImagesNode, SaveImage, TextEncodeQwenImage21, VAELoader, CLIPLoader, PrimitiveStringMultiline, ColorMatch, SetNode, VAEDecode, easy showAnything, SetNode, Image Comparer (rgthree), SaveImage, LoadImage, MaskPreview+, ImpactInt, LoadImage, PreviewImage, MaskPreview+, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, SetNode, GetNode, SetNode, GetNode, GetNode, SetNode, LayerUtility: CropByMask V2, GetNode, Image Comparer (rgthree), PreviewImage, SetNode, SetNode, LayerUtility: CropBoxResolve, easy showAnything, GetNode, PreviewImage, ImageCompositeMasked, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, GetNode, LayerMask: MaskGrow, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1多人换脸 局部重绘图生图处理工具_2113737567773487106.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1多人换脸 局部重绘图生图处理工具_2113737567773487106.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（85 个）：
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `QwenImage21Cache`
- `PrimitiveStringMultiline`
- `GetNode`
- `LayerUtility: ImageBlend`
- `PreviewImage`
- `取色器_孤海`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `BatchImagesNode`
- `SaveImage`
- `TextEncodeQwenImage21`
- `VAELoader`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `ColorMatch`
- `SetNode`
- `VAEDecode` ★核心
- `easy showAnything`
- `SetNode`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `MaskPreview+`
- `ImpactInt`
- `LoadImage`
- `PreviewImage`
- `MaskPreview+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LayerUtility: CropByMask V2`
- `GetNode`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `LayerUtility: CropBoxResolve`
- `easy showAnything`
- `GetNode`
- `PreviewImage`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `GetNode`
- `LayerMask: MaskGrow`
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

**识别到的模式**：text_to_image

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

覆盖率 **65%**（55/85）

**有卡**：`TextGenerateLTX2Prompt`、`CLIPLoader`、`QwenImage21Cache`、`LayerUtility: ImageBlend`、`取色器_孤海`、`LayerMask: MaskGrow`、`LayerUtility: ColorImage`、`UNETLoader`、`KSampler`、`BatchImagesNode`、`SaveImage`、`TextEncodeQwenImage21`、`VAELoader`、`ColorMatch`、`VAEDecode`、`LoadImage`、`MaskPreview+`、`ImpactInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize`、`LayerUtility: CropByMask V2`、`LayerUtility: CropBoxResolve`、`ImageCompositeMasked`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
