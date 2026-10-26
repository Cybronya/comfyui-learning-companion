---
name: text_to_image_upscale_lora_sampler_66
type: Text To Image
frequency: 4
level: strong
coverage: 0.87525
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageResize+, ImageScaleBy, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/6K保留质感究极放大｜seedVR2+ttp一分钟出图_2096335787100041218.json, 图片生成/图生图/一亿像素极速放大｜SeedVR2+TTP高清处理_2092884432926629890.json, 图片生成/图生图/一键效果图重新打光高清放大，图生图免费测试版快速出图_2112629848454819842.json, 图片生成/图生图/谷迹终极一键效果图｜免费测试版带水印直出_2112431895173750786.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_66

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/6K保留质感究极放大｜seedVR2+ttp一分钟出图_2096335787100041218.json、图片生成/图生图/一亿像素极速放大｜SeedVR2+TTP高清处理_2092884432926629890.json、图片生成/图生图/一键效果图重新打光高清放大，图生图免费测试版快速出图_2112629848454819842.json、图片生成/图生图/谷迹终极一键效果图｜免费测试版带水印直出_2112431895173750786.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
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
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `FloatSlider` —— 2/4 个有
- `ImpactMinMax` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `RHHiddenNodes` —— 2/4 个有
- `Seed_` —— 2/4 个有
- `easy boolean` —— 2/4 个有
- `easy int` —— 2/4 个有
- `Float` —— 1/4 个有
- `Int` —— 1/4 个有
- `KOOK_ImageCompression` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
