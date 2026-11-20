---
name: text_to_image_upscale_lora_sampler_125
type: Text To Image
frequency: 2
level: weak
coverage: 0.845
common_nodes: [CLIPLoader, CLIPTextEncode, ConstrainImage|pysssss, EmptyLatentImage, Get Image Size, Image Comparer (rgthree), ImageCASharpening+, ImageFromBatch, ImageResize+, ImageScaleToTotalPixels, ImageSharpen, ImageUpscaleWithModel, ImpactMinMax, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RH_Captioner, SaveImage, SeedVR2, SeedVR2BlockSwap, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy batchAnything, easy cleanGpuUsed, easy compare, easy forLoopEnd, easy forLoopStart, easy ifElse, easy imageBatchToImageList, easy imageColorMatch, easy imageCount, easy imageListToImageBatch, easy imageSize, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/建筑效果图＋wan2.2ttp高清放大_1919298729009156097.json, 图片生成/文生图/Wan2.2极致coser写真工作流（流萤lora）v2_1960194933040820225.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_125

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/建筑效果图＋wan2.2ttp高清放大_1919298729009156097.json、图片生成/文生图/Wan2.2极致coser写真工作流（流萤lora）v2_1960194933040820225.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConstrainImage|pysssss`
- `EmptyLatentImage`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageFromBatch`
- `ImageResize+`
- `ImageScaleToTotalPixels`
- `ImageSharpen`
- `ImageUpscaleWithModel`
- `ImpactMinMax`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RH_Captioner`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy compare`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageCount`
- `easy imageListToImageBatch`
- `easy imageSize`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `ApplyFBCacheOnModel` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `IPAdapterAdvanced` —— 1/2 个有
- `IPAdapterUnifiedLoader` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `JoinStrings` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `LayerUtility: GetImageSize` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `SaveLatent` —— 1/2 个有
- `Seed_` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.75 | - | 1 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 3 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 0.1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 0.1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
