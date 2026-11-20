---
name: image_to_image_upscale_sampler_unet
type: Image To Image
frequency: 11
level: strong
coverage: 0.861182
common_nodes: [CLIPLoader, GetImageSize+, ImageResize+, ImageScaleBy, ImageUpscaleWithModel, KSampler, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein 超级模糊变清晰又快又好小神器_2013240772572745729.json, 图片生成/图生图/Qwen千问8K高清放大！效果超赞!_2006346656115073025.json, 图片生成/图生图/Z-image图生图+放大-洗图去重_2071977702432796674.json, 图片生成/图生图/千问2511超清4-8K放大！无损细节，效果完美不偏移！_2011765840563146753.json, 图片生成/图生图/妙笔入梦超细节_2006298076486569986.json, 平台全量/Klein 一款快速高清的神器_2013185495823556609.json, 平台全量/Klein+Seed VR2 超级模糊变清晰_2054391782414266370.json, 平台全量/Qwen 千问8K放大！效果超赞  图片高清修复 写实无损放大  真实造像大师  纤毫毕现 极清人像_2015335030859505666.json, 平台全量/千问2511—8K放大_2006361465183277058.json, 平台全量/千问8K放大！效果超赞~_2026277599445520385.json, 平台全量/🤴Klein 超级模糊变清晰又快又好小神器 🤴_2013104685179215873.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_unet

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Klein 超级模糊变清晰又快又好小神器_2013240772572745729.json、图片生成/图生图/Qwen千问8K高清放大！效果超赞!_2006346656115073025.json、图片生成/图生图/Z-image图生图+放大-洗图去重_2071977702432796674.json、图片生成/图生图/千问2511超清4-8K放大！无损细节，效果完美不偏移！_2011765840563146753.json、图片生成/图生图/妙笔入梦超细节_2006298076486569986.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 10/11 个有
- `DapaoImageAspectRatioResizeNode` —— 10/11 个有
- `Image Comparer (rgthree)` —— 10/11 个有
- `ReferenceLatent` —— 10/11 个有
- `LoraLoaderModelOnly` —— 7/11 个有
- `ModelSamplingAuraFlow` —— 7/11 个有
- `Seed (rgthree)` —— 6/11 个有
- `TextEncodeQwenImageEditPlus` —— 6/11 个有
- `easy imageColorMatch` —— 6/11 个有
- `CLIPTextEncode` —— 5/11 个有
- `DapaoImageCompressionNode` —— 5/11 个有
- `ColorMatch` —— 4/11 个有
- `EmptyFlux2LatentImage` —— 4/11 个有
- `Fast Groups Bypasser (rgthree)` —— 4/11 个有
- `GetImageSize` —— 4/11 个有
- `GetNode` —— 3/11 个有
- `LayerUtility: ImageReel` —— 3/11 个有
- `LayerUtility: ImageReelComposit` —— 3/11 个有
- `SetNode` —— 3/11 个有
- `Note Plus (mtb)` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `DapaoSafeSaveImage` —— 1/11 个有
- `ImageScaleToTotalPixels` —— 1/11 个有
- `LayerUtility: PurgeVRAM` —— 1/11 个有
- `WujiCleaner` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 9 | 11 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 0.6 - 1 | 11 | 88% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 9，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，11 个样本，取值集中（一致性 88%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
