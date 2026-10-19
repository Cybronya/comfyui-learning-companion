---
name: unknown_workflow_video_lora_sampler_957
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.579
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetNode, ImageResizeKJv2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/图片唱歌_2007669635780448258.json, 音频生成/音频生成/InfiniteTalk数字人+index-TTS2同步音视频生成_1975033453995536385.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_957

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/图片唱歌_2007669635780448258.json、音频生成/音频生成/InfiniteTalk数字人+index-TTS2同步音视频生成_1975033453995536385.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：58%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 1/2 个有
- `AudioCrop` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `IndexTTS2_Emotion` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `QZ_ResolutionPreset` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `Text` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
