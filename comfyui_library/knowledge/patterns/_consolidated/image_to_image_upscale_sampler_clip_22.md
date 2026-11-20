---
name: image_to_image_upscale_sampler_clip_22
type: Image To Image
frequency: 7
level: strong
coverage: 0.800429
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), KSampler, LoadImage, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/工作流基础系列20-Flux.1文生图_图生图_局部重绘工作流_2047848807601278978.json, 平台全量/去水印工作流_2091053661416935426.json, 平台全量/去除边角水印去除、瑕疵修复、细节重绘、高清超放大一站式处理。_2092519700860334082.json, 平台全量/去除边角水印去除、瑕疵修复、细节重绘、高清超放大一站式处理。_2096788232104136706.json, 平台全量/去除边角水印去除、瑕疵修复、细节重绘、高清超放大一站式处理。_2097131065843474434.json, 平台全量/图像高清kontext_1950481200957870082.json, 平台全量/图片快速去水印、高清放大工作流_2085552886314004482.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/工作流基础系列20-Flux.1文生图_图生图_局部重绘工作流_2047848807601278978.json、平台全量/去水印工作流_2091053661416935426.json、平台全量/去除边角水印去除、瑕疵修复、细节重绘、高清超放大一站式处理。_2092519700860334082.json、平台全量/去除边角水印去除、瑕疵修复、细节重绘、高清超放大一站式处理。_2096788232104136706.json、平台全量/去除边角水印去除、瑕疵修复、细节重绘、高清超放大一站式处理。_2097131065843474434.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 6/7 个有
- `ImageUpscaleWithModel` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `ReferenceLatent` —— 6/7 个有
- `EmptySD3LatentImage` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有
- `SetLatentNoiseMask` —— 1/7 个有
- `UltimateSDUpscale` —— 1/7 个有
- `scale` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
