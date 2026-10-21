---
name: text_to_image_lora_sampler_clip_284
type: Text To Image
frequency: 3
level: strong
coverage: 0.744333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, GetNode, Image Comparer (rgthree), ImageScaleToTotalPixels, JjkText, KSampler, KSamplerSelect, Load Lora, LoadImage, LoraLoaderModelOnly, MultiTextConcatenate, PainterFluxImageEdit, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: [忽略多组孤海, CR Prompt Text, Load Lora]
members: [图片生成/图生图/2093626238224134145.json, 图片生成/文生图/trueV2升级版｜Flux2Klein老照片修复文生图洗图编辑_2093787210565902338.json, 图片生成/文生图/老照片修复洗图编辑｜Flux2Klein trueV2升级版多合一_2093453609873797121.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_284

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2093626238224134145.json、图片生成/文生图/trueV2升级版｜Flux2Klein老照片修复文生图洗图编辑_2093787210565902338.json、图片生成/文生图/老照片修复洗图编辑｜Flux2Klein trueV2升级版多合一_2093453609873797121.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `Load Lora`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MultiTextConcatenate`
- `PainterFluxImageEdit`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 2/3 个有
- `忽略多组孤海` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：忽略多组孤海、CR Prompt Text、Load Lora
