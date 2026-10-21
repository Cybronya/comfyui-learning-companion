---
name: unknown_workflow_sampler_clip_vae_29
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.5095
common_nodes: [Anything Everywhere, Anything Everywhere3, CLIPTextEncode, ConditioningZeroOut, KSampler (Efficient), LayerFilter: HDREffects, ModelSamplingFlux, PreviewImage, SaveImage, Seed Everywhere, StringFunction|pysssss, VAELoader]
problems: []
missing: [LayerFilter: HDREffects, StringFunction|pysssss, KSampler (Efficient), Seed Everywhere]
members: [图片生成/文生图/1951862230881128449.json, 图片生成/文生图/1951865922078322690.json, 图片生成/文生图/1952280309612097537.json, 图片生成/文生图/1952283213253259265.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_29

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1951862230881128449.json、图片生成/文生图/1951865922078322690.json、图片生成/文生图/1952280309612097537.json、图片生成/文生图/1952283213253259265.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：51%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler (Efficient)`
- `LayerFilter: HDREffects`
- `ModelSamplingFlux`
- `PreviewImage`
- `SaveImage`
- `Seed Everywhere`
- `StringFunction|pysssss`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 3/4 个有
- `EmptyLatentImage` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `DeepTranslatorTextNode` —— 2/4 个有
- `FluxGuidance` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `DualCLIPLoaderGGUF` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `VAEEncode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 800 | 800 - 800 | 3 | 100% |
| 高度 | 1200 | 1024 - 1200 | 3 | 93% |
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 0.85 - 1 | 4 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 800，观测区间 800 - 800，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1200，观测区间 1024 - 1200，3 个样本，取值集中（一致性 93%）
- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.85 - 1，4 个样本，取值集中（一致性 93%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerFilter: HDREffects、StringFunction|pysssss、KSampler (Efficient)、Seed Everywhere
