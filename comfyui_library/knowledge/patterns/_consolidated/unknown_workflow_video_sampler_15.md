---
name: unknown_workflow_video_sampler_15
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.899
common_nodes: [DownloadAndLoadMimicMotionModel, GetImageSizeAndCount, ImageResizeKJ, LoadImage, MimicMotionDecode, MimicMotionGetPoses, MimicMotionSampler, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1971772867861999618.json, 视频生成/图生视频/1897825295863336961.json, 视频生成/图生视频/1897011447497662466.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_15

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1971772867861999618.json、视频生成/图生视频/1897825295863336961.json、视频生成/图生视频/1897011447497662466.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `DownloadAndLoadMimicMotionModel`
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `LoadImage`
- `MimicMotionDecode`
- `MimicMotionGetPoses`
- `MimicMotionSampler`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `RIFE VFI` —— 2/3 个有
- `ReActorFaceSwap` —— 2/3 个有
- `CR Upscale Image` —— 1/3 个有
- `Int` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
