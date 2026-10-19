---
name: unknown_workflow_lora_sampler_clip_117
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.628
common_nodes: [Anything Everywhere, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CR Color Panel, CR Text, ConditioningZeroOut, DenseDiffusionAddCondNode, DenseDiffusionApplyNode, EmptyLatentImage, FluxResolutionNode, GetImageSize, ImageCASharpening+, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingAuraFlow, PreviewBridge, RH_Captioner, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, SolidMask, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: [CR Color Panel, CR Text, ImageCASharpening+, MathExpression|pysssss, easy cleanGpuUsed]
members: [图片生成/文生图/1956634749448982530.json, 图片生成/文生图/1987714485324591105.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_117

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1956634749448982530.json、图片生成/文生图/1987714485324591105.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Color Panel`
- `CR Text`
- `ConditioningZeroOut`
- `DenseDiffusionAddCondNode`
- `DenseDiffusionApplyNode`
- `EmptyLatentImage`
- `FluxResolutionNode`
- `GetImageSize`
- `ImageCASharpening+`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingAuraFlow`
- `PreviewBridge`
- `RH_Captioner`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 784 | - | 2 | 100% |
| 高度 | 672 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 784，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 672，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Color Panel、CR Text、ImageCASharpening+、MathExpression|pysssss、easy cleanGpuUsed
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
