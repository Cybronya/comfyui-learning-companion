---
name: unknown_workflow_lora_sampler_clip_110
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.679667
common_nodes: [Anything Everywhere, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CR Color Panel, CR Text, ConditioningZeroOut, DenseDiffusionAddCondNode, DenseDiffusionApplyNode, EmptyLatentImage, FluxResolutionNode, GetImageSize, ImageCASharpening+, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingAuraFlow, PreviewBridge, RH_Captioner, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, SolidMask, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: [CR Color Panel, CR Text, ImageCASharpening+, MathExpression|pysssss, easy cleanGpuUsed]
members: [图片生成/文生图/1956634749448982530.json, 图片生成/文生图/1987714485324591105.json, 图片生成/文生图/【文创周边冰箱贴】Qwen文生图-分区控制_2023674711632252930.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_110

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1956634749448982530.json、图片生成/文生图/1987714485324591105.json、图片生成/文生图/【文创周边冰箱贴】Qwen文生图-分区控制_2023674711632252930.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 3 个 workflow 都包含：
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
| 宽度 | 784 | 784 - 784 | 3 | 100% |
| 高度 | 672 | 672 - 672 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 784，观测区间 784 - 784，3 个样本，取值集中（一致性 100%）
- 高度 中位数 672，观测区间 672 - 672，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Color Panel、CR Text、ImageCASharpening+、MathExpression|pysssss、easy cleanGpuUsed
