---
name: text_to_image_lora_sampler_clip_591
type: Text To Image
frequency: 3
level: strong
coverage: 0.451
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ColorMatchV2, ComfyNumberConvert, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, KSamplerAdvanced, LoraLoaderModelOnly, MuyeTextEditOutput, ReferenceLatent, ResolutionSelector, SaveImage, Seed (rgthree), UNETLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/巨型建筑 _ 巨型怪物（Krea2 + Flux.2 Klein 三采样）_2075937547938779137.json, 平台全量/巨型建筑_巨型怪物Krea2_+_Flux.2_Klein_三采样_2076852622845374465.json, 平台全量/巨型建筑_巨型怪物Krea2_+_Flux.2_Klein_三采样_2076854581786660866.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_591

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/巨型建筑 _ 巨型怪物（Krea2 + Flux.2 Klein 三采样）_2075937547938779137.json、平台全量/巨型建筑_巨型怪物Krea2_+_Flux.2_Klein_三采样_2076852622845374465.json、平台全量/巨型建筑_巨型怪物Krea2_+_Flux.2_Klein_三采样_2076854581786660866.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：45%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ColorMatchV2`
- `ComfyNumberConvert`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `MuyeTextEditOutput`
- `ReferenceLatent`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy int`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
