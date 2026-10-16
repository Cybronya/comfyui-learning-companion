---
key: 视频生成/图生视频/LongCat 1.5数字人长视频工作流生产力版_2073710624823144449.json
name: LongCat 1.5数字人长视频工作流生产力版_2073710624823144449.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2073710624823144449.json
hash: 3ca36ecf7bcbf52a
coverage: 0.93617
learned_at: 2026-10-15 22:41:09
nodes: [ComfyMathExpression, easy indexAnything, Reroute, ReplaceVideoLatentFrames, WanVideoSchedulerv2, WanVideoTextEncodeCached, LongCatAvatarWhisperEmbeds, ComfyNumberConvert, WanVideoBlockSwap, WanVideoModelLoader, WanVideoEncode, WanVideoDecode, WanVideoLoraSelect, ImageResizeKJv2, Reroute, WanVideoEncode, WanVideoTextEncodeCached, Float, WanVideoDecode, Reroute, GetImageSizeAndCount, easy forLoopStart, ImageBatchExtendWithOverlap, GetImageSizeAndCount, GetImageRangeFromBatch, easy forLoopEnd, GetImageRangeFromBatch, WanVideoLongCatAvatarExtendEmbeds, WanVideoLongCatAvatarExtendEmbeds, easy indexAnything, ComfyMathExpression, ComfyMathExpression, easy promptList, easy promptList, LoadImage, INTConstant, INTConstant, WhisperModelLoader, VHS_VideoCombine, VHS_VideoCombine, WanVideoVAELoader, WanVideoSamplerv2, WanVideoSamplerv2, INTConstant, TrimAudioDuration, LoadAudio, INTConstant]
patterns: []
missing: []
---

# 视频生成/图生视频/LongCat 1.5数字人长视频工作流生产力版_2073710624823144449.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073710624823144449.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（47 个）：
- `ComfyMathExpression`
- `easy indexAnything`
- `Reroute`
- `ReplaceVideoLatentFrames`
- `WanVideoSchedulerv2`
- `WanVideoTextEncodeCached`
- `LongCatAvatarWhisperEmbeds`
- `ComfyNumberConvert`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `ImageResizeKJv2`
- `Reroute`
- `WanVideoEncode`
- `WanVideoTextEncodeCached`
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
- `WanVideoLongCatAvatarExtendEmbeds`
- `WanVideoLongCatAvatarExtendEmbeds`
- `easy indexAnything`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `easy promptList`
- `easy promptList`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `WhisperModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoSamplerv2` ★核心
- `WanVideoSamplerv2` ★核心
- `INTConstant`
- `TrimAudioDuration`
- `LoadAudio`
- `INTConstant`

## 知识

覆盖率 **94%**（44/47）

**有卡**：`ComfyMathExpression`、`easy indexAnything`、`ReplaceVideoLatentFrames`、`WanVideoSchedulerv2`、`WanVideoTextEncodeCached`、`LongCatAvatarWhisperEmbeds`、`ComfyNumberConvert`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoEncode`、`WanVideoDecode`、`WanVideoLoraSelect`、`ImageResizeKJv2`、`Float`、`GetImageSizeAndCount`、`easy forLoopStart`、`ImageBatchExtendWithOverlap`、`GetImageRangeFromBatch`、`easy forLoopEnd`、`WanVideoLongCatAvatarExtendEmbeds`、`easy promptList`、`LoadImage`、`INTConstant`、`WhisperModelLoader`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoSamplerv2`、`TrimAudioDuration`、`LoadAudio`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames、WanVideoLoraSelect
