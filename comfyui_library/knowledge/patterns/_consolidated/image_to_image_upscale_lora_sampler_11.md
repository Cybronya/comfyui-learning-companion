---
name: image_to_image_upscale_lora_sampler_11
type: Image To Image
frequency: 17
level: moderate
coverage: 0.793235
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetImageSize+, Image Comparer (rgthree), ImageCASharpening+, ImageResize+, ImageScaleBy, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, PrimitiveFloat, RH_Captioner, RunningHub Deepcleaner, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/⭐️⭐️⭐️⭐️⭐️换装神器——Klein 9B+Z image+SeedVR2修复_2019578876753616897.json, 图片生成/图生图/动漫短剧动漫人物图片高清放大工作流（Flux2-Klein高清放大8K）更像更好_2013564631800877057.json, 图片生成/图生图/多重放大工作流，配置最新的模型v2.0_2094267872523677698.json, 图片生成/图生图/多重放大工作流，配置最新的模型v2.0_2096809518779953153.json, 图片生成/图生图/多重放大工作流，配置最新的模型v2.0_2097154271379808258.json, 图片生成/图生图/高清放大Flux2-Klein_2021925905211334657.json, 平台全量/Flux2-Klein 修复 + Z-Image 洗图 + TTP分块放大到8K 强强联合_2044581536804114433.json, 平台全量/Flux2-Klein高清放大到8K-更强_2039589312219582466.json, 平台全量/Flux2-Klein高清放大到8K_2013589860396834818.json, 平台全量/Flux2-Klein高清放大到8K_2075254688865406978.json, 平台全量/Flux2-Klein高清放大到8K_2075255266349768706.json, 平台全量/Flux放大自用_2014570556498120706.json, 平台全量/Klein高清放大+seedvr2放大_2013590133685100546.json, 平台全量/多重放大工作流，配置最新的模型_2030901459339972609.json, 平台全量/提高图片清晰度_2032727488664707074.json, 数字人/数字人/强强联合 Flux2-Klein 修复 + Z-Image 洗图 + TTP分块放大到8K_2043517178133090306.json, 数字人/数字人/提高图片清晰度-阿浩_2026865402130731010.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/⭐️⭐️⭐️⭐️⭐️换装神器——Klein 9B+Z image+SeedVR2修复_2019578876753616897.json、图片生成/图生图/动漫短剧动漫人物图片高清放大工作流（Flux2-Klein高清放大8K）更像更好_2013564631800877057.json、图片生成/图生图/多重放大工作流，配置最新的模型v2.0_2094267872523677698.json、图片生成/图生图/多重放大工作流，配置最新的模型v2.0_2096809518779953153.json、图片生成/图生图/多重放大工作流，配置最新的模型v2.0_2097154271379808258.json…）

- **类型**：Image To Image
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 17 个 workflow 都包含：
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
- `LatentUpscaleBy` —— 16/17 个有
- `LayerUtility: ImageMaskScaleAs` —— 16/17 个有
- `LayerUtility: ImageReel` —— 16/17 个有
- `LayerUtility: ImageReelComposit` —— 16/17 个有
- `ReferenceLatent` —— 16/17 个有
- `Fast Groups Bypasser (rgthree)` —— 3/17 个有
- `Label (rgthree)` —— 2/17 个有
- `Anything Everywhere3` —— 1/17 个有
- `CropWithPadInfo_EditUtils` —— 1/17 个有
- `EditTextEncode_EditUtils` —— 1/17 个有
- `Flux2KleinConfigPreparer_EditUtils` —— 1/17 个有
- `Flux2KleinModelConfig_EditUtils` —— 1/17 个有
- `Flux2KleinOutputExtractor_EditUtils` —— 1/17 个有
- `Image Resize` —— 1/17 个有
- `LoadImageListFromDir //Inspire` —— 1/17 个有
- `PrimitiveStringMultiline` —— 1/17 个有
- `RepeatLatentBatch` —— 1/17 个有
- `WujiCleaner` —— 1/17 个有
- `easy int` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 17 | 59% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 17 | 40% |
| 采样算法 | 1 | 1 - 1 | 11 | 100% |
| 调度器 | euler | - | 17 | 65% |
| 重绘幅度 | beta57 | - | 17 | 59% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，17 个样本，一致性 59%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，17 个样本，取值分散，一致性仅 40%
- 采样算法 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，17 个样本，一致性 65%
- 重绘幅度 最常用 beta57，17 个样本，一致性 59%
- 高发问题（19/17 个样本）：Steps较低可能导致细节不足
