---
name: unknown_workflow_lora_sampler_unet_284
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.851
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, RHHiddenNodes, SaveImage, TextEncodeQwenImageEditPlus_lrzjason, UNETLoader, VAEDecode, VAELoader, easy getNode, easy positive, easy setNode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/一键证件照 生活照秒变精致证件照  照片精修  抠图换底   底色任选_2039859264612732929.json, 平台全量/生活照秒变精致证件照_ 照片精修 _ 抠图换底 _ 底色任选 _ 求职 _ 报名_自选服装_2010289220551712770.json, 平台全量/生活照秒变职业形象照，简历、头像、宣传照、半身_全身照片_2045037169294712833.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_284

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/一键证件照 生活照秒变精致证件照  照片精修  抠图换底   底色任选_2039859264612732929.json、平台全量/生活照秒变精致证件照_ 照片精修 _ 抠图换底 _ 底色任选 _ 求职 _ 报名_自选服装_2010289220551712770.json、平台全量/生活照秒变职业形象照，简历、头像、宣传照、半身_全身照片_2045037169294712833.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RHHiddenNodes`
- `SaveImage`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy getNode`
- `easy positive`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `AddBackgroundNode` —— 2/3 个有
- `Float` —— 2/3 个有
- `HivisionLayOutNode` —— 2/3 个有
- `HivisionNode` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `LaterProcessNode` —— 2/3 个有
- `ZHHivisionParamsNode` —— 2/3 个有
- `ImageStitch` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
