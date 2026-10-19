---
name: unknown_workflow_video_sampler_clip_80
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.969571
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, FramePackFindNearestBucket, FramePackSampler, GetImageSizeAndCount, LoadImage, VAEDecodeTiled, VAEEncode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1926986867307413505.json, 视频生成/图生视频/1949738766808342529.json, 视频生成/图生视频/1924759278522200066.json, 视频生成/图生视频/1930280141065457666.json, 视频生成/图生视频/1923621170799628290.json, 视频生成/文生视频/1927342348001513474.json, 视频生成/文生视频/framepack视频工作流_1980523888222359553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_80

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1926986867307413505.json、视频生成/图生视频/1949738766808342529.json、视频生成/图生视频/1924759278522200066.json、视频生成/图生视频/1930280141065457666.json、视频生成/图生视频/1923621170799628290.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FramePackFindNearestBucket`
- `FramePackSampler`
- `GetImageSizeAndCount`
- `LoadImage`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `LoadFramePackModel` —— 6/7 个有
- `ImageResize+` —— 5/7 个有
- `DownloadAndLoadFramePackModel` —— 2/7 个有
- `Anything Everywhere3` —— 1/7 个有
- `Bjornulf_ShowInt` —— 1/7 个有
- `Float` —— 1/7 个有
- `FramePackTorchCompileSettings` —— 1/7 个有
- `ImageScale` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `SaveAnimatedWEBP` —— 1/7 个有
- `easy imageScaleDown` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
