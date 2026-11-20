---
name: image_to_image_upscale_lora_sampler_20
type: Image To Image
frequency: 8
level: moderate
coverage: 0.7915
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetImageSize+, Image Comparer (rgthree), ImageCASharpening+, ImageResize+, ImageScaleBy, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, PrimitiveFloat, RH_Captioner, RunningHub Deepcleaner, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/⭐️⭐️⭐️⭐️⭐️换装神器——Klein 9B+Z image+SeedVR2修复_2019578876753616897.json, 图片生成/图生图/动漫短剧动漫人物图片高清放大工作流（Flux2-Klein高清放大8K）更像更好_2013564631800877057.json, 图片生成/图生图/多重放大工作流，配置最新的模型v2.0_2094267872523677698.json, 图片生成/图生图/多重放大工作流，配置最新的模型v2.0_2096809518779953153.json, 图片生成/图生图/多重放大工作流，配置最新的模型v2.0_2097154271379808258.json, 图片生成/图生图/高清放大Flux2-Klein_2021925905211334657.json, 数字人/数字人/强强联合 Flux2-Klein 修复 + Z-Image 洗图 + TTP分块放大到8K_2043517178133090306.json, 数字人/数字人/提高图片清晰度-阿浩_2026865402130731010.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_20

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/⭐️⭐️⭐️⭐️⭐️换装神器——Klein 9B+Z image+SeedVR2修复_2019578876753616897.json、图片生成/图生图/动漫短剧动漫人物图片高清放大工作流（Flux2-Klein高清放大8K）更像更好_2013564631800877057.json、图片生成/图生图/多重放大工作流，配置最新的模型v2.0_2094267872523677698.json、图片生成/图生图/多重放大工作流，配置最新的模型v2.0_2096809518779953153.json、图片生成/图生图/多重放大工作流，配置最新的模型v2.0_2097154271379808258.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveFloat`
- `RH_Captioner`
- `RunningHub Deepcleaner`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LatentUpscaleBy` —— 7/8 个有
- `LayerUtility: ImageMaskScaleAs` —— 7/8 个有
- `LayerUtility: ImageReel` —— 7/8 个有
- `LayerUtility: ImageReelComposit` —— 7/8 个有
- `ReferenceLatent` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `Anything Everywhere3` —— 1/8 个有
- `CropWithPadInfo_EditUtils` —— 1/8 个有
- `EditTextEncode_EditUtils` —— 1/8 个有
- `Flux2KleinConfigPreparer_EditUtils` —— 1/8 个有
- `Flux2KleinModelConfig_EditUtils` —— 1/8 个有
- `Flux2KleinOutputExtractor_EditUtils` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `WujiCleaner` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 8 | 8 | 22% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | simple | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 8，8 个样本，取值分散，一致性仅 22%
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 simple，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（10/8 个样本）：Steps较低可能导致细节不足
