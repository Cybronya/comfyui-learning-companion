---
name: image_to_image_upscale_lora_sampler_97
type: Image To Image
frequency: 2
level: weak
coverage: 0.719
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPLoader_Any, CLIPTextEncode, CR Text Concatenate, ColorCorrect, ConstrainImage|pysssss, EditTextEncode_EditUtils, Fast Groups Bypasser (rgthree), Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Get Image Size, GetImageSize+, GetNode, Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageScaleToTotalPixels, ImageScaleToTotalPixelsX, ImageUpscaleWithModel, Int Literal, KSampler, KSamplerAdvanced, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, PrimitiveInt, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SaveImageJPG_GH, SeedVR2, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, StringConstant, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextInput_, UNETLoader, UNETLoader_Any, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, VAELoader_Any, easy boolean, easy cleanGpuUsed, easy ifElse, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy imageScaleToNormPixels, easy imageSize, easy showAnything, 取色器_孤海, 图像缩放V2_孤海, 数学运算_孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/SeedVR2.5_+_TTP_分块放大_2115617911112032258.json, 图片生成/图生图/SeedVR2.5_+_TTP_分块放大_2115665854103908354.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_97

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/SeedVR2.5_+_TTP_分块放大_2115617911112032258.json、图片生成/图生图/SeedVR2.5_+_TTP_分块放大_2115665854103908354.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPLoader_Any`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ColorCorrect`
- `ConstrainImage|pysssss`
- `EditTextEncode_EditUtils`
- `Fast Groups Bypasser (rgthree)`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Get Image Size`
- `GetImageSize+`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixelsX`
- `ImageUpscaleWithModel`
- `Int Literal`
- `KSampler`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveInt`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SaveImageJPG_GH`
- `SeedVR2`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `StringConstant`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextInput_`
- `UNETLoader`
- `UNETLoader_Any`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VAELoader_Any`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `easy imageScaleToNormPixels`
- `easy imageSize`
- `easy showAnything`
- `取色器_孤海`
- `图像缩放V2_孤海`
- `数学运算_孤海`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | beta57 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 beta57，2 个样本，一致性 100%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
