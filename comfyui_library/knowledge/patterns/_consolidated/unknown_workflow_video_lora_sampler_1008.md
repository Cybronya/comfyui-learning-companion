---
name: unknown_workflow_video_lora_sampler_1008
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8015
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Infinitetalk_视频对口型-保持原视频动作一致_1979962837202276353.json, 数字人/数字人/zy1736_2015662602763898882.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1008

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/Infinitetalk_视频对口型-保持原视频动作一致_1979962837202276353.json、数字人/数字人/zy1736_2015662602763898882.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `Float to Int` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `RH_GetAudioDuration` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `VHS_LoadAudioUpload` —— 1/2 个有
- `easy int` —— 1/2 个有
- `easy seed` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `image_scale_pixel_v2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
