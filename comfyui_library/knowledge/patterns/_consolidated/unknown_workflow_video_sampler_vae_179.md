---
name: unknown_workflow_video_sampler_vae_179
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8825
common_nodes: [CLIPVisionLoader, CR Text, DownloadAndLoadWav2VecModel, FantasyTalkingModelLoader, FantasyTalkingWav2VecEmbeds, Int, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/1921810331054833666.json, 视频生成/图生视频/1917113415993856002.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_179

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1921810331054833666.json、视频生成/图生视频/1917113415993856002.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Text`
- `DownloadAndLoadWav2VecModel`
- `FantasyTalkingModelLoader`
- `FantasyTalkingWav2VecEmbeds`
- `Int`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `IndexTTSNode` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SaveAudio` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `SparkTTSClone` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
