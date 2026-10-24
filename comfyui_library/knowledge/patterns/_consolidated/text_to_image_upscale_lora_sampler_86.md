---
name: text_to_image_upscale_lora_sampler_86
type: Text To Image
frequency: 3
level: strong
coverage: 0.645333
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, ColorConverterGuhai, ColorCorrect, ConditioningZeroOut, EditTextEncode_EditUtils, EmptyLatentImage, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, GetImageSize+, GetNode, GoohaiUniversalSlider, GuHai_IDPhotoCrop, IDPhotoClothingSelector_孤海, Image Comparer (rgthree), ImageBlur, ImageComposite+, ImageResize+, ImageScaleBy, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RMBG, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, SingleImageLayoutNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text Concatenate, TextEncodeQwenImageEditPlus, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, easy imageColorMatch, easy seed, easy showAnything, solarL_SaveImagesToZip, 图像缩放V2_孤海, 孤海-取色器, 孤海-自定义颜色, 孤海注释, 布尔孤海, 忽略多组孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键证件照V2 侧脸转正换服装换背景高清排版_2094249465506000897.json, 图片生成/文生图/DRZY侧脸转正高清处理｜1.0.2图生图人像修复生成_2097092787421409281.json, 图片生成/文生图/DRZY侧脸转正高清版｜一张侧脸照秒变正脸大片_2097141464013824001.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_86

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/一键证件照V2 侧脸转正换服装换背景高清排版_2094249465506000897.json、图片生成/文生图/DRZY侧脸转正高清处理｜1.0.2图生图人像修复生成_2097092787421409281.json、图片生成/文生图/DRZY侧脸转正高清版｜一张侧脸照秒变正脸大片_2097141464013824001.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorConverterGuhai`
- `ColorCorrect`
- `ConditioningZeroOut`
- `EditTextEncode_EditUtils`
- `EmptyLatentImage`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `GetImageSize+`
- `GetNode`
- `GoohaiUniversalSlider`
- `GuHai_IDPhotoCrop`
- `IDPhotoClothingSelector_孤海`
- `Image Comparer (rgthree)`
- `ImageBlur`
- `ImageComposite+`
- `ImageResize+`
- `ImageScaleBy`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RMBG`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SingleImageLayoutNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text Concatenate`
- `TextEncodeQwenImageEditPlus`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`
- `easy imageColorMatch`
- `easy seed`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `图像缩放V2_孤海`
- `孤海-取色器`
- `孤海-自定义颜色`
- `孤海注释`
- `布尔孤海`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 2/3 个有
- `Flux2Scheduler` —— 2/3 个有
- `GrowMaskWithBlur` —— 2/3 个有
- `ImageSaveNode_孤海` —— 2/3 个有
- `KSamplerSelect` —— 2/3 个有
- `QwenEditConfigPreparer` —— 2/3 个有
- `RandomNoise` —— 2/3 个有
- `RemoveBackgroundWithMask` —— 2/3 个有
- `SAM3Segment` —— 2/3 个有
- `SamplerCustomAdvanced` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 2/3 个有
- `easy imageRemBg` —— 2/3 个有
- `ImageCASharpening+` —— 1/3 个有
- `孤海-图像添加水印` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（11/3 个样本）：Steps较低可能导致细节不足
