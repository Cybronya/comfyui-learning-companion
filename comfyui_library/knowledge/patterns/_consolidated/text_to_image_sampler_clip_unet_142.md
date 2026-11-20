---
name: text_to_image_sampler_clip_unet_142
type: Text To Image
frequency: 5
level: strong
coverage: 0.825
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/001.Z-image生图巅峰003.文生图_2033719257393012738.json, 图片生成/文生图/AI知识分享宝库丨Z-image文生图（优化出图比例）_1993874811084619777.json, 图片生成/文生图/Z-IMAGE 文生图_2020752365468520449.json, 图片生成/文生图/Z-image 基础文生图 V1（优化出图比例）_2003120005589999618.json, 图片生成/文生图/👾怪獸-Krea2 文生图-人物设计多lora选择 👾_2102397348696645634.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_142

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/001.Z-image生图巅峰003.文生图_2033719257393012738.json、图片生成/文生图/AI知识分享宝库丨Z-image文生图（优化出图比例）_1993874811084619777.json、图片生成/文生图/Z-IMAGE 文生图_2020752365468520449.json、图片生成/文生图/Z-image 基础文生图 V1（优化出图比例）_2003120005589999618.json、图片生成/文生图/👾怪獸-Krea2 文生图-人物设计多lora选择 👾_2102397348696645634.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `ImpactInt` —— 4/5 个有
- `ImpactSwitch` —— 4/5 个有
- `Int` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `easy positive` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `CR Text Concatenate` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `ConditioningKrea2Rebalance` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | 720 - 1920 | 5 | 66% |
| 高度 | 1080 | 1080 - 1920 | 5 | 75% |
| 采样步数 | 10 | 8 - 10 | 5 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1920，观测区间 720 - 1920，5 个样本
- 高度 中位数 1080，观测区间 1080 - 1920，5 个样本
- 采样步数 中位数 10，观测区间 8 - 10，5 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
