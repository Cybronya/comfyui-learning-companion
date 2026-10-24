---
name: unknown_workflow_video_sampler_clip_77
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.8955
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/KJ纯净版_图生视频_480p_1919644489483223042.json, 视频生成/图生视频/WAN2.1 万相图生视频，效果强悍！_1910561597662920706.json, 视频生成/图生视频/WAN2.1 万相图生视频，效果强悍！_1912679086651834369.json, 视频生成/图生视频/wan2.1万象图生视频跳舞大摆锤+lora+放大补帧_1911803069842292737.json, 视频生成/图生视频/wan2.1图生视频(cache加速版)_1954434539328290817.json, 视频生成/图生视频/万物生花特效_1924715221024501762.json, 视频生成/图生视频/万相1080P60帧图生视频360度旋转（360°旋转lora）_1900153764635095042.json, 视频生成/图生视频/电商产品旋转展示_1927224699863072769.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_77

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/KJ纯净版_图生视频_480p_1919644489483223042.json、视频生成/图生视频/WAN2.1 万相图生视频，效果强悍！_1910561597662920706.json、视频生成/图生视频/WAN2.1 万相图生视频，效果强悍！_1912679086651834369.json、视频生成/图生视频/wan2.1万象图生视频跳舞大摆锤+lora+放大补帧_1911803069842292737.json、视频生成/图生视频/wan2.1图生视频(cache加速版)_1954434539328290817.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
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
- `WanVideoBlockSwap` —— 7/8 个有
- `WanVideoLoraSelect` —— 5/8 个有
- `WanVideoTeaCache` —— 5/8 个有
- `CR Upscale Image` —— 4/8 个有
- `ImageResizeKJ` —— 4/8 个有
- `RIFE VFI` —— 4/8 个有
- `WanVideoEnhanceAVideo` —— 4/8 个有
- `WanVideoTorchCompileSettings` —— 4/8 个有
- `GetImageSizeAndCount` —— 3/8 个有
- `easy cleanGpuUsed` —— 3/8 个有
- `ImageResizeAdvanced` —— 2/8 个有
- `WanVideoContextOptions` —— 2/8 个有
- `WanVideoExperimentalArgs` —— 2/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `Primitive integer [Crystools]` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
