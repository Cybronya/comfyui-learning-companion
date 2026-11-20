---
name: image_to_image_upscale_lora_sampler_80
type: Image To Image
frequency: 2
level: weak
coverage: 0.906
common_nodes: [CLIPLoader, Image Comparer (rgthree), ImageResize+, ImageResizeKJv2, ImageScaleBy, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2 换脸-换头-换人工作流_2085541338174541825.json, 图片生成/图生图/一亿像素F2K+TTP+SeedVR2分块放大工作流_2035211798223261698.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_80

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Krea2 换脸-换头-换人工作流_2085541338174541825.json、图片生成/图生图/一亿像素F2K+TTP+SeedVR2分块放大工作流_2035211798223261698.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
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
- `CLIPTextEncode` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `GetImageSize+` —— 1/2 个有
- `Krea2EditGroundedEncode` —— 1/2 个有
- `Krea2EditModelPatch` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `easy imageColorMatch` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有
- `忽略多组孤海` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |
| 采样步数 | 7 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.85 | - | 2 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
