---
name: text_to_image_upscale_sampler_clip_13
type: Text To Image
frequency: 8
level: strong
coverage: 0.893875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image 人像高清写实_2018929641737687042.json, 图片生成/文生图/Z-image 时尚模特_2021047910590320642.json, 图片生成/文生图/Z-image电商高清生图_2051295739858440194.json, 图片生成/文生图/Z-image高清生图流_2035973546807136257.json, 图片生成/文生图/z-image-trubo_SD放大_2085217239367770114.json, 图片生成/文生图/zit高清_2094297752653094913.json, 图片生成/文生图/▶Z-image高清文生图流_2069006220459069441.json, 图片生成/文生图/▶Z-image高清生图_2037490216558141442.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Z-image 人像高清写实_2018929641737687042.json、图片生成/文生图/Z-image 时尚模特_2021047910590320642.json、图片生成/文生图/Z-image电商高清生图_2051295739858440194.json、图片生成/文生图/Z-image高清生图流_2035973546807136257.json、图片生成/文生图/z-image-trubo_SD放大_2085217239367770114.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
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
- `GetImageSize+` —— 7/8 个有
- `LayerUtility: PurgeVRAM V2` —— 7/8 个有
- `Seed (rgthree)` —— 7/8 个有
- `ImageSmartSharpen+` —— 6/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `Lora Loader Stack (rgthree)` —— 1/8 个有
- `ResolutionSelector` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 8 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 784 | 720 - 1280 | 8 | 78% |
| 高度 | 1240 | 720 - 1920 | 8 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，8 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 784，观测区间 720 - 1280，8 个样本
- 高度 中位数 1240，观测区间 720 - 1920，8 个样本
