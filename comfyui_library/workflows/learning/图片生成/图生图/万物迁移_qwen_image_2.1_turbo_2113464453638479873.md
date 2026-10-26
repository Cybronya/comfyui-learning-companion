---
key: 图片生成/图生图/万物迁移_qwen_image_2.1_turbo_2113464453638479873.json
name: 万物迁移_qwen_image_2.1_turbo_2113464453638479873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/万物迁移_qwen_image_2.1_turbo_2113464453638479873.json
hash: 1246103a345524fc
coverage: 0.758065
learned_at: 2026-10-26 22:04:37
nodes: [LayerUtility: ColorImage V2, ImageToMask, LayerUtility: ImageBlendAdvance, Image Comparer (rgthree), GetImageSize, LayerUtility: ColorImage V2, SaveImage, Int, LayerUtility: CropByMask V2, GetImageSize, MaxNode, MathExpression|pysssss, ImageScale, LayerMask: MaskGrow, easy showAnything, Mask Fill Holes, Mask Fill Holes, 孤海注释, ImageResizeKJv2, GetImageSize, Reroute, GetImageSize, LayerUtility: CropByMask V2, Reroute, CLIPLoader, KSamplerSelect, ManualSigmas, VAELoader, UNETLoader, QwenImage21Cache, VAEDecode, SamplerCustom, LoadImage, PreviewImage, TextEncodeQwenImage21, Int, 孤海注释, GrowMaskWithBlur, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: CropByMask V2, PreviewImage, LayerUtility: ImageRemoveAlpha, PreviewImage, LayerMask: MaskPreview, JjkText, GrowMaskWithBlur, LayerMask: MaskPreview, PreviewImage, PreviewImage, Image Comparer (rgthree), ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, LoraLoaderModelOnly, LoadImage, 孤海注释, PreviewBridge, PreviewBridge, EmptyImage, PreviewImage]
patterns: []
missing: []
---

# 图片生成/图生图/万物迁移_qwen_image_2.1_turbo_2113464453638479873.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/万物迁移_qwen_image_2.1_turbo_2113464453638479873.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
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
- `孤海注释`
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
- `孤海注释`
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
- `孤海注释`
- `PreviewBridge`
- `PreviewBridge`
- `EmptyImage`
- `PreviewImage`

## 知识

覆盖率 **76%**（47/62）

**有卡**：`LayerUtility: ColorImage V2`、`ImageToMask`、`LayerUtility: ImageBlendAdvance`、`GetImageSize`、`SaveImage`、`Int`、`LayerUtility: CropByMask V2`、`MaxNode`、`MathExpression|pysssss`、`ImageScale`、`LayerMask: MaskGrow`、`Mask Fill Holes`、`ImageResizeKJv2`、`CLIPLoader`、`KSamplerSelect`、`ManualSigmas`、`VAELoader`、`UNETLoader`、`QwenImage21Cache`、`VAEDecode`、`SamplerCustom`、`LoadImage`、`TextEncodeQwenImage21`、`GrowMaskWithBlur`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: MaskPreview`、`LayerUtility: ImageRemoveAlpha`、`LayerUtility: RestoreCropBox`、`LoraLoaderModelOnly`、`PreviewBridge`、`EmptyImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
