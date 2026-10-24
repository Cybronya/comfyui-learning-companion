---
key: 图片生成/图生图/细节恢复qwen image 2.1 图片清晰度增强方案_2109713939251687425.json
name: 细节恢复qwen image 2.1 图片清晰度增强方案_2109713939251687425
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/细节恢复qwen image 2.1 图片清晰度增强方案_2109713939251687425.json
hash: 0ca2733e437294d6
coverage: 0.810526
learned_at: 2026-10-23 13:21:41
nodes: [LayerUtility: ColorImage V2, ImageToMask, LayerUtility: ImageBlendAdvance, Image Comparer (rgthree), GetImageSize, LayerUtility: ColorImage V2, SaveImage, Int, LayerUtility: CropByMask V2, LayerUtility: CropByMask V2, GetImageSize, MaxNode, MathExpression|pysssss, ImageScale, LayerMask: MaskPreview, LayerMask: MaskGrow, easy showAnything, GrowMaskWithBlur, Mask Fill Holes, GrowMaskWithBlur, Mask Fill Holes, PreviewImage, Image Comparer (rgthree), ImageResizeKJv2, ImageResizeKJv2, Image Overlay, PreviewImage, LayerMask: MaskPreview, PreviewImage, LayerMask: MaskPreview, GetImageSize, LayerMask: MaskPreview, LayerMask: MaskPreview, LayerMask: MaskPreview, PreviewImage, Reroute, GetImageSize, LayerUtility: CropByMask V2, Reroute, CLIPLoader, KSamplerSelect, ManualSigmas, VAELoader, UNETLoader, QwenImage21Cache, JjkText, LayerUtility: RestoreCropBox, VAEDecode, SamplerCustom, PreviewImage, PreviewImage, LoraLoaderModelOnly, LoadImage, PreviewImage, PreviewImage, TextEncodeQwenImage21, Int, LayerFilter: GaussianBlur, KuwaharaBlur, Int, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, PreviewBridge, PreviewBridge, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/细节恢复qwen image 2.1 图片清晰度增强方案_2109713939251687425.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/细节恢复qwen image 2.1 图片清晰度增强方案_2109713939251687425.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（95 个）：
- `LayerUtility: ColorImage V2`
- `ImageToMask`
- `LayerUtility: ImageBlendAdvance`
- `Image Comparer (rgthree)`
- `GetImageSize`
- `LayerUtility: ColorImage V2`
- `SaveImage`
- `Int`
- `LayerUtility: CropByMask V2`
- `LayerUtility: CropByMask V2`
- `GetImageSize`
- `MaxNode`
- `MathExpression|pysssss`
- `ImageScale`
- `LayerMask: MaskPreview`
- `LayerMask: MaskGrow`
- `easy showAnything`
- `GrowMaskWithBlur`
- `Mask Fill Holes`
- `GrowMaskWithBlur`
- `Mask Fill Holes`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `Image Overlay`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `GetImageSize`
- `LayerMask: MaskPreview`
- `LayerMask: MaskPreview`
- `LayerMask: MaskPreview`
- `PreviewImage`
- `Reroute`
- `GetImageSize`
- `LayerUtility: CropByMask V2`
- `Reroute`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `VAELoader`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `JjkText`
- `LayerUtility: RestoreCropBox`
- `VAEDecode` ★核心
- `SamplerCustom` ★核心
- `PreviewImage`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `Int`
- `LayerFilter: GaussianBlur`
- `KuwaharaBlur`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewBridge`
- `PreviewBridge`
- `LoadImage`
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

覆盖率 **81%**（77/95）

**有卡**：`LayerUtility: ColorImage V2`、`ImageToMask`、`LayerUtility: ImageBlendAdvance`、`GetImageSize`、`SaveImage`、`Int`、`LayerUtility: CropByMask V2`、`MaxNode`、`MathExpression|pysssss`、`ImageScale`、`LayerMask: MaskPreview`、`LayerMask: MaskGrow`、`GrowMaskWithBlur`、`Mask Fill Holes`、`ImageResizeKJv2`、`Image Overlay`、`CLIPLoader`、`KSamplerSelect`、`ManualSigmas`、`VAELoader`、`UNETLoader`、`QwenImage21Cache`、`LayerUtility: RestoreCropBox`、`VAEDecode`、`SamplerCustom`、`LoraLoaderModelOnly`、`LoadImage`、`TextEncodeQwenImage21`、`LayerFilter: GaussianBlur`、`KuwaharaBlur`、`LayerUtility: ImageScaleByAspectRatio V2`、`PreviewBridge`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
