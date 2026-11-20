---
name: text_to_image_lora_sampler_clip_557
type: Text To Image
frequency: 3
level: moderate
coverage: 0.910667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Super Z-image 3.0+真实感Lora文生图批量跑 浮云2.9_2020686279058399234.json, 图片生成/文生图/【Supermate】z-image编辑工作流(Flux2 Klein版)_2013269468192968706.json, 图片生成/文生图/全新工作流！动漫生图+风格转绘二合一！_2058011143603576833.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_557

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Super Z-image 3.0+真实感Lora文生图批量跑 浮云2.9_2020686279058399234.json、图片生成/文生图/【Supermate】z-image编辑工作流(Flux2 Klein版)_2013269468192968706.json、图片生成/文生图/全新工作流！动漫生图+风格转绘二合一！_2058011143603576833.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `DrawMaskOnImage` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImagePadForOutpaint` —— 1/3 个有
- `ImageSharpen` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `JoinStringMulti` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `TTResolutionSelector` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 720 - 1344 | 3 | 76% |
| 高度 | 1280 | 768 - 1920 | 3 | 64% |
| 采样步数 | 30 | 15 - 40 | 3 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 3 | 19% |
| 采样算法 | euler | - | 3 | 33% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 720 - 1344，3 个样本
- 高度 中位数 1280，观测区间 768 - 1920，3 个样本
- 采样步数 中位数 30，观测区间 15 - 40，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，3 个样本，取值分散，一致性仅 19%
- 采样算法 最常用 euler，3 个样本，一致性 33%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
