---
name: text_to_image_upscale_sampler_clip_16
type: Text To Image
frequency: 5
level: strong
coverage: 0.8626
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image 人像高清写实_2018929641737687042.json, 图片生成/文生图/Z-image 时尚模特_2021047910590320642.json, 图片生成/文生图/z-image-trubo_SD放大_2085217239367770114.json, 图片生成/文生图/zit高清_2094297752653094913.json, 图片生成/文生图/▶Z-image高清文生图流_2069006220459069441.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_16

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-image 人像高清写实_2018929641737687042.json、图片生成/文生图/Z-image 时尚模特_2021047910590320642.json、图片生成/文生图/z-image-trubo_SD放大_2085217239367770114.json、图片生成/文生图/zit高清_2094297752653094913.json、图片生成/文生图/▶Z-image高清文生图流_2069006220459069441.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 4/5 个有
- `LayerUtility: PurgeVRAM V2` —— 4/5 个有
- `Seed (rgthree)` —— 4/5 个有
- `ImageSmartSharpen+` —— 3/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `Lora Loader Stack (rgthree)` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `ResolutionSelector` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 5 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 800 | 720 - 1080 | 5 | 85% |
| 高度 | 1200 | 1024 - 1920 | 5 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，5 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 800，观测区间 720 - 1080，5 个样本，取值集中（一致性 85%）
- 高度 中位数 1200，观测区间 1024 - 1920，5 个样本
