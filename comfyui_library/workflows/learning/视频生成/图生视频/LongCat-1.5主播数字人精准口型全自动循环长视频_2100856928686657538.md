---
key: 视频生成/图生视频/LongCat-1.5主播数字人精准口型全自动循环长视频_2100856928686657538.json
name: LongCat-1.5主播数字人精准口型全自动循环长视频_2100856928686657538
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LongCat-1.5主播数字人精准口型全自动循环长视频_2100856928686657538.json
hash: 6aa1f9086216885b
coverage: 0.525773
learned_at: 2026-10-17 02:14:11
nodes: [GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, SimpleMath+, TrimAudioDuration, LongCatAvatarWhisperEmbeds, WhisperModelLoader, easy showAnything, MathExpression|pysssss, WanVideoVAELoader, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, GetNode, GetNode, GetNode, ImageBatchExtendWithOverlap, GetNode, WanVideoEncode, WanVideoTextEncodeCached, WanVideoLongCatAvatarExtendEmbeds, easy showAnything, GetNode, GetNode, GetNode, PrimitiveNode, GetNode, GetNode, GetNode, WanVideoLongCatAvatarExtendEmbeds, WanVideoTextEncodeCached, PrimitiveNode, GetNode, GetNode, GetNode, ReplaceVideoLatentFrames, WanVideoDecode, ImageBatchExtendWithOverlap, GetNode, GetNode, MathExpression|pysssss, GetImageSizeAndCount, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSamplerv2, GetImageRangeFromBatch, WanVideoEncode, easy promptLine, INTConstant, INTConstant, INTConstant, FloatConstant, FloatConstant, SetNode, SetNode, SetNode, MathExpression|pysssss, FloatConstant, SetNode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSchedulerv2, WanVideoDecode, GetNode, WanVideoSamplerv2, SetNode, LoadImage, SetNode, easy forLoopStart, FloatConstant, WanVideoModelLoader, Reroute, WanVideoBlockSwap, VHS_VideoCombine, VHS_VideoCombine, easy showAnything, easy forLoopEnd, GetImageSizeAndCount, VHS_VideoCombine, LoadAudio, Text Multiline, INTConstant, PreviewAudio, WanVideoLoraSelect, easy promptLine, MarkdownNote, 孤海注释, Text Multiline]
patterns: []
missing: []
---

# 视频生成/图生视频/LongCat-1.5主播数字人精准口型全自动循环长视频_2100856928686657538.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LongCat-1.5主播数字人精准口型全自动循环长视频_2100856928686657538.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（97 个）：
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `TrimAudioDuration`
- `LongCatAvatarWhisperEmbeds`
- `WhisperModelLoader`
- `easy showAnything`
- `MathExpression|pysssss`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `WanVideoEncode`
- `WanVideoTextEncodeCached`
- `WanVideoLongCatAvatarExtendEmbeds`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `WanVideoTextEncodeCached`
- `PrimitiveNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ReplaceVideoLatentFrames`
- `WanVideoDecode`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `GetImageRangeFromBatch`
- `WanVideoEncode`
- `easy promptLine`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `FloatConstant`
- `FloatConstant`
- `SetNode`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `FloatConstant`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSchedulerv2`
- `WanVideoDecode`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `SetNode`
- `LoadImage`
- `SetNode`
- `easy forLoopStart`
- `FloatConstant`
- `WanVideoModelLoader`
- `Reroute`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy showAnything`
- `easy forLoopEnd`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `LoadAudio`
- `Text Multiline`
- `INTConstant`
- `PreviewAudio`
- `WanVideoLoraSelect`
- `easy promptLine`
- `MarkdownNote`
- `孤海注释`
- `Text Multiline`

## 知识

覆盖率 **53%**（51/97）

**有卡**：`SimpleMath+`、`TrimAudioDuration`、`LongCatAvatarWhisperEmbeds`、`WhisperModelLoader`、`MathExpression|pysssss`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`ImageBatchExtendWithOverlap`、`WanVideoEncode`、`WanVideoTextEncodeCached`、`WanVideoLongCatAvatarExtendEmbeds`、`ReplaceVideoLatentFrames`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoSamplerv2`、`GetImageRangeFromBatch`、`easy promptLine`、`INTConstant`、`FloatConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSchedulerv2`、`LoadImage`、`easy forLoopStart`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`easy forLoopEnd`、`LoadAudio`、`Text Multiline`、`PreviewAudio`、`WanVideoLoraSelect`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames、WanVideoLoraSelect
