---
name: unknown_workflow_video_upscale_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.793
common_nodes: [FaceRestoreCFWithModel, FaceRestoreModelLoader, ImageResize+, ImageUpscaleWithModel, LayerColor: Brightness & Contrast, LoadImage, PreviewImage, ReActorFaceSwap, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/快速换脸_1919744550246481921.json, 视频生成/图生视频/【视频流】Reactor视频换脸_1819030257314758658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/快速换脸_1919744550246481921.json、视频生成/图生视频/【视频流】Reactor视频换脸_1819030257314758658.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `FaceRestoreCFWithModel`
- `FaceRestoreModelLoader`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `LayerColor: Brightness & Contrast`
- `LoadImage`
- `PreviewImage`
- `ReActorFaceSwap`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
