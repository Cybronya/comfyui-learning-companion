---
name: unknown_workflow_video_105
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.775
common_nodes: [GrowMaskWithBlur, ImageFromBatch+, InvertMask, LayerMask: MaskBoxDetect, LayerUtility: CropByMask, LayerUtility: ImageBlendAdvance V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PM_BoxCropImage, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy imageSizeBySide]
problems: []
missing: []
members: [视频生成/图生视频/1976642655776055297.json, 视频生成/图生视频/1976608556025815041.json]
source: knowledge_consolidation
---

# unknown_workflow_video_105

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1976642655776055297.json、视频生成/图生视频/1976608556025815041.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `GrowMaskWithBlur`
- `ImageFromBatch+`
- `InvertMask`
- `LayerMask: MaskBoxDetect`
- `LayerUtility: CropByMask`
- `LayerUtility: ImageBlendAdvance V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PM_BoxCropImage`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy imageSizeBySide`

**可变部分**（部分 workflow 才有）：
- `ImageBatchMultiple+` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `easy imageCount` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
