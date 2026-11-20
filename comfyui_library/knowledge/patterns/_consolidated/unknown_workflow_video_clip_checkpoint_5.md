---
name: unknown_workflow_video_clip_checkpoint_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7475
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, DA3Inference, DA3Render, EmptyImage, GetImageSize, GetNode, INTConstant, ImageCompositeMasked, ImageFromBatch, ImageScaleToTotalPixels, Int, LoadDA3Model, LoadImage, LoadVideoUI, MaskComposite, PreviewAny, PreviewImage, RH_LLMAPI_NODE, SAM3_TrackPreview, SAM3_TrackToMask, SAM3_VideoTrack, SCAIL2ColoredMask, SaveVideo, SetNode, ShowAnything|Mie, SolidMask, VHS_LoadVideoFFmpeg, VHS_VideoCombine, VHS_VideoInfo, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/图生视频/参考素材（遮罩+景深+角色替换提示词）辅助工具_2115293330274865154.json, 视频生成/视频生视频/参考素材（遮罩+景深+角色替换提示词+背景360°环视）辅助工具_2115293330274865154.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_checkpoint_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/参考素材（遮罩+景深+角色替换提示词）辅助工具_2115293330274865154.json、视频生成/视频生视频/参考素材（遮罩+景深+角色替换提示词+背景360°环视）辅助工具_2115293330274865154.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `DA3Inference`
- `DA3Render`
- `EmptyImage`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageCompositeMasked`
- `ImageFromBatch`
- `ImageScaleToTotalPixels`
- `Int`
- `LoadDA3Model`
- `LoadImage`
- `LoadVideoUI`
- `MaskComposite`
- `PreviewAny`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `SAM3_TrackPreview`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SaveVideo`
- `SetNode`
- `ShowAnything|Mie`
- `SolidMask`
- `VHS_LoadVideoFFmpeg`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `cebcb156-47dd-40ff-971d-ab70021f3194` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
