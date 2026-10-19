---
name: text_to_image_sampler_clip_unet
type: Text To Image
frequency: 11
level: moderate
coverage: 0.969
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Seed]
members: [图片生成/图生图/2021581695731900418.json, 图片生成/文生图/1901871929287188482.json, 图片生成/文生图/1904463583671980033.json, 图片生成/文生图/1910491843820253185.json, 图片生成/文生图/1910503564932804610.json, 图片生成/文生图/1921302462970658818.json, 图片生成/文生图/1930451421953691649.json, 图片生成/文生图/1934106744388018178.json, 图片生成/文生图/1935524742722158593.json, 图片生成/文生图/1950469653418184706.json, 图片生成/文生图/1973765930620727297.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/2021581695731900418.json、图片生成/文生图/1901871929287188482.json、图片生成/文生图/1904463583671980033.json、图片生成/文生图/1910491843820253185.json、图片生成/文生图/1910503564932804610.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 10/11 个有
- `LoraLoaderModelOnly` —— 10/11 个有
- `FluxGuidance` —— 8/11 个有
- `ConditioningZeroOut` —— 3/11 个有
- `TeaCache` —— 3/11 个有
- `FluxResolutionNode` —— 2/11 个有
- `RH_Prompter` —— 2/11 个有
- `CLIPLoader` —— 1/11 个有
- `CLIPTextEncodeFlux` —— 1/11 个有
- `CR Seed` —— 1/11 个有
- `CheckpointLoaderSimple` —— 1/11 个有
- `ImageConcanate` —— 1/11 个有
- `RH_Translator` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 11 | 51% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 11 | 32% |
| 采样算法 | euler | - | 11 | 91% |
| 调度器 | simple | - | 11 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 800 | 512 - 1024 | 11 | 81% |
| 高度 | 1024 | 512 - 1536 | 11 | 74% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，11 个样本，取值分散，一致性仅 32%
- 采样算法 最常用 euler，11 个样本，一致性 91%
- 调度器 最常用 simple，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 800，观测区间 512 - 1024，11 个样本，取值集中（一致性 81%）
- 高度 中位数 1024，观测区间 512 - 1536，11 个样本
- 高发问题（7/11 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Seed
