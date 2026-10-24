---
name: text_to_image_sampler_clip_vae_24
type: Text To Image
frequency: 7
level: moderate
coverage: 0.904571
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-_2076232929050714114.json, 图片生成/文生图/Z-image-Base-文生图_2016479774817914881.json, 图片生成/文生图/Z-image-De-文生图_1998012102017212417.json, 图片生成/文生图/Z-image-base-极速文生图（4步）_2021737206347472898.json, 图片生成/文生图/Z-image-base文生图_2016370305647775745.json, 图片生成/文生图/anima_base 1.0 Moebius 风格文生图_2073322108050038785.json, 图片生成/文生图/潦草线条铅笔画_2017271179677016065.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_24

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Z-_2076232929050714114.json、图片生成/文生图/Z-image-Base-文生图_2016479774817914881.json、图片生成/文生图/Z-image-De-文生图_1998012102017212417.json、图片生成/文生图/Z-image-base-极速文生图（4步）_2021737206347472898.json、图片生成/文生图/Z-image-base文生图_2016370305647775745.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 6/7 个有
- `ModelSamplingAuraFlow` —— 5/7 个有
- `JjkText` —— 3/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `PreviewAny` —— 2/7 个有
- `NunchakuZImageDiTLoader` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `Qwen2.5` —— 1/7 个有
- `Text Concatenate` —— 1/7 个有
- `easy imageSave` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 960 | 720 - 1104 | 7 | 89% |
| 高度 | 1536 | 1280 - 1560 | 7 | 92% |
| 采样步数 | 25 | 4 - 40 | 7 | 48% |
| Prompt 约束强度(CFG) | 3 | 1 - 4.5 | 7 | 53% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 960，观测区间 720 - 1104，7 个样本，取值集中（一致性 89%）
- 高度 中位数 1536，观测区间 1280 - 1560，7 个样本，取值集中（一致性 92%）
- 采样步数 中位数 25，观测区间 4 - 40，7 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 4.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
