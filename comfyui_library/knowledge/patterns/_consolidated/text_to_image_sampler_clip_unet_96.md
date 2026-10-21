---
name: text_to_image_sampler_clip_unet_96
type: Text To Image
frequency: 5
level: strong
coverage: 0.91
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/人像写实文生图_2077971754424815618.json, 图片生成/文生图/墨幽人造人ZIB-8步_MYHuman-Z文生图_2066054505480933378.json, 图片生成/文生图/墨幽人造人ZIB-8步_MYHuman-Z文生图_2069999480446996482.json, 图片生成/文生图/墨幽人造人ZIB-8步_MYHuman-Z文生图_2070001157514293249.json, 图片生成/文生图/墨幽人造人ZIB-8步_MYHuman-Z文生图_2070002567194693634.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_96

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/人像写实文生图_2077971754424815618.json、图片生成/文生图/墨幽人造人ZIB-8步_MYHuman-Z文生图_2066054505480933378.json、图片生成/文生图/墨幽人造人ZIB-8步_MYHuman-Z文生图_2069999480446996482.json、图片生成/文生图/墨幽人造人ZIB-8步_MYHuman-Z文生图_2070001157514293249.json、图片生成/文生图/墨幽人造人ZIB-8步_MYHuman-Z文生图_2070002567194693634.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `RH_OneShot_Prompter` —— 1/5 个有
- `RH_Prompter` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `String Replace (mtb)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1184 | 768 - 1184 | 5 | 85% |
| 高度 | 1536 | 1024 - 1536 | 5 | 86% |
| 采样步数 | 8 | 8 - 12 | 5 | 82% |
| Prompt 约束强度(CFG) | 2 | 1 - 2 | 5 | 78% |
| 采样算法 | res_2s | - | 5 | 80% |
| 调度器 | bong_tangent | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1184，观测区间 768 - 1184，5 个样本，取值集中（一致性 85%）
- 高度 中位数 1536，观测区间 1024 - 1536，5 个样本，取值集中（一致性 86%）
- 采样步数 中位数 8，观测区间 8 - 12，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 2，5 个样本
- 采样算法 最常用 res_2s，5 个样本，一致性 80%
- 调度器 最常用 bong_tangent，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
