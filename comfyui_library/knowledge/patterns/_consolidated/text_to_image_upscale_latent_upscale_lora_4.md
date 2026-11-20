---
name: text_to_image_upscale_latent_upscale_lora_4
type: Text To Image
frequency: 6
level: strong
coverage: 0.9245
common_nodes: [BlockifyMask, CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, EmptyLatentImage, FluxKontextMultiReferenceLatentMethod, GH_CropRestore, GH_MaskCropV2, Get Image Size, GrowMaskWithBlur, GulfSeaImageMergeMask, Image Comparer (rgthree), Images to RGB, JjkText, KSampler, LG_Color_Match_V2, LatentUpscaleBy, LayerUtility: BooleanOperatorV2, LayerUtility: ColorImage, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, ReferenceLatent, SZ_KleinTiledKSampler, SaveImage, StringLength, TextEncodeQwenImageEditPlusCustom_lrzjason, TextEncodeQwenImageEditPlus_lrzjason, TextInput_, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy ifElse, easy imageSizeByLongerSide, solarL_SaveImagesToZip, 图像缩放V2_孤海, 图像缩放范围孤海, 布尔孤海, 数学运算_孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2511移除加局部重绘高品质｜擦除不留死角｜细节修图更干净_2102644646395600897.json, 图片生成/图生图/Qwen2511移除物体与局部重绘高品质工作流，清空提示词即移除输入即重绘_2102842820901036034.json, 图片生成/图生图/Qwen2511移除物体与局部重绘高品质工作流，清空提示词即移除输入即重绘_2105860216289054722.json, 图片生成/图生图/图像修复Qwen2511+Flux2-Klein｜消除局部重绘图生图修复_2114291807931691010.json, 图片生成/文生图/Qwen2511+Flux2-Klein图像修复｜消除瑕疵局部重绘_2108442417715306498.json, 图片生成/文生图/图像修复Qwen2511加Flux2 Klein消除局部重绘 图片精修方案_2108640223453343745.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen 2511移除加局部重绘高品质｜擦除不留死角｜细节修图更干净_2102644646395600897.json、图片生成/图生图/Qwen2511移除物体与局部重绘高品质工作流，清空提示词即移除输入即重绘_2102842820901036034.json、图片生成/图生图/Qwen2511移除物体与局部重绘高品质工作流，清空提示词即移除输入即重绘_2105860216289054722.json、图片生成/图生图/图像修复Qwen2511+Flux2-Klein｜消除局部重绘图生图修复_2114291807931691010.json、图片生成/文生图/Qwen2511+Flux2-Klein图像修复｜消除瑕疵局部重绘_2108442417715306498.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `BlockifyMask`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `EmptyLatentImage`
- `FluxKontextMultiReferenceLatentMethod`
- `GH_CropRestore`
- `GH_MaskCropV2`
- `Get Image Size`
- `GrowMaskWithBlur`
- `GulfSeaImageMergeMask`
- `Image Comparer (rgthree)`
- `Images to RGB`
- `JjkText`
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
- `solarL_SaveImagesToZip`
- `图像缩放V2_孤海`
- `图像缩放范围孤海`
- `布尔孤海`
- `数学运算_孤海`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 5/6 个有
- `LoadImageMask` —— 3/6 个有
- `PrimitiveBoolean` —— 3/6 个有
- `StringTrim` —— 3/6 个有
- `ThresholdMask` —— 3/6 个有
- `EmptyImage` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（18/6 个样本）：Steps较低可能导致细节不足
