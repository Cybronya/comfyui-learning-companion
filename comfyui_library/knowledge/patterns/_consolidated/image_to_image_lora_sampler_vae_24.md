---
name: image_to_image_lora_sampler_vae_24
type: Image To Image
frequency: 3
level: strong
coverage: 0.717
common_nodes: [AIO_Preprocessor, BasicScheduler, CLIPLoader, CM_IntBinaryCondition, CR Integer To String, CR Text, Canny, ConditioningZeroOut, DiffusionModelLoaderKJ, EG_TX_SFBLS, Fast Bypasser (rgthree), GetImageSize+, GetNode, GrowMask, Image Crop Face, ImageComposite+, ImageSmartSharpen+, ImageToMask, ImpactInt, ImpactSwitch, KSampler, KSamplerSelect, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: If , LayerUtility: ImageBlend, LoadImage, LoraLoaderModelOnly, LoraNames_, MaskBlur+, NoiseFromImage+, PathchSageAttentionKJ, PrimitiveString, ResizeImageMixlab, SamplerCustom, SaveImage, SetNode, SimpleMath+, StringContains, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, VAEEncode, VAELoader, easy imageSize, easy showAnything, easy textIndexSwitch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/klein万能工作流1.1_2019058259008688129.json, 图片生成/图生图/全能版klein工作流_2015085041012969473.json, 平台全量/klein万能工作流1.2_2020333324601925634.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_24

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/klein万能工作流1.1_2019058259008688129.json、图片生成/图生图/全能版klein工作流_2015085041012969473.json、平台全量/klein万能工作流1.2_2020333324601925634.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicScheduler`
- `CLIPLoader`
- `CM_IntBinaryCondition`
- `CR Integer To String`
- `CR Text`
- `Canny`
- `ConditioningZeroOut`
- `DiffusionModelLoaderKJ`
- `EG_TX_SFBLS`
- `Fast Bypasser (rgthree)`
- `GetImageSize+`
- `GetNode`
- `GrowMask`
- `Image Crop Face`
- `ImageComposite+`
- `ImageSmartSharpen+`
- `ImageToMask`
- `ImpactInt`
- `ImpactSwitch`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask`
- `LayerUtility: If `
- `LayerUtility: ImageBlend`
- `LoadImage`
- `LoraLoaderModelOnly`
- `LoraNames_`
- `MaskBlur+`
- `NoiseFromImage+`
- `PathchSageAttentionKJ`
- `PrimitiveString`
- `ResizeImageMixlab`
- `SamplerCustom`
- `SaveImage`
- `SetNode`
- `SimpleMath+`
- `StringContains`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`
- `easy showAnything`
- `easy textIndexSwitch`

**可变部分**（部分 workflow 才有）：
- `Bounded Image Crop` —— 2/3 个有
- `Bounded Image Crop with Mask` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `Latent Noise Injection` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `ResizeAndPadImage` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `TextEncodeQwenImageEdit` —— 2/3 个有
- `VAEDecodeTiled` —— 2/3 个有
- `CFGZeroStar` —— 1/3 个有
- `ColorMatch` —— 1/3 个有
- `DyPE_FLUX` —— 1/3 个有
- `EasyCache` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `ImpactInversedSwitch` —— 1/3 个有
- `TTP_Image_Assy` —— 1/3 个有
- `TTP_Image_Tile_Batch` —— 1/3 个有
- `TTP_Tile_image_size` —— 1/3 个有
- `easy imageBatchToImageList` —— 1/3 个有
- `easy imageCropFromMask` —— 1/3 个有
- `easy imageListToImageBatch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
