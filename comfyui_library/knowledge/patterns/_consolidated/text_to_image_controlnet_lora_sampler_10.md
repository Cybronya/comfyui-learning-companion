---
name: text_to_image_controlnet_lora_sampler_10
type: Text To Image
frequency: 3
level: strong
coverage: 0.855333
common_nodes: [Bookmark (rgthree), CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, CropWithPadInfo_EditUtils, DWPreprocessor, DrawMaskOnImage, EmptyLatentImage, GetImageSize, GrowMaskWithBlur, Image Comparer (rgthree), ImageScaleBy, JjkText, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadRembgByBiRefNetModel, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, PrimitiveBoolean, PrimitiveStringMultiline, QwenEditOutputExtractor_EditUtils, QwenEditTextEncode_EditUtils, ReferenceLatent, RembgByBiRefNetAdvanced, SaveImage, SetUnionControlNetType, SolidMask, UNETLoader, VAEDecode, VAELoader, ZML_SelectTextV2, easy ifElse, easy isNone, easy sam3ImageSegmentation, easy sam3ModelLoader, llama_cpp_instruct_adv, llama_cpp_model_loader, mxSlider, solarL_SaveImagesToZip, ttN concat, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QE2511 人物换装终极版｜上传原图服装图直接跑｜图生图_2096860144335417345.json, 图片生成/图生图/QE2511人物换装终极版｜角色一致性图生图生成_2096670787649490946.json, 图片生成/图生图/人物换装终QE2511_极版ENG角色一致性图生图_2082024707943129090.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/QE2511 人物换装终极版｜上传原图服装图直接跑｜图生图_2096860144335417345.json、图片生成/图生图/QE2511人物换装终极版｜角色一致性图生图生成_2096670787649490946.json、图片生成/图生图/人物换装终QE2511_极版ENG角色一致性图生图_2082024707943129090.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `Bookmark (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `CropWithPadInfo_EditUtils`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `EmptyLatentImage`
- `GetImageSize`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadRembgByBiRefNetModel`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `QwenEditOutputExtractor_EditUtils`
- `QwenEditTextEncode_EditUtils`
- `ReferenceLatent`
- `RembgByBiRefNetAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `ZML_SelectTextV2`
- `easy ifElse`
- `easy isNone`
- `easy sam3ImageSegmentation`
- `easy sam3ModelLoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `mxSlider`
- `solarL_SaveImagesToZip`
- `ttN concat`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `easy imageSizeBySide` —— 2/3 个有
- `Label (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 3 | 2 - 3 | 3 | 82% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 3，观测区间 2 - 3，3 个样本，取值集中（一致性 82%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
