---
name: image_to_image_upscale_sampler_clip_35
type: Image To Image
frequency: 4
level: moderate
coverage: 0.8905
common_nodes: [CLIPTextEncode, CM_IntToNumber, Florence2ModelLoader, Florence2Run, GetImageSize, Image Comparer (rgthree), ImageBatchToList, ImageScale, ImageUpscaleWithModel, KSampler, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Number Multiple Of, Number to Int, PreviewImage, PrimitiveInt, SaveImage, SeedVR2, SeedVR2BlockSwap, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux-Krea+TTP+双高清模型超高清修复_1990681400712073218.json, 平台全量/Flux+TTP超高清放大，最新优化版_1922187822483062786.json, 平台全量/Flux-Krea+TTP+双高清模型超高清放大_1950951675764867074.json, 平台全量/Wan2.1+TTP超高清放大_1950792152269914113.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_35

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux-Krea+TTP+双高清模型超高清修复_1990681400712073218.json、平台全量/Flux+TTP超高清放大，最新优化版_1922187822483062786.json、平台全量/Flux-Krea+TTP+双高清模型超高清放大_1950951675764867074.json、平台全量/Wan2.1+TTP超高清放大_1950792152269914113.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CM_IntToNumber`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageBatchToList`
- `ImageScale`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Number Multiple Of`
- `Number to Int`
- `PreviewImage`
- `PrimitiveInt`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `DualCLIPLoader` —— 3/4 个有
- `CLIPLoader` —— 1/4 个有
- `LayerFilter: GaussianBlur` —— 1/4 个有
- `LoraLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 4 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 0.15 | 0.1 - 0.15 | 4 | 84% |
| LoRA 模型强度 | 0.4 | - | 1 | 100% |
| LoRA 文本强度 | 0.4 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 0.15，观测区间 0.1 - 0.15，4 个样本，取值集中（一致性 84%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
