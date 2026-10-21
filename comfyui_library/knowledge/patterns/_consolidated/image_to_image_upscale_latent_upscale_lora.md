---
name: image_to_image_upscale_latent_upscale_lora
type: Image To Image
frequency: 2
level: weak
coverage: 0.8105
common_nodes: [BlockifyMask, CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, FluxKontextMultiReferenceLatentMethod, GH_CropRestore, GH_MaskCropV2, Get Image Size, GrowMaskWithBlur, GulfSeaImageMergeMask, Image Comparer (rgthree), Images to RGB, KSampler, LG_Color_Match_V2, LatentUpscaleBy, LayerUtility: BooleanOperatorV2, LayerUtility: ColorImage, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, ReferenceLatent, SZ_KleinTiledKSampler, SaveImage, StringLength, TextEncodeQwenImageEditPlusCustom_lrzjason, TextEncodeQwenImageEditPlus_lrzjason, TextInput_, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy ifElse, easy imageSizeByLongerSide, 图像缩放V2_孤海, 图像缩放范围孤海, 布尔孤海, 数学运算_孤海]
problems: [Steps较低可能导致细节不足]
missing: [Images to RGB, LayerUtility: BooleanOperatorV2, LayerUtility: ColorImage, 图像缩放V2_孤海, 图像缩放范围孤海, 布尔孤海, 数学运算_孤海, Get Image Size, easy imageSizeByLongerSide]
members: [图片生成/图生图/2102338587042865153.json, 图片生成/文生图/图像修复丨Qwen2511＋Flux2-Klein丨消除·局部重绘_2108075780692594690.json]
source: knowledge_consolidation
---

# image_to_image_upscale_latent_upscale_lora

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2102338587042865153.json、图片生成/文生图/图像修复丨Qwen2511＋Flux2-Klein丨消除·局部重绘_2108075780692594690.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `FluxKontextMultiReferenceLatentMethod`
- `GH_CropRestore`
- `GH_MaskCropV2`
- `Get Image Size`
- `GrowMaskWithBlur`
- `GulfSeaImageMergeMask`
- `Image Comparer (rgthree)`
- `Images to RGB`
- `KSampler`
- `LG_Color_Match_V2`
- `LatentUpscaleBy`
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: ColorImage`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenEditConfigPreparer`
- `ReferenceLatent`
- `SZ_KleinTiledKSampler`
- `SaveImage`
- `StringLength`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`
- `easy imageSizeByLongerSide`
- `图像缩放V2_孤海`
- `图像缩放范围孤海`
- `布尔孤海`
- `数学运算_孤海`

**可变部分**（部分 workflow 才有）：
- `LoadImageMask` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `StringTrim` —— 1/2 个有
- `ThresholdMask` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Images to RGB、LayerUtility: BooleanOperatorV2、LayerUtility: ColorImage、图像缩放V2_孤海、图像缩放范围孤海
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
