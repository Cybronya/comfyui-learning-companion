---
name: image_to_image_upscale_lora_sampler_106
type: Image To Image
frequency: 2
level: weak
coverage: 0.775
common_nodes: [AILab_ImagePreview, AILab_Preview, Bounded Image Crop with Mask, CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatchV2, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSizeAndCount, Image Comparer (rgthree), ImagePadForOutpaint, ImageResizeKJv2, ImageScaleToMaxDimension, ImpactMinMax, InvertMask, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2TorchCompileSettings, SeedVR2VideoUpscaler, UNETLoader_Any, UniBlockSwap, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图片编辑-动漫转写实-Boogu+Z_Image+Klein_2081385385854332929.json, 图片生成/图生图/图片编辑-转写实-Krea2+Z_Image+Klein_2082440101195501570.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_106

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图片编辑-动漫转写实-Boogu+Z_Image+Klein_2081385385854332929.json、图片生成/图生图/图片编辑-转写实-Krea2+Z_Image+Klein_2082440101195501570.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_ImagePreview`
- `AILab_Preview`
- `Bounded Image Crop with Mask`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatchV2`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSizeAndCount`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `ImageResizeKJv2`
- `ImageScaleToMaxDimension`
- `ImpactMinMax`
- `InvertMask`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2TorchCompileSettings`
- `SeedVR2VideoUpscaler`
- `UNETLoader_Any`
- `UniBlockSwap`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ConditioningKrea2Rebalance` —— 1/2 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `Krea2OstrisEditModelPatch` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `TextEncodeBooguEdit` —— 1/2 个有
- `TextEncodeKrea2OstrisEdit` —— 1/2 个有
- `UNETLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | exponential | - | 2 | 100% |
| 重绘幅度 | 0.7 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 exponential，2 个样本，一致性 100%
- 重绘幅度 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
