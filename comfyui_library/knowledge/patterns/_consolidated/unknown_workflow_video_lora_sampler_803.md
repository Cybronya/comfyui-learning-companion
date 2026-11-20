---
name: unknown_workflow_video_lora_sampler_803
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.783
common_nodes: [CR Prompt Text, ComfyMathExpression, ComfyNumberConvert, Float, GetImageRangeFromBatch, GetImageSizeAndCount, ImageBatchExtendWithOverlap, ImageResizeKJv2, Int, LoadAudio, LoadImage, LongCatAvatarWhisperEmbeds, ReplaceVideoLatentFrames, TrimAudioDuration, VHS_VideoCombine, WanAnimatePlus BlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, WhisperModelLoader, easy forLoopEnd, easy forLoopStart]
problems: []
missing: []
members: [数字人/数字人/Longcat-Avatar1.5-超长时长数字人（for循环）_2060344344913211393.json, 数字人/数字人/Longcat-Avatar1.5数字人说话循环静态手动遮罩_2067886174374551553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_803

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/Longcat-Avatar1.5-超长时长数字人（for循环）_2060344344913211393.json、数字人/数字人/Longcat-Avatar1.5数字人说话循环静态手动遮罩_2067886174374551553.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `Float`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `Int`
- `LoadAudio`
- `LoadImage`
- `LongCatAvatarWhisperEmbeds`
- `ReplaceVideoLatentFrames`
- `TrimAudioDuration`
- `VHS_VideoCombine`
- `WanAnimatePlus BlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WhisperModelLoader`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `CR Prompt List` —— 1/2 个有
- `CR Text Replace` —— 1/2 个有
- `ColorMatchV2` —— 1/2 个有
- `DrawMaskOnImage` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageCompositeMasked` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ProcessString` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有
- `easy indexAnything` —— 1/2 个有
- `easy promptList` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
