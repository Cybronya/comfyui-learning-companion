---
key: 图片生成/图生图/Qwen Image 2.1 Turbo万物迁移｜一键风格迁移高效出图加速版_2113443918649057281.json
name: Qwen Image 2.1 Turbo万物迁移｜一键风格迁移高效出图加速版_2113443918649057281
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 Turbo万物迁移｜一键风格迁移高效出图加速版_2113443918649057281.json
hash: 77689505dd306764
coverage: 0.85
learned_at: 2026-10-26 22:02:55
nodes: [LayerUtility: ColorImage V2, ImageToMask, LayerUtility: ImageBlendAdvance, Image Comparer (rgthree), GetImageSize, LayerUtility: ColorImage V2, SaveImage, Int, LayerUtility: CropByMask V2, GetImageSize, MaxNode, MathExpression|pysssss, ImageScale, LayerMask: MaskGrow, easy showAnything, Mask Fill Holes, Mask Fill Holes, ImageResizeKJv2, GetImageSize, Reroute, GetImageSize, LayerUtility: CropByMask V2, Reroute, CLIPLoader, KSamplerSelect, ManualSigmas, VAELoader, UNETLoader, QwenImage21Cache, VAEDecode, SamplerCustom, LoadImage, PreviewImage, TextEncodeQwenImage21, Int, GrowMaskWithBlur, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: CropByMask V2, PreviewImage, LayerUtility: ImageRemoveAlpha, PreviewImage, LayerMask: MaskPreview, JjkText, GrowMaskWithBlur, LayerMask: MaskPreview, PreviewImage, PreviewImage, Image Comparer (rgthree), ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, LoraLoaderModelOnly, LoadImage, PreviewBridge, PreviewBridge, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1 Turbo万物迁移｜一键风格迁移高效出图加速版_2113443918649057281.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 Turbo万物迁移｜一键风格迁移高效出图加速版_2113443918649057281.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（100 个）：
- `LayerUtility: ColorImage V2`
- `ImageToMask`
- `LayerUtility: ImageBlendAdvance`
- `Image Comparer (rgthree)`
- `GetImageSize`
- `LayerUtility: ColorImage V2`
- `SaveImage`
- `Int`
- `LayerUtility: CropByMask V2`
- `GetImageSize`
- `MaxNode`
- `MathExpression|pysssss`
- `ImageScale`
- `LayerMask: MaskGrow`
- `easy showAnything`
- `Mask Fill Holes`
- `Mask Fill Holes`
- `ImageResizeKJv2`
- `GetImageSize`
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
- `VAEDecode` ★核心
- `SamplerCustom` ★核心
- `LoadImage`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `Int`
- `GrowMaskWithBlur`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: CropByMask V2`
- `PreviewImage`
- `LayerUtility: ImageRemoveAlpha`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `JjkText`
- `GrowMaskWithBlur`
- `LayerMask: MaskPreview`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: RestoreCropBox`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `PreviewBridge`
- `PreviewBridge`
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

**识别到的模式**：text_to_image

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

覆盖率 **85%**（85/100）

**有卡**：`LayerUtility: ColorImage V2`、`ImageToMask`、`LayerUtility: ImageBlendAdvance`、`GetImageSize`、`SaveImage`、`Int`、`LayerUtility: CropByMask V2`、`MaxNode`、`MathExpression|pysssss`、`ImageScale`、`LayerMask: MaskGrow`、`Mask Fill Holes`、`ImageResizeKJv2`、`CLIPLoader`、`KSamplerSelect`、`ManualSigmas`、`VAELoader`、`UNETLoader`、`QwenImage21Cache`、`VAEDecode`、`SamplerCustom`、`LoadImage`、`TextEncodeQwenImage21`、`GrowMaskWithBlur`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: MaskPreview`、`LayerUtility: ImageRemoveAlpha`、`LayerUtility: RestoreCropBox`、`LoraLoaderModelOnly`、`PreviewBridge`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
