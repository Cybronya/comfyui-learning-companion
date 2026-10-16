---
key: 视频生成/图生视频/LongCat Avatar 1.5：8步极速生成、音频驱动超长数字人_2065330795597877250.json
name: LongCat Avatar 1.5：8步极速生成、音频驱动超长数字人_2065330795597877250.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2065330795597877250.json
hash: 4e7364e13173d92b
coverage: 0.506849
learned_at: 2026-10-15 22:39:38
nodes: [WanAnimatePlus BlockSwap, INTConstant, INTConstant, GetNode, SetNode, SetNode, INTConstant, SetNode, INTConstant, SetNode, GetNode, FloatConstant, SetNode, SetNode, ComfyMathExpression, SetNode, PreviewAudio, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, GetNode, SetNode, VHS_VideoCombine, PreviewAny, GetNode, GetNode, PreviewAny, GetNode, GetNode, GetNode, GetImageSize, GetNode, GetNode, ImageBatchExtendWithOverlap, VHS_VideoCombine, ImageResizeKJv2, easy forLoopEnd, WanVideoSamplerv2, GetNode, SetNode, WanVideoTextEncodeCached, WanVideoSchedulerv2, WanVideoModelLoader, WanVideoLoraSelect, WanVideoVAELoader, SetNode, WhisperModelLoader, LongCatAvatarWhisperEmbeds, WanVideoEncode, WanVideoSamplerv2, WanVideoLongCatAvatarExtendEmbeds, GetNode, WanVideoDecode, ComfyMathExpression, easy forLoopStart, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, GetNode, GetNode, TrimAudioDuration, GetNode, GetImageRangeFromBatch, WanVideoEncode, ReplaceVideoLatentFrames, WanVideoDecode, LoadAudio, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/LongCat Avatar 1.5：8步极速生成、音频驱动超长数字人_2065330795597877250.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2065330795597877250.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（73 个）：
- `WanAnimatePlus BlockSwap`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SetNode`
- `GetNode`
- `FloatConstant`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `PreviewAudio`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `GetNode`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `easy forLoopEnd`
- `WanVideoSamplerv2` ★核心
- `GetNode`
- `SetNode`
- `WanVideoTextEncodeCached`
- `WanVideoSchedulerv2`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `SetNode`
- `WhisperModelLoader`
- `LongCatAvatarWhisperEmbeds`
- `WanVideoEncode`
- `WanVideoSamplerv2` ★核心
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetNode`
- `WanVideoDecode`
- `ComfyMathExpression`
- `easy forLoopStart`
- `WanVideoEncode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetNode`
- `GetNode`
- `TrimAudioDuration`
- `GetNode`
- `GetImageRangeFromBatch`
- `WanVideoEncode`
- `ReplaceVideoLatentFrames`
- `WanVideoDecode`
- `LoadAudio`
- `LoadImage`

## 知识

覆盖率 **51%**（37/73）

**有卡**：`WanAnimatePlus BlockSwap`、`INTConstant`、`FloatConstant`、`ComfyMathExpression`、`PreviewAudio`、`VHS_VideoCombine`、`GetImageSize`、`ImageBatchExtendWithOverlap`、`ImageResizeKJv2`、`easy forLoopEnd`、`WanVideoSamplerv2`、`WanVideoTextEncodeCached`、`WanVideoSchedulerv2`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WhisperModelLoader`、`LongCatAvatarWhisperEmbeds`、`WanVideoEncode`、`WanVideoLongCatAvatarExtendEmbeds`、`WanVideoDecode`、`easy forLoopStart`、`TrimAudioDuration`、`GetImageRangeFromBatch`、`ReplaceVideoLatentFrames`、`LoadAudio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames、WanVideoLoraSelect
