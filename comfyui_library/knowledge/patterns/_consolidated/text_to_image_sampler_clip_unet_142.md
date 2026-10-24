---
name: text_to_image_sampler_clip_unet_142
type: Text To Image
frequency: 4
level: moderate
coverage: 0.7175
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/z-image-图生图_2057417058383646721.json, 图片生成/图生图/z-image-图生图_2060273356666134529.json, 图片生成/文生图/2-图像生成 (T2I+I2I) Z-Image Turbo 工作流_2053397476975104001.json, 图片生成/文生图/Z-Anime-基于ZIB底模的动漫风格模型_2064727085071032322.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_142

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/z-image-图生图_2057417058383646721.json、图片生成/图生图/z-image-图生图_2060273356666134529.json、图片生成/文生图/2-图像生成 (T2I+I2I) Z-Image Turbo 工作流_2053397476975104001.json、图片生成/文生图/Z-Anime-基于ZIB底模的动漫风格模型_2064727085071032322.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `Seed (rgthree)` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `Resize Image for SDXL` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1344 | 4 | 87% |
| 高度 | 1536 | 768 - 1536 | 4 | 75% |
| 采样步数 | 8 | 8 - 10 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 0.7 | 0.3 - 1 | 4 | 63% |
| LoRA 模型强度 | 1.11022e-16 | - | 2 | 0% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1344，4 个样本，取值集中（一致性 87%）
- 高度 中位数 1536，观测区间 768 - 1536，4 个样本
- 采样步数 中位数 8，观测区间 8 - 10，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 0.7，观测区间 0.3 - 1，4 个样本
- LoRA 模型强度 中位数 1.11022e-16，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
