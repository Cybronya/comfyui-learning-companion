---
key: 视频生成/图生视频/LongCat 1.5数字人循环工作流_2059800193100505090.json
name: LongCat 1.5数字人循环工作流_2059800193100505090.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LongCat 1.5数字人循环工作流_2059800193100505090.json
hash: 96afb400858c81a0
coverage: 0.93617
learned_at: 2026-10-15 22:38:42
nodes: [ComfyMathExpression, easy indexAnything, Reroute, ReplaceVideoLatentFrames, WanVideoSchedulerv2, WanVideoTextEncodeCached, WhisperModelLoader, LongCatAvatarWhisperEmbeds, ComfyNumberConvert, WanVideoBlockSwap, WanVideoModelLoader, WanVideoEncode, WanVideoDecode, WanVideoVAELoader, INTConstant, ImageResizeKJv2, Reroute, INTConstant, INTConstant, WanVideoEncode, WanVideoTextEncodeCached, WanVideoSamplerv2, WanVideoSamplerv2, Float, WanVideoDecode, Reroute, GetImageSizeAndCount, easy forLoopStart, ImageBatchExtendWithOverlap, GetImageSizeAndCount, GetImageRangeFromBatch, easy forLoopEnd, GetImageRangeFromBatch, TrimAudioDuration, WanVideoLongCatAvatarExtendEmbeds, WanVideoLongCatAvatarExtendEmbeds, easy indexAnything, ComfyMathExpression, ComfyMathExpression, LoadImage, INTConstant, easy promptList, WanVideoLoraSelect, LoadAudio, VHS_VideoCombine, easy promptList, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/LongCat 1.5数字人循环工作流_2059800193100505090.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2059800193100505090.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（47 个）：
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
- `WanVideoVAELoader`
- `INTConstant`
- `ImageResizeKJv2`
- `Reroute`
- `INTConstant`
- `INTConstant`
- `WanVideoEncode`
- `WanVideoTextEncodeCached`
- `WanVideoSamplerv2` ★核心
- `WanVideoSamplerv2` ★核心
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
- `LoadImage`
- `INTConstant`
- `easy promptList`
- `WanVideoLoraSelect`
- `LoadAudio`
- `VHS_VideoCombine`
- `easy promptList`
- `VHS_VideoCombine`

## 知识

覆盖率 **94%**（44/47）

**有卡**：`ComfyMathExpression`、`easy indexAnything`、`ReplaceVideoLatentFrames`、`WanVideoSchedulerv2`、`WanVideoTextEncodeCached`、`WhisperModelLoader`、`LongCatAvatarWhisperEmbeds`、`ComfyNumberConvert`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoEncode`、`WanVideoDecode`、`WanVideoVAELoader`、`INTConstant`、`ImageResizeKJv2`、`WanVideoSamplerv2`、`Float`、`GetImageSizeAndCount`、`easy forLoopStart`、`ImageBatchExtendWithOverlap`、`GetImageRangeFromBatch`、`easy forLoopEnd`、`TrimAudioDuration`、`WanVideoLongCatAvatarExtendEmbeds`、`LoadImage`、`easy promptList`、`WanVideoLoraSelect`、`LoadAudio`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames、WanVideoLoraSelect
