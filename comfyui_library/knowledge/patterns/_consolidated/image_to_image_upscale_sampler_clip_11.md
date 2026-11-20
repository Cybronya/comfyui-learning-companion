---
name: image_to_image_upscale_sampler_clip_11
type: Image To Image
frequency: 10
level: moderate
coverage: 0.9135
common_nodes: [CLIPTextEncode, ConditioningZeroOut, GetImageSize+, ImageResize+, ImageScaleBy, KSampler, LoadImage, ReferenceLatent, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2_klein_TrueV2多图编辑+SeedVR2放大_2056926047752507394.json, 图片生成/图生图/Flux2_klein_TrueV2编辑模型+SeedVR2放大_2056924292906053633.json, 图片生成/图生图/Flux2最新修复 高清放大_细节增强- 极速修复_2053278696852729857.json, 图片生成/图生图/Flux2最新修复_高清放大_细节增强-_极速修复_2053320142259531778.json, 图片生成/图生图/High-Definition Zoom_Detail Enhancement 高清放大_细节增强-_2104029734995845121.json, 图片生成/图生图/KOOK_Flux2 Klein 图像编辑9B_人像质感修复 V1_2012082787196604417.json, 图片生成/图生图/Kontext全能精修电商产品精修_2057766481882083329.json, 图片生成/图生图/kontext全能精修产品精修人像精修婚纱照精修全能精修_2044780452099137538.json, 图片生成/图生图/kontext全能精修产品精修电商产品精修_2054546020247326722.json, 图片生成/图生图/图片_Flux-Klein+SeedVR2放大_2077934290356236289.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_11

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Flux2_klein_TrueV2多图编辑+SeedVR2放大_2056926047752507394.json、图片生成/图生图/Flux2_klein_TrueV2编辑模型+SeedVR2放大_2056924292906053633.json、图片生成/图生图/Flux2最新修复 高清放大_细节增强- 极速修复_2053278696852729857.json、图片生成/图生图/Flux2最新修复_高清放大_细节增强-_极速修复_2053320142259531778.json、图片生成/图生图/High-Definition Zoom_Detail Enhancement 高清放大_细节增强-_2104029734995845121.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 9/10 个有
- `easy cleanGpuUsed` —— 8/10 个有
- `CLIPLoader` —— 7/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/10 个有
- `PreviewImage` —— 7/10 个有
- `Fast Groups Bypasser (rgthree)` —— 6/10 个有
- `Image Comparer (rgthree)` —— 6/10 个有
- `LoraLoaderModelOnly` —— 5/10 个有
- `Float` —— 4/10 个有
- `LatentUpscaleBy` —— 4/10 个有
- `DualCLIPLoader` —— 3/10 个有
- `FluxGuidance` —— 3/10 个有
- `Int` —— 3/10 个有
- `easy imageScaleDownBy` —— 3/10 个有
- `ResizeLongestToNode` —— 2/10 个有
- `CR Text` —— 1/10 个有
- `ChangeImageBatchSize //Inspire` —— 1/10 个有
- `EmptyFlux2LatentImage` —— 1/10 个有
- `GetImageSize` —— 1/10 个有
- `ImageCASharpening+` —— 1/10 个有
- `KOOK_SaveJPGImage` —— 1/10 个有
- `RunningHub Deepcleaner` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 12 | 10 | 56% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 0.5 - 1 | 10 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 12，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，10 个样本，取值集中（一致性 83%）
- 高发问题（7/10 个样本）：Steps较低可能导致细节不足
