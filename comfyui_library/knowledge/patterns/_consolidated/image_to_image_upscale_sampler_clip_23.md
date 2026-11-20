---
name: image_to_image_upscale_sampler_clip_23
type: Image To Image
frequency: 6
level: strong
coverage: 0.715167
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, DF_Integer, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageCASharpening+, ImageListToImageBatch, ImpactMinMax, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, PreviewImage, RHHiddenNodes, SaveImage, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll, easy imageBatchToImageList, easy imageSize, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问edit2511版一键动漫卡通转真人支持各种画风零偏移2K直出+red Z重绘修复细节+可选4K高清放大_1904700984499613698.json, 图片生成/图生图/迄今超强极速FLUX2 Klein-9b单图_双图_多图编辑极速出图+可选高清4K放大V2_2013181887820337154.json, 图片生成/图生图/迄今超强极速出图FLUX2 Klein-9b单图_双图_多图编辑极速出图+可选高清4K放大_2013168195938557954.json, 图片生成/图生图/迄今超强极速出图FLUX2 Klein-9b单图_双图_多图编辑极速出图+可选高清4K放大_2070157661773058049.json, 图片生成/图生图/迄今超强极速出图潜力无穷FLUX2 Klein-9b单图_双图_多图编辑极速出图+可选高清4K放大_2013152768189538305.json, 图片生成/文生图/迄今超强极速出图FLUX2 Klein-9b单图_双图_多图编辑极速出图+可选高清4K放大_2090309370855907329.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/千问edit2511版一键动漫卡通转真人支持各种画风零偏移2K直出+red Z重绘修复细节+可选4K高清放大_1904700984499613698.json、图片生成/图生图/迄今超强极速FLUX2 Klein-9b单图_双图_多图编辑极速出图+可选高清4K放大V2_2013181887820337154.json、图片生成/图生图/迄今超强极速出图FLUX2 Klein-9b单图_双图_多图编辑极速出图+可选高清4K放大_2013168195938557954.json、图片生成/图生图/迄今超强极速出图FLUX2 Klein-9b单图_双图_多图编辑极速出图+可选高清4K放大_2070157661773058049.json、图片生成/图生图/迄今超强极速出图潜力无穷FLUX2 Klein-9b单图_双图_多图编辑极速出图+可选高清4K放大_2013152768189538305.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DF_Integer`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageListToImageBatch`
- `ImpactMinMax`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
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
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy imageBatchToImageList`
- `easy imageSize`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 5/6 个有
- `CR Latent Input Switch` —— 5/6 个有
- `CR SDXL Aspect Ratio` —— 5/6 个有
- `EmptyFlux2LatentImage` —— 5/6 个有
- `FluxGuidance` —— 5/6 个有
- `FluxKontextImageScale` —— 5/6 个有
- `GetNode` —— 5/6 个有
- `ImageConcatMulti` —— 5/6 个有
- `ReferenceLatent` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `Anything Everywhere` —— 1/6 个有
- `CFGNorm` —— 1/6 个有
- `CheckpointLoaderSimple` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `ModelSamplingAuraFlow` —— 1/6 个有
- `QwenEditAdaptiveLongestEdge` —— 1/6 个有
- `QwenEditConfigPreparer` —— 1/6 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 1/6 个有
- `easy float` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
