---
name: image_to_image_upscale_sampler_clip_31
type: Image To Image
frequency: 3
level: strong
coverage: 0.897667
common_nodes: [BatchCount+, CLIPLoader, CLIPTextEncode, Display Int (rgthree), Get resolution [Crystools], GetImageSize+, Image Comparer (rgthree), ImageFromBatch, ImageResize+, ImageScaleBy, ImageTile+, ImageUntile+, Int, JWFloat, KSampler, Latent Noise Injection, LayerUtility: PurgeVRAM V2, LoadImage, MathExpression|pysssss, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader_Any, VAEDecode, VAEEncode, VAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image +seedvr2场景放大_2061392225396944898.json, 图片生成/图生图/Zimageseed VR2场景分块高清放大_2058008768167895041.json, 图片生成/图生图/z-image+seedvr2场景放大_2007312766293516290.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_31

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Z-image +seedvr2场景放大_2061392225396944898.json、图片生成/图生图/Zimageseed VR2场景分块高清放大_2058008768167895041.json、图片生成/图生图/z-image+seedvr2场景放大_2007312766293516290.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `BatchCount+`
- `CLIPLoader`
- `CLIPTextEncode`
- `Display Int (rgthree)`
- `Get resolution [Crystools]`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageFromBatch`
- `ImageResize+`
- `ImageScaleBy`
- `ImageTile+`
- `ImageUntile+`
- `Int`
- `JWFloat`
- `KSampler`
- `Latent Noise Injection`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MathExpression|pysssss`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader_Any`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `AdvancedLyingSigmaSampler` —— 2/3 个有
- `BasicGuider` —— 2/3 个有
- `BasicScheduler` —— 2/3 个有
- `ClipInterrogator` —— 2/3 个有
- `DF_Integer` —— 2/3 个有
- `ImageCASharpening+` —— 2/3 个有
- `ImpactMinMax` —— 2/3 个有
- `KSamplerSelect` —— 2/3 个有
- `RandomNoise` —— 2/3 个有
- `SamplerCustomAdvanced` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy imageSize` —— 2/3 个有
- `RHHiddenNodes` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 5 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 0.45 | 0.45 - 0.45 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 0.45，观测区间 0.45 - 0.45，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
