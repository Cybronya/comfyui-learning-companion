---
name: image_to_image_upscale_sampler_unet_2
type: Image To Image
frequency: 5
level: strong
coverage: 0.9104
common_nodes: [CLIPLoader, GetImageSize+, ImageResize+, ImageScaleBy, ImageUpscaleWithModel, KSampler, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein 超级模糊变清晰又快又好小神器_2013240772572745729.json, 图片生成/图生图/Qwen千问8K高清放大！效果超赞!_2006346656115073025.json, 图片生成/图生图/Z-image图生图+放大-洗图去重_2071977702432796674.json, 图片生成/图生图/千问2511超清4-8K放大！无损细节，效果完美不偏移！_2011765840563146753.json, 图片生成/图生图/妙笔入梦超细节_2006298076486569986.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_unet_2

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Klein 超级模糊变清晰又快又好小神器_2013240772572745729.json、图片生成/图生图/Qwen千问8K高清放大！效果超赞!_2006346656115073025.json、图片生成/图生图/Z-image图生图+放大-洗图去重_2071977702432796674.json、图片生成/图生图/千问2511超清4-8K放大！无损细节，效果完美不偏移！_2011765840563146753.json、图片生成/图生图/妙笔入梦超细节_2006298076486569986.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `DapaoImageAspectRatioResizeNode` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `ReferenceLatent` —— 4/5 个有
- `Seed (rgthree)` —— 3/5 个有
- `TextEncodeQwenImageEditPlus` —— 3/5 个有
- `easy imageColorMatch` —— 3/5 个有
- `CLIPTextEncode` —— 2/5 个有
- `DapaoImageCompressionNode` —— 2/5 个有
- `ColorMatch` —— 1/5 个有
- `DapaoSafeSaveImage` —— 1/5 个有
- `EmptyFlux2LatentImage` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `WujiCleaner` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 9 | 5 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0.6 - 1 | 5 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 9，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，5 个样本，取值集中（一致性 83%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
