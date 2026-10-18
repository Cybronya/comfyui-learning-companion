---
key: 视频生成/图生视频/longcat avartart 1.5-extend-auto_2061455238598586369.json
name: longcat avartart 1.5-extend-auto_2061455238598586369.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/longcat avartart 1.5-extend-auto_2061455238598586369.json
hash: ddb6cd7ca75cb31d
coverage: 0.532468
learned_at: 2026-10-15 22:38:54
nodes: [WanAnimatePlus BlockSwap, INTConstant, SetNode, INTConstant, SetNode, ImageResizeKJv2, SetNode, GetNode, SetNode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVAELoader, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, INTConstant, SetNode, INTConstant, SetNode, GetNode, WanVideoLongCatAvatarExtendEmbeds, SetNode, GetNode, GetNode, WanVideoSchedulerv2, WanVideoTextEncodeCached, GetNode, GetNode, ReplaceVideoLatentFrames, GetNode, WanVideoDecode, GetNode, GetNode, GetNode, WhisperModelLoader, GetNode, SetNode, SetNode, SetNode, LongCatAvatarWhisperEmbeds, TrimAudioDuration, VHS_VideoCombine, GetNode, WanVideoEncode, SetNode, SetNode, WanVideoSamplerv2, WanVideoDecode, VHS_VideoCombine, LoadAudio, ComfyMathExpression, FloatConstant, LoadImage, ImageBatchExtendWithOverlap, VHS_VideoCombine, PreviewAudio, PreviewAny, GetImageSize, VHS_VideoCombine, PreviewAny, WanVideoSamplerv2, WanVideoDecode, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoEncode, GetNode, GetNode, GetImageRangeFromBatch, VHS_VideoCombine, easy forLoopStart, easy forLoopEnd, ComfyMathExpression, GetNode, GetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/longcat avartart 1.5-extend-auto_2061455238598586369.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061455238598586369.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（77 个）：
- `WanAnimatePlus BlockSwap`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
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
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SetNode`
- `GetNode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoSchedulerv2`
- `WanVideoTextEncodeCached`
- `GetNode`
- `GetNode`
- `ReplaceVideoLatentFrames`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WhisperModelLoader`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LongCatAvatarWhisperEmbeds`
- `TrimAudioDuration`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoEncode`
- `SetNode`
- `SetNode`
- `WanVideoSamplerv2` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `LoadAudio`
- `ComfyMathExpression`
- `FloatConstant`
- `LoadImage`
- `ImageBatchExtendWithOverlap`
- `VHS_VideoCombine`
- `PreviewAudio`
- `PreviewAny`
- `GetImageSize`
- `VHS_VideoCombine`
- `PreviewAny`
- `WanVideoSamplerv2` ★核心
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `WanVideoEncode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`
- `easy forLoopStart`
- `easy forLoopEnd`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`

## 知识

覆盖率 **53%**（41/77）

**有卡**：`WanAnimatePlus BlockSwap`、`INTConstant`、`ImageResizeKJv2`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoLongCatAvatarExtendEmbeds`、`WanVideoSchedulerv2`、`WanVideoTextEncodeCached`、`ReplaceVideoLatentFrames`、`WanVideoDecode`、`WhisperModelLoader`、`LongCatAvatarWhisperEmbeds`、`TrimAudioDuration`、`VHS_VideoCombine`、`WanVideoEncode`、`WanVideoSamplerv2`、`LoadAudio`、`ComfyMathExpression`、`FloatConstant`、`LoadImage`、`ImageBatchExtendWithOverlap`、`PreviewAudio`、`GetImageSize`、`GetImageRangeFromBatch`、`easy forLoopStart`、`easy forLoopEnd`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames、WanVideoLoraSelect
