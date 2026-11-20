---
name: unknown_workflow_generic_1787
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.633
common_nodes: [BiRefNet_ModelLoader_Zho, BiRefNet_Zho, Fast Groups Muter (rgthree), GetImageSize+, GetNode, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), Image Comparer (rgthree), InspyrenetRembg, InvertMask, JoinImageWithAlpha, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageCombineAlpha, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Mask Batch, MaskPreview+, RMBG, ResizeMask, SAMLoader, SaveImage, SetNode]
problems: []
missing: []
members: [图片生成/图生图/自用抠图_2082349884757331970.json, 平台全量/抠图合集 · 多种抠图方法整合V2.0【待发布】_2039333366947913730.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1787

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/自用抠图_2082349884757331970.json、平台全量/抠图合集 · 多种抠图方法整合V2.0【待发布】_2039333366947913730.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 2 个 workflow 都包含：
- `BiRefNet_ModelLoader_Zho`
- `BiRefNet_Zho`
- `Fast Groups Muter (rgthree)`
- `GetImageSize+`
- `GetNode`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `Image Comparer (rgthree)`
- `InspyrenetRembg`
- `InvertMask`
- `JoinImageWithAlpha`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageCombineAlpha`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Mask Batch`
- `MaskPreview+`
- `RMBG`
- `ResizeMask`
- `SAMLoader`
- `SaveImage`
- `SetNode`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
