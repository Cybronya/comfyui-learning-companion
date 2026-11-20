---
name: image_to_image_upscale_sampler_clip_28
type: Image To Image
frequency: 6
level: moderate
coverage: 0.9255
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, LoadImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人像放大 _ 完美修复_1942199839058767874.json, 图片生成/图生图/图片-高清修复-人物建筑高清修复(不改变细节)_1960016022948491266.json, 平台全量/世间万物-增强质感+4K放大_1965429214486872066.json, 平台全量/人像专用4K放大-增强质感面部还原_1942457303419269121.json, 平台全量/人像专用4K放大-增强质感面部还原_1944364242663559169.json, 平台全量/图片细节高清修复放大_1946604200106029058.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/人像放大 _ 完美修复_1942199839058767874.json、图片生成/图生图/图片-高清修复-人物建筑高清修复(不改变细节)_1960016022948491266.json、平台全量/世间万物-增强质感+4K放大_1965429214486872066.json、平台全量/人像专用4K放大-增强质感面部还原_1942457303419269121.json、平台全量/人像专用4K放大-增强质感面部还原_1944364242663559169.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
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

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `ConstrainImage|pysssss` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `ApplyPulidFlux` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `PulidEvaClipLoader` —— 3/6 个有
- `PulidFluxModelLoader` —— 3/6 个有
- `PulidInsightFaceLoader` —— 3/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `ImageSharpen` —— 2/6 个有
- `Joy_caption_two` —— 2/6 个有
- `Joy_caption_two_load` —— 2/6 个有
- `CR Simple Image Compare` —— 1/6 个有
- `Float` —— 1/6 个有
- `Image Levels Adjustment` —— 1/6 个有
- `easy imageSave` —— 1/6 个有
- `easy imageSize` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 6 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | beta | - | 6 | 67% |
| 重绘幅度 | 0.35 | 0.1 - 0.4 | 6 | 62% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 67%
- 重绘幅度 中位数 0.35，观测区间 0.1 - 0.4，6 个样本
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
