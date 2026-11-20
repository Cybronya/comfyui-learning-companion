---
name: unknown_workflow_video_190
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7495
common_nodes: [BBoxesToSAM2, CR Prompt Text, DF_Get_image_size, ImageConcatMulti, ImageFromBatch+, JWInteger, LayerMask: LoadFlorence2Model, LayerMask: LoadSAM2Model, LayerMask: ObjectDetectorFL2, LayerMask: SAM2VideoUltra, LayerUtility: PurgeVRAM, Mask Invert, MaskPreview+, MaskToImage, PDIMAGE_LongerSize, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy showAnything]
problems: []
missing: []
members: [平台全量/DiffuEraser+FLorece 2+Sam2视频自动蒙版V1_1947152647931748354.json, 平台全量/DiffuEraser+Sam2全自动视频蒙版及主体消除V1_1947154092118695938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_190

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/DiffuEraser+FLorece 2+Sam2视频自动蒙版V1_1947152647931748354.json、平台全量/DiffuEraser+Sam2全自动视频蒙版及主体消除V1_1947154092118695938.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `BBoxesToSAM2`
- `CR Prompt Text`
- `DF_Get_image_size`
- `ImageConcatMulti`
- `ImageFromBatch+`
- `JWInteger`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: LoadSAM2Model`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2VideoUltra`
- `LayerUtility: PurgeVRAM`
- `Mask Invert`
- `MaskPreview+`
- `MaskToImage`
- `PDIMAGE_LongerSize`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DiffuEraserLoader` —— 1/2 个有
- `DiffuEraserSampler` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
