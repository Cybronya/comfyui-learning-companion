---
name: unknown_workflow_sampler_clip_unet_93
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.884286
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Latent Input Switch, Text Multiline, Text Find and Replace, Text String]
members: [图片生成/文生图/1953351554604695553.json, 图片生成/文生图/1953378626261712898.json, 图片生成/文生图/1953390443667095554.json, 图片生成/文生图/1953446698997743618.json, 图片生成/文生图/1953729540789075969.json, 图片生成/文生图/1953769832510574594.json, 图片生成/文生图/1962714914005626881.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_93

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1953351554604695553.json、图片生成/文生图/1953378626261712898.json、图片生成/文生图/1953390443667095554.json、图片生成/文生图/1953446698997743618.json、图片生成/文生图/1953729540789075969.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `FluxResolutionNode` —— 4/7 个有
- `Int` —— 3/7 个有
- `PrimitiveStringMultiline` —— 3/7 个有
- `RH_LLMAPI_NODE` —— 2/7 个有
- `Text Multiline` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `CR Latent Input Switch` —— 1/7 个有
- `Text Find and Replace` —— 1/7 个有
- `Text String` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 7 | 84% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 7 | 68% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，7 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Latent Input Switch、Text Multiline、Text Find and Replace、Text String
