---
name: unknown_workflow_video_lora_sampler_843
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9045
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPVisionLoader, CR Text, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, ImageFromBatch+, ImageResizeKJv2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PrimitiveInt, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2图生视频+动态字幕对口型（说话-唱歌）_1983773749944197122.json, 音频生成/音频生成/最新视频对口型工作流_1966738551159336961.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_843

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/wan2.2图生视频+动态字幕对口型（说话-唱歌）_1983773749944197122.json、音频生成/音频生成/最新视频对口型工作流_1966738551159336961.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `ImageResizeKJv2`
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
- `HAIGC_VideoSubtitleEnhanced` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `LoadWanVideoT5TextEncoder` —— 1/2 个有
- `SaveAudioMP3` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有
- `WanVideoSetBlockSwap` —— 1/2 个有
- `WanVideoTextEncode` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/2 个有
- `easy indexTTSGenerateSimple` —— 1/2 个有
- `孤海-取色器` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
