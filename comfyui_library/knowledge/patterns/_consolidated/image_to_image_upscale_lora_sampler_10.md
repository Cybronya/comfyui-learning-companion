---
name: image_to_image_upscale_lora_sampler_10
type: Image To Image
frequency: 17
level: strong
coverage: 0.591294
common_nodes: [Any Switch (rgthree), CLIPLoader, ColorConverterGuhai, ConditioningZeroOut, GetImageSize+, GetNode, GoohaiUniversalSlider, GuHai_IDPhotoCrop, IDPhotoClothingSelector_孤海, Image Comparer (rgthree), ImageComposite+, ImageResize+, ImageScaleBy, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RMBG, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text Concatenate, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, easy seed, 孤海-取色器, 孤海-自定义颜色, 布尔孤海, 忽略多组孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F.2Klein9B一键证件照侧脸转正换服装换背景高清排版_2065959891482800130.json, 图片生成/图生图/F.2Klein9B高清证件照换服装可选服装发型_2066644516085526530.json, 图片生成/图生图/一键证件照 侧脸转正 换服装 换背景_2068971920250462209.json, 图片生成/图生图/一键证件照 侧脸转正 换服装 换背景_2068974225230229506.json, 图片生成/图生图/一键证件照V2 _ 侧脸转正 _ 换服装 _ 换背景 _ 高清 _ 排版_2066008119477624834.json, 图片生成/图生图/一键证件照V2 _ 侧脸转正 _ 换服装 _ 换背景 _ 高清 _ 排版_2086068191733833729.json, 图片生成/图生图/一键证件照V2 _ 侧脸转正 _ 换服装 _ 换背景 _ 高清 _ 排版_2093895977299173377.json, 图片生成/图生图/端容正影一键证件照V2 _ 侧脸转正 _ 换服装 _ 换背景 _ 高清 _ 排版_2087796823166644226.json, 图片生成/图生图/老孙AI 一键证件照 _ 侧脸转正 _ 换服装 _ 换背景 _ 高清 _ 排版_2087376995108876289.json, 图片生成/文生图/一键证件照V2 _ 侧脸转正 _ 换服装 _ 换背景 _ 高清 _ 排版_2084721379785662466.json, 图片生成/文生图/一键转正_2087118370360614914.json, 图片生成/文生图/自用版  ai 蛮子 一键证件照工作流V1.0_2080866662601023489.json, 平台全量/一键证件照V2 _ 侧脸转正 _ 换服装 _ 换背景 _ 高清 _ 排版_2030897076795609089.json, 平台全量/一键证件照V2 _ 侧脸转正 _ 换服装 _ 换背景 _ 高清 _ 排版_2077047800021471234.json, 平台全量/一键证件照V20060606_2057623131275218945.json, 数字人/数字人/一键证件照  自选服饰 发型 背景_2108399463449583618.json, 数字人/数字人/一键证件照生成(侧脸转正换服装换背景换发型高清自动排版）_2095041911152275457.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/F.2Klein9B一键证件照侧脸转正换服装换背景高清排版_2065959891482800130.json、图片生成/图生图/F.2Klein9B高清证件照换服装可选服装发型_2066644516085526530.json、图片生成/图生图/一键证件照 侧脸转正 换服装 换背景_2068971920250462209.json、图片生成/图生图/一键证件照 侧脸转正 换服装 换背景_2068974225230229506.json、图片生成/图生图/一键证件照V2 _ 侧脸转正 _ 换服装 _ 换背景 _ 高清 _ 排版_2066008119477624834.json…）

- **类型**：Image To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 17 个 workflow 都包含：
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
- `CLIPTextEncode` —— 16/17 个有
- `ColorCorrect` —— 16/17 个有
- `EditTextEncode_EditUtils` —— 16/17 个有
- `Flux2KleinConfigPreparer_EditUtils` —— 16/17 个有
- `Flux2KleinModelConfig_EditUtils` —— 16/17 个有
- `ImageBlur` —— 16/17 个有
- `ImageCASharpening+` —— 16/17 个有
- `ReferenceLatent` —— 16/17 个有
- `TextInput_` —— 16/17 个有
- `easy imageColorMatch` —— 16/17 个有
- `图像缩放V2_孤海` —— 16/17 个有
- `SingleImageLayoutNode` —— 15/17 个有
- `easy showAnything` —— 15/17 个有
- `孤海-图像添加水印` —— 14/17 个有
- `孤海注释` —— 9/17 个有
- `CR String To Combo` —— 2/17 个有
- `ImageSaveNode_孤海` —— 2/17 个有
- `GoohaiAnySwitch` —— 1/17 个有
- `GrowMaskWithBlur` —— 1/17 个有
- `PrimitiveStringMultiline` —— 1/17 个有
- `QwenEditConfigPreparer` —— 1/17 个有
- `RemoveBackgroundWithMask` —— 1/17 个有
- `SAM3Segment` —— 1/17 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 1/17 个有
- `VRAM_Debug` —— 1/17 个有
- `easy imageRemBg` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 17 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 17 | 100% |
| 采样算法 | euler_ancestral | - | 17 | 88% |
| 调度器 | simple | - | 17 | 94% |
| 重绘幅度 | 0.86 | 0.8 - 1 | 17 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 34/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，17 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，17 个样本，一致性 88%
- 调度器 最常用 simple，17 个样本，一致性 94%
- 重绘幅度 中位数 0.86，观测区间 0.8 - 1，17 个样本，取值集中（一致性 96%）
- 高发问题（34/17 个样本）：Steps较低可能导致细节不足
