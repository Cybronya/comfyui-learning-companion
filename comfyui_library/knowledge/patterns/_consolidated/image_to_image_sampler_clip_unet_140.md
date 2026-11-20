---
name: image_to_image_sampler_clip_unet_140
type: Image To Image
frequency: 3
level: moderate
coverage: 0.792667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-图生图丨洗图_1988237602652381186.json, 图片生成/图生图/Z-image通用图生图工作流_2087374985752039425.json, 图片生成/图生图/Z-image通用图生图工作流_2087403054042796034.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_140

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-图生图丨洗图_1988237602652381186.json、图片生成/图生图/Z-image通用图生图工作流_2087374985752039425.json、图片生成/图生图/Z-image通用图生图工作流_2087403054042796034.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `JanusImageUnderstanding` —— 1/3 个有
- `JanusModelLoader` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | res_multistep | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.55 | 0.55 - 0.6 | 3 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 res_multistep，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.55，观测区间 0.55 - 0.6，3 个样本，取值集中（一致性 96%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
