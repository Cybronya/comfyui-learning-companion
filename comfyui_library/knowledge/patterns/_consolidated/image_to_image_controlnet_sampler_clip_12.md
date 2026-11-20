---
name: image_to_image_controlnet_sampler_clip_12
type: Image To Image
frequency: 4
level: strong
coverage: 0.815
common_nodes: [AnimeLineArtPreprocessor, Any Switch (rgthree), CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, GetImageSize+, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), GrowMask, Image Overlay, ImageBlend, ImageBlur, ImageCompositeMasked, ImageToMask, InvertMask, KSampler, LoadImage, MaskToImage, PreviewImage, SAMModelLoader (segment anything), SaveImage, SetLatentNoiseMask, Tensor Batch to Image, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键服装换色_1902155360839606273.json, 图片生成/图生图/一键服装换色_1920457275633238018.json, 图片生成/图生图/电商一键服装换色_1920019784732446722.json, 图片生成/图生图/电商模特一键换发色_1920098198424059905.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键服装换色_1902155360839606273.json、图片生成/图生图/一键服装换色_1920457275633238018.json、图片生成/图生图/电商一键服装换色_1920019784732446722.json、图片生成/图生图/电商模特一键换发色_1920098198424059905.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `AnimeLineArtPreprocessor`
- `Any Switch (rgthree)`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `GetImageSize+`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMask`
- `Image Overlay`
- `ImageBlend`
- `ImageBlur`
- `ImageCompositeMasked`
- `ImageToMask`
- `InvertMask`
- `KSampler`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SAMModelLoader (segment anything)`
- `SaveImage`
- `SetLatentNoiseMask`
- `Tensor Batch to Image`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Color Panel` —— 3/4 个有
- `DetailerForEach` —— 3/4 个有
- `GrowMaskWithBlur` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `LoraLoader` —— 3/4 个有
- `MaskToSEGS` —— 3/4 个有
- `Mask To Image (mtb)` —— 1/4 个有
- `SolidMask` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 4 | 90% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 4 | 100% |
| 采样算法 | dpmpp_2m | - | 4 | 100% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 0.5 | 0.5 - 0.58 | 4 | 93% |
| ControlNet 权重 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 0.3 | 0.3 - 0.3 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，4 个样本，一致性 100%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 0.58，4 个样本，取值集中（一致性 93%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.3，观测区间 0.3 - 0.3，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
