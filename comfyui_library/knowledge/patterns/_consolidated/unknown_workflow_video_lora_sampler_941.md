---
name: unknown_workflow_video_lora_sampler_941
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.487
common_nodes: [AudioCrop, AudioDuration_wan, CR Prompt Text, FloatConstant, GetImageRangeFromBatch, GetImageSizeAndCount, INTConstant, ImageBatchExtendWithOverlap, ImageResizeKJv2, LoadAudio, LoadImage, LongCatAvatarWhisperEmbeds, MathExpression_UTK, ReplaceVideoLatentFrames, ShowAnything|Mie, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoTextEncodeCached, WanVideoVAELoader, WhisperModelLoader, easy anythingIndexSwitch, easy forLoopEnd, easy forLoopStart, easy imageIndexSwitch]
problems: []
missing: []
members: [视频生成/文生视频/LongCat Avatar 单图循环数字人_2059633182730973185.json, 视频生成/文生视频/LongCat Avatar 多图切镜数字人_2059604643877056514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_941

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/LongCat Avatar 单图循环数字人_2059633182730973185.json、视频生成/文生视频/LongCat Avatar 多图切镜数字人_2059604643877056514.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：49%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `AudioDuration_wan`
- `CR Prompt Text`
- `FloatConstant`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LongCatAvatarWhisperEmbeds`
- `MathExpression_UTK`
- `ReplaceVideoLatentFrames`
- `ShowAnything|Mie`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WhisperModelLoader`
- `easy anythingIndexSwitch`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageIndexSwitch`

**可变部分**（部分 workflow 才有）：
- `ProcessString` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
