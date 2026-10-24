---
key: 图片生成/图生图/Flux.1-万物重绘_万物迁移_1982490386239242241.json
name: Flux.1-万物重绘_万物迁移_1982490386239242241
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1-万物重绘_万物迁移_1982490386239242241.json
hash: a1958ed9a4010154
coverage: 0.805556
learned_at: 2026-10-23 10:58:43
nodes: [easy imageSizeBySide, JWImageResizeByLongerSide, LayerUtility: ImageRemoveAlpha, easy int, Bounded Image Crop with Mask, LayerUtility: ColorImage V2, easy imageSizeBySide, easy imageSizeBySide, MathExpression|pysssss, JWImageResizeByLongerSide, LayerUtility: ColorPicker, Note, easy cleanGpuUsed, LayerMask: SegmentAnythingUltra V2, LayerMask: SegmentAnythingUltra V2, easy positive, ImageResize+, Note, easy imageSize, MaskPreview+, easy cleanGpuUsed, PreviewImage, Note, Note, CLIPTextEncode, DifferentialDiffusion, FluxGuidance, CLIPTextEncode, StyleModelApply, CLIPVisionEncode, InpaintModelConditioning, VAEDecode, ImpactImageBatchToImageList, easy int, InpaintStitch, ImageToMask, easy cleanGpuUsed, easy imageCropFromMask, easy imageConcat, LayerUtility: ColorImage, LayerUtility: ColorImage, easy imageSize, Bounded Image Blend with Mask, LayerUtility: ImageScaleRestore V2, easy imageSize, PreviewImage, UNETLoader, StyleModelLoader, DualCLIPLoader, CLIPVisionLoader, VAELoader, Image Comparer (rgthree), RepeatLatentBatch, LayerMask: MaskGrow, MaskToImage, PreviewImage, PreviewBridge, KSampler, ImageToMask, InpaintCrop, PreviewImage, easy imageSize, easy imageSize, PreviewImage, easy imageSize, easy imageSize, PreviewImage, ImageConcanate, LayerUtility: ImageScaleRestore V2, CR Upscale Image, easy cleanGpuUsed, ImageConcanate, PreviewImage, easy cleanGpuUsed, LayerMask: SegmentAnythingUltra V2, easy cleanGpuUsed, easy imageSize, PreviewImage, ImageToMask, Note, Note, CR Upscale Image, PreviewImage, ImageConcanate, CR Color Panel, PreviewImage, LayerUtility: ImageBlendAdvance, Reroute, LayerMask: SegformerB2ClothesUltra, easy ifElse, easy isMaskEmpty, Any Switch (rgthree), Fast Bypasser (rgthree), easy cleanGpuUsed, MaskPreview+, GetImageSize+, JWImageResize, ImageCompositeMasked, LayerMask: MaskGrow, JWMaskResize, Bounded Image Crop with Mask, easy imageSize, Bounded Image Crop with Mask, LoadImage, LoadImage, SaveImage, MarkdownNote, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 688794612121324, "steps": 30}
---

# 图片生成/图生图/Flux.1-万物重绘_万物迁移_1982490386239242241.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1-万物重绘_万物迁移_1982490386239242241.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（108 个）：
- `easy imageSizeBySide`
- `JWImageResizeByLongerSide`
- `LayerUtility: ImageRemoveAlpha`
- `easy int`
- `Bounded Image Crop with Mask`
- `LayerUtility: ColorImage V2`
- `easy imageSizeBySide`
- `easy imageSizeBySide`
- `MathExpression|pysssss`
- `JWImageResizeByLongerSide`
- `LayerUtility: ColorPicker`
- `Note`
- `easy cleanGpuUsed`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerMask: SegmentAnythingUltra V2`
- `easy positive`
- `ImageResize+`
- `Note`
- `easy imageSize`
- `MaskPreview+`
- `easy cleanGpuUsed`
- `PreviewImage`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `DifferentialDiffusion`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `StyleModelApply`
- `CLIPVisionEncode`
- `InpaintModelConditioning`
- `VAEDecode` ★核心
- `ImpactImageBatchToImageList`
- `easy int`
- `InpaintStitch`
- `ImageToMask`
- `easy cleanGpuUsed`
- `easy imageCropFromMask`
- `easy imageConcat`
- `LayerUtility: ColorImage`
- `LayerUtility: ColorImage`
- `easy imageSize`
- `Bounded Image Blend with Mask`
- `LayerUtility: ImageScaleRestore V2`
- `easy imageSize`
- `PreviewImage`
- `UNETLoader` ★核心
- `StyleModelLoader`
- `DualCLIPLoader`
- `CLIPVisionLoader`
- `VAELoader`
- `Image Comparer (rgthree)`
- `RepeatLatentBatch`
- `LayerMask: MaskGrow`
- `MaskToImage`
- `PreviewImage`
- `PreviewBridge`
- `KSampler` ★核心
- `ImageToMask`
- `InpaintCrop`
- `PreviewImage`
- `easy imageSize`
- `easy imageSize`
- `PreviewImage`
- `easy imageSize`
- `easy imageSize`
- `PreviewImage`
- `ImageConcanate`
- `LayerUtility: ImageScaleRestore V2`
- `CR Upscale Image`
- `easy cleanGpuUsed`
- `ImageConcanate`
- `PreviewImage`
- `easy cleanGpuUsed`
- `LayerMask: SegmentAnythingUltra V2`
- `easy cleanGpuUsed`
- `easy imageSize`
- `PreviewImage`
- `ImageToMask`
- `Note`
- `Note`
- `CR Upscale Image`
- `PreviewImage`
- `ImageConcanate`
- `CR Color Panel`
- `PreviewImage`
- `LayerUtility: ImageBlendAdvance`
- `Reroute`
- `LayerMask: SegformerB2ClothesUltra`
- `easy ifElse`
- `easy isMaskEmpty`
- `Any Switch (rgthree)`
- `Fast Bypasser (rgthree)`
- `easy cleanGpuUsed`
- `MaskPreview+`
- `GetImageSize+`
- `JWImageResize`
- `ImageCompositeMasked`
- `LayerMask: MaskGrow`
- `JWMaskResize`
- `Bounded Image Crop with Mask`
- `easy imageSize`
- `Bounded Image Crop with Mask`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `seed` = `688794612121324`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **81%**（87/108）

**有卡**：`easy imageSizeBySide`、`JWImageResizeByLongerSide`、`LayerUtility: ImageRemoveAlpha`、`easy int`、`Bounded Image Crop with Mask`、`LayerUtility: ColorImage V2`、`MathExpression|pysssss`、`LayerUtility: ColorPicker`、`easy cleanGpuUsed`、`LayerMask: SegmentAnythingUltra V2`、`easy positive`、`ImageResize+`、`easy imageSize`、`MaskPreview+`、`CLIPTextEncode`、`DifferentialDiffusion`、`FluxGuidance`、`StyleModelApply`、`CLIPVisionEncode`、`InpaintModelConditioning`、`VAEDecode`、`ImpactImageBatchToImageList`、`InpaintStitch`、`ImageToMask`、`easy imageCropFromMask`、`easy imageConcat`、`LayerUtility: ColorImage`、`Bounded Image Blend with Mask`、`LayerUtility: ImageScaleRestore V2`、`UNETLoader`、`StyleModelLoader`、`DualCLIPLoader`、`CLIPVisionLoader`、`VAELoader`、`RepeatLatentBatch`、`LayerMask: MaskGrow`、`MaskToImage`、`PreviewBridge`、`KSampler`、`InpaintCrop`、`ImageConcanate`、`CR Upscale Image`、`CR Color Panel`、`LayerUtility: ImageBlendAdvance`、`LayerMask: SegformerB2ClothesUltra`、`easy isMaskEmpty`、`Fast Bypasser (rgthree)`、`GetImageSize+`、`JWImageResize`、`ImageCompositeMasked`、`JWMaskResize`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、RepeatLatentBatch
