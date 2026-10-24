---
name: unknown_workflow_video_lora_sampler_201
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.615222
common_nodes: [CreateCFGScheduleFloatList, Display Any (rgthree), GetNode, LoadImage, PreviewImage, Seed (rgthree), SetNode, VHS_VideoCombine, VideoContinuationGenerator, WanVideoBlender, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSigmaToStep, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/wan2.2 2张旋转-简化_2038442502138630146.json, 图片生成/图生图/wan2.2 4张旋转_2031620500375474178.json, 视频生成/图生视频/Wan2.2 Fun VACE多张图首尾帧串联_1968331846952079361.json, 视频生成/图生视频/Wan2.2 Fun VACE多张图首尾帧串联_1968663694437699585.json, 视频生成/图生视频/wan2.2 2张旋转_2037003847746461698.json, 视频生成/图生视频/wan2.2 4张旋转-简化_2037072303892209666.json, 视频生成/图生视频/wan2.2 4张旋转-简化_2039320713127006210.json, 视频生成/图生视频/wan2.2 4张旋转-简化_2039344777270923265.json, 视频生成/图生视频/wan2.2-4张旋转-简化-新提示词_2039706653515321346.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_201

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/wan2.2 2张旋转-简化_2038442502138630146.json、图片生成/图生图/wan2.2 4张旋转_2031620500375474178.json、视频生成/图生视频/Wan2.2 Fun VACE多张图首尾帧串联_1968331846952079361.json、视频生成/图生视频/Wan2.2 Fun VACE多张图首尾帧串联_1968663694437699585.json、视频生成/图生视频/wan2.2 2张旋转_2037003847746461698.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 9 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `Display Any (rgthree)`
- `GetNode`
- `LoadImage`
- `PreviewImage`
- `Seed (rgthree)`
- `SetNode`
- `VHS_VideoCombine`
- `VideoContinuationGenerator`
- `WanVideoBlender`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSigmaToStep`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 8/9 个有
- `CR Text` —— 6/9 个有
- `ImageConcanate` —— 6/9 个有
- `ImpactSwitch` —— 6/9 个有
- `RH_LLMAPI_NODE` —— 6/9 个有
- `Anything Everywhere` —— 1/9 个有
- `Bjornulf_ShowFloat` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `PrimitiveFloat` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `ShowText|pysssss` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
