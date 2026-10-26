---
key: 数字人/数字人/Longcat-Avatar1.5-超长时长数字人（for循环）_2060344344913211393.json
name: Longcat-Avatar1.5-超长时长数字人（for循环）_2060344344913211393
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Longcat-Avatar1.5-超长时长数字人（for循环）_2060344344913211393.json
hash: f0c847886a8ed702
coverage: 1
learned_at: 2026-10-26 01:56:26
nodes: [WhisperModelLoader, WanVideoVAELoader, ImageResizeKJv2, LoadImage, LoadAudio, WanVideoModelLoader, VHS_VideoCombine, WanVideoSampler, WanVideoLoraSelect, easy forLoopEnd, TrimAudioDuration, GetImageSizeAndCount, WanVideoEncode, LongCatAvatarWhisperEmbeds, WanAnimatePlus BlockSwap, GetImageRangeFromBatch, WanVideoTextEncodeCached, ComfyNumberConvert, ComfyMathExpression, ComfyMathExpression, easy indexAnything, WanVideoDecode, WanVideoSampler, WanVideoTextEncodeCached, ComfyMathExpression, easy indexAnything, VHS_VideoCombine, WanVideoLongCatAvatarExtendEmbeds, easy forLoopStart, WanVideoLongCatAvatarExtendEmbeds, ReplaceVideoLatentFrames, WanVideoEncode, WanVideoDecode, GetImageRangeFromBatch, ImageBatchExtendWithOverlap, GetImageSizeAndCount, Float, Int, Int, Int, Int, easy promptList, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text]
patterns: []
missing: []
---

# 数字人/数字人/Longcat-Avatar1.5-超长时长数字人（for循环）_2060344344913211393.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Longcat-Avatar1.5-超长时长数字人（for循环）_2060344344913211393.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（47 个）：
- `WhisperModelLoader`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadAudio`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `easy forLoopEnd`
- `TrimAudioDuration`
- `GetImageSizeAndCount`
- `WanVideoEncode`
- `LongCatAvatarWhisperEmbeds`
- `WanAnimatePlus BlockSwap`
- `GetImageRangeFromBatch`
- `WanVideoTextEncodeCached`
- `ComfyNumberConvert`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `easy indexAnything`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `ComfyMathExpression`
- `easy indexAnything`
- `VHS_VideoCombine`
- `WanVideoLongCatAvatarExtendEmbeds`
- `easy forLoopStart`
- `WanVideoLongCatAvatarExtendEmbeds`
- `ReplaceVideoLatentFrames`
- `WanVideoEncode`
- `WanVideoDecode`
- `GetImageRangeFromBatch`
- `ImageBatchExtendWithOverlap`
- `GetImageSizeAndCount`
- `Float`
- `Int`
- `Int`
- `Int`
- `Int`
- `easy promptList`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`

## 知识

覆盖率 **100%**（47/47）

**有卡**：`WhisperModelLoader`、`WanVideoVAELoader`、`ImageResizeKJv2`、`LoadImage`、`LoadAudio`、`WanVideoModelLoader`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoLoraSelect`、`easy forLoopEnd`、`TrimAudioDuration`、`GetImageSizeAndCount`、`WanVideoEncode`、`LongCatAvatarWhisperEmbeds`、`WanAnimatePlus BlockSwap`、`GetImageRangeFromBatch`、`WanVideoTextEncodeCached`、`ComfyNumberConvert`、`ComfyMathExpression`、`easy indexAnything`、`WanVideoDecode`、`WanVideoLongCatAvatarExtendEmbeds`、`easy forLoopStart`、`ReplaceVideoLatentFrames`、`ImageBatchExtendWithOverlap`、`Float`、`Int`、`easy promptList`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames、WanVideoLoraSelect
