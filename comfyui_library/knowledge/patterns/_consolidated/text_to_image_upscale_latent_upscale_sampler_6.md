---
name: text_to_image_upscale_latent_upscale_sampler_6
type: Text To Image
frequency: 3
level: moderate
coverage: 0.876
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, LatentUpscaleBy, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/【RICK】肖像大师高清版(模特生成)_1906519526463442946.json, 图片生成/文生图/图像细节放大_2012407929160343554.json, 图片生成/文生图/文生图基础款_1990029530519793666.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_sampler_6

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/【RICK】肖像大师高清版(模特生成)_1906519526463442946.json、图片生成/文生图/图像细节放大_2012407929160343554.json、图片生成/文生图/文生图基础款_1990029530519793666.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `LatentUpscaleBy`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LatentUpscale` —— 1/3 个有
- `Lora Loader` —— 1/3 个有
- `PortraitMaster_中文版` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 768 | 3 | 100% |
| 高度 | 1024 | 512 - 1280 | 3 | 66% |
| 采样步数 | 20 | 20 - 40 | 3 | 65% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | normal | - | 3 | 33% |
| 重绘幅度 | 1 | 0.59 - 1 | 3 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 768，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 512 - 1280，3 个样本
- 采样步数 中位数 20，观测区间 20 - 40，3 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 normal，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 0.59 - 1，3 个样本
