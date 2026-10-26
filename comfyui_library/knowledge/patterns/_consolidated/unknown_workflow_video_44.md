---
name: unknown_workflow_video_44
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.825
common_nodes: [CreateShapeMask, DownloadAndLoadLivePortraitModels, GetImageSizeAndCount, GrowMaskWithBlur, LivePortraitComposite, LivePortraitCropper, LivePortraitProcess, LoadImage, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LivePortrait人类表情迁移___在线生图_1901488965541863425.json, 视频生成/图生视频/LivePortrait动物表情迁移___在线生图_1901493735421812738.json, 视频生成/图生视频/LivePortrait视频驱动表情控制_1952985639379734530.json, 视频生成/图生视频/【RICK】livePortait驱动图片_1906528268223172609.json]
source: knowledge_consolidation
---

# unknown_workflow_video_44

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LivePortrait人类表情迁移___在线生图_1901488965541863425.json、视频生成/图生视频/LivePortrait动物表情迁移___在线生图_1901493735421812738.json、视频生成/图生视频/LivePortrait视频驱动表情控制_1952985639379734530.json、视频生成/图生视频/【RICK】livePortait驱动图片_1906528268223172609.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateShapeMask`
- `DownloadAndLoadLivePortraitModels`
- `GetImageSizeAndCount`
- `GrowMaskWithBlur`
- `LivePortraitComposite`
- `LivePortraitCropper`
- `LivePortraitProcess`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 3/4 个有
- `LivePortraitLoadMediaPipeCropper` —— 3/4 个有
- `LivePortraitRetargeting` —— 3/4 个有
- `MaskPreview+` —— 3/4 个有
- `Display Int (rgthree)` —— 2/4 个有
- `VHS_VideoInfo` —— 2/4 个有
- `LivePortraitLoadCropper` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `VHS_VideoInfoLoaded` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
