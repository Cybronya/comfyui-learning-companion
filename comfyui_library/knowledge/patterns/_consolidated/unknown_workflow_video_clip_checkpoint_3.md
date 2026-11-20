---
name: unknown_workflow_video_clip_checkpoint_3
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.87575
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, LayerUtility: ImageScaleByAspectRatio V2, LoadMoGeModel, MoGeGeometryToFOV, MoGeInference, PrimitiveInt, RMBG, RTDETR_detect, SAM3DBody_FaceExpression, SAM3DBody_Loader, SAM3DBody_Predict, SAM3DBody_Render, SAM3DBody_Smooth, SAM3_VideoTrack, UNETLoader, VHS_LoadVideo, VHS_VideoCombine, easy positive]
problems: []
missing: []
members: [平台全量/1-Aiden-sam3d-人体白模渲染！！_2109726889379192833.json, 平台全量/1-Aiden-sam3d-人体白模渲染！！多人版本！！_2110351832131391490.json, 平台全量/人体白模渲染！！_2111395938391646210.json, 视频生成/图生视频/1-Aiden-sam3d-人体白模渲染！！多人版本！！_2113777422448553986.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_checkpoint_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/1-Aiden-sam3d-人体白模渲染！！_2109726889379192833.json、平台全量/1-Aiden-sam3d-人体白模渲染！！多人版本！！_2110351832131391490.json、平台全量/人体白模渲染！！_2111395938391646210.json、视频生成/图生视频/1-Aiden-sam3d-人体白模渲染！！多人版本！！_2113777422448553986.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadMoGeModel`
- `MoGeGeometryToFOV`
- `MoGeInference`
- `PrimitiveInt`
- `RMBG`
- `RTDETR_detect`
- `SAM3DBody_FaceExpression`
- `SAM3DBody_Loader`
- `SAM3DBody_Predict`
- `SAM3DBody_Render`
- `SAM3DBody_Smooth`
- `SAM3_VideoTrack`
- `UNETLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `DrawBBoxes` —— 2/4 个有
- `ImageCompositeMasked` —— 2/4 个有
- `ImageToMask` —— 2/4 个有
- `LayerColor: AutoAdjust` —— 2/4 个有
- `LayerColor: BrightnessContrastV2` —— 2/4 个有
- `MaskToImage` —— 2/4 个有
- `SAM3_TrackPreview` —— 2/4 个有
- `SAM3_TrackToMask` —— 2/4 个有
- `SCAIL2ColoredMask` —— 2/4 个有
- `孤海注释` —— 2/4 个有
- `忽略多组孤海` —— 2/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
