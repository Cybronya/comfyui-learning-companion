---
name: unknown_workflow_sampler_clip_vae_31
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5115
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), KSampler (Efficient), LayerFilter: HDREffects, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, PreviewImage, SaveImage, StringFunction|pysssss, VAELoader]
problems: []
missing: [LayerFilter: HDREffects, StringFunction|pysssss, KSampler (Efficient), Seed Everywhere]
members: [图片生成/文生图/1960541449391661058.json, 图片生成/文生图/1985254236038569985.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_31

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1960541449391661058.json、图片生成/文生图/1985254236038569985.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler (Efficient)`
- `LayerFilter: HDREffects`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `PreviewImage`
- `SaveImage`
- `StringFunction|pysssss`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Seed Everywhere` —— 1/2 个有
- `VAEUtils_CustomVAELoader` —— 1/2 个有
- `VAEUtils_VAEDecodeTiled` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.75 | - | 2 | 67% |
| 宽度 | 1112 | - | 2 | 92% |
| 高度 | 764 | - | 2 | 66% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.75，样本不足，未给区间，2 个样本
- 宽度 中位数 1112，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 高度 中位数 764，样本不足，未给区间，2 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：LayerFilter: HDREffects、StringFunction|pysssss、KSampler (Efficient)、Seed Everywhere
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
