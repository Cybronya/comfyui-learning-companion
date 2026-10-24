---
name: text_to_image_upscale_lora_sampler_98
type: Text To Image
frequency: 3
level: weak
coverage: 0.867
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageResize+, ImageScaleBy, KSampler, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image一键文生图工作流｜8K直出人像写真特效生成_2097486456024559617.json, 图片生成/文生图/Z-Image亿级像素文生图v3｜细节纤毫毕现超高清_2095586298563219457.json, 图片生成/文生图/Z-Image文生图8K_2100484708844007425.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_98

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-Image一键文生图工作流｜8K直出人像写真特效生成_2097486456024559617.json、图片生成/文生图/Z-Image亿级像素文生图v3｜细节纤毫毕现超高清_2095586298563219457.json、图片生成/文生图/Z-Image文生图8K_2100484708844007425.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
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
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `solarL_SaveImagesToZip` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LatentPixelScale` —— 1/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `VAEDecodeTiled` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1080 | 3 | 0% |
| 高度 | 80 | 80 - 1920 | 3 | 0% |
| 采样步数 | 4 | 4 - 9 | 3 | 58% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 3 | 51% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1080，3 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，3 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 9，3 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，3 个样本
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
