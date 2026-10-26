---
key: 数字人/数字人/Longcat-Avatar1.5数字人说话循环静态手动遮罩_2067886174374551553.json
name: Longcat-Avatar1.5数字人说话循环静态手动遮罩_2067886174374551553
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Longcat-Avatar1.5数字人说话循环静态手动遮罩_2067886174374551553.json
hash: d1be77c4cc1f31a7
coverage: 0.565657
learned_at: 2026-10-26 01:56:27
nodes: [WanVideoLoraSelect, WanVideoModelLoader, GetNode, SetNode, Int, SetNode, Int, GetNode, GetNode, WanVideoLongCatAvatarExtendEmbeds, GetNode, GetNode, GetNode, GetNode, GetNode, WhisperModelLoader, WanVideoLongCatAvatarExtendEmbeds, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetImageRangeFromBatch, ImageBatchExtendWithOverlap, CR Prompt List, WanVideoTextEncodeCached, WanVideoTextEncodeCached, CR Prompt List, ComfyMathExpression, WanVideoEncode, ReplaceVideoLatentFrames, GetNode, WanVideoDecode, GetNode, easy forLoopEnd, GetImageSizeAndCount, GetImageSizeAndCount, LongCatAvatarWhisperEmbeds, ComfyNumberConvert, ComfyMathExpression, PreviewAudio, GetNode, easy showAnything, SetNode, GetNode, GetNode, SetNode, WanAnimatePlus BlockSwap, GetNode, SetNode, WanVideoVAELoader, SetNode, GetNode, ComfyMathExpression, GetNode, WanVideoSampler, easy showAnything, GetNode, InvertMask, GetNode, ColorMatchV2, easy imageRemBg, easy forLoopStart, InvertMask, GetNode, ColorMatchV2, easy imageRemBg, LoadImage, WanVideoDecode, GetImageRangeFromBatch, ImageCompositeMasked, ImageCompositeMasked, WanVideoSampler, SetNode, GetNode, SetNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, Qwen3_VQA, CR Text Replace, Float, Int, Int, TrimAudioDuration, LoadAudio, GetNode, easy showAnything, InvertMask, WanVideoEncode, ImageResizeKJv2, DrawMaskOnImage, PreviewImage, MarkdownNote, CR Prompt Text, easy showAnything, ProcessString, SetNode]
patterns: []
missing: []
---

# 数字人/数字人/Longcat-Avatar1.5数字人说话循环静态手动遮罩_2067886174374551553.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Longcat-Avatar1.5数字人说话循环静态手动遮罩_2067886174374551553.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（99 个）：
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `GetNode`
- `SetNode`
- `Int`
- `SetNode`
- `Int`
- `GetNode`
- `GetNode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WhisperModelLoader`
- `WanVideoLongCatAvatarExtendEmbeds`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `ImageBatchExtendWithOverlap`
- `CR Prompt List`
- `WanVideoTextEncodeCached`
- `WanVideoTextEncodeCached`
- `CR Prompt List`
- `ComfyMathExpression`
- `WanVideoEncode`
- `ReplaceVideoLatentFrames`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `easy forLoopEnd`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `LongCatAvatarWhisperEmbeds`
- `ComfyNumberConvert`
- `ComfyMathExpression`
- `PreviewAudio`
- `GetNode`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanAnimatePlus BlockSwap`
- `GetNode`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `WanVideoSampler` ★核心
- `easy showAnything`
- `GetNode`
- `InvertMask`
- `GetNode`
- `ColorMatchV2`
- `easy imageRemBg`
- `easy forLoopStart`
- `InvertMask`
- `GetNode`
- `ColorMatchV2`
- `easy imageRemBg`
- `LoadImage`
- `WanVideoDecode`
- `GetImageRangeFromBatch`
- `ImageCompositeMasked`
- `ImageCompositeMasked`
- `WanVideoSampler` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `Qwen3_VQA`
- `CR Text Replace`
- `Float`
- `Int`
- `Int`
- `TrimAudioDuration`
- `LoadAudio`
- `GetNode`
- `easy showAnything`
- `InvertMask`
- `WanVideoEncode`
- `ImageResizeKJv2`
- `DrawMaskOnImage`
- `PreviewImage`
- `MarkdownNote`
- `CR Prompt Text`
- `easy showAnything`
- `ProcessString`
- `SetNode`

## 知识

覆盖率 **57%**（56/99）

**有卡**：`WanVideoLoraSelect`、`WanVideoModelLoader`、`Int`、`WanVideoLongCatAvatarExtendEmbeds`、`WhisperModelLoader`、`GetImageRangeFromBatch`、`ImageBatchExtendWithOverlap`、`CR Prompt List`、`WanVideoTextEncodeCached`、`ComfyMathExpression`、`WanVideoEncode`、`ReplaceVideoLatentFrames`、`WanVideoDecode`、`easy forLoopEnd`、`GetImageSizeAndCount`、`LongCatAvatarWhisperEmbeds`、`ComfyNumberConvert`、`PreviewAudio`、`WanAnimatePlus BlockSwap`、`WanVideoVAELoader`、`WanVideoSampler`、`InvertMask`、`ColorMatchV2`、`easy imageRemBg`、`easy forLoopStart`、`LoadImage`、`ImageCompositeMasked`、`VHS_VideoCombine`、`Qwen3_VQA`、`CR Text Replace`、`Float`、`TrimAudioDuration`、`LoadAudio`、`ImageResizeKJv2`、`DrawMaskOnImage`、`CR Prompt Text`、`ProcessString`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ReplaceVideoLatentFrames、WanVideoLoraSelect
