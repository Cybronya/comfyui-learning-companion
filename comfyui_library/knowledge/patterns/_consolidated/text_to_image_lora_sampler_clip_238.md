---
name: text_to_image_lora_sampler_clip_238
type: Text To Image
frequency: 3
level: moderate
coverage: 0.979333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/▶▷Krea2文生图_2107457543818801153.json, 图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_2098225838008389634.json, 图片生成/文生图/泳装系列Z-image真实人像质感御姐美女_2104743758045728769.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_238

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/▶▷Krea2文生图_2107457543818801153.json、图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_2098225838008389634.json、图片生成/文生图/泳装系列Z-image真实人像质感御姐美女_2104743758045728769.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `QZ_ResolutionPreset` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 30 | 3 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 768 | 768 - 1024 | 3 | 86% |
| 高度 | 1280 | 1024 - 1344 | 3 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 30，3 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 1024，3 个样本，取值集中（一致性 86%）
- 高度 中位数 1280，观测区间 1024 - 1344，3 个样本，取值集中（一致性 89%）
