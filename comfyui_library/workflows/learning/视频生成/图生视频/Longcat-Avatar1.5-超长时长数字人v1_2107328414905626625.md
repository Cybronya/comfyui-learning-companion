---
key: 视频生成/图生视频/Longcat-Avatar1.5-超长时长数字人v1_2107328414905626625.json
name: Longcat-Avatar1.5-超长时长数字人v1_2107328414905626625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Longcat-Avatar1.5-超长时长数字人v1_2107328414905626625.json
hash: 87f987eb9139db81
coverage: 1
learned_at: 2026-10-17 22:17:46
nodes: [WhisperModelLoader, WanVideoVAELoader, ImageResizeKJv2, WanVideoModelLoader, VHS_VideoCombine, WanVideoSampler, WanVideoLoraSelect, easy forLoopEnd, TrimAudioDuration, GetImageSizeAndCount, WanVideoEncode, LongCatAvatarWhisperEmbeds, WanAnimatePlus BlockSwap, GetImageRangeFromBatch, WanVideoTextEncodeCached, ComfyNumberConvert, ComfyMathExpression, ComfyMathExpression, easy indexAnything, WanVideoDecode, WanVideoSampler, WanVideoTextEncodeCached, ComfyMathExpression, easy indexAnything, VHS_VideoCombine, WanVideoLongCatAvatarExtendEmbeds, easy forLoopStart, WanVideoLongCatAvatarExtendEmbeds, ReplaceVideoLatentFrames, WanVideoEncode, WanVideoDecode, GetImageRangeFromBatch, ImageBatchExtendWithOverlap, GetImageSizeAndCount, Float, Int, Int, Int, Int, easy promptList, LoadImage, LoadAudio, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/Longcat-Avatar1.5-超长时长数字人v1_2107328414905626625.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Longcat-Avatar1.5-超长时长数字人v1_2107328414905626625.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（47 个）：
- `WhisperModelLoader`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
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
- `LoadImage`
- `LoadAudio`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`

## 知识

覆盖率 **100%**（47/47）

**有卡**：`WhisperModelLoader`、`WanVideoVAELoader`、`ImageResizeKJv2`、`WanVideoModelLoader`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoLoraSelect`、`easy forLoopEnd`、`TrimAudioDuration`、`GetImageSizeAndCount`、`WanVideoEncode`、`LongCatAvatarWhisperEmbeds`、`WanAnimatePlus BlockSwap`、`GetImageRangeFromBatch`、`WanVideoTextEncodeCached`、`ComfyNumberConvert`、`ComfyMathExpression`、`easy indexAnything`、`WanVideoDecode`、`WanVideoLongCatAvatarExtendEmbeds`、`easy forLoopStart`、`ReplaceVideoLatentFrames`、`ImageBatchExtendWithOverlap`、`Float`、`Int`、`easy promptList`、`LoadImage`、`LoadAudio`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames、WanVideoLoraSelect
