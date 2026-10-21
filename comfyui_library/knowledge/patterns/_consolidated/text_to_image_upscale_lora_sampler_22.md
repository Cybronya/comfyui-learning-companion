---
name: text_to_image_upscale_lora_sampler_22
type: Text To Image
frequency: 5
level: weak
coverage: 0.8542
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), ImageResize+, ImageScaleBy, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 图生图无限裂变（3采样）4K高清_2074851653878112257.json, 图片生成/文生图/Qwen2512 文生图工作流_2071432588077654017.json, 图片生成/文生图/Z-Image文生图+TTP高清放大_2059978387187388417.json, 图片生成/文生图/ZImage文生图（TTP高清4K）_2096553840748355585.json, 图片生成/文生图/人像写真 美图生成洗图 虚拟美女模特 Z-Image文生图_提示词反推+SeedVR2TTP高清放大_2060190994372579329.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_22

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Krea2 图生图无限裂变（3采样）4K高清_2074851653878112257.json、图片生成/文生图/Qwen2512 文生图工作流_2071432588077654017.json、图片生成/文生图/Z-Image文生图+TTP高清放大_2059978387187388417.json、图片生成/文生图/ZImage文生图（TTP高清4K）_2096553840748355585.json、图片生成/文生图/人像写真 美图生成洗图 虚拟美女模特 Z-Image文生图_提示词反推+SeedVR2TTP高清放大_2060190994372579329.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
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
- `ConditioningZeroOut` —— 4/5 个有
- `ConstrainImage|pysssss` —— 4/5 个有
- `Get Image Size` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `PurgeVRAM_UTK` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `RTXVideoSuperResolution` —— 1/5 个有
- `TTResolutionSelector` —— 1/5 个有
- `TextEncodeQwenImageEditPlus` —— 1/5 个有
- `VAEEncode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1080 | 5 | 77% |
| 高度 | 1536 | 512 - 1920 | 5 | 66% |
| 采样步数 | 10 | 2 - 25 | 5 | 34% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 5 | 25% |
| 采样算法 | dpmpp_2m_sde | - | 5 | 60% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0.3 - 1 | 5 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1080，5 个样本
- 高度 中位数 1536，观测区间 512 - 1920，5 个样本
- 采样步数 中位数 10，观测区间 2 - 25，5 个样本，取值分散，一致性仅 34%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 dpmpp_2m_sde，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，5 个样本
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
