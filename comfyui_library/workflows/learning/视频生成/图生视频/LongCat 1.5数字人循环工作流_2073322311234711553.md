---
key: 视频生成/图生视频/LongCat 1.5数字人循环工作流_2073322311234711553.json
name: LongCat 1.5数字人循环工作流_2073322311234711553.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LongCat 1.5数字人循环工作流_2073322311234711553.json
hash: ab6b9f0b09f7c88f
coverage: 0.93617
learned_at: 2026-10-15 22:41:05
nodes: [VHS_VideoCombine, ComfyMathExpression, easy indexAnything, Reroute, ReplaceVideoLatentFrames, WanVideoSchedulerv2, WanVideoTextEncodeCached, WhisperModelLoader, LongCatAvatarWhisperEmbeds, ComfyNumberConvert, WanVideoBlockSwap, WanVideoModelLoader, WanVideoEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoVAELoader, INTConstant, ImageResizeKJv2, INTConstant, Reroute, INTConstant, INTConstant, LoadImage, VHS_VideoCombine, WanVideoEncode, WanVideoTextEncodeCached, WanVideoSamplerv2, WanVideoSamplerv2, LoadAudio, Float, WanVideoDecode, Reroute, GetImageSizeAndCount, easy forLoopStart, ImageBatchExtendWithOverlap, GetImageSizeAndCount, GetImageRangeFromBatch, easy forLoopEnd, GetImageRangeFromBatch, TrimAudioDuration, WanVideoLongCatAvatarExtendEmbeds, WanVideoLongCatAvatarExtendEmbeds, easy indexAnything, ComfyMathExpression, ComfyMathExpression, easy promptList, easy promptList]
patterns: []
missing: []
---

# 视频生成/图生视频/LongCat 1.5数字人循环工作流_2073322311234711553.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073322311234711553.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（47 个）：
- `VHS_VideoCombine`
- `ComfyMathExpression`
- `easy indexAnything`
- `Reroute`
- `ReplaceVideoLatentFrames`
- `WanVideoSchedulerv2`
- `WanVideoTextEncodeCached`
- `WhisperModelLoader`
- `LongCatAvatarWhisperEmbeds`
- `ComfyNumberConvert`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `INTConstant`
- `ImageResizeKJv2`
- `INTConstant`
- `Reroute`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoEncode`
- `WanVideoTextEncodeCached`
- `WanVideoSamplerv2` ★核心
- `WanVideoSamplerv2` ★核心
- `LoadAudio`
- `Float`
- `WanVideoDecode`
- `Reroute`
- `GetImageSizeAndCount`
- `easy forLoopStart`
- `ImageBatchExtendWithOverlap`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `easy forLoopEnd`
- `GetImageRangeFromBatch`
- `TrimAudioDuration`
- `WanVideoLongCatAvatarExtendEmbeds`
- `WanVideoLongCatAvatarExtendEmbeds`
- `easy indexAnything`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `easy promptList`
- `easy promptList`

## 知识

覆盖率 **94%**（44/47）

**有卡**：`VHS_VideoCombine`、`ComfyMathExpression`、`easy indexAnything`、`ReplaceVideoLatentFrames`、`WanVideoSchedulerv2`、`WanVideoTextEncodeCached`、`WhisperModelLoader`、`LongCatAvatarWhisperEmbeds`、`ComfyNumberConvert`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoEncode`、`WanVideoDecode`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`INTConstant`、`ImageResizeKJv2`、`LoadImage`、`WanVideoSamplerv2`、`LoadAudio`、`Float`、`GetImageSizeAndCount`、`easy forLoopStart`、`ImageBatchExtendWithOverlap`、`GetImageRangeFromBatch`、`easy forLoopEnd`、`TrimAudioDuration`、`WanVideoLongCatAvatarExtendEmbeds`、`easy promptList`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames、WanVideoLoraSelect
