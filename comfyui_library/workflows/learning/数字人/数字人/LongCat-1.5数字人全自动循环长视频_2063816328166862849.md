---
key: 数字人/数字人/LongCat-1.5数字人全自动循环长视频_2063816328166862849.json
name: LongCat-1.5数字人全自动循环长视频_2063816328166862849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LongCat-1.5数字人全自动循环长视频_2063816328166862849.json
hash: 62376ee09559035d
coverage: 0.526316
learned_at: 2026-10-26 01:56:20
nodes: [GetNode, WanVideoDecode, GetNode, GetNode, GetNode, GetNode, easy promptLine, GetNode, GetNode, ImageBatchExtendWithOverlap, WanVideoTextEncodeCached, PrimitiveNode, GetNode, GetNode, GetNode, easy showAnything, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetNode, GetNode, WanVideoModelLoader, WanVideoLoraSelect, SetNode, GetNode, WanVideoSamplerv2, WanVideoSamplerv2, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, ImageBatchExtendWithOverlap, GetNode, WanVideoDecode, WanVideoTextEncodeCached, SetNode, GetNode, GetNode, SetNode, WanVideoSchedulerv2, easy forLoopEnd, GetImageSizeAndCount, LongCatAvatarWhisperEmbeds, SimpleMath+, Reroute, SetNode, WanVideoVAELoader, GetNode, GetNode, easy promptLine, easy showAnything, VHS_VideoCombine, GetNode, PrimitiveNode, easy showAnything, GetNode, SetNode, WanVideoLongCatAvatarExtendEmbeds, ReplaceVideoLatentFrames, WanVideoEncode, easy forLoopStart, TrimAudioDuration, VHS_VideoCombine, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, WhisperModelLoader, INTConstant, FloatConstant, MathExpression|pysssss, MathExpression|pysssss, WanVideoBlockSwap, PreviewAudio, LayerUtility: ImageScaleByAspectRatio V2, GetNode, LoadAudio, SetNode, SetNode, SetNode, INTConstant, SetNode, GetNode, SetNode, INTConstant, SetNode, SetNode, SetNode, FloatConstant, SetNode, LoadImage, FloatConstant, FloatConstant, INTConstant, MathExpression|pysssss, Text Multiline, VHS_VideoCombine, 孤海注释]
patterns: []
missing: []
---

# 数字人/数字人/LongCat-1.5数字人全自动循环长视频_2063816328166862849.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LongCat-1.5数字人全自动循环长视频_2063816328166862849.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（95 个）：
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy promptLine`
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
- `WanVideoSchedulerv2`
- `easy forLoopEnd`
- `GetImageSizeAndCount`
- `LongCatAvatarWhisperEmbeds`
- `SimpleMath+`
- `Reroute`
- `SetNode`
- `WanVideoVAELoader`
- `GetNode`
- `GetNode`
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
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `WhisperModelLoader`
- `INTConstant`
- `FloatConstant`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `WanVideoBlockSwap`
- `PreviewAudio`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `LoadAudio`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `SetNode`
- `GetNode`
- `SetNode`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SetNode`
- `FloatConstant`
- `SetNode`
- `LoadImage`
- `FloatConstant`
- `FloatConstant`
- `INTConstant`
- `MathExpression|pysssss`
- `Text Multiline`
- `VHS_VideoCombine`
- `孤海注释`

## 知识

覆盖率 **53%**（50/95）

**有卡**：`WanVideoDecode`、`easy promptLine`、`ImageBatchExtendWithOverlap`、`WanVideoTextEncodeCached`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSamplerv2`、`WanVideoEncode`、`WanVideoLongCatAvatarExtendEmbeds`、`WanVideoSchedulerv2`、`easy forLoopEnd`、`GetImageSizeAndCount`、`LongCatAvatarWhisperEmbeds`、`SimpleMath+`、`WanVideoVAELoader`、`VHS_VideoCombine`、`ReplaceVideoLatentFrames`、`easy forLoopStart`、`TrimAudioDuration`、`GetImageRangeFromBatch`、`WhisperModelLoader`、`INTConstant`、`FloatConstant`、`MathExpression|pysssss`、`WanVideoBlockSwap`、`PreviewAudio`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadAudio`、`LoadImage`、`Text Multiline`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames、WanVideoLoraSelect
