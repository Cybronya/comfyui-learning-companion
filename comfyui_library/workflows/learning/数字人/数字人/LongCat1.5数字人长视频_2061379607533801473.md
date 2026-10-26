---
key: 数字人/数字人/LongCat1.5数字人长视频_2061379607533801473.json
name: LongCat1.5数字人长视频_2061379607533801473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LongCat1.5数字人长视频_2061379607533801473.json
hash: ea610da642c0d16c
coverage: 0.541667
learned_at: 2026-10-26 01:56:23
nodes: [GetNode, WanVideoDecode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, ImageBatchExtendWithOverlap, WanVideoTextEncodeCached, PrimitiveNode, GetNode, GetNode, easy showAnything, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetNode, GetNode, GetNode, WanVideoModelLoader, WanVideoLoraSelect, SetNode, GetNode, WanVideoSamplerv2, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, ImageBatchExtendWithOverlap, GetNode, WanVideoTextEncodeCached, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, WanVideoSchedulerv2, easy forLoopEnd, GetImageSizeAndCount, LongCatAvatarWhisperEmbeds, SimpleMath+, Reroute, SetNode, WanVideoVAELoader, FloatConstant, GetNode, MathExpression|pysssss, easy promptLine, easy showAnything, PrimitiveNode, easy showAnything, WanVideoLongCatAvatarExtendEmbeds, TrimAudioDuration, PreviewAudio, VHS_VideoCombine, VHS_VideoCombine, GetImageSizeAndCount, WhisperModelLoader, FloatConstant, WanVideoBlockSwap, ReplaceVideoLatentFrames, WanVideoDecode, GetNode, easy forLoopStart, GetNode, SetNode, GetNode, SetNode, SetNode, MathExpression|pysssss, MathExpression|pysssss, easy promptLine, GetNode, WanVideoSamplerv2, GetNode, GetImageRangeFromBatch, WanVideoEncode, VHS_VideoCombine, INTConstant, SetNode, INTConstant, SetNode, FloatConstant, INTConstant, LoadImage, SetNode, INTConstant, SetNode, Float, CM_IntToFloat, GetAudioDurationFromAudio, LoadAudio, Text Multiline, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
---

# 数字人/数字人/LongCat1.5数字人长视频_2061379607533801473.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LongCat1.5数字人长视频_2061379607533801473.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（96 个）：
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `WanVideoTextEncodeCached`
- `PrimitiveNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `SetNode`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `WanVideoEncode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `WanVideoTextEncodeCached`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoSchedulerv2`
- `easy forLoopEnd`
- `GetImageSizeAndCount`
- `LongCatAvatarWhisperEmbeds`
- `SimpleMath+`
- `Reroute`
- `SetNode`
- `WanVideoVAELoader`
- `FloatConstant`
- `GetNode`
- `MathExpression|pysssss`
- `easy promptLine`
- `easy showAnything`
- `PrimitiveNode`
- `easy showAnything`
- `WanVideoLongCatAvatarExtendEmbeds`
- `TrimAudioDuration`
- `PreviewAudio`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `WhisperModelLoader`
- `FloatConstant`
- `WanVideoBlockSwap`
- `ReplaceVideoLatentFrames`
- `WanVideoDecode`
- `GetNode`
- `easy forLoopStart`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy promptLine`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `GetNode`
- `GetImageRangeFromBatch`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SetNode`
- `FloatConstant`
- `INTConstant`
- `LoadImage`
- `SetNode`
- `INTConstant`
- `SetNode`
- `Float`
- `CM_IntToFloat`
- `GetAudioDurationFromAudio`
- `LoadAudio`
- `Text Multiline`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 知识

覆盖率 **54%**（52/96）

**有卡**：`WanVideoDecode`、`ImageBatchExtendWithOverlap`、`WanVideoTextEncodeCached`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSamplerv2`、`WanVideoEncode`、`WanVideoLongCatAvatarExtendEmbeds`、`WanVideoSchedulerv2`、`easy forLoopEnd`、`GetImageSizeAndCount`、`LongCatAvatarWhisperEmbeds`、`SimpleMath+`、`WanVideoVAELoader`、`FloatConstant`、`MathExpression|pysssss`、`easy promptLine`、`TrimAudioDuration`、`PreviewAudio`、`VHS_VideoCombine`、`WhisperModelLoader`、`WanVideoBlockSwap`、`ReplaceVideoLatentFrames`、`easy forLoopStart`、`GetImageRangeFromBatch`、`INTConstant`、`LoadImage`、`Float`、`CM_IntToFloat`、`GetAudioDurationFromAudio`、`LoadAudio`、`Text Multiline`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames、WanVideoLoraSelect
