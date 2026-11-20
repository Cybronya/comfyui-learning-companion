---
name: unknown_workflow_inpaint_sampler_clip_92
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7565
common_nodes: [Anything Everywhere, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ConstrainImage|pysssss, CropMask, DF_Integer, Flux2Scheduler, GrowMask, GrowMaskWithBlur, Image Comparer (rgthree), ImageCASharpening+, ImageColorMatch+, ImageConcatMulti, ImageListToImageBatch, ImageResize+, ImageResizeKJv2, ImpactMinMax, InpaintModelConditioning, KSamplerSelect, LayerMask: SegformerB2ClothesUltra, LayerUtility: CropBoxResolve, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, LoadImage, LoadImageMask, MaskBlur+, MaskPreview+, MathExpression|pysssss, PreviewImage, PrimitiveInt, RH_LLMAPI_NODE, RH_Nano_Banana2_Image2Image, RH_Translator, RandomNoise, ReferenceLatent, ResizeMask, SamplerCustomAdvanced, SaveImage, SeedVR2, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, ZML_AnyTypeSwitch, ZML_MaskStroke, easy cleanGpuUsed, easy clearCacheAll, easy imageBatchToImageList, easy imageSize, easy showAnything, 遮罩内外扩展]
problems: []
missing: []
members: [图片生成/图生图/AIGC-换装_人_2027213889129156609.json, 平台全量/全能图片V1 4k服装上身（带完美裁剪恢复）_1992047018400960513.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_92

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/AIGC-换装_人_2027213889129156609.json、平台全量/全能图片V1 4k服装上身（带完美裁剪恢复）_1992047018400960513.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `CropMask`
- `DF_Integer`
- `Flux2Scheduler`
- `GrowMask`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageColorMatch+`
- `ImageConcatMulti`
- `ImageListToImageBatch`
- `ImageResize+`
- `ImageResizeKJv2`
- `ImpactMinMax`
- `InpaintModelConditioning`
- `KSamplerSelect`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoadImageMask`
- `MaskBlur+`
- `MaskPreview+`
- `MathExpression|pysssss`
- `PreviewImage`
- `PrimitiveInt`
- `RH_LLMAPI_NODE`
- `RH_Nano_Banana2_Image2Image`
- `RH_Translator`
- `RandomNoise`
- `ReferenceLatent`
- `ResizeMask`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZML_AnyTypeSwitch`
- `ZML_MaskStroke`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy imageBatchToImageList`
- `easy imageSize`
- `easy showAnything`
- `遮罩内外扩展`

**可变部分**（部分 workflow 才有）：
- `QwenMultiangleCameraNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
