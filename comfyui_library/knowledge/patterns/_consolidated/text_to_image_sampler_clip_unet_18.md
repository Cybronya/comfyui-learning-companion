---
name: text_to_image_sampler_clip_unet_18
type: Text To Image
frequency: 15
level: moderate
coverage: 0.890867
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-turbo文生图3D国漫CG风格_2074209841383567362.json, 图片生成/文生图/Z-image-turbo文生图赛璐璐平涂动漫风格_2077821791761948673.json, 图片生成/文生图/Z-image-turbo文生图超写实真人摄影风格_2076587497584414722.json, 图片生成/文生图/Z-image-turbo：最简文生图工作流_1996508267809480705.json, 图片生成/文生图/Z-image-刘亦菲专用_1996450752195338242.json, 图片生成/文生图/Z-image-暗黑浮世绘_1997401855502258178.json, 图片生成/文生图/Z-image基础文生图，zimage文生图_1998203845559902209.json, 图片生成/文生图/Z-image文生图工作流_2009195465652314113.json, 图片生成/文生图/krea2-Afterlight（光影美学文生图）_2083839367738642434.json, 图片生成/文生图/krea2_turbo_基础文生图工作流_2078078374207115266.json, 图片生成/文生图/krea2基础文生图_2071164326781734914.json, 图片生成/文生图/krea2基础文生图文生图工作流_2089571734700773377.json, 图片生成/文生图/krea2基础文生图高清出图工作流_2089673479443533826.json, 图片生成/文生图/qwen2512大雷甜妹JK制服少女_2018569892831694850.json, 图片生成/文生图/qwen_image_edit-2509 文生图_2026532700005339137.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_18

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/Z-image-turbo文生图3D国漫CG风格_2074209841383567362.json、图片生成/文生图/Z-image-turbo文生图赛璐璐平涂动漫风格_2077821791761948673.json、图片生成/文生图/Z-image-turbo文生图超写实真人摄影风格_2076587497584414722.json、图片生成/文生图/Z-image-turbo：最简文生图工作流_1996508267809480705.json、图片生成/文生图/Z-image-刘亦菲专用_1996450752195338242.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 14/15 个有
- `ConditioningZeroOut` —— 9/15 个有
- `ModelSamplingAuraFlow` —— 5/15 个有
- `GetNode` —— 4/15 个有
- `SetNode` —— 4/15 个有
- `CR Latent Input Switch` —— 3/15 个有
- `easy seed` —— 2/15 个有
- `CFGNorm` —— 1/15 个有
- `CR Text` —— 1/15 个有
- `LatentFrequencyEnhancer_lrzjason` —— 1/15 个有
- `LayerUtility: PurgeVRAM` —— 1/15 个有
- `LayerUtility: TextJoin` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 864 | 752 - 1920 | 15 | 70% |
| 高度 | 1536 | 864 - 1920 | 15 | 80% |
| 采样步数 | 10 | 4 - 16 | 15 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 15 | 51% |
| 采样算法 | euler | - | 15 | 60% |
| 调度器 | simple | - | 15 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 864，观测区间 752 - 1920，15 个样本
- 高度 中位数 1536，观测区间 864 - 1920，15 个样本，取值集中（一致性 80%）
- 采样步数 中位数 10，观测区间 4 - 16，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，15 个样本
- 采样算法 最常用 euler，15 个样本，一致性 60%
- 调度器 最常用 simple，15 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（8/15 个样本）：Steps较低可能导致细节不足
