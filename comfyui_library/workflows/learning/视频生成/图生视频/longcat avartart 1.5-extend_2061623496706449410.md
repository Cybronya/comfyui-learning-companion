---
key: 视频生成/图生视频/longcat avartart 1.5-extend_2061623496706449410.json
name: longcat avartart 1.5-extend_2061623496706449410.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2061623496706449410.json
hash: d769f526f95ff1bf
coverage: 0.528571
learned_at: 2026-10-15 22:38:55
nodes: [WanAnimatePlus BlockSwap, INTConstant, SetNode, INTConstant, SetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, SetNode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVAELoader, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, FloatConstant, SetNode, SetNode, GetImageSize, WanVideoEncode, SetNode, WanVideoSamplerv2, GetNode, GetNode, WanVideoSchedulerv2, SetNode, SetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, WanVideoDecode, ReplaceVideoLatentFrames, GetNode, WanVideoDecode, WanVideoEncode, WanVideoDecode, PreviewAny, LoadAudio, WhisperModelLoader, GetNode, ComfyMathExpression, SetNode, SetNode, SetNode, LongCatAvatarWhisperEmbeds, TrimAudioDuration, PreviewAudio, WanVideoSamplerv2, VHS_VideoCombine, VHS_VideoCombine, LoadImage, WanVideoTextEncodeCached, INTConstant, INTConstant, GetNode, WanVideoLongCatAvatarExtendEmbeds, GetNode, GetNode, GetNode, WanVideoLongCatAvatarExtendEmbeds, GetImageRangeFromBatch, GetNode, ImageBatchExtendWithOverlap, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/longcat avartart 1.5-extend_2061623496706449410.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061623496706449410.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（70 个）：
- `WanAnimatePlus BlockSwap`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `FloatConstant`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `WanVideoEncode`
- `SetNode`
- `WanVideoSamplerv2` ★核心
- `GetNode`
- `GetNode`
- `WanVideoSchedulerv2`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoDecode`
- `ReplaceVideoLatentFrames`
- `GetNode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoDecode`
- `PreviewAny`
- `LoadAudio`
- `WhisperModelLoader`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `SetNode`
- `LongCatAvatarWhisperEmbeds`
- `TrimAudioDuration`
- `PreviewAudio`
- `WanVideoSamplerv2` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **53%**（37/70）

**有卡**：`WanAnimatePlus BlockSwap`、`INTConstant`、`ImageResizeKJv2`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`FloatConstant`、`GetImageSize`、`WanVideoEncode`、`WanVideoSamplerv2`、`WanVideoSchedulerv2`、`VHS_VideoCombine`、`WanVideoDecode`、`ReplaceVideoLatentFrames`、`LoadAudio`、`WhisperModelLoader`、`ComfyMathExpression`、`LongCatAvatarWhisperEmbeds`、`TrimAudioDuration`、`PreviewAudio`、`LoadImage`、`WanVideoTextEncodeCached`、`WanVideoLongCatAvatarExtendEmbeds`、`GetImageRangeFromBatch`、`ImageBatchExtendWithOverlap`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames、WanVideoLoraSelect
