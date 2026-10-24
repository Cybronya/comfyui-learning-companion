---
name: image_to_image_lora_sampler_unet_50
type: Image To Image
frequency: 11
level: moderate
coverage: 0.896909
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2509无任何lora的老照片修复_1980226057456562178.json, 图片生成/图生图/2509溶车图+修正车身反射和背景透视_2057363765670268930.json, 图片生成/图生图/2511人物变瘦工作流_2009102963037446146.json, 图片生成/图生图/2511人物变胖工作流_2004180546605465601.json, 图片生成/图生图/2511人物变胖工作流_2009151148367810561.json, 图片生成/图生图/Qwen image edit 人物变微胖_2010359009227841537.json, 图片生成/图生图/Qwen image edit 人物变瘦_2010352422505418753.json, 图片生成/图生图/Qwen image edit 人物变胖_2010346301300412417.json, 图片生成/图生图/Qwen-Edit  动漫转真人+zimage+放大_2058045653837762562.json, 图片生成/图生图/人物变胖变瘦·动物男女动漫等_2012151853038968833.json, 图片生成/图生图/👾怪獸-Qwen 2511-Unblur-Anything高清修复👾_2014653934102646786.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_50

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/2509无任何lora的老照片修复_1980226057456562178.json、图片生成/图生图/2509溶车图+修正车身反射和背景透视_2057363765670268930.json、图片生成/图生图/2511人物变瘦工作流_2009102963037446146.json、图片生成/图生图/2511人物变胖工作流_2004180546605465601.json、图片生成/图生图/2511人物变胖工作流_2009151148367810561.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 10/11 个有
- `TextEncodeQwenImageEditPlus` —— 10/11 个有
- `FluxKontextMultiReferenceLatentMethod` —— 9/11 个有
- `SeedVR2LoadDiTModel` —— 9/11 个有
- `SeedVR2LoadVAEModel` —— 9/11 个有
- `SeedVR2VideoUpscaler` —— 9/11 个有
- `ImageScaleBy` —— 8/11 个有
- `ImageScaleToTotalPixels` —— 7/11 个有
- `CR Text` —— 6/11 个有
- `PreviewImage` —— 6/11 个有
- `ReferenceLatent` —— 5/11 个有
- `GetImageSize` —— 4/11 个有
- `easy cleanGpuUsed` —— 4/11 个有
- `孤海图像缩放按像素` —— 4/11 个有
- `CLIPTextEncode` —— 2/11 个有
- `ConditioningZeroOut` —— 2/11 个有
- `ImageConcatMulti` —— 2/11 个有
- `LayerUtility: PurgeVRAM V2` —— 2/11 个有
- `EmptyLatentImage` —— 1/11 个有
- `Fast Groups Muter (rgthree)` —— 1/11 个有
- `ImageConcanate` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `SetLatentNoiseMask` —— 1/11 个有
- `TextEncodeQwenImageEdit` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1536 | - | 1 | 100% |
| 采样步数 | 8 | 4 - 20 | 11 | 48% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 0.1 - 1 | 11 | 61% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，11 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.1 - 1，11 个样本
- 高发问题（19/11 个样本）：Steps较低可能导致细节不足
