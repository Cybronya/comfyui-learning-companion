---
name: image_to_image_upscale_sampler_clip_7
type: Image To Image
frequency: 16
level: moderate
coverage: 0.834063
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSize+, ImageResize+, ImageScaleBy, KSampler, LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/Flux2 Klein+KOOK+图像编辑+9B版本+人像4K_8k高清放大_2012156583878336514.json, 图片生成/图生图/Flux2+Z-image+SeedVR2-超级高清8K（更强更真）（产品+人像）_2039910094120423425.json, 图片生成/图生图/Flux2-Klein 修复 + Z-Image 洗图 + TTP分块放大到8K 强强联合_2013514626708803585.json, 图片生成/图生图/Flux2-Klein终极高清修复8k_2019769198448222209.json, 图片生成/图生图/Flux2-Klein高清放大到8K-更强 林耀_2013919769916870658.json, 图片生成/图生图/Flux2-Klein高清放大到8K-更强_2013426675601645570.json, 图片生成/图生图/Flux2-Klein高清放大到8K-更强（适用于人像）_2014883606484754434.json, 图片生成/图生图/Flux2-Klein高清放大到8K_2076143022093455362.json, 图片生成/图生图/Flux2-Klein高清放大到8K_2076208373338562562.json, 图片生成/图生图/Flux2-Klein高清放大到8K（超强）_2014240945021132802.json, 图片生成/图生图/KOOK_Flux2 Klein 图像编辑9B_人像洗图质感修复 V2_2012079372005543937.json, 图片生成/图生图/Klein高清放大+seedvr2放大V2.0（优化偏色问题）_2039169050110074882.json, 图片生成/图生图/Klein高清放大+seedvr2放大（自用）_2016100671904292866.json, 图片生成/图生图/Z-Image 洗图 +高清修复 + TTP分块_2016060527511871490.json, 图片生成/图生图/Z-Image：图生图超清放大，细节重生，老图焕发专业级画质！_1998574481641758722.json, 图片生成/图生图/⭐️⭐️⭐️⭐️⭐️合成打光-场景融合-flux2 klein产品场景合成（可画遮罩绘前景遮挡）_2020342521519415297.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_7

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein+KOOK+图像编辑+9B版本+人像4K_8k高清放大_2012156583878336514.json、图片生成/图生图/Flux2+Z-image+SeedVR2-超级高清8K（更强更真）（产品+人像）_2039910094120423425.json、图片生成/图生图/Flux2-Klein 修复 + Z-Image 洗图 + TTP分块放大到8K 强强联合_2013514626708803585.json、图片生成/图生图/Flux2-Klein终极高清修复8k_2019769198448222209.json、图片生成/图生图/Flux2-Klein高清放大到8K-更强 林耀_2013919769916870658.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 15/16 个有
- `LoraLoaderModelOnly` —— 15/16 个有
- `ReferenceLatent` —— 15/16 个有
- `Image Comparer (rgthree)` —— 14/16 个有
- `ImageCASharpening+` —— 14/16 个有
- `KSamplerAdvanced` —— 14/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 14/16 个有
- `ModelSamplingAuraFlow` —— 14/16 个有
- `RunningHub Deepcleaner` —— 14/16 个有
- `VAEDecode` —— 14/16 个有
- `PrimitiveFloat` —— 12/16 个有
- `RH_Captioner` —— 12/16 个有
- `easy showAnything` —— 12/16 个有
- `LatentUpscaleBy` —— 11/16 个有
- `LayerUtility: ImageReel` —— 11/16 个有
- `LayerUtility: ImageReelComposit` —— 11/16 个有
- `LayerUtility: ImageMaskScaleAs` —— 10/16 个有
- `CR Text` —— 3/16 个有
- `EmptyFlux2LatentImage` —— 3/16 个有
- `GetImageSize` —— 3/16 个有
- `KOOK_SaveJPGImage` —— 2/16 个有
- `LatentPixelScale` —— 2/16 个有
- `UpscaleModelLoader` —— 2/16 个有
- `VAEDecodeTiled` —— 2/16 个有
- `easy imageScaleDownBy` —— 2/16 个有
- `GrowMaskWithBlur` —— 1/16 个有
- `ImageUpscaleWithModel` —— 1/16 个有
- `LayerMask: BiRefNetUltraV2` —— 1/16 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/16 个有
- `MaskPreview+` —— 1/16 个有
- `PainterFluxImageEdit` —— 1/16 个有
- `SolidMask` —— 1/16 个有
- `WujiCleaner` —— 1/16 个有
- `easy imageDetailTransfer` —— 1/16 个有
- `孤海-遮罩混合运算` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 16 | 62% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 16 | 37% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | euler | - | 16 | 62% |
| 重绘幅度 | beta57 | - | 16 | 62% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/16 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 最常用 randomize，16 个样本，一致性 62%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，16 个样本，取值分散，一致性仅 37%
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，16 个样本，一致性 62%
- 重绘幅度 最常用 beta57，16 个样本，一致性 62%
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
