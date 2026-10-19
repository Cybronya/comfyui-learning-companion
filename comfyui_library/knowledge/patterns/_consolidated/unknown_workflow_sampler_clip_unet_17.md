---
name: unknown_workflow_sampler_clip_unet_17
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.898636
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [Note Plus (mtb), CR Latent Input Switch, Text Multiline, Text Find and Replace, Text String]
members: [图片生成/文生图/1953057914565103617.json, 图片生成/文生图/1953059659532988418.json, 图片生成/文生图/1953087441538322434.json, 图片生成/文生图/1953143788371906562.json, 图片生成/文生图/1953162182935703553.json, 图片生成/文生图/1953252280764141569.json, 图片生成/文生图/1953287044091023361.json, 图片生成/文生图/1953378626261712898.json, 图片生成/文生图/1953446698997743618.json, 图片生成/文生图/1953729540789075969.json, 图片生成/文生图/1953769832510574594.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_17

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/1953057914565103617.json、图片生成/文生图/1953059659532988418.json、图片生成/文生图/1953087441538322434.json、图片生成/文生图/1953143788371906562.json、图片生成/文生图/1953162182935703553.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 5/11 个有
- `Int` —— 4/11 个有
- `PathchSageAttentionKJ` —— 2/11 个有
- `Text Multiline` —— 2/11 个有
- `CR Latent Input Switch` —— 1/11 个有
- `FluxResolutionNode` —— 1/11 个有
- `Note Plus (mtb)` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `Text Find and Replace` —— 1/11 个有
- `Text String` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 11 | 93% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 11 | 60% |
| 采样算法 | euler | - | 11 | 91% |
| 调度器 | simple | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，11 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 91%
- 调度器 最常用 simple，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Note Plus (mtb)、CR Latent Input Switch、Text Multiline、Text Find and Replace、Text String
