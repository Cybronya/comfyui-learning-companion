---
name: text_to_image_upscale_lora_sampler_55
type: Text To Image
frequency: 4
level: strong
coverage: 0.89975
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CM_BoolToInt, CM_FloatBinaryOperation, ConditioningZeroOut, DF_Int_to_Float, EmptyLatentImage, EmptySD3LatentImage, ExecutionBlocker, GrowMaskWithBlur, ImageRGBA2RGB, ImpactNeg, Int, IntConditions, InvertMask, IterativeImageUpscale, JjkText, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LanPaint_MaskBlend, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, Mask_White_Area_Ratio, PixelKSampleUpscalerProvider, PlaySound|pysssss, PrimitiveBoolean, PrimitiveFloat, Qwen3_VQA, RHLLMChatNode, SaveImage, SaveLatent, SolidMask, StringConcatenate, ToBool, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy anythingIndexSwitch, easy cleanGpuUsed, easy mathString, easy showAnything, sanmi IntToBOOLEAN, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2k_4k高清语义遵从｜krea2图片编辑V5局部重绘 强一致性图生图新版_2089419976624132097.json, 图片生成/图生图/局部重绘强一致性2k 4k高清语义遵从krea2图片编辑V5图生图反推提示词_2088376439962947586.json, 图片生成/图生图/局部重绘强一致性2k_4k高清语义遵从V5｜krea2反推提示词图生图最新版_2088346284326473730.json, 图片生成/图生图/局部重绘强一致性｜krea2图片编辑V4 语义遵从 2k_4k高清图生图_2089418504192741377.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_55

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2k_4k高清语义遵从｜krea2图片编辑V5局部重绘 强一致性图生图新版_2089419976624132097.json、图片生成/图生图/局部重绘强一致性2k 4k高清语义遵从krea2图片编辑V5图生图反推提示词_2088376439962947586.json、图片生成/图生图/局部重绘强一致性2k_4k高清语义遵从V5｜krea2反推提示词图生图最新版_2088346284326473730.json、图片生成/图生图/局部重绘强一致性｜krea2图片编辑V4 语义遵从 2k_4k高清图生图_2089418504192741377.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_BoolToInt`
- `CM_FloatBinaryOperation`
- `ConditioningZeroOut`
- `DF_Int_to_Float`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `ExecutionBlocker`
- `GrowMaskWithBlur`
- `ImageRGBA2RGB`
- `ImpactNeg`
- `Int`
- `IntConditions`
- `InvertMask`
- `IterativeImageUpscale`
- `JjkText`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LanPaint_MaskBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask_White_Area_Ratio`
- `PixelKSampleUpscalerProvider`
- `PlaySound|pysssss`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `Qwen3_VQA`
- `RHLLMChatNode`
- `SaveImage`
- `SaveLatent`
- `SolidMask`
- `StringConcatenate`
- `ToBool`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`
- `easy mathString`
- `easy showAnything`
- `sanmi IntToBOOLEAN`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `StringReplace` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
