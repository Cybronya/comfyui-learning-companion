---
name: unknown_workflow_lora_sampler_clip_112
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9498
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-rebalance文生图_1999689524483682305.json, 图片生成/文生图/Qwen2512+文生图_2010038639497056258.json, 图片生成/文生图/Z-image Base Distilled蒸馏加速版_2019063606171668481.json, 图片生成/文生图/Z-image 文生图_2017213414262710273.json, 图片生成/文生图/【官版】Qwen Image-8步优化加速-增加宽高参数版本_1961085397939982338.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_112

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen-rebalance文生图_1999689524483682305.json、图片生成/文生图/Qwen2512+文生图_2010038639497056258.json、图片生成/文生图/Z-image Base Distilled蒸馏加速版_2019063606171668481.json、图片生成/文生图/Z-image 文生图_2017213414262710273.json、图片生成/文生图/【官版】Qwen Image-8步优化加速-增加宽高参数版本_1961085397939982338.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `ImpactInt` —— 2/5 个有
- `LayerUtility: ImageReel` —— 2/5 个有
- `LayerUtility: ImageReelComposit` —— 2/5 个有
- `CFGNorm` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `StringFunction|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 5 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（7/5 个样本）：Steps较低可能导致细节不足
