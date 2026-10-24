---
name: text_to_image_upscale_lora_sampler_120
type: Text To Image
frequency: 2
level: weak
coverage: 0.749
common_nodes: [CLIPLoader, CLIPLoaderGGUF, CLIPTextEncode, CR Prompt List, CR Prompt Text, CR Text, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, Fast Bypasser (rgthree), Fast Groups Bypasser (rgthree), Flux2KleinEditTextEncode_EditUtils, GetNode, INTConstant, Image Comparer (rgthree), ImageFromBatch, ImageScaleToTotalPixels, KSampler, KSamplerAdvanced, LayerColor: BrightnessContrastV2, LayerFilter: AddGrain, LayerFilter: GaussianBlurV2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LayerUtility: NumberCalculator, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingAuraFlow, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TTResolutionSelector, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/多功能图像生成工作流 全能图像编辑方案一键搞定_2109068594117169154.json, 图片生成/图生图/青沫-多功能图像生成（自用）_2079086291660136450.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_120

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/多功能图像生成工作流 全能图像编辑方案一键搞定_2109068594117169154.json、图片生成/图生图/青沫-多功能图像生成（自用）_2079086291660136450.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPLoaderGGUF`
- `CLIPTextEncode`
- `CR Prompt List`
- `CR Prompt Text`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Flux2KleinEditTextEncode_EditUtils`
- `GetNode`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageFromBatch`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerAdvanced`
- `LayerColor: BrightnessContrastV2`
- `LayerFilter: AddGrain`
- `LayerFilter: GaussianBlurV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore V2`
- `LayerUtility: NumberCalculator`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TTResolutionSelector`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 2.5 | - | 2 | 40% |
| Prompt 约束强度(CFG) | 2.75 | - | 2 | 36% |
| 采样算法 | er_sde | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 552 | - | 2 | 14% |
| 高度 | 808 | - | 2 | 10% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 2.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 552，样本不足，未给区间，2 个样本，取值分散，一致性仅 14%
- 高度 中位数 808，样本不足，未给区间，2 个样本，取值分散，一致性仅 10%
- 高发问题（9/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
