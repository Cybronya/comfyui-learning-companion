---
name: text_to_image_lora_sampler_clip_196
type: Text To Image
frequency: 9
level: weak
coverage: 0.791444
common_nodes: [Any Switch (rgthree), CFGGuider, CLIPLoader, CLIPTextEncode, CR Text Concatenate, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GH_ImageVideoComparer, GetImageSize, ImageScaleToTotalPixels, ImageSharpen, JsonExtractString, KSampler, KSamplerSelect, LoraLoaderModelOnly, PreviewAny, PreviewImage, PrimitiveStringMultiline, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, TextConcatenator, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAEEncode, VAELoader, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image2.1最强开源模型图像编辑整合工作流 全能改图_2105410925342846978.json, 图片生成/图生图/Qwen image2.1最强开源模型图像编辑整合工作流 全能改图_2108654377069273089.json, 图片生成/图生图/Qwen_image2.1-最强开源模型，图像编辑整合工作流_2104823312131125249.json, 图片生成/图生图/Qwen_image2.1-最强开源模型，图像编辑整合工作流_2110573536854233089.json, 图片生成/图生图/Qwen_image2.1-最强开源模型，图像编辑整合工作流_2111274795575894018.json, 图片生成/图生图/Qwen_image2.1图像编辑整合包，最强开源模型图生图_2110492929373589505.json, 图片生成/文生图/Qwen_image2.1+Z_image+Krea2三模型文生图合集工作流_2104673944501575681.json, 图片生成/文生图/Qwen_image2.1、Z_image、Krea2_文生图工作流合集_2103746262452498433.json, 图片生成/文生图/Qwen_image2.1、Z_image、Krea2文生图合集｜三大模型一站式出图_2104485822958489602.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_196

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen image2.1最强开源模型图像编辑整合工作流 全能改图_2105410925342846978.json、图片生成/图生图/Qwen image2.1最强开源模型图像编辑整合工作流 全能改图_2108654377069273089.json、图片生成/图生图/Qwen_image2.1-最强开源模型，图像编辑整合工作流_2104823312131125249.json、图片生成/图生图/Qwen_image2.1-最强开源模型，图像编辑整合工作流_2110573536854233089.json、图片生成/图生图/Qwen_image2.1-最强开源模型，图像编辑整合工作流_2111274795575894018.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 9 个 workflow 都包含：
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
- `ComfySwitchNode` —— 6/9 个有
- `Fast Groups Bypasser (rgthree)` —— 6/9 个有
- `Image Compare (mtb)` —— 6/9 个有
- `LoadImage` —— 6/9 个有
- `ResolutionSelector` —— 6/9 个有
- `SDPoseOODLoader` —— 6/9 个有
- `SDPoseOODProcessor` —— 6/9 个有
- `SaveImageAdvanced` —— 6/9 个有
- `SetLatentNoiseMask` —— 6/9 个有
- `YOLOModelLoader` —— 6/9 个有
- `DrawMaskOnImage` —— 5/9 个有
- `GetNode` —— 5/9 个有
- `INTConstant` —— 5/9 个有
- `ImageConcanate` —— 5/9 个有
- `InpaintCropImproved` —— 5/9 个有
- `InpaintStitchImproved` —— 5/9 个有
- `JjkText` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/9 个有
- `SetNode` —— 5/9 个有
- `SimpleMath+` —— 5/9 个有
- `solarL_SaveImagesToZip` —— 5/9 个有
- `忽略多组孤海` —— 4/9 个有
- `ModelSamplingAuraFlow` —— 3/9 个有
- `TTResolutionSelector` —— 3/9 个有
- `ImageAndMaskPreview` —— 1/9 个有
- `LayerMask: MaskGrow` —— 1/9 个有
- `MaskFillHoles` —— 1/9 个有
- `孤海图像缩放按像素` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 30 | 9 | 8% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 9 | 41% |
| 采样算法 | er_sde | - | 9 | 56% |
| 调度器 | beta | - | 9 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 1024 | 9 | 6% |
| 高度 | 80 | 80 - 1024 | 9 | 6% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 30，9 个样本，取值分散，一致性仅 8%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，9 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 er_sde，9 个样本，一致性 56%
- 调度器 最常用 beta，9 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，9 个样本，取值分散，一致性仅 6%
- 高度 中位数 80，观测区间 80 - 1024，9 个样本，取值分散，一致性仅 6%
- 高发问题（11/9 个样本）：Steps较低可能导致细节不足
