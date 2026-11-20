---
name: unknown_workflow_sampler_clip_unet_553
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.903
common_nodes: [AddLabel, CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, Flux2Scheduler, ImagesConcanateToGrid, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, PreviewAny, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Seed (rgthree), StringConcatenate, Text, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy batchAnything, easy convertAnything, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: []
missing: []
members: [平台全量/工作流基础系列1.1-Klein单图编辑工作流-CFG值的影响-使用For循环_2043573380951052290.json, 平台全量/工作流基础系列1.2-Klein单图编辑工作流-Step值的影响-使用For循环_2043586158503927809.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_553

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/工作流基础系列1.1-Klein单图编辑工作流-CFG值的影响-使用For循环_2043573380951052290.json、平台全量/工作流基础系列1.2-Klein单图编辑工作流-Step值的影响-使用For循环_2043586158503927809.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `AddLabel`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `ImagesConcanateToGrid`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `PreviewAny`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `StringConcatenate`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy batchAnything`
- `easy convertAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
