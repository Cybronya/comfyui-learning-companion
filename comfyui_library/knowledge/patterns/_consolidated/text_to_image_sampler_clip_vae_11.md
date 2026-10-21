---
name: text_to_image_sampler_clip_vae_11
type: Text To Image
frequency: 8
level: moderate
coverage: 0.91825
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图_2016773236125605889.json, 图片生成/文生图/文生图_2070723264158191617.json, 图片生成/文生图/文生图z-image-turbo_2080295709659713538.json, 图片生成/文生图/文生图ziamge_2015340435937431553.json, 图片生成/文生图/文生图工作流_2092188994711937026.json, 图片生成/文生图/文生图（最强最快真实感Z-image）_1993837816855592961.json, 图片生成/文生图/最新Krea2+Turbo文生图 双采样加强版_2071061410838302722.json, 图片生成/文生图/最新文生图Krea2+Turbo 双采样加强版_2071101261251960834.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_11

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/文生图_2016773236125605889.json、图片生成/文生图/文生图_2070723264158191617.json、图片生成/文生图/文生图z-image-turbo_2080295709659713538.json、图片生成/文生图/文生图ziamge_2015340435937431553.json、图片生成/文生图/文生图工作流_2092188994711937026.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 7/8 个有
- `Int` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `RH_Captioner` —— 1/8 个有
- `TTResolutionSelector` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1920 | 8 | 71% |
| 高度 | 1180 | 1024 - 1920 | 8 | 76% |
| 采样步数 | 8.5 | 3 - 10 | 8 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 0.4 - 1 | 8 | 69% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1920，8 个样本
- 高度 中位数 1180，观测区间 1024 - 1920，8 个样本
- 采样步数 中位数 8.5，观测区间 3 - 10，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，8 个样本
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
