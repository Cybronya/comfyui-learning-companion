---
name: text_to_image_upscale_lora_sampler_56
type: Text To Image
frequency: 4
level: weak
coverage: 0.843
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ConstrainImage|pysssss, EmptyLatentImage, Fast Groups Bypasser (rgthree), Get Image Size, Image Comparer (rgthree), ImageResize+, ImageResizeKJv2, ImageScaleBy, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, PurgeVRAM_UTK, RMBG, RTXVideoSuperResolution, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TTResolutionSelector, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/3采样无限裂变｜Krea2图生图4K高清批量产出_2089070522083663874.json, 图片生成/图生图/4K高清图生图无限裂变｜Krea2三采样画质增强批量出图_2088727564708831234.json, 图片生成/图生图/Krea2 图生图无限裂变（3采样）4K高清_2085266353233158146.json, 图片生成/文生图/Krea2 图生图无限裂变（3采样）4K高清_2074851653878112257.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_56

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/3采样无限裂变｜Krea2图生图4K高清批量产出_2089070522083663874.json、图片生成/图生图/4K高清图生图无限裂变｜Krea2三采样画质增强批量出图_2088727564708831234.json、图片生成/图生图/Krea2 图生图无限裂变（3采样）4K高清_2085266353233158146.json、图片生成/文生图/Krea2 图生图无限裂变（3采样）4K高清_2074851653878112257.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `PurgeVRAM_UTK`
- `RMBG`
- `RTXVideoSuperResolution`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TTResolutionSelector`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/4 个有
- `solarL_SaveImagesToZip` —— 2/4 个有
- `孤海注释` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 296 | 80 - 512 | 4 | 27% |
| 高度 | 296 | 80 - 512 | 4 | 27% |
| 采样步数 | 3 | 2 - 4 | 4 | 67% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4.5 | 4 | 36% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 50% |
| 重绘幅度 | 0.65 | 0.3 - 1 | 4 | 46% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 296，观测区间 80 - 512，4 个样本，取值分散，一致性仅 27%
- 高度 中位数 296，观测区间 80 - 512，4 个样本，取值分散，一致性仅 27%
- 采样步数 中位数 3，观测区间 2 - 4，4 个样本
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4.5，4 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 50%
- 重绘幅度 中位数 0.65，观测区间 0.3 - 1，4 个样本，取值分散，一致性仅 46%
- 高发问题（14/4 个样本）：Steps较低可能导致细节不足
