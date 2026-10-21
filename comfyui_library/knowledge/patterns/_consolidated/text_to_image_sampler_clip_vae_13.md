---
name: text_to_image_sampler_clip_vae_13
type: Text To Image
frequency: 6
level: moderate
coverage: 0.946667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-_2076232929050714114.json, 图片生成/文生图/Z-image-Base-文生图_2016479774817914881.json, 图片生成/文生图/Z-image-De-文生图_1998012102017212417.json, 图片生成/文生图/Z-image-base-极速文生图（4步）_2021737206347472898.json, 图片生成/文生图/Z-image-base文生图_2016192732154306562.json, 图片生成/文生图/Z-image-base文生图_2016370305647775745.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_13

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-_2076232929050714114.json、图片生成/文生图/Z-image-Base-文生图_2016479774817914881.json、图片生成/文生图/Z-image-De-文生图_1998012102017212417.json、图片生成/文生图/Z-image-base-极速文生图（4步）_2021737206347472898.json、图片生成/文生图/Z-image-base文生图_2016192732154306562.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 5/6 个有
- `UNETLoader` —— 5/6 个有
- `PreviewAny` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `NunchakuZImageDiTLoader` —— 1/6 个有
- `Qwen2.5` —— 1/6 个有
- `easy imageSave` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 960 | 720 - 1184 | 6 | 86% |
| 高度 | 1548 | 1280 - 1560 | 6 | 93% |
| 采样步数 | 25 | 4 - 50 | 6 | 36% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4 | 6 | 52% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 960，观测区间 720 - 1184，6 个样本，取值集中（一致性 86%）
- 高度 中位数 1548，观测区间 1280 - 1560，6 个样本，取值集中（一致性 93%）
- 采样步数 中位数 25，观测区间 4 - 50，6 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
