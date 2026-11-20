---
name: unknown_workflow_lora_sampler_clip_289
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.812
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, Get resolution [Crystools], ImageFromBatch, Int, KSamplerSelect, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Seed (rgthree), Switch any [Crystools], UNETLoader, VAEDecode, VAEEncode, VAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy getNode, easy imageConcat, easy imageIndexSwitch, easy setNode, easy textIndexSwitch]
problems: []
missing: []
members: [图片生成/图生图/Klein 人物一键多视图工作流  pro max_2024147507437113345.json, 平台全量/Flux2+Klein+人物一键多视图工作流+（6G显存可用）_2074043421899190274.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_289

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Klein 人物一键多视图工作流  pro max_2024147507437113345.json、平台全量/Flux2+Klein+人物一键多视图工作流+（6G显存可用）_2074043421899190274.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `Get resolution [Crystools]`
- `ImageFromBatch`
- `Int`
- `KSamplerSelect`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `Switch any [Crystools]`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy getNode`
- `easy imageConcat`
- `easy imageIndexSwitch`
- `easy setNode`
- `easy textIndexSwitch`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
