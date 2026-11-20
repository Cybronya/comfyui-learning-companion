---
name: unknown_workflow_generic_1561
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7135
common_nodes: [GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), LayerMask: BiRefNetUltra, LayerMask: BiRefNetUltraV2, LayerMask: HumanPartsUltra, LayerMask: LoadBiRefNetModelV2, LayerMask: ObjectDetectorMask, LayerMask: ObjectDetectorYOLO8, LayerMask: PersonMaskUltra V2, LayerMask: SAM2Ultra, LayerMask: SegformerB2ClothesUltra, LayerMask: SegmentAnythingUltra, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageRemoveAlpha, Load Image From Url (mtb), LoadImage, MaskPreview+, PreviewImage, SAMLoader, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/8合1抠图专用整合流_1914555301436293122.json, 平台全量/抠图专用模块整合流（人物、动物、物品、多人、指定元素）_1915074616895668225.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1561

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/8合1抠图专用整合流_1914555301436293122.json、平台全量/抠图专用模块整合流（人物、动物、物品、多人、指定元素）_1915074616895668225.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `LayerMask: BiRefNetUltra`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: HumanPartsUltra`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: ObjectDetectorMask`
- `LayerMask: ObjectDetectorYOLO8`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: SAM2Ultra`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerMask: SegmentAnythingUltra`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageRemoveAlpha`
- `Load Image From Url (mtb)`
- `LoadImage`
- `MaskPreview+`
- `PreviewImage`
- `SAMLoader`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Image Rembg (Remove Background)` —— 1/2 个有
- `Image Save` —— 1/2 个有
- `InspyrenetRembg` —— 1/2 个有
- `LayerMask: LoadFlorence2Model` —— 1/2 个有
- `LayerMask: MaskPreview` —— 1/2 个有
- `LayerMask: ObjectDetectorFL2` —— 1/2 个有
- `LayerMask: TransparentBackgroundUltra` —— 1/2 个有
- `LayerUtility: ColorPicker` —— 1/2 个有
- `Load Image Batch` —— 1/2 个有
- `Load Image Sequence (mtb)` —— 1/2 个有
- `SaveImageToLocal` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
