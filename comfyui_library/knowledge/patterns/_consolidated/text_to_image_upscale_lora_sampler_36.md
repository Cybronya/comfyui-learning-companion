---
name: text_to_image_upscale_lora_sampler_36
type: Text To Image
frequency: 3
level: strong
coverage: 0.656333
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CR Text, ConditioningAverage, ConditioningZeroOut, Constant Number, DownloadAndLoadFlorence2Model, EmptyLatentImage, Florence2Run, GetNode, Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, ImpactInt, KSampler, Latent Noise Injection, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Seed (rgthree), SetNode, TTP_CoordinateSplitter, TTP_Image_Tile_Batch, TTP_Tile_image_size, TTP_condsetarea_merge, TTP_condtobatch, TextEncodeQwenImageEditPlus, UNETLoader, UnetLoaderGGUF, Upscale Model Loader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy imageBatchToImageList, easy imageColorMatch, easy imageInsetCrop]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/251225001.011.Z-image超级细节极致放大文生图_2004241630595084289.json, 图片生成/文生图/LH-DMT版本-2.生图片类-036.Z-image超级细节极致放大文生图_2016519472814755841.json, 图片生成/文生图/🤖Z-image超级细节极致放大 适合细节控【文生图】_2000425123586994178.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_36

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/251225001.011.Z-image超级细节极致放大文生图_2004241630595084289.json、图片生成/文生图/LH-DMT版本-2.生图片类-036.Z-image超级细节极致放大文生图_2016519472814755841.json、图片生成/文生图/🤖Z-image超级细节极致放大 适合细节控【文生图】_2000425123586994178.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningAverage`
- `ConditioningZeroOut`
- `Constant Number`
- `DownloadAndLoadFlorence2Model`
- `EmptyLatentImage`
- `Florence2Run`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImpactInt`
- `KSampler`
- `Latent Noise Injection`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `TTP_CoordinateSplitter`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TTP_condsetarea_merge`
- `TTP_condtobatch`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `UnetLoaderGGUF`
- `Upscale Model Loader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageInsetCrop`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 2/3 个有
- `Note Plus (mtb)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 720 | 3 | 100% |
| 高度 | 1280 | 1280 - 1280 | 3 | 100% |
| 采样步数 | 5 | 5 - 5 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | kl_optimal | - | 3 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 0.3 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 720，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 kl_optimal，3 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.3，3 个样本，取值集中（一致性 100%）
- 高发问题（9/3 个样本）：Steps较低可能导致细节不足
