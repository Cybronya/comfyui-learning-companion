---
name: text_to_image_upscale_lora_sampler_54
type: Text To Image
frequency: 5
level: strong
coverage: 0.887
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, ImpactImageBatchToImageList, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein 9b渲染级精修｜图生图高清放大_2090097677299175425.json, 图片生成/图生图/Klein服装3D精修｜精修图生图一键出图_2092936140880965634.json, 图片生成/图生图/Klein珠宝首饰渲染级精修_AI高清产品图增强工作流_2085625356773580801.json, 图片生成/图生图/Klein珠宝首饰渲染级精修_AI高清产品图增强工作流_2085639604258037761.json, 图片生成/图生图/自适应纠正透视溶图｜klein场景图生图处理_2092941702922334210.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_54

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Klein 9b渲染级精修｜图生图高清放大_2090097677299175425.json、图片生成/图生图/Klein服装3D精修｜精修图生图一键出图_2092936140880965634.json、图片生成/图生图/Klein珠宝首饰渲染级精修_AI高清产品图增强工作流_2085625356773580801.json、图片生成/图生图/Klein珠宝首饰渲染级精修_AI高清产品图增强工作流_2085639604258037761.json、图片生成/图生图/自适应纠正透视溶图｜klein场景图生图处理_2092941702922334210.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
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
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 4/5 个有
- `FluxGuidance` —— 4/5 个有
- `GetImageSize+` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `CFGGuider` —— 3/5 个有
- `Flux2Scheduler` —— 3/5 个有
- `GrowMaskWithBlur` —— 3/5 个有
- `KSamplerSelect` —— 3/5 个有
- `LayerUtility: ImageMaskScaleAs` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `MaskToImage` —— 3/5 个有
- `Mix Images By Mask` —— 3/5 个有
- `RandomNoise` —— 3/5 个有
- `ReferenceLatent` —— 3/5 个有
- `SamplerCustomAdvanced` —— 3/5 个有
- `easy imageColorMatch` —— 3/5 个有
- `孤海注释` —— 3/5 个有
- `ConstrainImage|pysssss` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `Fast Groups Muter (rgthree)` —— 2/5 个有
- `ImageLoader` —— 2/5 个有
- `Int` —— 2/5 个有
- `PainterFluxImageEdit` —— 2/5 个有
- `PixaromaLabel` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `CR Text Input Switch (4 way)` —— 1/5 个有
- `EmptyFlux2LatentImage` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `SeedVR2LoadDiTModel` —— 1/5 个有
- `SeedVR2LoadVAEModel` —— 1/5 个有
- `SeedVR2VideoUpscaler` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（12/5 个样本）：Steps较低可能导致细节不足
