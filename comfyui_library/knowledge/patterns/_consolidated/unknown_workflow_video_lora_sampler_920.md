---
name: unknown_workflow_video_lora_sampler_920
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5065
common_nodes: [ComfyMathExpression, GetNode, INTConstant, ImageResizeKJv2, LoadAudio, LoadImage, LongCatAvatarWhisperEmbeds, PreviewAny, SetNode, TrimAudioDuration, VHS_VideoCombine, WanAnimatePlus BlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoTextEncodeCached, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/longcat avartart 1.5-single_2061466076168409089.json, 视频生成/图生视频/longcat avartart 1.5-数字人-人物对口型-单人_2063165866346377218.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_920

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/longcat avartart 1.5-single_2061466076168409089.json、视频生成/图生视频/longcat avartart 1.5-数字人-人物对口型-单人_2063165866346377218.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 2 个 workflow 都包含：
- `ComfyMathExpression`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LongCatAvatarWhisperEmbeds`
- `PreviewAny`
- `SetNode`
- `TrimAudioDuration`
- `VHS_VideoCombine`
- `WanAnimatePlus BlockSwap`
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

**可变部分**（部分 workflow 才有）：
- `FloatConstant` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
