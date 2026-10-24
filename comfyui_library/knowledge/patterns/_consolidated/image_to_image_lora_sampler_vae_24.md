---
name: image_to_image_lora_sampler_vae_24
type: Image To Image
frequency: 2
level: weak
coverage: 0.7085
common_nodes: [AIO_Preprocessor, BasicScheduler, CLIPLoader, CM_IntBinaryCondition, CR Integer To String, CR Text, Canny, ConditioningZeroOut, DiffusionModelLoaderKJ, EG_TX_SFBLS, Fast Bypasser (rgthree), GetImageSize+, GetNode, GrowMask, Image Crop Face, ImageComposite+, ImageScaleBy, ImageSmartSharpen+, ImageToMask, ImpactInt, ImpactSwitch, KSampler, KSamplerSelect, Latent Noise Injection, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: If , LayerUtility: ImageBlend, LoadImage, LoraLoaderModelOnly, LoraNames_, MaskBlur+, NoiseFromImage+, PathchSageAttentionKJ, PrimitiveString, ResizeImageMixlab, SamplerCustom, SaveImage, SetNode, SimpleMath+, StringContains, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageSize, easy showAnything, easy textIndexSwitch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/klein万能工作流1.1_2019058259008688129.json, 图片生成/图生图/全能版klein工作流_2015085041012969473.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_24

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/klein万能工作流1.1_2019058259008688129.json、图片生成/图生图/全能版klein工作流_2015085041012969473.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
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
- `ImageScaleBy`
- `ImageSmartSharpen+`
- `ImageToMask`
- `ImpactInt`
- `ImpactSwitch`
- `KSampler`
- `KSamplerSelect`
- `Latent Noise Injection`
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
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`
- `easy showAnything`
- `easy textIndexSwitch`

**可变部分**（部分 workflow 才有）：
- `Bounded Image Crop` —— 1/2 个有
- `Bounded Image Crop with Mask` —— 1/2 个有
- `CFGZeroStar` —— 1/2 个有
- `DyPE_FLUX` —— 1/2 个有
- `EasyCache` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `ResizeAndPadImage` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `easy imageCropFromMask` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
