---
key: 视频生成/图生视频/LongCat-Video-Avatar1.5多图分镜数字人_2059649854489583618.json
name: LongCat-Video-Avatar1.5多图分镜数字人_2059649854489583618.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2059649854489583618.json
hash: 900d7cbd5b0bd64a
coverage: 0.553719
learned_at: 2026-10-15 22:38:41
nodes: [SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, WanVideoEncode, GetNode, ImageResizeKJv2, CLIPVisionLoader, SetNode, Reroute, DownloadAndLoadWav2VecModel, GetNode, GetNode, GetNode, SetNode, MelBandRoFormerSampler, SetNode, PreviewAny, SetNode, WanVideoSamplerv2, TrimAudioDuration, SetNode, SetNode, SetNode, INTConstant, FloatConstant, SetNode, INTConstant, INTConstant, INTConstant, GetNode, WanVideoSchedulerv2, SetNode, GetNode, GetNode, GetNode, Int, Note, Int, GetNode, GetNode, GetNode, WanVideoLongCatAvatarExtendEmbeds, ForLoopOpen, GetNode, Reroute, LoadImage, LoadImage, LoadImage, ForLoopClose, GetNode, easy convertAnything, LongCatAvatarWhisperEmbeds, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoVAELoader, WanVideoModelLoader, SetNode, GetNode, WanVideoTextEncodeCached, GetImageRangeFromBatch, WanVideoTextEncodeCached, MathExpression|pysssss, MathExpression|pysssss, GetImageRangeFromBatch, WanVideoDecode, WanVideoLongCatAvatarExtendEmbeds, Float, GetNode, GetImageRangeFromBatch, ReplaceVideoLatentFrames, ReplaceVideoLatentFrames, WanVideoDecode, GetImageSizeAndCount, GetNode, Int, Int, VHS_GetImageCount, MathExpression|pysssss, ImageBatchExtendWithOverlap, WanVideoSamplerv2, INTConstant, SetNode, GetNode, ImageResizeKJv2, SetNode, GetNode, WanVideoEncode, WanVideoEncode, SetNode, RH_LLMAPI_NODE, CR Prompt Text, CR Prompt Text, RH_LLMAPI_NODE, Int, Text Load Line From File, SetNode, MelBandRoFormerModelLoader, PreviewAudio, VHS_VideoCombine, Wav2VecModelLoader, WhisperModelLoader, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, LoadImage, ImageBatchMulti, LoadAudio]
patterns: []
missing: []
---

# 视频生成/图生视频/LongCat-Video-Avatar1.5多图分镜数字人_2059649854489583618.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2059649854489583618.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（121 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `GetNode`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `SetNode`
- `Reroute`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `PreviewAny`
- `SetNode`
- `WanVideoSamplerv2` ★核心
- `TrimAudioDuration`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `FloatConstant`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `WanVideoSchedulerv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `Note`
- `Int`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `ForLoopOpen`
- `GetNode`
- `Reroute`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ForLoopClose`
- `GetNode`
- `easy convertAnything`
- `LongCatAvatarWhisperEmbeds`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `SetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `GetImageRangeFromBatch`
- `WanVideoTextEncodeCached`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetImageRangeFromBatch`
- `WanVideoDecode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `Float`
- `GetNode`
- `GetImageRangeFromBatch`
- `ReplaceVideoLatentFrames`
- `ReplaceVideoLatentFrames`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetNode`
- `Int`
- `Int`
- `VHS_GetImageCount`
- `MathExpression|pysssss`
- `ImageBatchExtendWithOverlap`
- `WanVideoSamplerv2` ★核心
- `INTConstant`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `WanVideoEncode`
- `WanVideoEncode`
- `SetNode`
- `RH_LLMAPI_NODE`
- `CR Prompt Text`
- `CR Prompt Text`
- `RH_LLMAPI_NODE`
- `Int`
- `Text Load Line From File`
- `SetNode`
- `MelBandRoFormerModelLoader`
- `PreviewAudio`
- `VHS_VideoCombine`
- `Wav2VecModelLoader`
- `WhisperModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PreviewImage`
- `LoadImage`
- `ImageBatchMulti`
- `LoadAudio`

## 知识

覆盖率 **55%**（67/121）

**有卡**：`WanVideoEncode`、`ImageResizeKJv2`、`CLIPVisionLoader`、`DownloadAndLoadWav2VecModel`、`MelBandRoFormerSampler`、`WanVideoSamplerv2`、`TrimAudioDuration`、`INTConstant`、`FloatConstant`、`WanVideoSchedulerv2`、`Int`、`WanVideoLongCatAvatarExtendEmbeds`、`ForLoopOpen`、`LoadImage`、`ForLoopClose`、`easy convertAnything`、`LongCatAvatarWhisperEmbeds`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`GetImageRangeFromBatch`、`MathExpression|pysssss`、`WanVideoDecode`、`Float`、`ReplaceVideoLatentFrames`、`GetImageSizeAndCount`、`VHS_GetImageCount`、`ImageBatchExtendWithOverlap`、`RH_LLMAPI_NODE`、`CR Prompt Text`、`Text Load Line From File`、`MelBandRoFormerModelLoader`、`PreviewAudio`、`VHS_VideoCombine`、`Wav2VecModelLoader`、`WhisperModelLoader`、`ImageBatchMulti`、`LoadAudio`

**用到的条目**：LoadImage、MelBandRoFormerSampler、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames
