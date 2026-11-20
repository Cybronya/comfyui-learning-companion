---
name: image_to_image_upscale_sampler_clip_62
type: Image To Image
frequency: 2
level: weak
coverage: 0.8155
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningAverage, ConditioningZeroOut, GetImageSize, Image Comparer (rgthree), ImageResizeKJv2, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/image+TTP放大、修复、洗图，超级细腻_2054378266760359938.json, 平台全量/z image 专用分块4K高清-ttp版本_2005320792026083329.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_62

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/image+TTP放大、修复、洗图，超级细腻_2054378266760359938.json、平台全量/z image 专用分块4K高清-ttp版本_2005320792026083329.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningAverage`
- `ConditioningZeroOut`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `APersonMaskGenerator` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `Florence2ModelLoader` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `ImageCompositeMasked` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Qwen3VL_Advanced` —— 1/2 个有
- `ResizeMask` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `Text Concatenate (JPS)` —— 1/2 个有
- `TextInput_` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.2 | - | 2 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.2，样本不足，未给区间，2 个样本
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
