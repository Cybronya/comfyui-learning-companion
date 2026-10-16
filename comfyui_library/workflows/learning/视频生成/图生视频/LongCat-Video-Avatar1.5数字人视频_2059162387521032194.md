---
key: 视频生成/图生视频/LongCat-Video-Avatar1.5数字人视频_2059162387521032194.json
name: LongCat-Video-Avatar1.5数字人视频_2059162387521032194.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2059162387521032194.json
hash: 3426e158359d631a
coverage: 0.509259
learned_at: 2026-10-15 22:38:37
nodes: [SetNode, SetNode, WanVideoBlockSwap, WanVideoTorchCompileSettings, SetNode, GetNode, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoVAELoader, WanVideoTextEncodeCached, GetNode, ForLoopOpen, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoEncode, GetNode, GetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, CLIPVisionLoader, SetNode, WanVideoDecode, Reroute, MelBandRoFormerModelLoader, DownloadAndLoadWav2VecModel, Wav2VecModelLoader, WanVideoLongCatAvatarExtendEmbeds, GetNode, GetNode, GetNode, WanVideoDecode, ReplaceVideoLatentFrames, Reroute, SetNode, GetImageRangeFromBatch, MathExpression|pysssss, SetNode, MelBandRoFormerSampler, WanVideoSamplerv2, SetNode, PreviewAny, SetNode, ImageBatchExtendWithOverlap, GetImageSizeAndCount, WanVideoSamplerv2, TrimAudioDuration, SetNode, GetNode, PreviewAudio, INTConstant, SetNode, SetNode, INTConstant, FloatConstant, SetNode, SetNode, INTConstant, INTConstant, INTConstant, GetNode, WanVideoModelLoader, ForLoopClose, WanVideoSchedulerv2, WanVideoEncode, LongCatAvatarWhisperEmbeds, WhisperModelLoader, SetNode, GetNode, GetNode, easy convertAnything, VHS_VideoCombine, LoadAudio, WanVideoLongCatAvatarExtendEmbeds, SetNode, WanVideoTextEncodeCached, Text Load Line From File, Text Load Line From File, MathExpression|pysssss, VHS_VideoCombine, GetNode, GetNode, WanVideoLoraSelect, GetNode, Int, Int, Int, TextInput_, Note, VHS_VideoCombine, Int, LoadImage, Float, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/LongCat-Video-Avatar1.5数字人视频_2059162387521032194.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2059162387521032194.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（108 个）：
- `SetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `GetNode`
- `ForLoopOpen`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoDecode`
- `Reroute`
- `MelBandRoFormerModelLoader`
- `DownloadAndLoadWav2VecModel`
- `Wav2VecModelLoader`
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `ReplaceVideoLatentFrames`
- `Reroute`
- `SetNode`
- `GetImageRangeFromBatch`
- `MathExpression|pysssss`
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `WanVideoSamplerv2` ★核心
- `SetNode`
- `PreviewAny`
- `SetNode`
- `ImageBatchExtendWithOverlap`
- `GetImageSizeAndCount`
- `WanVideoSamplerv2` ★核心
- `TrimAudioDuration`
- `SetNode`
- `GetNode`
- `PreviewAudio`
- `INTConstant`
- `SetNode`
- `SetNode`
- `INTConstant`
- `FloatConstant`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `WanVideoModelLoader`
- `ForLoopClose`
- `WanVideoSchedulerv2`
- `WanVideoEncode`
- `LongCatAvatarWhisperEmbeds`
- `WhisperModelLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy convertAnything`
- `VHS_VideoCombine`
- `LoadAudio`
- `WanVideoLongCatAvatarExtendEmbeds`
- `SetNode`
- `WanVideoTextEncodeCached`
- `Text Load Line From File`
- `Text Load Line From File`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `WanVideoLoraSelect`
- `GetNode`
- `Int`
- `Int`
- `Int`
- `TextInput_`
- `Note`
- `VHS_VideoCombine`
- `Int`
- `LoadImage`
- `Float`
- `Int`

## 知识

覆盖率 **51%**（55/108）

**有卡**：`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`ForLoopOpen`、`WanVideoEncode`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoDecode`、`MelBandRoFormerModelLoader`、`DownloadAndLoadWav2VecModel`、`Wav2VecModelLoader`、`WanVideoLongCatAvatarExtendEmbeds`、`ReplaceVideoLatentFrames`、`GetImageRangeFromBatch`、`MathExpression|pysssss`、`MelBandRoFormerSampler`、`WanVideoSamplerv2`、`ImageBatchExtendWithOverlap`、`GetImageSizeAndCount`、`TrimAudioDuration`、`PreviewAudio`、`INTConstant`、`FloatConstant`、`WanVideoModelLoader`、`ForLoopClose`、`WanVideoSchedulerv2`、`LongCatAvatarWhisperEmbeds`、`WhisperModelLoader`、`easy convertAnything`、`VHS_VideoCombine`、`LoadAudio`、`Text Load Line From File`、`WanVideoLoraSelect`、`Int`、`TextInput_`、`LoadImage`、`Float`

**用到的条目**：LoadImage、MelBandRoFormerSampler、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames
