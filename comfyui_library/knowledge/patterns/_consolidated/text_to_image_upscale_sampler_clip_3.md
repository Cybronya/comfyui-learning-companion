---
name: text_to_image_upscale_sampler_clip_3
type: Text To Image
frequency: 19
level: weak
coverage: 0.878947
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageResize+, ImageScaleBy, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Rika-zit去水印放大真实人像流_2057641336878227458.json, 图片生成/文生图/Z-Image 一键出图，细节拉满 8K_2104461803777519617.json, 图片生成/文生图/Z-Image 图片生图片，文字生图片高清放大_2013423377024819202.json, 图片生成/文生图/Z-Image 在线工具｜一键 8K 高清原图直出_2086062971993808898.json, 图片生成/文生图/Z-Image 文生图｜分块放大·2倍预检_2098694544182308865.json, 图片生成/文生图/Z-Image-turbo_文生图8K直出_2018494305006002178.json, 图片生成/文生图/Z-Image8K直出_2018854704565981185.json, "图片生成/文生图/Z-Image【全新VAE Z_image_turbo-VAE,加强细节更高清】_2015214610697162753.json", 图片生成/文生图/Z-Image文生图+4320_7680_2062034472941477889.json, 图片生成/文生图/Z-Image文生图_2064637986431660033.json, 图片生成/文生图/Z-Image文生图（_2003443734752706561.json, 图片生成/文生图/Z-Image文生图（_2039874309291778050.json, 图片生成/文生图/Z-Image文生图（可大尺度）_2004890910724943874.json, 图片生成/文生图/Z-image 文生图+无损8K高清放大版本_2003443997819453442.json, 图片生成/文生图/Zimage-艺术人像摄影_如梦似幻-Kook版 文生图_2078417819166920705.json, 图片生成/文生图/Zimage-艺术人像摄影_如梦似幻-Kook版 文生图_2078469610759872514.json, 图片生成/文生图/文生图+高清放大Z-image（lora真实幻想+如梦似幻）+全节点注释_2085274976416002049.json, 图片生成/文生图/艺术人像摄影-Zimage_如梦似幻-Kook版_2079187188364955650.json, 图片生成/文生图/随手薅一个文生图-zit 小红书模型+超级放大。_2074677008407293953.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/Rika-zit去水印放大真实人像流_2057641336878227458.json、图片生成/文生图/Z-Image 一键出图，细节拉满 8K_2104461803777519617.json、图片生成/文生图/Z-Image 图片生图片，文字生图片高清放大_2013423377024819202.json、图片生成/文生图/Z-Image 在线工具｜一键 8K 高清原图直出_2086062971993808898.json、图片生成/文生图/Z-Image 文生图｜分块放大·2倍预检_2098694544182308865.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
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
- `PreviewImage` —— 18/19 个有
- `ModelSamplingAuraFlow` —— 14/19 个有
- `PrimitiveFloat` —— 14/19 个有
- `Text Multiline` —— 14/19 个有
- `LoraLoaderModelOnly` —— 13/19 个有
- `DyPE_FLUX` —— 8/19 个有
- `LoadImage` —— 6/19 个有
- `CR Text` —— 5/19 个有
- `ImageCASharpening+` —— 5/19 个有
- `PhotoShakeNode` —— 5/19 个有
- `RunningHub Deepcleaner` —— 5/19 个有
- `easy seed` —— 2/19 个有
- `Fast Groups Bypasser (rgthree)` —— 1/19 个有
- `Int` —— 1/19 个有
- `LayerUtility: ImageReel` —— 1/19 个有
- `LayerUtility: ImageReelComposit` —— 1/19 个有
- `SaveImageJPG_GH` —— 1/19 个有
- `SaveImageToLocal` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 720 - 1920 | 19 | 76% |
| 高度 | 1920 | 1080 - 1920 | 19 | 81% |
| 采样步数 | 9 | 8 - 50 | 19 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 19 | 26% |
| 采样算法 | euler | - | 19 | 74% |
| 调度器 | sgm_uniform | - | 19 | 74% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 720 - 1920，19 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，19 个样本，取值集中（一致性 81%）
- 采样步数 中位数 9，观测区间 8 - 50，19 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，19 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler，19 个样本，一致性 74%
- 调度器 最常用 sgm_uniform，19 个样本，一致性 74%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（19/19 个样本）：Steps较低可能导致细节不足
