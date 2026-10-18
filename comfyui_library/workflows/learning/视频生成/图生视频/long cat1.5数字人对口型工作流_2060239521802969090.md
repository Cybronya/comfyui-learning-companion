---
key: 视频生成/图生视频/long cat1.5数字人对口型工作流_2060239521802969090.json
name: long cat1.5数字人对口型工作流_2060239521802969090.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/long cat1.5数字人对口型工作流_2060239521802969090.json
hash: f0c1d6cfc4aa6de2
coverage: 0.453988
learned_at: 2026-10-15 22:38:46
nodes: [SetNode, SetNode, WanVideoSamplerv2, GetNode, WanVideoDecode, GetNode, WanVideoSamplerv2, WanVideoEncode, WanVideoDecode, ReplaceVideoLatentFrames, ImageBatchExtendWithOverlap, SetNode, SetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetImageSizeAndCount, GetNode, GetNode, WanVideoSamplerv2, WanVideoEncode, WanVideoDecode, ReplaceVideoLatentFrames, ImageBatchExtendWithOverlap, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, SetNode, SetNode, GetNode, WanVideoLongCatAvatarExtendEmbeds, GetNode, GetImageSizeAndCount, GetNode, GetNode, WanVideoSamplerv2, WanVideoEncode, WanVideoDecode, ReplaceVideoLatentFrames, ImageBatchExtendWithOverlap, GetNode, GetNode, GetNode, GetImageRangeFromBatch, VHS_VideoCombine, GetNode, GetNode, SetNode, SetNode, GetNode, WanVideoLongCatAvatarExtendEmbeds, GetNode, GetImageSizeAndCount, GetNode, GetNode, WanVideoSamplerv2, WanVideoEncode, WanVideoDecode, ReplaceVideoLatentFrames, ImageBatchExtendWithOverlap, GetNode, GetNode, GetNode, GetImageRangeFromBatch, VHS_VideoCombine, GetNode, GetNode, SetNode, SetNode, WanVideoLongCatAvatarExtendEmbeds, GetImageRangeFromBatch, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, VHS_VideoCombine, WanVideoLoraSelect, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, SetNode, SetNode, GetNode, ComfyNumberConvert, SimpleMath+, LongCatAvatarWhisperEmbeds, GetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, WanVideoEncode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, INTConstant, INTConstant, SetNode, GetNode, WanVideoLongCatAvatarExtendEmbeds, GetNode, GetImageSizeAndCount, GetNode, GetNode, WanVideoSamplerv2, WanVideoEncode, WanVideoDecode, ReplaceVideoLatentFrames, ImageBatchExtendWithOverlap, GetNode, GetNode, GetNode, GetImageRangeFromBatch, VHS_VideoCombine, GetNode, GetNode, WanVideoTextEncodeCached, WanVideoTextEncodeCached, WanVideoTextEncodeCached, WanVideoTextEncodeCached, WanVideoTextEncodeCached, WhisperModelLoader, GetNode, SetNode, GetNode, WanVideoLongCatAvatarExtendEmbeds, WanVideoSchedulerv2, GetNode, GetNode, GetNode, GetImageRangeFromBatch, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, Note, GetNode, SetNode, SetNode, GetNode, GetNode, WanVideoLongCatAvatarExtendEmbeds, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, TrimAudioDuration, FloatConstant, Fast Groups Bypasser (rgthree), LoadImage, INTConstant, INTConstant, LoadAudio]
patterns: []
missing: []
---

# 视频生成/图生视频/long cat1.5数字人对口型工作流_2060239521802969090.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2060239521802969090.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（163 个）：
- `SetNode`
- `SetNode`
- `WanVideoSamplerv2` ★核心
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `WanVideoEncode`
- `WanVideoDecode`
- `ReplaceVideoLatentFrames`
- `ImageBatchExtendWithOverlap`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `WanVideoEncode`
- `WanVideoDecode`
- `ReplaceVideoLatentFrames`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `WanVideoEncode`
- `WanVideoDecode`
- `ReplaceVideoLatentFrames`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `WanVideoEncode`
- `WanVideoDecode`
- `ReplaceVideoLatentFrames`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `ComfyNumberConvert`
- `SimpleMath+`
- `LongCatAvatarWhisperEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `WanVideoEncode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `GetNode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `WanVideoEncode`
- `WanVideoDecode`
- `ReplaceVideoLatentFrames`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoTextEncodeCached`
- `WanVideoTextEncodeCached`
- `WanVideoTextEncodeCached`
- `WanVideoTextEncodeCached`
- `WhisperModelLoader`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `WanVideoSchedulerv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `Note`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `TrimAudioDuration`
- `FloatConstant`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `LoadAudio`

## 知识

覆盖率 **45%**（74/163）

**有卡**：`WanVideoSamplerv2`、`WanVideoDecode`、`WanVideoEncode`、`ReplaceVideoLatentFrames`、`ImageBatchExtendWithOverlap`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`WanVideoLongCatAvatarExtendEmbeds`、`GetImageRangeFromBatch`、`WanVideoTextEncodeCached`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`ComfyNumberConvert`、`SimpleMath+`、`LongCatAvatarWhisperEmbeds`、`ImageResizeKJv2`、`INTConstant`、`WhisperModelLoader`、`WanVideoSchedulerv2`、`TrimAudioDuration`、`FloatConstant`、`LoadImage`、`LoadAudio`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames、WanVideoLoraSelect
