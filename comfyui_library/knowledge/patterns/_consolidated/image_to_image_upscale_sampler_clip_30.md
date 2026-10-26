---
name: image_to_image_upscale_sampler_clip_30
type: Image To Image
frequency: 3
level: weak
coverage: 0.9
common_nodes: [CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), ImageListToImageBatch, ImageUpscaleWithModel, ImpactImageBatchToImageList, KSampler, LoadImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/RFMSR 放大+Z-image图像优化放大 🍺_2084172739774083074.json, 图片生成/图生图/TTP放大-自用-满血效果_1989182643759616001.json, 图片生成/图生图/无损细节高清放大【基于WAN_FLUX的TTP】_1963811400824213506.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_30

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/RFMSR 放大+Z-image图像优化放大 🍺_2084172739774083074.json、图片生成/图生图/TTP放大-自用-满血效果_1989182643759616001.json、图片生成/图生图/无损细节高清放大【基于WAN_FLUX的TTP】_1963811400824213506.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `DualCLIPLoader` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ModelSamplingSD3` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_RFMSR_ModelLoader` —— 1/3 个有
- `RH_RFMSR_Upscale` —— 1/3 个有
- `VAEDecode` —— 1/3 个有
- `easy imageBatchToImageList` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 30 | 3 | 41% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 33% |
| 重绘幅度 | 0.3 | 0.2 - 0.9 | 3 | 34% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 30，3 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 33%
- 重绘幅度 中位数 0.3，观测区间 0.2 - 0.9，3 个样本，取值分散，一致性仅 34%
- 高发问题（2/3 个样本）：发现KSampler但没有VAEDecode
