---
name: unknown_workflow_video_sampler_vae_98
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9038
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2028880263652052993.json, 视频生成/图生视频/1998953194820620290.json, 视频生成/图生视频/2070420975967100929.json, 视频生成/图生视频/2035945836609277954.json, 音频生成/音频生成/数字人（图片对口型）＋声音克隆（单人_双人）_2013652200806944769.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_98

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2028880263652052993.json、视频生成/图生视频/1998953194820620290.json、视频生成/图生视频/2070420975967100929.json、视频生成/图生视频/2035945836609277954.json、音频生成/音频生成/数字人（图片对口型）＋声音克隆（单人_双人）_2013652200806944769.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAudio` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `RH_GetAudioDuration` —— 3/5 个有
- `WanVideoLoraSelectMulti` —— 3/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `PrimitiveFloat` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有
- `ToInt` —— 2/5 个有
- `WanVideoLoraSelect` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `Int` —— 1/5 个有
- `LatentSyncNode` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `SaveAudio` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `VideoLengthAdjuster` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/5 个有
- `easy indexTTSAudioMerge` —— 1/5 个有
- `easy indexTTSEmotionVector` —— 1/5 个有
- `easy indexTTSGenerateSimple` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
