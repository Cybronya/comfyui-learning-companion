---
name: unknown_workflow_upscale_sampler_clip_43
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.841
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageListToImageBatch, ImageResizeKJ, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/高清放大工作流v1_1891665306362793985.json, 图片生成/图生图/高清无损放大（自定义放大倍数）_2057424072681807873.json, 图片生成/文生图/kontext 文生图+图生图  后期高清放大_1931964242503905282.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_43

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/高清放大工作流v1_1891665306362793985.json、图片生成/图生图/高清无损放大（自定义放大倍数）_2057424072681807873.json、图片生成/文生图/kontext 文生图+图生图  后期高清放大_1931964242503905282.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `Joy_caption_two` —— 2/3 个有
- `Joy_caption_two_load` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `JanusImageUnderstanding` —— 1/3 个有
- `JanusModelLoader` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `RH_ComfyFluxKontext` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `workflow/modes组` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
