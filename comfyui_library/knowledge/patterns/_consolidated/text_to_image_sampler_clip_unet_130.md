---
name: text_to_image_sampler_clip_unet_130
type: Text To Image
frequency: 3
level: moderate
coverage: 0.806
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Anime-基于ZIB底模的动漫风格模型_2064727085071032322.json, 图片生成/文生图/Z-image两条对比工作流，测试不同参数对图片生成的影响_2077645152755208194.json, 图片生成/文生图/（贞贞版）Z-image-Kook真实幻想文生图V1_1995736528510922753.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_130

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-Anime-基于ZIB底模的动漫风格模型_2064727085071032322.json、图片生成/文生图/Z-image两条对比工作流，测试不同参数对图片生成的影响_2077645152755208194.json、图片生成/文生图/（贞贞版）Z-image-Kook真实幻想文生图V1_1995736528510922753.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1080 | 3 | 97% |
| 高度 | 1536 | 1536 - 1920 | 3 | 89% |
| 采样步数 | 9 | 8 - 10 | 3 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 33% |
| 重绘幅度 | 0.3 | 0.2 - 1 | 3 | 29% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1080，3 个样本，取值集中（一致性 97%）
- 高度 中位数 1536，观测区间 1536 - 1920，3 个样本，取值集中（一致性 89%）
- 采样步数 中位数 9，观测区间 8 - 10，3 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 33%
- 重绘幅度 中位数 0.3，观测区间 0.2 - 1，3 个样本，取值分散，一致性仅 29%
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
