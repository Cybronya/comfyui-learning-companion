---
name: text_to_image_sampler_clip_unet_53
type: Text To Image
frequency: 8
level: strong
coverage: 0.93825
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Int, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/AI知识分享宝库丨Z-image文生图（优化出图比例）_1993874811084619777.json, 图片生成/文生图/API-z-image_2066009097937448961.json, 图片生成/文生图/API-z-image_2066893780837560322.json, 图片生成/文生图/API-z-image_2085310412328886273.json, 图片生成/文生图/API-z-image_2100574150950739970.json, 图片生成/文生图/Z-IMAGE 文生图_2020752365468520449.json, 图片生成/文生图/Z-image 基础文生图 V1（优化出图比例）_2003120005589999618.json, 图片生成/文生图/👾怪獸-Krea2 文生图-人物设计多lora选择 👾_2102397348696645634.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_53

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/AI知识分享宝库丨Z-image文生图（优化出图比例）_1993874811084619777.json、图片生成/文生图/API-z-image_2066009097937448961.json、图片生成/文生图/API-z-image_2066893780837560322.json、图片生成/文生图/API-z-image_2085310412328886273.json、图片生成/文生图/API-z-image_2100574150950739970.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Int`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `ImpactSwitch` —— 4/8 个有
- `LoadImage` —— 4/8 个有
- `Text _O` —— 4/8 个有
- `ImpactInt` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `easy positive` —— 3/8 个有
- `CR Text Concatenate` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `ConditioningKrea2Rebalance` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 2168 | 1080 - 2416 | 8 | 79% |
| 高度 | 1080 | 1080 - 1920 | 8 | 77% |
| 采样步数 | 10 | 8 - 14 | 8 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 2168，观测区间 1080 - 2416，8 个样本
- 高度 中位数 1080，观测区间 1080 - 1920，8 个样本
- 采样步数 中位数 10，观测区间 8 - 14，8 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
