---
name: unknown_workflow_video_sampler_clip_64
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8936
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.1图生视频(cache加速版)_1954434539328290817.json, 视频生成/图生视频/wan2.1捏捏乐_1896450417918345217.json, 视频生成/图生视频/wan2.1通义万相图生视频蹦蹦跳跳工作流_1899811031231639553.json, 视频生成/图生视频/wan镜头拉近到眼睛_1915835994845941761.json, 视频生成/图生视频/万物生花特效_1924715221024501762.json, 视频生成/图生视频/万相SkyreelsV2图生视频突破5秒时长_1914997055247347713.json, 视频生成/图生视频/电商产品旋转展示_1927224699863072769.json, 视频生成/图生视频/直播子弹时间特效_1927650029039960065.json, 视频生成/图生视频/直播定制赛亚人特效视频_1926260024211894274.json, 视频生成/图生视频/直播戏服变身_1926859927644704769.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_64

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/wan2.1图生视频(cache加速版)_1954434539328290817.json、视频生成/图生视频/wan2.1捏捏乐_1896450417918345217.json、视频生成/图生视频/wan2.1通义万相图生视频蹦蹦跳跳工作流_1899811031231639553.json、视频生成/图生视频/wan镜头拉近到眼睛_1915835994845941761.json、视频生成/图生视频/万物生花特效_1924715221024501762.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 9/10 个有
- `WanVideoBlockSwap` —— 8/10 个有
- `WanVideoEnhanceAVideo` —— 8/10 个有
- `WanVideoTeaCache` —— 8/10 个有
- `WanVideoTorchCompileSettings` —— 8/10 个有
- `ImageResizeKJ` —— 7/10 个有
- `WanVideoExperimentalArgs` —— 5/10 个有
- `JjkText` —— 4/10 个有
- `GetImageSizeAndCount` —— 2/10 个有
- `Int` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `WanVideoSLG` —— 2/10 个有
- `CropFace` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有
- `WanVideoContextOptions` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
