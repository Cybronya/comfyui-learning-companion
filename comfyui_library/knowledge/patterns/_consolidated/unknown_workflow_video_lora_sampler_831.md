---
name: unknown_workflow_video_lora_sampler_831
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.907
common_nodes: [Bjornulf_ShowStringText, GetImageSizeAndCount, INTConstant, ImageResizeKJ, ImageResizeKJv2, Int, JjkConcat, LTXVPromptEnhancer, LTXVPromptEnhancerLoader, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, TTP_text_mix, TextInput_, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/AI短剧角色超长表演万相WAN2.2+6段For循环超长图生视频最长6分镜连续_1954097242955235330.json, 视频生成/图生视频/Wan2.2_ESRGAN超分_Lightx2v加速+提示词优化_1980666931474776066.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_831

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/AI短剧角色超长表演万相WAN2.2+6段For循环超长图生视频最长6分镜连续_1954097242955235330.json、视频生成/图生视频/Wan2.2_ESRGAN超分_Lightx2v加速+提示词优化_1980666931474776066.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

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
- `MathExpression|pysssss`
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
- `ForLoopClose` —— 1/2 个有
- `ForLoopOpen` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `GridStrings` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `Int2String` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `WanVideoContextOptions` —— 1/2 个有
- `WanVideoEnhanceAVideo` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `WanVideoSLG` —— 1/2 个有
- `easy batchAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
