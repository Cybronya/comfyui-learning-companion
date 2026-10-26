---
name: unknown_workflow_video_sampler_13
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.938
common_nodes: [CLIPLoader, CogVideoDecode, CogVideoImageEncode, CogVideoSampler, CogVideoTextEncode, DownloadAndLoadCogVideoModel, ImageResizeKJ, LoadImage, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/CogVideoX-I2V 图生视频_1844070499650539521.json, 视频生成/图生视频/CogVideoX-I2V 竖屏模式-图生视频_1844805165072175106.json, 视频生成/图生视频/图片转视频 CogVideoX-5b-I2V_1836407132143992833.json, 视频生成/图生视频/图片转视频 CogVideoX-5b-I2V_1977986107558219777.json, 视频生成/图生视频/抖音网红视频图生视频_1888124057349718017.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_13

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/CogVideoX-I2V 图生视频_1844070499650539521.json、视频生成/图生视频/CogVideoX-I2V 竖屏模式-图生视频_1844805165072175106.json、视频生成/图生视频/图片转视频 CogVideoX-5b-I2V_1836407132143992833.json、视频生成/图生视频/图片转视频 CogVideoX-5b-I2V_1977986107558219777.json、视频生成/图生视频/抖音网红视频图生视频_1888124057349718017.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CogVideoDecode`
- `CogVideoImageEncode`
- `CogVideoSampler`
- `CogVideoTextEncode`
- `DownloadAndLoadCogVideoModel`
- `ImageResizeKJ`
- `LoadImage`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner` —— 4/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `RIFE VFI` —— 2/5 个有
- `VideoCombine_Adv` —— 2/5 个有
- `ImageResizeAdvanced` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
