---
name: unknown_workflow_upscale_sampler_unet_14
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.902
common_nodes: [CLIPLoader, Get Image Size, Image Comparer (rgthree), ImageFromBatch, ImageResize+, ImpactMinMax, KOOK_ImageCompression, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader, VAEDecode, VAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy imageCount, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-klein-9B-图像修复+SeedVR2+TTP分块高清放大_2020053134378274817.json, 图片生成/图生图/boogu-edit-动漫转真人+高清分块放大_2078462361790402562.json, 平台全量/极致放大修复 Flux2-klein-9B-图像修复+SeedVR2+TTP分块高清放大_2020737795316260865.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_14

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux2-klein-9B-图像修复+SeedVR2+TTP分块高清放大_2020053134378274817.json、图片生成/图生图/boogu-edit-动漫转真人+高清分块放大_2078462361790402562.json、平台全量/极致放大修复 Flux2-klein-9B-图像修复+SeedVR2+TTP分块高清放大_2020737795316260865.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageFromBatch`
- `ImageResize+`
- `ImpactMinMax`
- `KOOK_ImageCompression`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 2/3 个有
- `PainterFluxImageEdit` —— 2/3 个有
- `EmptyLatentImage` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `TextEncodeBooguEdit` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 3 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1280 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，3 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
