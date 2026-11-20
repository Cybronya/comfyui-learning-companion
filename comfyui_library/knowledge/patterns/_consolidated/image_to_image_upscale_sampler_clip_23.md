---
name: image_to_image_upscale_sampler_clip_23
type: Image To Image
frequency: 7
level: moderate
coverage: 0.874857
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), ImageListToImageBatch, ImageUpscaleWithModel, KSampler, LoadImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Zimage高清放大-tile-ttp_2091322574046318593.json, 平台全量/wan2.2图像高清放大 ttp版本_1950337532607291394.json, 平台全量/wan人像放大工作流_2041436328868450306.json, 平台全量/z-Image-4k-8k高清放大_1993988824430821378.json, 平台全量/【Wan2.2图像放大】 人物模特超清8K真实纹理_2046533363250503682.json, 平台全量/【Wan2.2图像放大】 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像一键放大_1997898218027540482.json, 平台全量/偏写实风格放大细化流程_2048597505096556545.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/Zimage高清放大-tile-ttp_2091322574046318593.json、平台全量/wan2.2图像高清放大 ttp版本_1950337532607291394.json、平台全量/wan人像放大工作流_2041436328868450306.json、平台全量/z-Image-4k-8k高清放大_1993988824430821378.json、平台全量/【Wan2.2图像放大】 人物模特超清8K真实纹理_2046533363250503682.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageUpscaleWithModel`
- `KSampler`
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

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `easy cleanGpuUsed` —— 6/7 个有
- `ModelSamplingSD3` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `ModelPatchLoader` —— 2/7 个有
- `QwenImageDiffsynthControlnet` —— 2/7 个有
- `TilePreprocessor` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有
- `CR Text Input Switch` —— 1/7 个有
- `ConditioningClamp` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `Float` —— 1/7 个有
- `LayerMask: LoadFlorence2Model` —— 1/7 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 5 - 10 | 7 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | heun | - | 7 | 71% |
| 调度器 | beta | - | 7 | 86% |
| 重绘幅度 | 0.1 | 0.1 - 0.3 | 7 | 47% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 5 - 10，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 heun，7 个样本，一致性 71%
- 调度器 最常用 beta，7 个样本，一致性 86%
- 重绘幅度 中位数 0.1，观测区间 0.1 - 0.3，7 个样本，取值分散，一致性仅 47%
