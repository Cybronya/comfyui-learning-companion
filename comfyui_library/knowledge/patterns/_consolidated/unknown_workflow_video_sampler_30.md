---
name: unknown_workflow_video_sampler_30
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.937
common_nodes: [DownloadAndLoadMimicMotionModel, GetImageSizeAndCount, ImageResizeKJ, LoadImage, MimicMotionDecode, MimicMotionGetPoses, MimicMotionSampler, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/图生视频舞蹈版本_1820785763674927106.json, 视频生成/图生视频/MimicMotion一张照片转跳舞视频_1909639467118882818.json, 视频生成/图生视频/一键生成美女跳舞视频_1897884391828312065.json, 视频生成/图生视频/全民舞王_1897011447497662466.json, 视频生成/图生视频/美女一键跳舞_1899399710896209921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_30

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/图生视频舞蹈版本_1820785763674927106.json、视频生成/图生视频/MimicMotion一张照片转跳舞视频_1909639467118882818.json、视频生成/图生视频/一键生成美女跳舞视频_1897884391828312065.json、视频生成/图生视频/全民舞王_1897011447497662466.json、视频生成/图生视频/美女一键跳舞_1899399710896209921.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
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
- `RIFE VFI` —— 4/5 个有
- `ImageCASharpening+` —— 3/5 个有
- `ImageScale` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
