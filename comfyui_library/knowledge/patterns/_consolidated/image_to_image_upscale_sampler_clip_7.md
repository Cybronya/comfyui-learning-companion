---
name: image_to_image_upscale_sampler_clip_7
type: Image To Image
frequency: 2
level: weak
coverage: 0.715
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DF_Integer, FluxGuidance, GetNode, Image Comparer (rgthree), ImageCASharpening+, ImageListToImageBatch, ImpactMinMax, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, PreviewImage, RHHiddenNodes, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageSize, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/迄今超强极速出图FLUX2 Klein-9b单图_双图_多图编辑极速出图+可选高清4K放大_2090309370855907329.json, 视频生成/文生视频/皮肤质感_2086968485917323265.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/迄今超强极速出图FLUX2 Klein-9b单图_双图_多图编辑极速出图+可选高清4K放大_2090309370855907329.json、视频生成/文生视频/皮肤质感_2086968485917323265.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DF_Integer`
- `FluxGuidance`
- `GetNode`
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
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageSize`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `CR Latent Input Switch` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `CR SDXL Aspect Ratio` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `EmptyFlux2LatentImage` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `ImageColorMatch+` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `MagCache` —— 1/2 个有
- `ModelSamplingSD3` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有
- `SeedVR2GGUF` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有
- `easy float` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.575 | - | 2 | 26% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.575，样本不足，未给区间，2 个样本，取值分散，一致性仅 26%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
