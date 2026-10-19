---
name: unknown_workflow_video_lora_sampler_492
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.47425
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, Float, FloatConstant, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageBatchExtendWithOverlap, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PreviewAny, ReplaceVideoLatentFrames, SetNode, TrimAudioDuration, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoTextEncodeCached, WanVideoVAELoader, Wav2VecModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/2002585439628345345.json, 视频生成/图生视频/2002677838857793538.json, 视频生成/图生视频/2059649854489583618.json, 视频生成/图生视频/2059162387521032194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_492

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2002585439628345345.json、视频生成/图生视频/2002677838857793538.json、视频生成/图生视频/2059649854489583618.json、视频生成/图生视频/2059162387521032194.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：47%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `Float`
- `FloatConstant`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PreviewAny`
- `ReplaceVideoLatentFrames`
- `SetNode`
- `TrimAudioDuration`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `Wav2VecModelLoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `ForLoopClose` —— 2/4 个有
- `ForLoopOpen` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `Int` —— 2/4 个有
- `JWInteger` —— 2/4 个有
- `LongCatAvatarWhisperEmbeds` —— 2/4 个有
- `MathExpression|pysssss` —— 2/4 个有
- `MultiTalkWav2VecEmbeds` —— 2/4 个有
- `PreviewAudio` —— 2/4 个有
- `Text Load Line From File` —— 2/4 个有
- `WhisperModelLoader` —— 2/4 个有
- `easy convertAnything` —— 2/4 个有
- `ImageBatchMulti` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `TextInput_` —— 1/4 个有
- `VHS_GetImageCount` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
