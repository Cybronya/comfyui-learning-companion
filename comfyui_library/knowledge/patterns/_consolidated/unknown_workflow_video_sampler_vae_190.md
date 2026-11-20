---
name: unknown_workflow_video_sampler_vae_190
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.945333
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/FusionX图生视频0620_1935947628817342465.json, 视频生成/图生视频/Wan FusionX 图生视频-极速版_1940936064079183874.json, 视频生成/图生视频/Wan2.1(KJ)图片到视频基础工作流_1947465024660983810.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_190

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/FusionX图生视频0620_1935947628817342465.json、视频生成/图生视频/Wan FusionX 图生视频-极速版_1940936064079183874.json、视频生成/图生视频/Wan2.1(KJ)图片到视频基础工作流_1947465024660983810.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 2/3 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/3 个有
- `GIMMVFI_interpolate` —— 2/3 个有
- `ImageResizeKJ` —— 2/3 个有
- `WanVideoClipVisionEncode` —— 2/3 个有
- `WanVideoSLG` —— 2/3 个有
- `WanVideoTeaCache` —— 2/3 个有
- `ImageFromBatch+` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `WanVideoExperimentalArgs` —— 1/3 个有
- `WanVideoFreeInitArgs` —— 1/3 个有
- `WanVideoLoraSelectMulti` —— 1/3 个有
- `WanVideoVACEModelSelect` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
