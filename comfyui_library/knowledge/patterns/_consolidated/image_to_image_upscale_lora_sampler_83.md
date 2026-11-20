---
name: image_to_image_upscale_lora_sampler_83
type: Image To Image
frequency: 3
level: strong
coverage: 0.947
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/wan2.2 文生图+放大合集_1975596827603021826.json, 平台全量/响响-TTP高清放大_2025897527521845250.json, 平台全量/响响的AIGC超真实放大_1997560880059596801.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_83

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/wan2.2 文生图+放大合集_1975596827603021826.json、平台全量/响响-TTP高清放大_2025897527521845250.json、平台全量/响响的AIGC超真实放大_1997560880059596801.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `PlaySound|pysssss` —— 2/3 个有
- `EmptyHunyuanLatentVideo` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `LoaderGGUF` —— 1/3 个有
- `SeedVR2BlockSwap` —— 1/3 个有
- `SeedVR2GGUF` —— 1/3 个有
- `Text` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.1 | 0.1 - 0.1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.1，观测区间 0.1 - 0.1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
