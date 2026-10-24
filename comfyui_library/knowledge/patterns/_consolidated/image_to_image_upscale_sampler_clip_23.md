---
name: image_to_image_upscale_sampler_clip_23
type: Image To Image
frequency: 5
level: moderate
coverage: 0.845
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux+z-image+8K修复放大_2096514629408215042.json, 图片生成/图生图/flux+z-image+8K修复放大_2096872445746696193.json, 图片生成/图生图/高清放大_细节增强-Flux2最新修复工作流_2015366607190626306.json, 图片生成/图生图/高清放大_细节增强-Flux2最新修复工作流_2074470837457080322.json, 图片生成/图生图/高清放大_细节增强-High-Definition Zoom_Detail Enhancement_2108834173459984386.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/flux+z-image+8K修复放大_2096514629408215042.json、图片生成/图生图/flux+z-image+8K修复放大_2096872445746696193.json、图片生成/图生图/高清放大_细节增强-Flux2最新修复工作流_2015366607190626306.json、图片生成/图生图/高清放大_细节增强-Flux2最新修复工作流_2074470837457080322.json、图片生成/图生图/高清放大_细节增强-High-Definition Zoom_Detail Enhancement_2108834173459984386.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
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
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/5 个有
- `LatentUpscaleBy` —— 3/5 个有
- `ReferenceLatent` —— 3/5 个有
- `AV_LoraLoader` —— 2/5 个有
- `KOOK_ImageCompression` —— 2/5 个有
- `LatentFrequencyEnhancer_lrzjason` —— 2/5 个有
- `PainterFluxImageEdit` —— 2/5 个有
- `Power Lora Loader (rgthree)` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 4 | 4 - 8 | 5 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 0.8 | 0.05 - 0.8 | 5 | 27% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.8，观测区间 0.05 - 0.8，5 个样本，取值分散，一致性仅 27%
- 风险：重绘幅度 观测到 0.05，低于常用下限 0.1（）
- 高发问题（7/5 个样本）：Steps较低可能导致细节不足
