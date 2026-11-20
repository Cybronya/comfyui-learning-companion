---
name: image_to_image_upscale_lora_sampler_37
type: Image To Image
frequency: 5
level: moderate
coverage: 0.9238
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ConstrainImage|pysssss, Flux2Scheduler, Image Comparer (rgthree), ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, ImpactImageBatchToImageList, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein_服装3D精修_2087367024208080897.json, 图片生成/图生图/Klein_极致肤质人像一致性精修_2087367800963813378.json, 图片生成/图生图/klein_自适应纠正场景透视溶图_2087903504638758913.json, 图片生成/图生图/测试自用_2064958565051359234.json, 平台全量/klein _ 自适应纠正场景透视溶图_2028661072953085954.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_37

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Klein_服装3D精修_2087367024208080897.json、图片生成/图生图/Klein_极致肤质人像一致性精修_2087367800963813378.json、图片生成/图生图/klein_自适应纠正场景透视溶图_2087903504638758913.json、图片生成/图生图/测试自用_2064958565051359234.json、平台全量/klein _ 自适应纠正场景透视溶图_2028661072953085954.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `GetImageSize+` —— 4/5 个有
- `Int` —— 4/5 个有
- `DualCLIPLoader` —— 3/5 个有
- `FluxGuidance` —— 3/5 个有
- `PreviewImage` —— 2/5 个有
- `SeedVR2LoadDiTModel` —— 2/5 个有
- `SeedVR2LoadVAEModel` —— 2/5 个有
- `SeedVR2VideoUpscaler` —— 2/5 个有
- `CR Draw Shape` —— 1/5 个有
- `EmptyFlux2LatentImage` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `GetImageSizeAndCount` —— 1/5 个有
- `Image Crop Location` —— 1/5 个有
- `ImageCompositeMasked` —— 1/5 个有
- `LayerMask: BiRefNetUltraV2` —— 1/5 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/5 个有
- `Mask Crop Region` —— 1/5 个有
- `MaskPreview+` —— 1/5 个有
- `SplitImageWithAlpha` —— 1/5 个有
- `TTP_Expand_And_Mask` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | kl_optimal | - | 5 | 60% |
| 重绘幅度 | 0.4 | 0.08 - 0.4 | 5 | 42% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 kl_optimal，5 个样本，一致性 60%
- 重绘幅度 中位数 0.4，观测区间 0.08 - 0.4，5 个样本，取值分散，一致性仅 42%
- 风险：重绘幅度 观测到 0.08，低于常用下限 0.1（）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
