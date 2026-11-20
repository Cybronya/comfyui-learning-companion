---
name: unknown_workflow_video_lora_sampler_988
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.579
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/视频对口型数字人_InfiniteTalk_V2V_2083750945984442370.json, 音频生成/音频生成/★视频数字人支持克隆+配音_2048759846756945922.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_988

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/视频对口型数字人_InfiniteTalk_V2V_2083750945984442370.json、音频生成/音频生成/★视频数字人支持克隆+配音_2048759846756945922.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：58%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `VHS_LoadVideo`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 1/2 个有
- `DownloadAndLoadWav2VecModel` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `Wav2VecModelLoader` —— 1/2 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/2 个有
- `easy indexTTSGenerateSimple` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
