---
name: text_to_image_upscale_lora_sampler_54
type: Text To Image
frequency: 2
level: weak
coverage: 0.642
common_nodes: [Any Switch (rgthree), CFGGuider, CLIPLoader, CLIPTextEncode, ColorConverterGuhai, ColorCorrect, ConditioningZeroOut, EditTextEncode_EditUtils, EmptyLatentImage, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2Scheduler, GetImageSize+, GetNode, GoohaiUniversalSlider, GrowMaskWithBlur, GuHai_IDPhotoCrop, IDPhotoClothingSelector_孤海, Image Comparer (rgthree), ImageBlur, ImageComposite+, ImageResize+, ImageSaveNode_孤海, ImageScaleBy, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, QwenEditConfigPreparer, RMBG, RandomNoise, ReferenceLatent, RemoveBackgroundWithMask, SAM3Segment, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, SimpleMath+, SingleImageLayoutNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text Concatenate, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlusCustom_lrzjason, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, easy imageColorMatch, easy imageRemBg, easy seed, easy showAnything, solarL_SaveImagesToZip, 图像缩放V2_孤海, 孤海-取色器, 孤海-自定义颜色, 孤海注释, 布尔孤海, 忽略多组孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/DRZY侧脸转正高清处理｜1.0.2图生图人像修复生成_2097092787421409281.json, 图片生成/文生图/DRZY侧脸转正高清版｜一张侧脸照秒变正脸大片_2097141464013824001.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_54

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/DRZY侧脸转正高清处理｜1.0.2图生图人像修复生成_2097092787421409281.json、图片生成/文生图/DRZY侧脸转正高清版｜一张侧脸照秒变正脸大片_2097141464013824001.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorConverterGuhai`
- `ColorCorrect`
- `ConditioningZeroOut`
- `EditTextEncode_EditUtils`
- `EmptyLatentImage`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2Scheduler`
- `GetImageSize+`
- `GetNode`
- `GoohaiUniversalSlider`
- `GrowMaskWithBlur`
- `GuHai_IDPhotoCrop`
- `IDPhotoClothingSelector_孤海`
- `Image Comparer (rgthree)`
- `ImageBlur`
- `ImageComposite+`
- `ImageResize+`
- `ImageSaveNode_孤海`
- `ImageScaleBy`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenEditConfigPreparer`
- `RMBG`
- `RandomNoise`
- `ReferenceLatent`
- `RemoveBackgroundWithMask`
- `SAM3Segment`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SimpleMath+`
- `SingleImageLayoutNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text Concatenate`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`
- `easy imageColorMatch`
- `easy imageRemBg`
- `easy seed`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `图像缩放V2_孤海`
- `孤海-取色器`
- `孤海-自定义颜色`
- `孤海注释`
- `布尔孤海`
- `忽略多组孤海`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（8/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
