---
name: image_to_image_upscale_lora_sampler_61
type: Image To Image
frequency: 3
level: moderate
coverage: 0.898
common_nodes: [Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2 换脸-换头-换人工作流_2085541338174541825.json, 图片生成/图生图/一亿像素F2K+TTP+SeedVR2分块放大工作流_2035211798223261698.json, 图片生成/图生图/溶图_2004450924959596546.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_61

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Krea2 换脸-换头-换人工作流_2085541338174541825.json、图片生成/图生图/一亿像素F2K+TTP+SeedVR2分块放大工作流_2035211798223261698.json、图片生成/图生图/溶图_2004450924959596546.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `CLIPTextEncode` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `GetImageSize+` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `ReferenceLatent` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `DetailTransfer` —— 1/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `EmptyLatentImage` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `Krea2EditGroundedEncode` —— 1/3 个有
- `Krea2EditModelPatch` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `easy imageColorMatch` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有
- `忽略多组孤海` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |
| 采样步数 | 10 | 4 - 30 | 3 | 24% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.7 - 1 | 3 | 84% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 30，3 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，3 个样本，取值集中（一致性 84%）
