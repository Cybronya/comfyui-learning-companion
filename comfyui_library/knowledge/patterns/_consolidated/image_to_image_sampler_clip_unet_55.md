---
name: image_to_image_sampler_clip_unet_55
type: Image To Image
frequency: 7
level: strong
coverage: 0.825714
common_nodes: [ApplyPulidFlux, BboxDetectorSEGS, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, GrowMaskWithBlur, ImageResize+, KSampler, LoadImage, MaskToImage, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RepeatLatentBatch, SaveImage, SegsToCombinedMask, SetLatentNoiseMask, UNETLoader, UltralyticsDetectorProvider, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX KERA+PULID+高清修复 最强换脸工作流_1968852750496878593.json, 图片生成/图生图/FLUX PULID换脸（可多人）_1963421660617510914.json, 图片生成/图生图/FLUX.1 Krea + PULID 人像换脸_1951530450911219713.json, 图片生成/图生图/Flux PULID 最强换脸_1914677873192464386.json, 图片生成/图生图/最强换脸 PULID + Flux 工作流_1915586150789222402.json, 图片生成/图生图/最强换脸 PULID + Flux 工作流_1927923154654773249.json, 图片生成/图生图/老牌最强换脸工具 PULID 和 Flux 生图_1915586739849592834.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_55

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/FLUX KERA+PULID+高清修复 最强换脸工作流_1968852750496878593.json、图片生成/图生图/FLUX PULID换脸（可多人）_1963421660617510914.json、图片生成/图生图/FLUX.1 Krea + PULID 人像换脸_1951530450911219713.json、图片生成/图生图/Flux PULID 最强换脸_1914677873192464386.json、图片生成/图生图/最强换脸 PULID + Flux 工作流_1915586150789222402.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `ApplyPulidFlux`
- `BboxDetectorSEGS`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `GrowMaskWithBlur`
- `ImageResize+`
- `KSampler`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RepeatLatentBatch`
- `SaveImage`
- `SegsToCombinedMask`
- `SetLatentNoiseMask`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `SUPIR_Upscale` —— 6/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `ApplyTeaCachePatchAdvanced` —— 1/7 个有
- `FluxForwardOverrider` —— 1/7 个有
- `Image Crop Face` —— 1/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `LP-TranslateToEN` —— 1/7 个有
- `PulidFluxFaceDetector` —— 1/7 个有
- `PulidFluxOptions` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 30 | 7 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | normal | - | 7 | 100% |
| 重绘幅度 | 0.7 | 0.7 - 0.7 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 30，7 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 normal，7 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.7 - 0.7，7 个样本，取值集中（一致性 100%）
