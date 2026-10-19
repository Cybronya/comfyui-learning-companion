---
name: unknown_workflow_video_sampler_vae_106
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8706
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1945071960848257026.json, 视频生成/图生视频/1945761108445556738.json, 视频生成/图生视频/1915024014367227906.json, 视频生成/图生视频/1933541518860800001.json, 视频生成/图生视频/1933704774371954690.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_106

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1945071960848257026.json、视频生成/图生视频/1945761108445556738.json、视频生成/图生视频/1915024014367227906.json、视频生成/图生视频/1933541518860800001.json、视频生成/图生视频/1933704774371954690.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 4/5 个有
- `WanVideoTeaCache` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 4/5 个有
- `CLIPVisionLoader` —— 3/5 个有
- `ImageResizeKJ` —— 3/5 个有
- `Int` —— 3/5 个有
- `WanVideoSLG` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `LoadAudio` —— 2/5 个有
- `LoadWanVideoClipTextEncoder` —— 2/5 个有
- `MathExpression|pysssss` —— 2/5 个有
- `RH_Captioner` —— 2/5 个有
- `WanVideoFreeInitArgs` —— 2/5 个有
- `WanVideoVRAMManagement` —— 2/5 个有
- `WanVideoExperimentalArgs` —— 1/5 个有
- `WanVideoMagCache` —— 1/5 个有
- `easy seed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
