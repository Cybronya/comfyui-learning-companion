---
name: text_to_image_lora_sampler_clip_192
type: Text To Image
frequency: 4
level: weak
coverage: 0.82325
common_nodes: [Any Switch (rgthree), CFGGuider, CLIPLoader, CLIPTextEncode, CR Text Concatenate, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GH_ImageVideoComparer, GetImageSize, ImageScaleToTotalPixels, ImageSharpen, JsonExtractString, KSampler, KSamplerSelect, LoraLoaderModelOnly, PreviewAny, PreviewImage, PrimitiveStringMultiline, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, TextConcatenator, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAEEncode, VAELoader, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [CR Text Concatenate, Image Compare (mtb), LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, 忽略多组孤海, Seed (rgthree)]
members: [图片生成/图生图/2104823312131125249.json, 图片生成/文生图/Qwen_image2.1+Z_image+Krea2三模型文生图合集工作流_2104673944501575681.json, 图片生成/文生图/Qwen_image2.1、Z_image、Krea2_文生图工作流合集_2103746262452498433.json, 图片生成/文生图/Qwen_image2.1、Z_image、Krea2文生图合集｜三大模型一站式出图_2104485822958489602.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_192

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2104823312131125249.json、图片生成/文生图/Qwen_image2.1+Z_image+Krea2三模型文生图合集工作流_2104673944501575681.json、图片生成/文生图/Qwen_image2.1、Z_image、Krea2_文生图工作流合集_2103746262452498433.json、图片生成/文生图/Qwen_image2.1、Z_image、Krea2文生图合集｜三大模型一站式出图_2104485822958489602.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GH_ImageVideoComparer`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `ImageSharpen`
- `JsonExtractString`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `TextConcatenator`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 3/4 个有
- `TTResolutionSelector` —— 3/4 个有
- `JjkText` —— 2/4 个有
- `solarL_SaveImagesToZip` —— 2/4 个有
- `忽略多组孤海` —— 2/4 个有
- `ComfySwitchNode` —— 1/4 个有
- `DrawMaskOnImage` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `Image Compare (mtb)` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `InpaintCropImproved` —— 1/4 个有
- `InpaintStitchImproved` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `ResolutionSelector` —— 1/4 个有
- `SDPoseOODLoader` —— 1/4 个有
- `SDPoseOODProcessor` —— 1/4 个有
- `SaveImageAdvanced` —— 1/4 个有
- `SetLatentNoiseMask` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `YOLOModelLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 552 | 80 - 1024 | 4 | 14% |
| 高度 | 552 | 80 - 1024 | 4 | 14% |
| 采样步数 | 6 | 4 - 30 | 4 | 6% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4.5 | 4 | 36% |
| 采样算法 | er_sde | - | 4 | 50% |
| 调度器 | beta | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 552，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 14%
- 高度 中位数 552，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 14%
- 采样步数 中位数 6，观测区间 4 - 30，4 个样本，取值分散，一致性仅 6%
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4.5，4 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，4 个样本，一致性 50%
- 调度器 最常用 beta，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、Image Compare (mtb)、LayerUtility: ImageScaleByAspectRatio V2、SimpleMath+、忽略多组孤海
