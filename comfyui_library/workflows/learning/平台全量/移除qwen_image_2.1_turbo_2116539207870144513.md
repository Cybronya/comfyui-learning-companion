---
key: 平台全量/移除qwen_image_2.1_turbo_2116539207870144513.json
name: 移除qwen_image_2.1_turbo_2116539207870144513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/移除qwen_image_2.1_turbo_2116539207870144513.json
hash: 3dd39c6c5c6ba711
coverage: 0.728814
learned_at: 2026-11-14 02:27:27
nodes: [Image Comparer (rgthree), SaveImage, UNETLoader, QwenImage21Cache, CLIPLoader, KSamplerSelect, VAELoader, LoraLoaderModelOnly, VAEDecode, SamplerCustom, TextEncodeQwenImage21, LoadImage, LayerUtility: ImageRemoveAlpha, PreviewImage, GrowMaskWithBlur, GetImageSize, Mask Fill Holes, MathExpression|pysssss, LayerUtility: CropByMask V2, easy showAnything, LayerUtility: CropByMask V2, PreviewImage, LayerUtility: RestoreCropBox, ImageToMask, LayerUtility: ImageBlendAdvance, LayerUtility: ColorImage V2, LayerUtility: ColorImage V2, LayerMask: MaskGrow, MaskPreview+, PreviewImage, Image Comparer (rgthree), MaxNode, PreviewImage, GetImageSize, ImageScale, PreviewImage, ComfyMathExpression, easy showAnything, ComfyMathExpression, easy showAnything, GetImageSize, ImagePadForOutpaint, Image Bounds, Inset Image Bounds, Bounded Image Crop, ImageScaleToMaxDimension, ManualSigmas, PreviewImage, PreviewImage, Reroute, 忽略多组孤海, ManualSigmas, JjkText, Text Concatenate (JPS), CR Text Replace, CR String To Number, CR Image Input Switch (4 way), JjkText, JjkText]
patterns: []
missing: []
---

# 平台全量/移除qwen_image_2.1_turbo_2116539207870144513.json

> 来源文件 `comfyui_library/workflows/平台全量/移除qwen_image_2.1_turbo_2116539207870144513.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `Image Comparer (rgthree)`
- `SaveImage`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `SamplerCustom` ★核心
- `TextEncodeQwenImage21`
- `LoadImage`
- `LayerUtility: ImageRemoveAlpha`
- `PreviewImage`
- `GrowMaskWithBlur`
- `GetImageSize`
- `Mask Fill Holes`
- `MathExpression|pysssss`
- `LayerUtility: CropByMask V2`
- `easy showAnything`
- `LayerUtility: CropByMask V2`
- `PreviewImage`
- `LayerUtility: RestoreCropBox`
- `ImageToMask`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ColorImage V2`
- `LayerMask: MaskGrow`
- `MaskPreview+`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `MaxNode`
- `PreviewImage`
- `GetImageSize`
- `ImageScale`
- `PreviewImage`
- `ComfyMathExpression`
- `easy showAnything`
- `ComfyMathExpression`
- `easy showAnything`
- `GetImageSize`
- `ImagePadForOutpaint`
- `Image Bounds`
- `Inset Image Bounds`
- `Bounded Image Crop`
- `ImageScaleToMaxDimension`
- `ManualSigmas`
- `PreviewImage`
- `PreviewImage`
- `Reroute`
- `忽略多组孤海`
- `ManualSigmas`
- `JjkText`
- `Text Concatenate (JPS)`
- `CR Text Replace`
- `CR String To Number`
- `CR Image Input Switch (4 way)`
- `JjkText`
- `JjkText`

## 知识

覆盖率 **73%**（43/59）

**有卡**：`SaveImage`、`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`KSamplerSelect`、`VAELoader`、`LoraLoaderModelOnly`、`VAEDecode`、`SamplerCustom`、`TextEncodeQwenImage21`、`LoadImage`、`LayerUtility: ImageRemoveAlpha`、`GrowMaskWithBlur`、`GetImageSize`、`Mask Fill Holes`、`MathExpression|pysssss`、`LayerUtility: CropByMask V2`、`LayerUtility: RestoreCropBox`、`ImageToMask`、`LayerUtility: ImageBlendAdvance`、`LayerUtility: ColorImage V2`、`LayerMask: MaskGrow`、`MaskPreview+`、`MaxNode`、`ImageScale`、`ComfyMathExpression`、`ImagePadForOutpaint`、`Image Bounds`、`Inset Image Bounds`、`Bounded Image Crop`、`ImageScaleToMaxDimension`、`ManualSigmas`、`忽略多组孤海`、`Text Concatenate (JPS)`、`CR Text Replace`、`CR String To Number`、`CR Image Input Switch (4 way)`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
