---
name: text_to_image_upscale_lora_sampler_10
type: Text To Image
frequency: 4
level: strong
coverage: 0.88625
common_nodes: [AILab_QwenVL, BasicScheduler, CFGGuider, CLIPLoader, CLIPLoaderGGUF, CLIPTextEncode, CR Text, ConditioningZeroOut, DisableNoise, EditTextEncode_EditUtils, EmptyLatentImage, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, GetImageSize+, GoogleTranslateTextNode, Image Comparer (rgthree), Image Filter Adjustments, ImageCASharpening+, ImageListToImageBatch, ImageResize+, ImageScaleBy, ImageUpscaleWithModel, ImpactImageBatchToImageList, Int, JjkText, KSampler, KSamplerAdvanced, KSamplerSelect, LayerColor: Levels, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ModelSamplingSD3, PainterFluxImageEdit, PreviewImage, PrimitiveFloat, PrimitiveInt, QwenImageIntegratedKSampler, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, SimpleMath+, SplitSigmas, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy getNode, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy setNode, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/设计编辑工作流 图片设计修改优化一站搞定_2105143285072351234.json, 图片生成/反推提示词/通用设计编辑助理，文生图反推提示词图生图多合一工作流_2103193262772285441.json, 图片生成/文生图/全能设计编辑工作流｜文生图反推提示词图生图三合一_2103080101171785730.json, 图片生成/文生图/通用设计编辑助理，文生图反推提示词图生图多合一工作流_2103193262772285441.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/设计编辑工作流 图片设计修改优化一站搞定_2105143285072351234.json、图片生成/反推提示词/通用设计编辑助理，文生图反推提示词图生图多合一工作流_2103193262772285441.json、图片生成/文生图/全能设计编辑工作流｜文生图反推提示词图生图三合一_2103080101171785730.json、图片生成/文生图/通用设计编辑助理，文生图反推提示词图生图多合一工作流_2103193262772285441.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_QwenVL`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPLoaderGGUF`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DisableNoise`
- `EditTextEncode_EditUtils`
- `EmptyLatentImage`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `GetImageSize+`
- `GoogleTranslateTextNode`
- `Image Comparer (rgthree)`
- `Image Filter Adjustments`
- `ImageCASharpening+`
- `ImageListToImageBatch`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LayerColor: Levels`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ModelSamplingSD3`
- `PainterFluxImageEdit`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `QwenImageIntegratedKSampler`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `SimpleMath+`
- `SplitSigmas`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy getNode`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `easy setNode`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Set Value On Boolean` —— 1/4 个有
- `DetailDaemonSamplerNode` —— 1/4 个有
- `WanVideoNAG` —— 1/4 个有
- `XB_CanvasLabel` —— 1/4 个有
- `easy boolean` —— 1/4 个有
- `easy textSwitch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（16/4 个样本）：Steps较低可能导致细节不足
