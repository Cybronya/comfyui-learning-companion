---
name: text_to_image_sampler_clip_unet_50
type: Text To Image
frequency: 9
level: moderate
coverage: 0.961333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FLUX.1_ipadapter_1880962162222067713.json, 图片生成/文生图/flux 2文生图 丨电商场景图_1997117365974405121.json, 图片生成/文生图/kontext文生多图（基础模型，快速出图）_2021770258335408129.json, 图片生成/文生图/krea2 turbo文生图_2069631042172055554.json, 图片生成/文生图/krea2 turbo文生图_2069632468088606722.json, 图片生成/文生图/krea2 turbo文生图_2069636296083075074.json, 图片生成/文生图/krea2 turbo文生图（最新开源，质量极高，速度极快）_2069769763433304066.json, 图片生成/文生图/krea2_文生图_2081989846117216258.json, 图片生成/文生图/宝宝版 文生图_2009166166715011074.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_50

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/FLUX.1_ipadapter_1880962162222067713.json、图片生成/文生图/flux 2文生图 丨电商场景图_1997117365974405121.json、图片生成/文生图/kontext文生多图（基础模型，快速出图）_2021770258335408129.json、图片生成/文生图/krea2 turbo文生图_2069631042172055554.json、图片生成/文生图/krea2 turbo文生图_2069632468088606722.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 7/9 个有
- `DualCLIPLoader` —— 3/9 个有
- `FluxGuidance` —— 3/9 个有
- `DeepTranslatorTextNode` —— 2/9 个有
- `ApplyIPAdapterFlux` —— 1/9 个有
- `CR Text` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `IPAdapterFluxLoader` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `NunchakuFluxDiTLoader` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 22 | 9 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.76 | 9 | 78% |
| 采样算法 | euler | - | 9 | 56% |
| 调度器 | simple | - | 9 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1024 | 768 - 1504 | 9 | 83% |
| 高度 | 1536 | 504 - 1920 | 9 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 22，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.76，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 56%
- 调度器 最常用 simple，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 1504，9 个样本，取值集中（一致性 83%）
- 高度 中位数 1536，观测区间 504 - 1920，9 个样本
- 高发问题（5/9 个样本）：Steps较低可能导致细节不足
