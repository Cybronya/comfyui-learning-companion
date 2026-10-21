---
key: 图片生成/图生图/细节恢复 qwen_image_2.1_2107159669243473921.json
name: 细节恢复 qwen_image_2.1_2107159669243473921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/细节恢复 qwen_image_2.1_2107159669243473921.json
hash: 5287ae5db20ccabe
coverage: 0.742857
learned_at: 2026-10-21 00:55:43
nodes: [LayerUtility: ColorImage V2, ImageToMask, LayerUtility: ImageBlendAdvance, Image Comparer (rgthree), GetImageSize, LayerUtility: ColorImage V2, SaveImage, Int, LayerUtility: CropByMask V2, LayerUtility: CropByMask V2, GetImageSize, MaxNode, MathExpression|pysssss, ImageScale, LayerMask: MaskPreview, LayerMask: MaskGrow, easy showAnything, GrowMaskWithBlur, Mask Fill Holes, GrowMaskWithBlur, Mask Fill Holes, PreviewImage, Image Comparer (rgthree), 孤海注释, ImageResizeKJv2, ImageResizeKJv2, Image Overlay, PreviewImage, LayerMask: MaskPreview, PreviewImage, LayerMask: MaskPreview, GetImageSize, LayerMask: MaskPreview, LayerMask: MaskPreview, LayerMask: MaskPreview, PreviewImage, 孤海注释, Reroute, GetImageSize, 孤海注释, LayerUtility: CropByMask V2, Reroute, CLIPLoader, KSamplerSelect, ManualSigmas, VAELoader, UNETLoader, QwenImage21Cache, JjkText, LayerUtility: RestoreCropBox, VAEDecode, SamplerCustom, PreviewImage, PreviewImage, LoraLoaderModelOnly, LoadImage, PreviewImage, PreviewImage, TextEncodeQwenImage21, Int, LayerFilter: GaussianBlur, KuwaharaBlur, Int, 孤海注释, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, PreviewBridge, PreviewBridge, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/细节恢复 qwen_image_2.1_2107159669243473921.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/细节恢复 qwen_image_2.1_2107159669243473921.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（70 个）：
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
- `孤海注释`
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
- `孤海注释`
- `Reroute`
- `GetImageSize`
- `孤海注释`
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
- `孤海注释`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewBridge`
- `PreviewBridge`
- `LoadImage`

## 知识

覆盖率 **74%**（52/70）

**有卡**：`LayerUtility: ColorImage V2`、`ImageToMask`、`LayerUtility: ImageBlendAdvance`、`GetImageSize`、`SaveImage`、`Int`、`LayerUtility: CropByMask V2`、`MaxNode`、`MathExpression|pysssss`、`ImageScale`、`LayerMask: MaskPreview`、`LayerMask: MaskGrow`、`GrowMaskWithBlur`、`Mask Fill Holes`、`ImageResizeKJv2`、`Image Overlay`、`CLIPLoader`、`KSamplerSelect`、`ManualSigmas`、`VAELoader`、`UNETLoader`、`QwenImage21Cache`、`LayerUtility: RestoreCropBox`、`VAEDecode`、`SamplerCustom`、`LoraLoaderModelOnly`、`LoadImage`、`TextEncodeQwenImage21`、`LayerFilter: GaussianBlur`、`KuwaharaBlur`、`LayerUtility: ImageScaleByAspectRatio V2`、`PreviewBridge`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
