---
name: image_to_image_upscale_lora_sampler_2
type: Image To Image
frequency: 5
level: strong
coverage: 0.5748
common_nodes: [Any Switch (rgthree), CLIPLoader, ColorConverterGuhai, ConditioningZeroOut, GetImageSize+, GetNode, GoohaiUniversalSlider, GuHai_IDPhotoCrop, IDPhotoClothingSelector_孤海, Image Comparer (rgthree), ImageComposite+, ImageResize+, ImageScaleBy, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RMBG, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text Concatenate, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, easy seed, 孤海-取色器, 孤海-自定义颜色, 布尔孤海, 忽略多组孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/一键证件照V2 _ 侧脸转正 _ 换服装 _ 换背景 _ 高清 _ 排版_2084721379785662466.json, 图片生成/文生图/一键转正_2087118370360614914.json, 图片生成/文生图/自用版  ai 蛮子 一键证件照工作流V1.0_2080866662601023489.json, 数字人/数字人/一键证件照  自选服饰 发型 背景_2108399463449583618.json, 数字人/数字人/一键证件照生成(侧脸转正换服装换背景换发型高清自动排版）_2095041911152275457.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/一键证件照V2 _ 侧脸转正 _ 换服装 _ 换背景 _ 高清 _ 排版_2084721379785662466.json、图片生成/文生图/一键转正_2087118370360614914.json、图片生成/文生图/自用版  ai 蛮子 一键证件照工作流V1.0_2080866662601023489.json、数字人/数字人/一键证件照  自选服饰 发型 背景_2108399463449583618.json、数字人/数字人/一键证件照生成(侧脸转正换服装换背景换发型高清自动排版）_2095041911152275457.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：57%

## 共有节点

全部 5 个 workflow 都包含：
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
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`
- `easy seed`
- `孤海-取色器`
- `孤海-自定义颜色`
- `布尔孤海`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 4/5 个有
- `ColorCorrect` —— 4/5 个有
- `EditTextEncode_EditUtils` —— 4/5 个有
- `Flux2KleinConfigPreparer_EditUtils` —— 4/5 个有
- `Flux2KleinModelConfig_EditUtils` —— 4/5 个有
- `ImageBlur` —— 4/5 个有
- `ImageCASharpening+` —— 4/5 个有
- `ReferenceLatent` —— 4/5 个有
- `SingleImageLayoutNode` —— 4/5 个有
- `TextInput_` —— 4/5 个有
- `easy imageColorMatch` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `图像缩放V2_孤海` —— 4/5 个有
- `孤海-图像添加水印` —— 3/5 个有
- `孤海注释` —— 3/5 个有
- `CR String To Combo` —— 1/5 个有
- `GrowMaskWithBlur` —— 1/5 个有
- `ImageSaveNode_孤海` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `QwenEditConfigPreparer` —— 1/5 个有
- `RemoveBackgroundWithMask` —— 1/5 个有
- `SAM3Segment` —— 1/5 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 1/5 个有
- `VRAM_Debug` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 5 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler_ancestral | - | 5 | 60% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 0.86 | 0.8 - 1 | 5 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 0.86，观测区间 0.8 - 1，5 个样本，取值集中（一致性 92%）
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足
