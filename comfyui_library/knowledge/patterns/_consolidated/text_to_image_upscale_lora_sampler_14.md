---
name: text_to_image_upscale_lora_sampler_14
type: Text To Image
frequency: 3
level: strong
coverage: 0.936667
common_nodes: [AIO_Preprocessor, BlockifyMask, CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, CropWithPadInfo, DrawMaskOnImage, EmptyLatentImage, GetImageSize+, ImageConcanate, ImageResize+, ImageResizeKJ, ImageScaleBy, ImageScaleToTotalPixels, JjkText, KOOK_ImageCompression, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ImageBlend, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveInt, QwenEditConfigPreparer, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit一键快背景 图生图搭配人物替换效率翻倍_2107248174195892226.json, 图片生成/图生图/QwenEdit图生图换背景 可同步调整姿势完成角色人物替换_2107250684616855554.json, 图片生成/图生图/图生图QwenEdit快速换背景 人物替换一步搞定_2107249399859605505.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_14

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/QwenEdit一键快背景 图生图搭配人物替换效率翻倍_2107248174195892226.json、图片生成/图生图/QwenEdit图生图换背景 可同步调整姿势完成角色人物替换_2107250684616855554.json、图片生成/图生图/图生图QwenEdit快速换背景 人物替换一步搞定_2107249399859605505.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `BlockifyMask`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `DrawMaskOnImage`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageConcanate`
- `ImageResize+`
- `ImageResizeKJ`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KOOK_ImageCompression`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `QwenEditConfigPreparer`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 2/3 个有

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
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
