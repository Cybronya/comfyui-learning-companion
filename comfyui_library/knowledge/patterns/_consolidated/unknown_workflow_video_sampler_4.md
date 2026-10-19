---
name: unknown_workflow_video_sampler_4
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.928333
common_nodes: [DownloadAndLoadMimicMotionModel, GetImageSizeAndCount, LoadImage, MimicMotionDecode, MimicMotionGetPoses, MimicMotionSampler, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1953091916986519553.json, 视频生成/图生视频/2036712403487956993.json, 视频生成/图生视频/1909639467118882818.json, 视频生成/图生视频/1909815248260427777.json, 视频生成/图生视频/1897884391828312065.json, 视频生成/图生视频/1896079729521262594.json, 视频生成/图生视频/1898671504601894913.json, 视频生成/图生视频/1899399710896209921.json, 视频生成/图生视频/1898791557779410945.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_4

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1953091916986519553.json、视频生成/图生视频/2036712403487956993.json、视频生成/图生视频/1909639467118882818.json、视频生成/图生视频/1909815248260427777.json、视频生成/图生视频/1897884391828312065.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `DownloadAndLoadMimicMotionModel`
- `GetImageSizeAndCount`
- `LoadImage`
- `MimicMotionDecode`
- `MimicMotionGetPoses`
- `MimicMotionSampler`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 8/9 个有
- `RIFE VFI` —— 7/9 个有
- `ImageScale` —— 6/9 个有
- `ImageCASharpening+` —— 5/9 个有
- `DiffusersScheduler` —— 4/9 个有
- `PreviewImage` —— 2/9 个有
- `EmptyImage` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `Note Plus (mtb)` —— 1/9 个有
- `ReActorFaceSwap` —— 1/9 个有
- `easy imageSize` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
