---
name: image_to_image_upscale_lora_sampler_16
type: Image To Image
frequency: 2
level: weak
coverage: 0.6065
common_nodes: [Any Switch (rgthree), CLIPLoader, ColorConverterGuhai, ConditioningZeroOut, GetImageSize+, GetNode, GoohaiUniversalSlider, GuHai_IDPhotoCrop, IDPhotoClothingSelector_孤海, Image Comparer (rgthree), ImageCASharpening+, ImageComposite+, ImageResize+, ImageScaleBy, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RMBG, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text Concatenate, TextEncodeQwenImageEditPlus, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, easy seed, 孤海-取色器, 孤海-图像添加水印, 孤海-自定义颜色, 布尔孤海, 忽略多组孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/一键证件照  自选服饰 发型 背景_2108399463449583618.json, 数字人/数字人/一键证件照生成(侧脸转正换服装换背景换发型高清自动排版）_2095041911152275457.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_16

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/一键证件照  自选服饰 发型 背景_2108399463449583618.json、数字人/数字人/一键证件照生成(侧脸转正换服装换背景换发型高清自动排版）_2095041911152275457.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `ColorConverterGuhai`
- `ConditioningZeroOut`
- `GetImageSize+`
- `GetNode`
- `GoohaiUniversalSlider`
- `GuHai_IDPhotoCrop`
- `IDPhotoClothingSelector_孤海`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageComposite+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RMBG`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
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
- `easy seed`
- `孤海-取色器`
- `孤海-图像添加水印`
- `孤海-自定义颜色`
- `布尔孤海`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/2 个有
- `CR String To Combo` —— 1/2 个有
- `ColorCorrect` —— 1/2 个有
- `EditTextEncode_EditUtils` —— 1/2 个有
- `Flux2KleinConfigPreparer_EditUtils` —— 1/2 个有
- `Flux2KleinModelConfig_EditUtils` —— 1/2 个有
- `ImageBlur` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `SingleImageLayoutNode` —— 1/2 个有
- `easy imageColorMatch` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `图像缩放V2_孤海` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 0.93 | - | 2 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 0.93，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
