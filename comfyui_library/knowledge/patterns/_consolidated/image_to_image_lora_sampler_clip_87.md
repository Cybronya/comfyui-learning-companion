---
name: image_to_image_lora_sampler_clip_87
type: Image To Image
frequency: 3
level: strong
coverage: 0.718
common_nodes: [Any Switch (rgthree), CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, FluxKontextImageScale, GetImageSize, GetNode, GoogleTranslateTextNode, Image Blend by Mask, Image Comparer (rgthree), ImageScaleBy, ImageStitch, ImpactMinMax, KSampler, LayerUtility: ColorImage, LoadImage, LoadImageOutput, LoraLoaderModelOnly, Mask Fill Holes, MaskToImage, PreviewImage, ReferenceLatent, SaveImage, SeedVR2GGUF, SetNode, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, 孤海_kontext生图比例, 孤海图像缩放按像素]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux-kontext 万能P图_2088595299035078658.json, 图片生成/图生图/一键去水印_水印消除_去马赛克_万物P图_1979437416035553282.json, 图片生成/文生图/Flux-kontext 万能P图_2084694321634299905.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_87

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux-kontext 万能P图_2088595299035078658.json、图片生成/图生图/一键去水印_水印消除_去马赛克_万物P图_1979437416035553282.json、图片生成/文生图/Flux-kontext 万能P图_2084694321634299905.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GetImageSize`
- `GetNode`
- `GoogleTranslateTextNode`
- `Image Blend by Mask`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageStitch`
- `ImpactMinMax`
- `KSampler`
- `LayerUtility: ColorImage`
- `LoadImage`
- `LoadImageOutput`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskToImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2GGUF`
- `SetNode`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `孤海_kontext生图比例`
- `孤海图像缩放按像素`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `RHHiddenNodes` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
