---
name: text_to_image_upscale_lora_sampler_32
type: Text To Image
frequency: 7
level: weak
coverage: 0.844571
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/3采样无限裂变｜Krea2图生图4K高清批量产出_2089070522083663874.json, 图片生成/图生图/4K高清图生图无限裂变｜Krea2三采样画质增强批量出图_2088727564708831234.json, 图片生成/图生图/Krea2 图生图无限裂变（3采样）4K高清_2085266353233158146.json, 图片生成/图生图/Qwen-Image-2.1 写实照片转动漫｜二次元风格化_2112483717431255042.json, 图片生成/图生图/Qwen_image_2.1高清修复流程，老图一键放大到4K_2113105105196249089.json, 图片生成/文生图/Krea2 图生图无限裂变（3采样）4K高清_2074851653878112257.json, 图片生成/文生图/Qwen Image 2.1文生图图生视频高清工作流合集处理工具_2102497280900296705.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_32

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/3采样无限裂变｜Krea2图生图4K高清批量产出_2089070522083663874.json、图片生成/图生图/4K高清图生图无限裂变｜Krea2三采样画质增强批量出图_2088727564708831234.json、图片生成/图生图/Krea2 图生图无限裂变（3采样）4K高清_2085266353233158146.json、图片生成/图生图/Qwen-Image-2.1 写实照片转动漫｜二次元风格化_2112483717431255042.json、图片生成/图生图/Qwen_image_2.1高清修复流程，老图一键放大到4K_2113105105196249089.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
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
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 6/7 个有
- `LayerUtility: PurgeVRAM` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `JjkText` —— 5/7 个有
- `solarL_SaveImagesToZip` —— 5/7 个有
- `ConditioningZeroOut` —— 4/7 个有
- `ConstrainImage|pysssss` —— 4/7 个有
- `Get Image Size` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `PurgeVRAM_UTK` —— 4/7 个有
- `RMBG` —— 4/7 个有
- `RTXVideoSuperResolution` —— 4/7 个有
- `TTResolutionSelector` —— 4/7 个有
- `TextEncodeQwenImageEditPlus` —— 4/7 个有
- `VAEEncode` —— 4/7 个有
- `孤海注释` —— 4/7 个有
- `ComfySwitchNode` —— 3/7 个有
- `GetNode` —— 3/7 个有
- `ResolutionSelector` —— 3/7 个有
- `SetNode` —— 3/7 个有
- `TextEncodeQwenImage21` —— 3/7 个有
- `QwenImage21Cache` —— 2/7 个有
- `Any Switch (rgthree)` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `EmptyImage` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `ImageConcanate` —— 1/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `Latent Switch (JPS)` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 512 | 7 | 4% |
| 高度 | 80 | 80 - 512 | 7 | 4% |
| 采样步数 | 4 | 2 - 4 | 7 | 74% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 7 | 55% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 71% |
| 重绘幅度 | 1 | 0.3 - 1 | 7 | 60% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 512，7 个样本，取值分散，一致性仅 4%
- 高度 中位数 80，观测区间 80 - 512，7 个样本，取值分散，一致性仅 4%
- 采样步数 中位数 4，观测区间 2 - 4，7 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，7 个样本
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，7 个样本
- 高发问题（18/7 个样本）：Steps较低可能导致细节不足
