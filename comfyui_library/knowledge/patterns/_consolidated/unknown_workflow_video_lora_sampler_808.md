---
name: unknown_workflow_video_lora_sampler_808
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.905
common_nodes: [Bjornulf_ShowStringText, GetImageSizeAndCount, INTConstant, ImageResizeKJ, ImageResizeKJv2, Int, JjkConcat, LTXVPromptEnhancer, LTXVPromptEnhancerLoader, LoadImage, LoadWanVideoT5TextEncoder, Note Plus (mtb), TTP_text_mix, TextInput_, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2_I2V_KJ图生视频+智能优化+加速版Borges_1951969407968948225.json, 视频生成/图生视频/Wan2.2_I2V_KJ图生视频_Lightx2v加速开关+提示词智能优化开关 Borges_1951996290366427137.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_808

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.2_I2V_KJ图生视频+智能优化+加速版Borges_1951969407968948225.json、视频生成/图生视频/Wan2.2_I2V_KJ图生视频_Lightx2v加速开关+提示词智能优化开关 Borges_1951996290366427137.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `Bjornulf_ShowStringText`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `Int`
- `JjkConcat`
- `LTXVPromptEnhancer`
- `LTXVPromptEnhancerLoader`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Note Plus (mtb)`
- `TTP_text_mix`
- `TextInput_`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `CreateCFGScheduleFloatList` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
