---
key: 视频生成/图生视频/LongCatAvatar_audio_image_to_video_example_Kijai_2004028313129656322.json
name: LongCatAvatar_audio_image_to_video_example_Kijai_2004028313129656322.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LongCatAvatar_audio_image_to_video_example_Kijai_2004028313129656322.json
hash: 0540c5793f39d8a4
coverage: 0.431373
learned_at: 2026-10-15 22:33:52
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, PreviewAny, GetNode, Note, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSamplerv2, Reroute, Reroute, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, WanVideoDecode, GetNode, WanVideoDecode, GetNode, GetNode, WanVideoEncode, GetNode, ReplaceVideoLatentFrames, GetNode, GetNode, GetNode, GetNode, Reroute, GetNode, Reroute, GetNode, ImageBatchExtendWithOverlap, WanVideoLongCatAvatarExtendEmbeds, GetNode, GetImageSizeAndCount, GetImageRangeFromBatch, WanVideoDecode, GetNode, Reroute, Reroute, MarkdownNote, SetNode, Note, SetNode, SetNode, WanVideoSamplerv2, GetNode, GetNode, WanVideoSamplerv2, Note, MarkdownNote, GetNode, SetNode, GetNode, GetNode, VHS_VideoCombine, WanVideoModelLoader, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoVAELoader, CLIPVisionLoader, LoadImage, ImageResizeKJv2, WanVideoEncode, SetNode, LoadAudio, TrimAudioDuration, MelBandRoFormerSampler, MelBandRoFormerModelLoader, MarkdownNote, DownloadAndLoadWav2VecModel, Wav2VecModelLoader, INTConstant, INTConstant, INTConstant, INTConstant, FloatConstant, WanVideoTextEncodeCached, WanVideoLongCatAvatarExtendEmbeds, GetNode, WanVideoSchedulerv2, GetImageSizeAndCount, WanVideoLongCatAvatarExtendEmbeds, GetNode, GetNode, WanVideoEncode, GetImageRangeFromBatch, ReplaceVideoLatentFrames, ImageBatchExtendWithOverlap, MultiTalkWav2VecEmbeds, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/LongCatAvatar_audio_image_to_video_example_Kijai_2004028313129656322.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2004028313129656322.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（102 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `PreviewAny`
- `GetNode`
- `Note`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `Reroute`
- `Reroute`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `GetNode`
- `ReplaceVideoLatentFrames`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `GetNode`
- `Reroute`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetNode`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `WanVideoDecode`
- `GetNode`
- `Reroute`
- `Reroute`
- `MarkdownNote`
- `SetNode`
- `Note`
- `SetNode`
- `SetNode`
- `WanVideoSamplerv2` ★核心
- `GetNode`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `Note`
- `MarkdownNote`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `LoadImage`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `SetNode`
- `LoadAudio`
- `TrimAudioDuration`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `MarkdownNote`
- `DownloadAndLoadWav2VecModel`
- `Wav2VecModelLoader`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `FloatConstant`
- `WanVideoTextEncodeCached`
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetNode`
- `WanVideoSchedulerv2`
- `GetImageSizeAndCount`
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `GetImageRangeFromBatch`
- `ReplaceVideoLatentFrames`
- `ImageBatchExtendWithOverlap`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **43%**（44/102）

**有卡**：`WanVideoSamplerv2`、`WanVideoDecode`、`WanVideoEncode`、`ReplaceVideoLatentFrames`、`ImageBatchExtendWithOverlap`、`WanVideoLongCatAvatarExtendEmbeds`、`GetImageSizeAndCount`、`GetImageRangeFromBatch`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`CLIPVisionLoader`、`LoadImage`、`ImageResizeKJv2`、`LoadAudio`、`TrimAudioDuration`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`DownloadAndLoadWav2VecModel`、`Wav2VecModelLoader`、`INTConstant`、`FloatConstant`、`WanVideoTextEncodeCached`、`WanVideoSchedulerv2`、`MultiTalkWav2VecEmbeds`

**用到的条目**：LoadImage、MelBandRoFormerSampler、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames
