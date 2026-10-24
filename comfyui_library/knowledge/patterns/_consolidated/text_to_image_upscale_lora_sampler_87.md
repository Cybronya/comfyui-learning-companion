---
name: text_to_image_upscale_lora_sampler_87
type: Text To Image
frequency: 3
level: strong
coverage: 0.873333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, GrowMask, Image Comparer (rgthree), ImageUpscaleWithModel, InvertMask, JjkText, JoinImageWithAlpha, KSampler, KSamplerSelect, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, Upscale Model Loader, VAEDecode, VAEEncode, VAELoader, YUAN_TXTConvertAny, easy cleanGpuUsed, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/产品精修工作流 电商商品图高质量处理方案_2104999525751541761.json, 图片生成/图生图/产品精修工作流，图生图电商产品细节增强处理工具_2105765084374065153.json, 图片生成/图生图/产品精修工作流｜精修打光图生图｜电商商品图影棚级质感_2104781884969537537.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_87

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/产品精修工作流 电商商品图高质量处理方案_2104999525751541761.json、图片生成/图生图/产品精修工作流，图生图电商产品细节增强处理工具_2105765084374065153.json、图片生成/图生图/产品精修工作流｜精修打光图生图｜电商商品图影棚级质感_2104781884969537537.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `GrowMask`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `InvertMask`
- `JjkText`
- `JoinImageWithAlpha`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `Upscale Model Loader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `YUAN_TXTConvertAny`
- `easy cleanGpuUsed`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `ImpactInt` —— 2/3 个有
- `ImpactMinMax` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `TTP_Image_Assy` —— 2/3 个有
- `TTP_Image_Tile_Batch` —— 2/3 个有
- `UltimateSDUpscaleCustomSample` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `easy imageScaleDownToSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
