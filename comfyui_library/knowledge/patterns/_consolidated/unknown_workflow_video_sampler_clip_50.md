---
name: unknown_workflow_video_sampler_clip_50
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9164
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1919644489483223042.json, 视频生成/图生视频/1910561597662920706.json, 视频生成/图生视频/1912679086651834369.json, 视频生成/图生视频/1911803069842292737.json, 视频生成/图生视频/1954434539328290817.json, 视频生成/图生视频/1930215748042657793.json, 视频生成/图生视频/1919937999688372225.json, 视频生成/图生视频/1924715221024501762.json, 视频生成/图生视频/1900153764635095042.json, 视频生成/图生视频/1927224699863072769.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_50

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1919644489483223042.json、视频生成/图生视频/1910561597662920706.json、视频生成/图生视频/1912679086651834369.json、视频生成/图生视频/1911803069842292737.json、视频生成/图生视频/1954434539328290817.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：92%

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
- `WanVideoBlockSwap` —— 9/10 个有
- `WanVideoLoraSelect` —— 7/10 个有
- `CR Upscale Image` —— 6/10 个有
- `RIFE VFI` —— 6/10 个有
- `WanVideoTeaCache` —— 5/10 个有
- `ImageResizeKJ` —— 4/10 个有
- `WanVideoEnhanceAVideo` —— 4/10 个有
- `WanVideoTorchCompileSettings` —— 4/10 个有
- `GetImageSizeAndCount` —— 3/10 个有
- `easy cleanGpuUsed` —— 3/10 个有
- `ImageResizeAdvanced` —— 2/10 个有
- `WanVideoContextOptions` —— 2/10 个有
- `WanVideoExperimentalArgs` —— 2/10 个有
- `Fast Groups Muter (rgthree)` —— 1/10 个有
- `JjkText` —— 1/10 个有
- `Primitive integer [Crystools]` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
