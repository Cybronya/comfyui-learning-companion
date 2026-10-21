---
name: image_to_image_lora_sampler_unet_16
type: Image To Image
frequency: 5
level: strong
coverage: 0.8222
common_nodes: [AIO_Preprocessor, BlockifyMask, CFGNorm, CLIPLoader, ConditioningZeroOut, DrawMaskOnImage, ImageConcanate, ImageResizeKJ, ImageScaleToTotalPixels, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ImageBlend, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, QwenEditConfigPreparer, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ImageBlend, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/图生图/2071115067344642049.json, 图片生成/文生图/QwenEdit 双图参考+图片编辑+全节点注释_2076698649215721473.json, 图片生成/文生图/动作  姿势   换背景 人物替换 一键换背景 图生图  QwenEdit_2082649352681644034.json, 图片生成/文生图/动作  姿势   换背景 人物替换 一键换背景 图生图  QwenEdit_2082663471916863490.json, 图片生成/文生图/换姿势  换背景 角色替换  人物替换 一键换背景 图生图  QwenEdit_2079853075891834882.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_16

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2071115067344642049.json、图片生成/文生图/QwenEdit 双图参考+图片编辑+全节点注释_2076698649215721473.json、图片生成/文生图/动作  姿势   换背景 人物替换 一键换背景 图生图  QwenEdit_2082649352681644034.json、图片生成/文生图/动作  姿势   换背景 人物替换 一键换背景 图生图  QwenEdit_2082663471916863490.json、图片生成/文生图/换姿势  换背景 角色替换  人物替换 一键换背景 图生图  QwenEdit_2079853075891834882.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `AIO_Preprocessor`
- `BlockifyMask`
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `DrawMaskOnImage`
- `ImageConcanate`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `QwenEditConfigPreparer`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CropWithPadInfo` —— 4/5 个有
- `GetImageSize+` —— 4/5 个有
- `ImageResize+` —— 4/5 个有
- `ImageScaleBy` —— 4/5 个有
- `KOOK_ImageCompression` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `SeedVR2LoadDiTModel` —— 4/5 个有
- `SeedVR2LoadVAEModel` —— 4/5 个有
- `SeedVR2VideoUpscaler` —— 4/5 个有
- `TTP_Image_Assy` —— 4/5 个有
- `TTP_Image_Tile_Batch` —— 4/5 个有
- `TTP_Tile_image_size` —— 4/5 个有
- `PreviewImage` —— 2/5 个有
- `CR Text` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | beta57 | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 beta57，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerMask: BiRefNetUltraV2、LayerMask: LoadBiRefNetModelV2、LayerUtility: ImageBlend、LayerUtility: ImageRemoveAlpha、LayerUtility: ImageScaleByAspectRatio V2
