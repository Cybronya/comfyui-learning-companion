---
name: unknown_workflow_video_lora_sampler_804
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CR Prompt Text, ComfyMathExpression, ComfyNumberConvert, Float, ImageResizeKJv2, Int, LoadAudio, LoadImage, LongCatAvatarWhisperEmbeds, TrimAudioDuration, VHS_VideoCombine, WanAnimatePlus BlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [数字人/数字人/Longcat-avatar1.5-数字人_2060540965919744002.json, 视频生成/图生视频/Longcat-Avatar1.5-超长时长数字人v1_2107328414905626625.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_804

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/Longcat-avatar1.5-数字人_2060540965919744002.json、视频生成/图生视频/Longcat-Avatar1.5-超长时长数字人v1_2107328414905626625.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `Float`
- `ImageResizeKJv2`
- `Int`
- `LoadAudio`
- `LoadImage`
- `LongCatAvatarWhisperEmbeds`
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

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageBatchExtendWithOverlap` —— 1/2 个有
- `ReplaceVideoLatentFrames` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有
- `easy indexAnything` —— 1/2 个有
- `easy promptList` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
