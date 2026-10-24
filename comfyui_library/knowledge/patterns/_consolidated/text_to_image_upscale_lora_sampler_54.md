---
name: text_to_image_upscale_lora_sampler_54
type: Text To Image
frequency: 4
level: strong
coverage: 0.80425
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScaleBy, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, PrimitiveFloat, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2511+SVR2模糊图像高清放大(4K、8K)_2008796433620668418.json, 图片生成/图生图/qwen-image-edit+TTP+SeedVR图片高清放大_2034445585201242114.json, 图片生成/图生图/模糊图像高清放大8K_2008104716613459969.json, 图片生成/图生图/模糊图像高清放大_2077679861883297794.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_54

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2511+SVR2模糊图像高清放大(4K、8K)_2008796433620668418.json、图片生成/图生图/qwen-image-edit+TTP+SeedVR图片高清放大_2034445585201242114.json、图片生成/图生图/模糊图像高清放大8K_2008104716613459969.json、图片生成/图生图/模糊图像高清放大_2077679861883297794.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageScaleBy`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveFloat`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `GetImageSize+` —— 2/4 个有
- `KOOK_ImageCompression` —— 2/4 个有
- `LayerUtility: ImageReel` —— 2/4 个有
- `LayerUtility: ImageReelComposit` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `DisTorchPurgeVRAMV2` —— 1/4 个有
- `Getter` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `Setter` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |
| 采样步数 | 4 | 4 - 8 | 4 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
