---
name: unknown_workflow_upscale_clip_checkpoint_7
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6955
common_nodes: [Any Switch (rgthree), Bounded Image Blend, Bounded Image Crop with Mask, CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, ConditioningZeroOut, DF_Float, DownloadAndLoadFlorence2Model, Fast Groups Bypasser (rgthree), Florence2Run, FluxGuidance, Image Comparer (rgthree), ImageScale, ImageUpscaleWithModel, JWImageResizeByLongerSide, JWMaskResize, LayerMask: MaskEdgeUltraDetail, LayerMask: PersonMaskUltra V2, LayerMask: SegmentAnythingUltra V2, LayerUtility: ColorImage V2, LayerUtility: ImageBlend, Load Image Batch, LoadImage, Mask Fill Holes, MaskPreview+, PreviewImage, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, SimpleMath+, Text Concatenate, UpscaleModelLoader, VAELoader, easy imageColorMatch, easy imageSize, easy positive, easy showAnything]
problems: []
missing: []
members: [平台全量/人像高清SUPIR+TTP高清放大_1929901110008647682.json, 平台全量/人像高清放大 人脸保持不变 支持多人_1936470154978971649.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_checkpoint_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/人像高清SUPIR+TTP高清放大_1929901110008647682.json、平台全量/人像高清放大 人脸保持不变 支持多人_1936470154978971649.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Bounded Image Blend`
- `Bounded Image Crop with Mask`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ConditioningZeroOut`
- `DF_Float`
- `DownloadAndLoadFlorence2Model`
- `Fast Groups Bypasser (rgthree)`
- `Florence2Run`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScale`
- `ImageUpscaleWithModel`
- `JWImageResizeByLongerSide`
- `JWMaskResize`
- `LayerMask: MaskEdgeUltraDetail`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlend`
- `Load Image Batch`
- `LoadImage`
- `Mask Fill Holes`
- `MaskPreview+`
- `PreviewImage`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`
- `SimpleMath+`
- `Text Concatenate`
- `UpscaleModelLoader`
- `VAELoader`
- `easy imageColorMatch`
- `easy imageSize`
- `easy positive`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 1/2 个有
- `BasicScheduler` —— 1/2 个有
- `DF_Integer` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `Image Lucy Sharpen` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `ImpactImageBatchToImageList` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `KSamplerSelect` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `NunchakuFluxDiTLoader` —— 1/2 个有
- `NunchakuFluxLoraLoader` —— 1/2 个有
- `NunchakuTextEncoderLoader` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `TTP_Image_Assy` —— 1/2 个有
- `TTP_Image_Tile_Batch` —— 1/2 个有
- `TTP_Tile_image_size` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `UltimateSDUpscale` —— 1/2 个有
- `VAEDecodeTiled` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
