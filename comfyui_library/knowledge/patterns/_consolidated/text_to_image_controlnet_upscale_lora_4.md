---
name: text_to_image_controlnet_upscale_lora_4
type: Text To Image
frequency: 4
level: strong
coverage: 0.7685
common_nodes: [CLIPLoader, CLIPTextEncode, CannyEdgePreprocessor, ClipLoaderGGUF, ConditioningZeroOut, Convert Masks to Images, DepthAnythingV2Preprocessor, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, GetImageSize+, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, Image Comparer (rgthree), ImageCompositeMasked, ImageResize+, ImageScaleBy, ImpactSwitch, KSampler, LayerMask: MaskStroke, LayerUtility: ColorImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaraScottIsEmptyOrNone_v1, ModelPatchLoader, PreviewImage, RMBG, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, ZImageFunControlnet, Zoe-DepthMapPreprocessor, easy cleanGpuUsed, easy ifElse, ttN concat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Background Replacement +Lighting_2049509168872165378.json, 图片生成/图生图/人像合成-换背景_打光_高清修复  全流程工作流_2034587450303057922.json, 图片生成/图生图/摄影打光写真合成-(电商_cos专用）专业级工作流_2030703990211612674.json, 平台全量/光影重塑  人像摄影写真 电商场景合成 融图合成溶图 cos 高清放大_2069287891917950978.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Background Replacement +Lighting_2049509168872165378.json、图片生成/图生图/人像合成-换背景_打光_高清修复  全流程工作流_2034587450303057922.json、图片生成/图生图/摄影打光写真合成-(电商_cos专用）专业级工作流_2030703990211612674.json、平台全量/光影重塑  人像摄影写真 电商场景合成 融图合成溶图 cos 高清放大_2069287891917950978.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CannyEdgePreprocessor`
- `ClipLoaderGGUF`
- `ConditioningZeroOut`
- `Convert Masks to Images`
- `DepthAnythingV2Preprocessor`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetImageSize+`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageResize+`
- `ImageScaleBy`
- `ImpactSwitch`
- `KSampler`
- `LayerMask: MaskStroke`
- `LayerUtility: ColorImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaraScottIsEmptyOrNone_v1`
- `ModelPatchLoader`
- `PreviewImage`
- `RMBG`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZImageFunControlnet`
- `Zoe-DepthMapPreprocessor`
- `easy cleanGpuUsed`
- `easy ifElse`
- `ttN concat`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 3/4 个有
- `PainterFluxImageEdit` —— 3/4 个有
- `workflow>提示词` —— 3/4 个有
- `easy imageConcat` —— 2/4 个有
- `AILab_QwenVL` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `GroundingDinoModelLoader (segment anything)` —— 1/4 个有
- `GroundingDinoSAMSegment (segment anything)` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `SAMLoader` —— 1/4 个有
- `easy positive` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1536 | 1536 - 1536 | 4 | 100% |
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
