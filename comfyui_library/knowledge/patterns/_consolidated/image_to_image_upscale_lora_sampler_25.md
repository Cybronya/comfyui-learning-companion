---
name: image_to_image_upscale_lora_sampler_25
type: Image To Image
frequency: 6
level: strong
coverage: 0.815833
common_nodes: [CFGNorm, CLIPLoader, CM_BoolToInt, EmptySD3LatentImage, ExecutionBlocker, ImageRGBA2RGB, ImpactNeg, Int, IterativeImageUpscale, JjkText, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PixelKSampleUpscalerProvider, PlaySound|pysssss, PrimitiveBoolean, PrimitiveFloat, SaveImage, SaveLatent, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy anythingIndexSwitch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/krea2双图编辑V2 一致性增强 2k_4k高清出图 迭代超分极致细节_2080233598787080194.json, 图片生成/图生图/krea2图片编辑V4 局部重绘 强一致性 2k_4k高清 语义遵从_2080140064025309186.json, 图片生成/图生图/krea2图片编辑V5 局部重绘 强一致性 2k_4k高清 语义遵从 最新版2026.7.2_2080573584233295873.json, 图片生成/图生图/krea2图片编辑V6 全新超清4k放大 局部重绘优化 语义遵从 一致性 26.08.17_2089183599777107969.json, 图片生成/图生图/krea2图片编辑_语义遵从  局部重绘 超强一致性_2089638583782170625.json, 图片生成/图生图/krea2图片编辑_语义遵从_局部重绘_超强一致性_2090060187771162625.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_25

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/krea2双图编辑V2 一致性增强 2k_4k高清出图 迭代超分极致细节_2080233598787080194.json、图片生成/图生图/krea2图片编辑V4 局部重绘 强一致性 2k_4k高清 语义遵从_2080140064025309186.json、图片生成/图生图/krea2图片编辑V5 局部重绘 强一致性 2k_4k高清 语义遵从 最新版2026.7.2_2080573584233295873.json、图片生成/图生图/krea2图片编辑V6 全新超清4k放大 局部重绘优化 语义遵从 一致性 26.08.17_2089183599777107969.json、图片生成/图生图/krea2图片编辑_语义遵从  局部重绘 超强一致性_2089638583782170625.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CM_BoolToInt`
- `EmptySD3LatentImage`
- `ExecutionBlocker`
- `ImageRGBA2RGB`
- `ImpactNeg`
- `Int`
- `IterativeImageUpscale`
- `JjkText`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PixelKSampleUpscalerProvider`
- `PlaySound|pysssss`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `SaveImage`
- `SaveLatent`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy anythingIndexSwitch`

**可变部分**（部分 workflow 才有）：
- `CM_FloatBinaryOperation` —— 5/6 个有
- `ConditioningZeroOut` —— 5/6 个有
- `DF_Int_to_Float` —— 5/6 个有
- `GrowMaskWithBlur` —— 5/6 个有
- `IntConditions` —— 5/6 个有
- `RHLLMChatNode` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `easy mathString` —— 5/6 个有
- `sanmi IntToBOOLEAN` —— 5/6 个有
- `InvertMask` —— 4/6 个有
- `LanPaint_MaskBlend` —— 4/6 个有
- `Mask_White_Area_Ratio` —— 4/6 个有
- `PreviewAny` —— 4/6 个有
- `Qwen3_VQA` —— 4/6 个有
- `SolidMask` —— 4/6 个有
- `StringConcatenate` —— 4/6 个有
- `ToBool` —— 4/6 个有
- `孤海注释` —— 4/6 个有
- `StringReplace` —— 3/6 个有
- `easy showAnything` —— 2/6 个有
- `1hew_TextToAny` —— 1/6 个有
- `GetImageSize` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `RH_RFMSR_ModelLoader` —— 1/6 个有
- `RH_RFMSR_Upscale` —— 1/6 个有
- `图像缩放V2_孤海` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
