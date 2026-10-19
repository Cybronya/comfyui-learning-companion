---
name: image_to_image_upscale_lora_sampler_7
type: Image To Image
frequency: 2
level: weak
coverage: 0.8505
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, Flux2Scheduler, FluxKVCache, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, easy cleanGpuUsed, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, SimpleMath+, easy cleanGpuUsed, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch]
members: [图片生成/图生图/1914251049425694721.json, 视频生成/图生视频/2079739645310619650.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/1914251049425694721.json、视频生成/图生视频/2079739645310619650.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EditTextEncode_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `Flux2Scheduler`
- `FluxKVCache`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `ColorMatchPro` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Flux2KleinEditTextEncode_EditUtils` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `LCSColorAnchor` —— 1/2 个有
- `LCSLoadData` —— 1/2 个有
- `LatentColorMatchSimple` —— 1/2 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/2 个有
- `MemoryCleaner` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `SeedVR2Conditioning` —— 1/2 个有
- `SeedVR2Preprocess` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `TTP_Image_Assy` —— 1/2 个有
- `TTP_Image_Tile_Batch` —— 1/2 个有
- `TTP_Tile_image_size` —— 1/2 个有
- `easy imageBatchToImageList` —— 1/2 个有
- `easy imageListToImageBatch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 2.5 | - | 2 | 40% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 50% |
| 调度器 | linear_quadratic | - | 2 | 50% |
| 重绘幅度 | 0.7 | - | 2 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 50%
- 调度器 最常用 linear_quadratic，2 个样本，一致性 50%
- 重绘幅度 中位数 0.7，样本不足，未给区间，2 个样本
- 高发问题（5/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: ImageScaleRestore V2、SimpleMath+、easy cleanGpuUsed、easy imageBatchToImageList
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
