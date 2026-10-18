---
key: 视频生成/图生视频/LongCatAvatar_audio_image_to_video_auto-extend_2004216271933767681.json
name: LongCatAvatar_audio_image_to_video_auto-extend_2004216271933767681.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LongCatAvatar_audio_image_to_video_auto-extend_2004216271933767681.json
hash: 61543bf35621512d
coverage: 0.430233
learned_at: 2026-10-15 22:33:53
nodes: [SetNode, SetNode, FloatConstant, GetNode, GetNode, GetNode, INTConstant, SetNode, SetNode, INTConstant, INTConstant, WanVideoModelLoader, WanVideoBlockSwap, WanVideoVAELoader, SetNode, SetNode, CLIPVisionLoader, SetNode, MarkdownNote, WanVideoLoraSelect, Note, Note, LoadImage, GetNode, GetNode, ImageResizeKJv2, GetNode, WanVideoEncode, SetNode, LoadAudio, MelBandRoFormerSampler, DownloadAndLoadWav2VecModel, MarkdownNote, SetNode, PreviewAny, SetNode, INTConstant, WanVideoSchedulerv2, SetNode, SetNode, WanVideoLongCatAvatarExtendEmbeds, GetNode, GetNode, WanVideoSamplerv2, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoLongCatAvatarExtendEmbeds, Reroute, WanVideoEncode, GetNode, GetNode, GetImageRangeFromBatch, ReplaceVideoLatentFrames, WanVideoDecode, VHS_VideoCombine, SetNode, PreviewAny, MelBandRoFormerModelLoader, MarkdownNote, GetNode, SetNode, GetImageSizeAndCount, Reroute, GetNode, easy forLoopStart, ImageBatchExtendWithOverlap, GetNode, easy forLoopEnd, GetNode, MathExpression|pysssss, SetNode, GetNode, WanVideoDecode, WanVideoSamplerv2, WanVideoTextEncodeCached, Note, MultiTalkWav2VecEmbeds, TrimAudioDuration, GetNode, GetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/LongCatAvatar_audio_image_to_video_auto-extend_2004216271933767681.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2004216271933767681.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（86 个）：
- `SetNode`
- `SetNode`
- `FloatConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `MarkdownNote`
- `WanVideoLoraSelect`
- `Note`
- `Note`
- `LoadImage`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `WanVideoEncode`
- `SetNode`
- `LoadAudio`
- `MelBandRoFormerSampler` ★核心
- `DownloadAndLoadWav2VecModel`
- `MarkdownNote`
- `SetNode`
- `PreviewAny`
- `SetNode`
- `INTConstant`
- `WanVideoSchedulerv2`
- `SetNode`
- `SetNode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetNode`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `Reroute`
- `WanVideoEncode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `ReplaceVideoLatentFrames`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `SetNode`
- `PreviewAny`
- `MelBandRoFormerModelLoader`
- `MarkdownNote`
- `GetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `Reroute`
- `GetNode`
- `easy forLoopStart`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `easy forLoopEnd`
- `GetNode`
- `MathExpression|pysssss`
- `SetNode`
- `GetNode`
- `WanVideoDecode`
- `WanVideoSamplerv2` ★核心
- `WanVideoTextEncodeCached`
- `Note`
- `MultiTalkWav2VecEmbeds`
- `TrimAudioDuration`
- `GetNode`
- `GetNode`

## 知识

覆盖率 **43%**（37/86）

**有卡**：`FloatConstant`、`INTConstant`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoLoraSelect`、`LoadImage`、`ImageResizeKJv2`、`WanVideoEncode`、`LoadAudio`、`MelBandRoFormerSampler`、`DownloadAndLoadWav2VecModel`、`WanVideoSchedulerv2`、`WanVideoLongCatAvatarExtendEmbeds`、`WanVideoSamplerv2`、`VHS_VideoCombine`、`GetImageRangeFromBatch`、`ReplaceVideoLatentFrames`、`WanVideoDecode`、`MelBandRoFormerModelLoader`、`GetImageSizeAndCount`、`easy forLoopStart`、`ImageBatchExtendWithOverlap`、`easy forLoopEnd`、`MathExpression|pysssss`、`WanVideoTextEncodeCached`、`MultiTalkWav2VecEmbeds`、`TrimAudioDuration`

**用到的条目**：LoadImage、MelBandRoFormerSampler、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames
