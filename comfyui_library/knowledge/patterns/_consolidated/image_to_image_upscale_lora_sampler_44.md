---
name: image_to_image_upscale_lora_sampler_44
type: Image To Image
frequency: 4
level: moderate
coverage: 0.8455
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit-2511任意风格转写实+质感提升+高清放大_2010545002090340354.json, 图片生成/图生图/Qwen2511动漫转真实：超越次元！任意动漫转写实_2010543831434928129.json, 图片生成/图生图/QwenEdit2511任意风格转写实+质感提升+高清放大_2010332144446480386.json, 图片生成/图生图/Z-Image：神级像素图生图+高清放大_2084916556001275906.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_44

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit-2511任意风格转写实+质感提升+高清放大_2010545002090340354.json、图片生成/图生图/Qwen2511动漫转真实：超越次元！任意动漫转写实_2010543831434928129.json、图片生成/图生图/QwenEdit2511任意风格转写实+质感提升+高清放大_2010332144446480386.json、图片生成/图生图/Z-Image：神级像素图生图+高清放大_2084916556001275906.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
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
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 3/4 个有
- `CropWithPadInfo` —— 3/4 个有
- `GetImageSize+` —— 3/4 个有
- `KSamplerAdvanced` —— 3/4 个有
- `LayerUtility: ImageReel` —— 3/4 个有
- `LayerUtility: ImageReelComposit` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `QwenEditConfigPreparer` —— 3/4 个有
- `QwenEditOutputExtractor` —— 3/4 个有
- `RH_Captioner` —— 3/4 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `LatentPixelScale` —— 2/4 个有
- `PrimitiveFloat` —— 2/4 个有
- `QwenEditAdaptiveLongestEdge` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `VAEDecodeTiled` —— 2/4 个有
- `AddLabel` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `KOOK_ImageCompression` —— 1/4 个有
- `Qwen3_VQA` —— 1/4 个有
- `图像缩放V2_孤海` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | 1 - 9 | 4 | 51% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | res_2m | - | 4 | 50% |
| 重绘幅度 | 0.175 | - | 2 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 9，4 个样本
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_2m，4 个样本，一致性 50%
- 重绘幅度 中位数 0.175，样本不足，未给区间，2 个样本
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
