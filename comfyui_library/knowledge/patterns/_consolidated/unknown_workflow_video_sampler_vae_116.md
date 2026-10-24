---
name: unknown_workflow_video_sampler_vae_116
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9448
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/b站开源二次元ani全能视频S视频模型_1945071960848257026.json, 视频生成/图生视频/lightx2v-720P-图到视频-rank128-rank32-FreeInit对比测试_1945761108445556738.json, 视频生成/图生视频/pose-sync1024_1921944895412699138.json, 视频生成/图生视频/万相Skyreels V2图生长视频_1915024014367227906.json, 视频生成/文生视频/Uni-DIT-720p-14B-pose_1917099381894615042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_116

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/b站开源二次元ani全能视频S视频模型_1945071960848257026.json、视频生成/图生视频/lightx2v-720P-图到视频-rank128-rank32-FreeInit对比测试_1945761108445556738.json、视频生成/图生视频/pose-sync1024_1921944895412699138.json、视频生成/图生视频/万相Skyreels V2图生长视频_1915024014367227906.json、视频生成/文生视频/Uni-DIT-720p-14B-pose_1917099381894615042.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 4/5 个有
- `WanVideoTeaCache` —— 4/5 个有
- `LoadWanVideoClipTextEncoder` —— 3/5 个有
- `WanVideoExperimentalArgs` —— 3/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `CLIPVisionLoader` —— 2/5 个有
- `Int` —— 2/5 个有
- `RH_Captioner` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `WanVideoFreeInitArgs` —— 2/5 个有
- `WanVideoUniAnimatePoseInput` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `KepStringLiteral` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `TextInputBasic` —— 1/5 个有
- `WanVideoMagCache` —— 1/5 个有
- `easy seed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
