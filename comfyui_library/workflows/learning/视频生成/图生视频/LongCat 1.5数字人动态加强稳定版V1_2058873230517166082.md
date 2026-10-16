---
key: 视频生成/图生视频/LongCat 1.5数字人动态加强稳定版V1_2058873230517166082.json
name: LongCat 1.5数字人动态加强稳定版V1_2058873230517166082.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2058873230517166082.json
hash: 5b89b5baa5d87e88
coverage: 0.478261
learned_at: 2026-10-15 22:38:31
nodes: [SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, Reroute, GetNode, SetNode, SetNode, SetNode, GetNode, ImageBatchExtendWithOverlap, GetNode, WanVideoEncode, GetNode, ReplaceVideoLatentFrames, GetNode, GetNode, GetNode, GetNode, Reroute, GetNode, ImageBatchExtendWithOverlap, GetImageRangeFromBatch, WanVideoDecode, GetNode, INTConstant, WanVideoLongCatAvatarExtendEmbeds, GetImageSizeAndCount, WhisperModelLoader, GetNode, GetNode, GetNode, GetNode, Reroute, WanVideoDecode, GetNode, GetNode, WanVideoLongCatAvatarExtendEmbeds, GetNode, GetNode, GetNode, SetNode, TrimAudioDuration, SetNode, LongCatAvatarWhisperEmbeds, SetNode, GetNode, GetNode, GetNode, GetImageRangeFromBatch, WanVideoEncode, GetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, WanVideoDecode, WanVideoLongCatAvatarExtendEmbeds, GetNode, GetNode, WanVideoEncode, GetNode, ReplaceVideoLatentFrames, GetNode, GetNode, GetNode, GetNode, Reroute, GetNode, ImageBatchExtendWithOverlap, GetImageRangeFromBatch, WanVideoDecode, GetNode, WanVideoLongCatAvatarExtendEmbeds, Reroute, GetNode, WanVideoEncode, SetNode, SetNode, WanVideoModelLoader, SetNode, SetNode, FloatConstant, Reroute, GetImageSizeAndCount, WanVideoSamplerv2, GetImageSizeAndCount, Reroute, GetNode, WanVideoEncode, GetNode, ReplaceVideoLatentFrames, GetNode, GetNode, GetNode, GetNode, Reroute, GetNode, ImageBatchExtendWithOverlap, GetImageRangeFromBatch, WanVideoDecode, GetNode, WanVideoLongCatAvatarExtendEmbeds, GetNode, GetImageSizeAndCount, Reroute, WanVideoSamplerv2, WanVideoSamplerv2, Reroute, PreviewAny, WanVideoSchedulerv2, SetNode, WanVideoTextEncodeCached, Reroute, ImageResizeKJv2, GetNode, WanVideoEncode, LoadImage, WanVideoTextEncodeCached, WanVideoTextEncodeCached, WanVideoTextEncodeCached, WanVideoTextEncodeCached, GetNode, GetNode, GetNode, VHS_VideoCombine, WanVideoSamplerv2, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoVAELoader, ComfyMathExpression, INTConstant, INTConstant, LoadAudio, CR Prompt Text, CR Text Replace, LoadImage, ProcessString, CR Prompt List, CR Prompt List, CR Prompt List, CR Prompt List, CR Prompt List, easy showAnything, easy showAnything, easy showAnything, easy showAnything, easy showAnything, easy showAnything, WanVideoSamplerv2, INTConstant, VHS_VideoCombine, ReplaceVideoLatentFrames, Float, RH_LLMAPI_Pro_Node, ComfyNumberConvert]
patterns: []
missing: []
---

# 视频生成/图生视频/LongCat 1.5数字人动态加强稳定版V1_2058873230517166082.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2058873230517166082.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（161 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `WanVideoEncode`
- `GetNode`
- `ReplaceVideoLatentFrames`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `GetImageRangeFromBatch`
- `WanVideoDecode`
- `GetNode`
- `INTConstant`
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetImageSizeAndCount`
- `WhisperModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `TrimAudioDuration`
- `SetNode`
- `LongCatAvatarWhisperEmbeds`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `WanVideoEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `WanVideoDecode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `GetNode`
- `ReplaceVideoLatentFrames`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `GetImageRangeFromBatch`
- `WanVideoDecode`
- `GetNode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `Reroute`
- `GetNode`
- `WanVideoEncode`
- `SetNode`
- `SetNode`
- `WanVideoModelLoader`
- `SetNode`
- `SetNode`
- `FloatConstant`
- `Reroute`
- `GetImageSizeAndCount`
- `WanVideoSamplerv2` ★核心
- `GetImageSizeAndCount`
- `Reroute`
- `GetNode`
- `WanVideoEncode`
- `GetNode`
- `ReplaceVideoLatentFrames`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `GetImageRangeFromBatch`
- `WanVideoDecode`
- `GetNode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetNode`
- `GetImageSizeAndCount`
- `Reroute`
- `WanVideoSamplerv2` ★核心
- `WanVideoSamplerv2` ★核心
- `Reroute`
- `PreviewAny`
- `WanVideoSchedulerv2`
- `SetNode`
- `WanVideoTextEncodeCached`
- `Reroute`
- `ImageResizeKJv2`
- `GetNode`
- `WanVideoEncode`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `WanVideoTextEncodeCached`
- `WanVideoTextEncodeCached`
- `WanVideoTextEncodeCached`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoSamplerv2` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `ComfyMathExpression`
- `INTConstant`
- `INTConstant`
- `LoadAudio`
- `CR Prompt Text`
- `CR Text Replace`
- `LoadImage`
- `ProcessString`
- `CR Prompt List`
- `CR Prompt List`
- `CR Prompt List`
- `CR Prompt List`
- `CR Prompt List`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `WanVideoSamplerv2` ★核心
- `INTConstant`
- `VHS_VideoCombine`
- `ReplaceVideoLatentFrames`
- `Float`
- `RH_LLMAPI_Pro_Node`
- `ComfyNumberConvert`

## 知识

覆盖率 **48%**（77/161）

**有卡**：`ImageBatchExtendWithOverlap`、`WanVideoEncode`、`ReplaceVideoLatentFrames`、`GetImageRangeFromBatch`、`WanVideoDecode`、`INTConstant`、`WanVideoLongCatAvatarExtendEmbeds`、`GetImageSizeAndCount`、`WhisperModelLoader`、`TrimAudioDuration`、`LongCatAvatarWhisperEmbeds`、`ImageResizeKJv2`、`WanVideoModelLoader`、`FloatConstant`、`WanVideoSamplerv2`、`WanVideoSchedulerv2`、`WanVideoTextEncodeCached`、`LoadImage`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`ComfyMathExpression`、`LoadAudio`、`CR Prompt Text`、`CR Text Replace`、`ProcessString`、`CR Prompt List`、`Float`、`RH_LLMAPI_Pro_Node`、`ComfyNumberConvert`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames、WanVideoLoraSelect
