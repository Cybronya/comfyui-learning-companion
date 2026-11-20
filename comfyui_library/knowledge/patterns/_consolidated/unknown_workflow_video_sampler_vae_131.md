---
name: unknown_workflow_video_sampler_vae_131
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 1
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/CausVid-3步720文生视频(Wan2.1&MoviiGen&Skyreels)_1923393888814624770.json, 视频生成/文生视频/Self Forcing-文生图&图生视频_1933051482759630849.json, 视频生成/文生视频/万相WanVACE-14B文生视频_1923955106968948737.json, 视频生成/文生视频/文生视频(Wan2.1-VACE-14B)_1922920161509261314.json, 视频生成/文生视频/最新wan2.1 首_中_尾多 图生视频_1935254064009498626.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_131

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/CausVid-3步720文生视频(Wan2.1&MoviiGen&Skyreels)_1923393888814624770.json、视频生成/文生视频/Self Forcing-文生图&图生视频_1933051482759630849.json、视频生成/文生视频/万相WanVACE-14B文生视频_1923955106968948737.json、视频生成/文生视频/文生视频(Wan2.1-VACE-14B)_1922920161509261314.json、视频生成/文生视频/最新wan2.1 首_中_尾多 图生视频_1935254064009498626.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 4/5 个有
- `String Literal` —— 4/5 个有
- `WanVideoBlockSwap` —— 4/5 个有
- `WanVideoSLG` —— 4/5 个有
- `WanVideoTeaCache` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 4/5 个有
- `GetImageSizeAndCount` —— 2/5 个有
- `ImageResizeKJ` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `WanVideoVACEStartToEndFrame` —— 2/5 个有
- `GetImageRangeFromBatch` —— 1/5 个有
- `ImageBatchMulti` —— 1/5 个有
- `MaskBatchMulti` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `WanVideoLoraSelect` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
