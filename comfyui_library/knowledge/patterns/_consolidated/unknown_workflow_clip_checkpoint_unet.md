---
name: unknown_workflow_clip_checkpoint_unet
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8195
common_nodes: [BuildPoseFile, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, GetVideoComponents, LoadMoGeModel, LoadVideo, MoGeGeometryToFOV, MoGeInference, RTDETR_detect, SAM3DBody_FaceExpression, SAM3DBody_Loader, SAM3DBody_Predict, SAM3DBody_Render, SAM3DBody_Smooth, SAM3_VideoTrack, Save3DAdvanced, SaveVideo, UNETLoader, Video Slice]
problems: []
missing: []
members: [comfyui-workflow-templates-json/utility_sam3d_body.json, 数字人/数字人/人物视频转3D骨骼模型动画 utility_sam3d_body_2108819434642169857.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_checkpoint_unet

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（comfyui-workflow-templates-json/utility_sam3d_body.json、数字人/数字人/人物视频转3D骨骼模型动画 utility_sam3d_body_2108819434642169857.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `BuildPoseFile`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `GetVideoComponents`
- `LoadMoGeModel`
- `LoadVideo`
- `MoGeGeometryToFOV`
- `MoGeInference`
- `RTDETR_detect`
- `SAM3DBody_FaceExpression`
- `SAM3DBody_Loader`
- `SAM3DBody_Predict`
- `SAM3DBody_Render`
- `SAM3DBody_Smooth`
- `SAM3_VideoTrack`
- `Save3DAdvanced`
- `SaveVideo`
- `UNETLoader`
- `Video Slice`

**可变部分**（部分 workflow 才有）：
- `Float` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
