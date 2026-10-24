---
name: text_to_image_upscale_lora_sampler_60
type: Text To Image
frequency: 4
level: strong
coverage: 0.68425
common_nodes: [AILab_ImagePreview, AILab_Preview, BatchImagesNode, CFGGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, Display Int (rgthree), EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSizeAndCount, GetNode, Image Comparer (rgthree), ImageConcatMulti, ImageFromBatch, ImageMergeTileList, ImageResizeKJv2, ImageScaleBy, ImageScaleToMaxDimension, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2TorchCompileSettings, SeedVR2VideoUpscaler, SetNode, SplitImageToTileList, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy float, easy forLoopEnd, easy forLoopStart, easy imageBatchToImageList, easy imageListToImageBatch, easy int, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein 9B图片编辑｜分块无限放大角色一致性高清图生图_2093059675297247234.json, 图片生成/图生图/Klein-9B图片编辑｜分块无限放大角色一致性高清_2093215234919063553.json, 图片生成/图生图/Klein_9B图片编辑｜分块无限放大角色一致性高清图生图_2093524472065257474.json, 图片生成/图生图/Klein_9B图片编辑｜分块无限放大角色一致性高清图生图_2093621771516862465.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_60

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Klein 9B图片编辑｜分块无限放大角色一致性高清图生图_2093059675297247234.json、图片生成/图生图/Klein-9B图片编辑｜分块无限放大角色一致性高清_2093215234919063553.json、图片生成/图生图/Klein_9B图片编辑｜分块无限放大角色一致性高清图生图_2093524472065257474.json、图片生成/图生图/Klein_9B图片编辑｜分块无限放大角色一致性高清图生图_2093621771516862465.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_ImagePreview`
- `AILab_Preview`
- `BatchImagesNode`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `Display Int (rgthree)`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSizeAndCount`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageMergeTileList`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `ImageScaleToMaxDimension`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2TorchCompileSettings`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SplitImageToTileList`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy float`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy int`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 2/4 个有

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
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
