---
name: image_to_image_lora_sampler_clip_159
type: Image To Image
frequency: 3
level: moderate
coverage: 0.972
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxKontextMultiReferenceLatentMethod, ImageScaleToTotalPixels, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/图片无损放大与文字清晰还原_2028741805247832066.json, 平台全量/超级放大 升级版，解决分块色差问题_2017914960130613249.json, 平台全量/超级放大！！！_1859768331329998849.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_159

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/图片无损放大与文字清晰还原_2028741805247832066.json、平台全量/超级放大 升级版，解决分块色差问题_2017914960130613249.json、平台全量/超级放大！！！_1859768331329998849.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 2/3 个有
- `AdaptiveTTPTilePlannerMinimal` —— 1/3 个有
- `BasicGuider` —— 1/3 个有
- `BasicScheduler` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Float` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `KSamplerSelect` —— 1/3 个有
- `PreviewImageHighPrec` —— 1/3 个有
- `RandomNoise` —— 1/3 个有
- `SamplerCustomAdvanced` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 20 | 3 | 49% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 20，3 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
