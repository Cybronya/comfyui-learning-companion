---
name: text_to_image_upscale_lora_sampler_26
type: Text To Image
frequency: 4
level: moderate
coverage: 0.76525
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, Fast Bypasser (rgthree), Fast Groups Bypasser (rgthree), Flux2KleinEditTextEncode_EditUtils, ImageFromBatch, KSampler, LayerColor: BrightnessContrastV2, LayerFilter: AddGrain, LayerFilter: GaussianBlurV2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LayerUtility: NumberCalculator, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingAuraFlow, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, Fast Bypasser (rgthree), Label (rgthree), LayerColor: BrightnessContrastV2, LayerFilter: AddGrain, LayerFilter: GaussianBlurV2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LayerUtility: NumberCalculator, MathExpression|pysssss, easy cleanGpuUsed, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, CR Prompt List, CR Prompt Text, easy imageSize]
members: [图片生成/图生图/2079086291660136450.json, 图片生成/文生图/Instagram休闲风格-运动达人_2083385582033657858.json, 图片生成/文生图/复古运动生活风场景图（Krea2）_2081554364421992450.json, 图片生成/文生图/棚拍风格-商业摄影（Krea2）_2081579433747636226.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_26

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2079086291660136450.json、图片生成/文生图/Instagram休闲风格-运动达人_2083385582033657858.json、图片生成/文生图/复古运动生活风场景图（Krea2）_2081554364421992450.json、图片生成/文生图/棚拍风格-商业摄影（Krea2）_2081579433747636226.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Flux2KleinEditTextEncode_EditUtils`
- `ImageFromBatch`
- `KSampler`
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
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `PreviewAny` —— 3/4 个有
- `ResolutionSelector` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `llama_cpp_instruct_adv` —— 3/4 个有
- `llama_cpp_model_loader` —— 3/4 个有
- `llama_cpp_parameters` —— 3/4 个有
- `Any Switch (rgthree)` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `CLIPLoaderGGUF` —— 1/4 个有
- `CR Prompt List` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `KSamplerAdvanced` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `TTResolutionSelector` —— 1/4 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4.5 | 1 - 8 | 4 | 22% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | res_2s | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1536 | 4 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4.5，观测区间 1 - 8，4 个样本，取值分散，一致性仅 22%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1536，4 个样本，取值集中（一致性 81%）
- 高发问题（13/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Fast Bypasser (rgthree)、Label (rgthree)、LayerColor: BrightnessContrastV2、LayerFilter: AddGrain
