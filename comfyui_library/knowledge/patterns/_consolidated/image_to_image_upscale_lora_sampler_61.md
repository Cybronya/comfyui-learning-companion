---
name: image_to_image_upscale_lora_sampler_61
type: Image To Image
frequency: 3
level: strong
coverage: 0.894333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageScaleBy, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/去水印+高清放大 Watermark Removal High-Resolution Image E_2092788122122801153.json, 图片生成/图生图/室内-FLUX日景光影优化工作流_2044313078275248130.json, 图片生成/图生图/溶图_2004450924959596546.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_61

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/去水印+高清放大 Watermark Removal High-Resolution Image E_2092788122122801153.json、图片生成/图生图/室内-FLUX日景光影优化工作流_2044313078275248130.json、图片生成/图生图/溶图_2004450924959596546.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 2/3 个有
- `TTP_Image_Assy` —— 2/3 个有
- `TTP_Image_Tile_Batch` —— 2/3 个有
- `TTP_Tile_image_size` —— 2/3 个有
- `ConstrainImage|pysssss` —— 1/3 个有
- `DetailTransfer` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `FluxKontextImageScale` —— 1/3 个有
- `Get Image Size` —— 1/3 个有
- `GetImageSize+` —— 1/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 3 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
