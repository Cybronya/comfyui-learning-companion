---
name: unknown_workflow_sampler_checkpoint
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.886
common_nodes: [CheckpointLoaderSimple, DF_Get_image_size, GrowMask, Image Blend by Mask, Image Blending Mode, Image Comparer (rgthree), Image Filter Adjustments, Image Levels Adjustment, ImageBlur, ImageCompositeMasked, ImageInvert, ImageRemoveBackground+, ImageResizeKJv2, LBMSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadLBMModel, MaskToImage, PreviewImage, SaveImage, TransparentBGSession+, easy hiresFix]
problems: []
missing: []
members: [图片生成/图生图/图片-换背景-打光_1972669271623028738.json, 平台全量/lbm打光工作流 防细节丢失_1928257364128841729.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图片-换背景-打光_1972669271623028738.json、平台全量/lbm打光工作流 防细节丢失_1928257364128841729.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `DF_Get_image_size`
- `GrowMask`
- `Image Blend by Mask`
- `Image Blending Mode`
- `Image Comparer (rgthree)`
- `Image Filter Adjustments`
- `Image Levels Adjustment`
- `ImageBlur`
- `ImageCompositeMasked`
- `ImageInvert`
- `ImageRemoveBackground+`
- `ImageResizeKJv2`
- `LBMSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadLBMModel`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `TransparentBGSession+`
- `easy hiresFix`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
