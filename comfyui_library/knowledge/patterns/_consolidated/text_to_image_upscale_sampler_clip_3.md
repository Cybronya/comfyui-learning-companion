---
name: text_to_image_upscale_sampler_clip_3
type: Text To Image
frequency: 28
level: strong
coverage: 0.879857
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageResize+, ImageScaleBy, KSampler, PreviewImage, PrimitiveFloat, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-Image文生图_图生图8K_2034141777422192641.json, 图片生成/图生图/Z-image 图生图+无损8K高清放大版本_2003459369322881025.json, 图片生成/图生图/Z-image图生图（优化版）无损8K高清放大版本_2003799035490279425.json, 图片生成/图生图/二次元重绘（高幅度）_2027284859885981698.json, 图片生成/图生图/洗图重绘Qwen反推提示词i-zimage生图_2028770579750330370.json, 图片生成/图生图/洗图重绘Qwen反推提示词i-zimage生图_2039906645194575874.json, 图片生成/图生图/超级简单+一键生成-文生图+Z-Image在线8K直出_2079719986809102338.json, 图片生成/文生图/Z-Image 一键出图，细节拉满 8K_2104461803777519617.json, 图片生成/文生图/Z-Image 图片生图片，文字生图片高清放大_2013423377024819202.json, 图片生成/文生图/Z-Image 在线工具｜一键 8K 高清原图直出_2086062971993808898.json, 图片生成/文生图/Z-Image 文生图｜分块放大·2倍预检_2098694544182308865.json, 图片生成/文生图/Z-Image-turbo_文生图8K直出_2018494305006002178.json, 图片生成/文生图/Z-Image-在线8K直出_2035195841148887041.json, 图片生成/文生图/Z-Image8K直出_2018854704565981185.json, "图片生成/文生图/Z-Image【全新VAE Z_image_turbo-VAE,加强细节更高清】_2015214610697162753.json", 图片生成/文生图/Z-Image在线8K直出_2003290778174685185.json, 图片生成/文生图/Z-Image在线8K直出_2041399225958801409.json, 图片生成/文生图/Z-Image在线8K直出_2041433488611610626.json, 图片生成/文生图/Z-Image在线8K直出_2046755453375356929.json, 图片生成/文生图/Z-Image在线8K直出_2058716850577563650.json, 图片生成/文生图/Z-Image在线8K直出_2072664211423064066.json, 图片生成/文生图/Z-Image在线8K直出_2072676192607629314.json, 图片生成/文生图/Z-Image在线8K直出_2073387571807342593.json, 图片生成/文生图/Z-Image在线8K直出_2073387973390983170.json, 图片生成/文生图/Z-Image在线8K直出_2081990378743484418.json, 图片生成/文生图/Z-Image在线8K直出_2081993328593301505.json, 图片生成/文生图/Z-Image文生图+4320_7680_2062034472941477889.json, 图片生成/文生图/Z-image 文生图+无损8K高清放大版本_2003443997819453442.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/图生图/Z-Image文生图_图生图8K_2034141777422192641.json、图片生成/图生图/Z-image 图生图+无损8K高清放大版本_2003459369322881025.json、图片生成/图生图/Z-image图生图（优化版）无损8K高清放大版本_2003799035490279425.json、图片生成/图生图/二次元重绘（高幅度）_2027284859885981698.json、图片生成/图生图/洗图重绘Qwen反推提示词i-zimage生图_2028770579750330370.json…）

- **类型**：Text To Image
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 28 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `PreviewImage`
- `PrimitiveFloat`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 26/28 个有
- `Text Multiline` —— 26/28 个有
- `LoraLoaderModelOnly` —— 24/28 个有
- `LoadImage` —— 10/28 个有
- `Qwen3_VQA` —— 5/28 个有
- `ConditioningZeroOut` —— 3/28 个有
- `DyPE_FLUX` —— 3/28 个有
- `Fast Groups Muter (rgthree)` —— 3/28 个有
- `Image Comparer (rgthree)` —— 3/28 个有
- `LayerUtility: ImageReel` —— 3/28 个有
- `LayerUtility: ImageReelComposit` —— 3/28 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/28 个有
- `VAEEncode` —— 3/28 个有
- `GetImageSize` —— 2/28 个有
- `ShowAnything|Mie` —— 2/28 个有
- `CR Text` —— 1/28 个有
- `PrimitiveInt` —— 1/28 个有
- `easy seed` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 10 | 28 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 28 | 100% |
| 采样算法 | euler | - | 28 | 100% |
| 调度器 | sgm_uniform | - | 28 | 93% |
| 重绘幅度 | 1 | 0.2 - 1 | 28 | 85% |
| 宽度 | 1080 | 720 - 1440 | 28 | 91% |
| 高度 | 1920 | 1280 - 1920 | 28 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 31/28 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 10，28 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，28 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，28 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，28 个样本，取值集中（一致性 85%）
- 宽度 中位数 1080，观测区间 720 - 1440，28 个样本，取值集中（一致性 91%）
- 高度 中位数 1920，观测区间 1280 - 1920，28 个样本，取值集中（一致性 92%）
- 高发问题（31/28 个样本）：Steps较低可能导致细节不足
