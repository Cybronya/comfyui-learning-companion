---
name: unknown_workflow_sampler_clip_unet_212
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.828667
common_nodes: [Anything Everywhere, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CR Color Panel, CR Text, ConditioningZeroOut, DenseDiffusionAddCondNode, DenseDiffusionApplyNode, EmptyLatentImage, FluxResolutionNode, GetImageSize, ImageCASharpening+, KSamplerSelect, LoadImage, MathExpression|pysssss, ModelSamplingAuraFlow, PreviewBridge, RH_Captioner, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, SolidMask, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/反推提示词/34bxtcy_2049761499433934850.json, 图片生成/图生图/【文创周边冰箱贴】Qwen 文生图 分区控制 冰箱贴_1996401178248355842.json, 图片生成/图生图/【文创周边冰箱贴】Qwen 文生图 分区控制 冰箱贴_2009940896887873538.json, 图片生成/文生图/【文创周边冰箱贴】Qwen文生图-分区控制_1956634749448982530.json, 图片生成/文生图/【文创周边冰箱贴】Qwen文生图-分区控制_2023674711632252930.json, 图片生成/文生图/文创冰箱贴一键生成_1987714485324591105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_212

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/34bxtcy_2049761499433934850.json、图片生成/图生图/【文创周边冰箱贴】Qwen 文生图 分区控制 冰箱贴_1996401178248355842.json、图片生成/图生图/【文创周边冰箱贴】Qwen 文生图 分区控制 冰箱贴_2009940896887873538.json、图片生成/文生图/【文创周边冰箱贴】Qwen文生图-分区控制_1956634749448982530.json、图片生成/文生图/【文创周边冰箱贴】Qwen文生图-分区控制_2023674711632252930.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `LayerUtility: TextJoin` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 784 | 784 - 784 | 6 | 100% |
| 高度 | 672 | 672 - 672 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 784，观测区间 784 - 784，6 个样本，取值集中（一致性 100%）
- 高度 中位数 672，观测区间 672 - 672，6 个样本，取值集中（一致性 100%）
