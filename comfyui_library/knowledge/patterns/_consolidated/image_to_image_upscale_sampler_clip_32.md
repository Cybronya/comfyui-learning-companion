---
name: image_to_image_upscale_sampler_clip_32
type: Image To Image
frequency: 3
level: moderate
coverage: 0.877667
common_nodes: [CLIPLoader, CLIPTextEncode, ImageListToImageBatch, ImageUpscaleWithModel, KSampler, LoadImage, ModelSamplingSD3, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/wan高清写实放大api_1957979462142935041.json, 图片生成/图生图/万相2.2高清放大TTP放大_1946954453464952834.json, 图片生成/图生图/（高清放大）Wan2.2 - 14B - 加速版 -  图片高清放大_1977811440935600129.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/wan高清写实放大api_1957979462142935041.json、图片生成/图生图/万相2.2高清放大TTP放大_1946954453464952834.json、图片生成/图生图/（高清放大）Wan2.2 - 14B - 加速版 -  图片高清放大_1977811440935600129.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageListToImageBatch`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `ConstrainImage|pysssss` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LayerUtility: BooleanOperatorV2` —— 1/3 个有
- `LayerUtility: If ` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `easy imageScaleDownToSize` —— 1/3 个有
- `easy int` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 5 - 10 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | heun | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 0.1 | 0.1 - 0.2 | 3 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 5 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 heun，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 0.1，观测区间 0.1 - 0.2，3 个样本
