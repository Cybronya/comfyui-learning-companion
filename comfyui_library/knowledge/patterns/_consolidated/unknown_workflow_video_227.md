---
name: unknown_workflow_video_227
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8035
common_nodes: [ImageAndMaskPreview, ImageFromBatch+, ImageResizeKJv2, InvertMask, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, MaskToImage, MatAnyone2, PrimitiveInt, RH_Translator, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/电商视频抠图 matAnyone2_2036644994483752961.json, 视频生成/图生视频/电商视频抠图 matAnyone2_2081996629795758081.json]
source: knowledge_consolidation
---

# unknown_workflow_video_227

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/电商视频抠图 matAnyone2_2036644994483752961.json、视频生成/图生视频/电商视频抠图 matAnyone2_2081996629795758081.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageAndMaskPreview`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `InvertMask`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `MaskToImage`
- `MatAnyone2`
- `PrimitiveInt`
- `RH_Translator`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
