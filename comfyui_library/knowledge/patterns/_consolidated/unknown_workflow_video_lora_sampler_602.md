---
name: unknown_workflow_video_lora_sampler_602
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.904667
common_nodes: [Audio Duration (mtb), AudioSeparation, CLIPVisionLoader, CR Text, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, ImageFromBatch+, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PrimitiveInt, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1971843495331819522.json, 视频生成/图生视频/1983773749944197122.json, 音频生成/音频生成/最新视频对口型工作流_1966738551159336961.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_602

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1971843495331819522.json、视频生成/图生视频/1983773749944197122.json、音频生成/音频生成/最新视频对口型工作流_1966738551159336961.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PrimitiveInt`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `HAIGC_VideoSubtitleEnhanced` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `JWFloat` —— 1/3 个有
- `LoadWanVideoT5TextEncoder` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `SaveAudioMP3` —— 1/3 个有
- `VHS_VideoInfo` —— 1/3 个有
- `WanVideoImageToVideoEncode` —— 1/3 个有
- `WanVideoSetBlockSwap` —— 1/3 个有
- `WanVideoTextEncode` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/3 个有
- `easy indexTTSGenerateSimple` —— 1/3 个有
- `孤海-取色器` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
