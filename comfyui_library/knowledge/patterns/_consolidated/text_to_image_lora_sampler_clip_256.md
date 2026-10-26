---
name: text_to_image_lora_sampler_clip_256
type: Text To Image
frequency: 8
level: weak
coverage: 0.741875
common_nodes: [Any Switch (rgthree), CFGGuider, CLIPLoader, CLIPTextEncode, CR Text Concatenate, ColorMatch, ComfySwitchNode, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GH_ImageVideoComparer, GetImageSize, Image Compare (mtb), ImageScaleToTotalPixels, ImageSharpen, JsonExtractString, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewAny, PreviewImage, PrimitiveStringMultiline, RandomNoise, ReferenceLatent, ResolutionSelector, SDPoseOODLoader, SDPoseOODProcessor, SamplerCustomAdvanced, SaveImage, SaveImageAdvanced, Seed (rgthree), SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, SetLatentNoiseMask, TextConcatenator, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAEEncode, VAELoader, YOLOModelLoader, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image2.1最强开源模型 图像编辑整合处理工具_2114088484360245249.json, 图片生成/图生图/Qwen image2.1最强开源模型图像编辑整合工作流 全能改图_2105410925342846978.json, 图片生成/图生图/Qwen image2.1最强开源模型图像编辑整合工作流 全能改图_2108654377069273089.json, 图片生成/图生图/Qwen_image2.1-最强开源模型，图像编辑整合工作流_2104823312131125249.json, 图片生成/图生图/Qwen_image2.1-最强开源模型，图像编辑整合工作流_2110573536854233089.json, 图片生成/图生图/Qwen_image2.1-最强开源模型，图像编辑整合工作流_2111274795575894018.json, 图片生成/图生图/Qwen_image2.1-最强开源模型，图像编辑整合工作流_2113460425001095170.json, 图片生成/图生图/Qwen_image2.1图像编辑整合包，最强开源模型图生图_2110492929373589505.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_256

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen image2.1最强开源模型 图像编辑整合处理工具_2114088484360245249.json、图片生成/图生图/Qwen image2.1最强开源模型图像编辑整合工作流 全能改图_2105410925342846978.json、图片生成/图生图/Qwen image2.1最强开源模型图像编辑整合工作流 全能改图_2108654377069273089.json、图片生成/图生图/Qwen_image2.1-最强开源模型，图像编辑整合工作流_2104823312131125249.json、图片生成/图生图/Qwen_image2.1-最强开源模型，图像编辑整合工作流_2110573536854233089.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 8 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ColorMatch`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GH_ImageVideoComparer`
- `GetImageSize`
- `Image Compare (mtb)`
- `ImageScaleToTotalPixels`
- `ImageSharpen`
- `JsonExtractString`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ReferenceLatent`
- `ResolutionSelector`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SaveImageAdvanced`
- `Seed (rgthree)`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SetLatentNoiseMask`
- `TextConcatenator`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `YOLOModelLoader`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `DrawMaskOnImage` —— 7/8 个有
- `GetNode` —— 7/8 个有
- `INTConstant` —— 7/8 个有
- `ImageConcanate` —— 7/8 个有
- `InpaintCropImproved` —— 7/8 个有
- `InpaintStitchImproved` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `SetNode` —— 7/8 个有
- `SimpleMath+` —— 7/8 个有
- `JjkText` —— 4/8 个有
- `solarL_SaveImagesToZip` —— 4/8 个有
- `忽略多组孤海` —— 4/8 个有
- `EmptyImage` —— 1/8 个有
- `ImageAndMaskPreview` —— 1/8 个有
- `LayerMask: MaskGrow` —— 1/8 个有
- `MaskFillHoles` —— 1/8 个有
- `孤海图像缩放按像素` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 552 | 80 - 1024 | 8 | 14% |
| 高度 | 552 | 80 - 1024 | 8 | 14% |
| 采样步数 | 17 | 4 - 30 | 8 | 24% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4.5 | 8 | 36% |
| 采样算法 | er_sde | - | 8 | 50% |
| 调度器 | beta | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 552，观测区间 80 - 1024，8 个样本，取值分散，一致性仅 14%
- 高度 中位数 552，观测区间 80 - 1024，8 个样本，取值分散，一致性仅 14%
- 采样步数 中位数 17，观测区间 4 - 30，8 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4.5，8 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，8 个样本，一致性 50%
- 调度器 最常用 beta，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（4/8 个样本）：Steps较低可能导致细节不足
