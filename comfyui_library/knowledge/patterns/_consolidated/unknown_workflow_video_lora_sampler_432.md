---
name: unknown_workflow_video_lora_sampler_432
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.644
common_nodes: [CreateCFGScheduleFloatList, GetNode, LoadImage, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSigmaToStep, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1967355921259225089.json, 视频生成/图生视频/1968331846952079361.json, 视频生成/图生视频/1968663694437699585.json, 视频生成/图生视频/2037003847746461698.json, 视频生成/图生视频/2037072303892209666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_432

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1967355921259225089.json、视频生成/图生视频/1968331846952079361.json、视频生成/图生视频/1968663694437699585.json、视频生成/图生视频/2037003847746461698.json、视频生成/图生视频/2037072303892209666.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetNode`
- `LoadImage`
- `SetNode`
- `VHS_VideoCombine`
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

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `Display Any (rgthree)` —— 4/5 个有
- `ImageConcanate` —— 4/5 个有
- `ImpactSwitch` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `RH_LLMAPI_NODE` —— 4/5 个有
- `Seed (rgthree)` —— 4/5 个有
- `VideoContinuationGenerator` —— 4/5 个有
- `WanVideoBlender` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `INTConstant` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `Anything Everywhere` —— 1/5 个有
- `Bjornulf_ShowFloat` —— 1/5 个有
- `Float` —— 1/5 个有
- `ImageResizeKJ` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
