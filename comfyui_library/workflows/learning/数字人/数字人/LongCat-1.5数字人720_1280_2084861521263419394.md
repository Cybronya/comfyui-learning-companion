---
key: 数字人/数字人/LongCat-1.5数字人720_1280_2084861521263419394.json
name: LongCat-1.5数字人720_1280_2084861521263419394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LongCat-1.5数字人720_1280_2084861521263419394.json
hash: 09fa9a1a15caa3f0
coverage: 0.531915
learned_at: 2026-10-18 19:07:42
nodes: [GetNode, WanVideoDecode, GetNode, GetNode, GetNode, SetNode, GetNode, easy promptLine, GetNode, GetNode, GetNode, ImageBatchExtendWithOverlap, WanVideoTextEncodeCached, PrimitiveNode, GetNode, GetNode, GetNode, easy showAnything, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetNode, GetNode, GetNode, WanVideoModelLoader, WanVideoLoraSelect, SetNode, GetNode, WanVideoSamplerv2, WanVideoSamplerv2, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, ImageBatchExtendWithOverlap, GetNode, WanVideoDecode, WanVideoTextEncodeCached, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, WanVideoSchedulerv2, easy forLoopEnd, GetImageSizeAndCount, LongCatAvatarWhisperEmbeds, SimpleMath+, Reroute, SetNode, WanVideoVAELoader, FloatConstant, SetNode, SetNode, SetNode, GetNode, GetNode, MathExpression|pysssss, easy promptLine, easy showAnything, VHS_VideoCombine, GetNode, PrimitiveNode, easy showAnything, GetNode, SetNode, WanVideoLongCatAvatarExtendEmbeds, ReplaceVideoLatentFrames, WanVideoEncode, easy forLoopStart, TrimAudioDuration, PreviewAudio, SetNode, VHS_VideoCombine, VHS_VideoCombine, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, WhisperModelLoader, INTConstant, INTConstant, INTConstant, FloatConstant, SetNode, LoadImage, LoadAudio, FloatConstant, MathExpression|pysssss, Text Multiline, MathExpression|pysssss, FloatConstant, WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, INTConstant]
patterns: []
missing: []
---

# 数字人/数字人/LongCat-1.5数字人720_1280_2084861521263419394.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LongCat-1.5数字人720_1280_2084861521263419394.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（94 个）：
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `easy promptLine`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `WanVideoTextEncodeCached`
- `PrimitiveNode`
- `GetNode`
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
- `WanVideoSamplerv2` ★核心
- `WanVideoEncode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `WanVideoDecode`
- `WanVideoTextEncodeCached`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
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
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `easy promptLine`
- `easy showAnything`
- `VHS_VideoCombine`
- `GetNode`
- `PrimitiveNode`
- `easy showAnything`
- `GetNode`
- `SetNode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `ReplaceVideoLatentFrames`
- `WanVideoEncode`
- `easy forLoopStart`
- `TrimAudioDuration`
- `PreviewAudio`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `WhisperModelLoader`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `FloatConstant`
- `SetNode`
- `LoadImage`
- `LoadAudio`
- `FloatConstant`
- `MathExpression|pysssss`
- `Text Multiline`
- `MathExpression|pysssss`
- `FloatConstant`
- `WanVideoBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`

## 知识

覆盖率 **53%**（50/94）

**有卡**：`WanVideoDecode`、`easy promptLine`、`ImageBatchExtendWithOverlap`、`WanVideoTextEncodeCached`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSamplerv2`、`WanVideoEncode`、`WanVideoLongCatAvatarExtendEmbeds`、`WanVideoSchedulerv2`、`easy forLoopEnd`、`GetImageSizeAndCount`、`LongCatAvatarWhisperEmbeds`、`SimpleMath+`、`WanVideoVAELoader`、`FloatConstant`、`MathExpression|pysssss`、`VHS_VideoCombine`、`ReplaceVideoLatentFrames`、`easy forLoopStart`、`TrimAudioDuration`、`PreviewAudio`、`GetImageRangeFromBatch`、`WhisperModelLoader`、`INTConstant`、`LoadImage`、`LoadAudio`、`Text Multiline`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames、WanVideoLoraSelect
