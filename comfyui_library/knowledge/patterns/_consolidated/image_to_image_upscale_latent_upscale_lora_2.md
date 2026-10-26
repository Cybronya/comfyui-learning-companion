---
name: image_to_image_upscale_latent_upscale_lora_2
type: Image To Image
frequency: 4
level: strong
coverage: 0.93675
common_nodes: [BlockifyMask, CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, FluxKontextMultiReferenceLatentMethod, GH_CropRestore, GH_MaskCropV2, Get Image Size, GrowMaskWithBlur, GulfSeaImageMergeMask, Image Comparer (rgthree), Images to RGB, KSampler, LG_Color_Match_V2, LatentUpscaleBy, LayerUtility: BooleanOperatorV2, LayerUtility: ColorImage, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, ReferenceLatent, SZ_KleinTiledKSampler, SaveImage, StringLength, TextEncodeQwenImageEditPlusCustom_lrzjason, TextEncodeQwenImageEditPlus_lrzjason, TextInput_, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy ifElse, easy imageSizeByLongerSide, 图像缩放V2_孤海, 图像缩放范围孤海, 布尔孤海, 数学运算_孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2511 移除 + 局部重绘 高品质_2102338587042865153.json, 图片生成/图生图/图像修复丨Qwen2511＋Flux2-Klein丨消除·局部重绘_2112371459015401473.json, 图片生成/图生图/图像修复丨Qwen2511＋Flux2-Klein丨消除·局部重绘_2113919615620435970.json, 图片生成/文生图/图像修复丨Qwen2511＋Flux2-Klein丨消除·局部重绘_2108075780692594690.json]
source: knowledge_consolidation
---

# image_to_image_upscale_latent_upscale_lora_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen2511 移除 + 局部重绘 高品质_2102338587042865153.json、图片生成/图生图/图像修复丨Qwen2511＋Flux2-Klein丨消除·局部重绘_2112371459015401473.json、图片生成/图生图/图像修复丨Qwen2511＋Flux2-Klein丨消除·局部重绘_2113919615620435970.json、图片生成/文生图/图像修复丨Qwen2511＋Flux2-Klein丨消除·局部重绘_2108075780692594690.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
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
- `LoadImageMask` —— 3/4 个有
- `PrimitiveBoolean` —— 3/4 个有
- `StringTrim` —— 3/4 个有
- `ThresholdMask` —— 3/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
