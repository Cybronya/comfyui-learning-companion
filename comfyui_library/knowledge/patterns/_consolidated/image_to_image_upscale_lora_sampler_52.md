---
name: image_to_image_upscale_lora_sampler_52
type: Image To Image
frequency: 4
level: moderate
coverage: 0.83225
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageSharpen, KSampler, KSamplerSelect, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image-base+高清放大 文生图_图生图  高清放大Z-image+Flux2-klein_2020661220746993665.json, 图片生成/图生图/flux-2-klein全家桶系列7（单图+双图+三图编辑流）_2042089381166587905.json, 图片生成/文生图/Z-image-base+高清放大_2019659749075197954.json, 平台全量/星绘-Z-私房写真摄影（内置重绘、放大）_2003676832719355905.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_52

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Z-image-base+高清放大 文生图_图生图  高清放大Z-image+Flux2-klein_2020661220746993665.json、图片生成/图生图/flux-2-klein全家桶系列7（单图+双图+三图编辑流）_2042089381166587905.json、图片生成/文生图/Z-image-base+高清放大_2019659749075197954.json、平台全量/星绘-Z-私房写真摄影（内置重绘、放大）_2003676832719355905.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageSharpen`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 3/4 个有
- `EmptySD3LatentImage` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `MemoryCleaner` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Qwen3_VQA` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `SomethingToString` —— 3/4 个有
- `ImageScaleBy` —— 2/4 个有
- `CR Latent Input Switch` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ImpactGaussianBlurMask` —— 1/4 个有
- `InpaintModelConditioning` —— 1/4 个有
- `Mask Fill Holes` —— 1/4 个有
- `MaskPreview+` —— 1/4 个有
- `Mute / Bypass Relay (rgthree)` —— 1/4 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/4 个有
- `PlaySound|pysssss` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `图像缩放V2_孤海` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 6 - 40 | 4 | 46% |
| Prompt 约束强度(CFG) | 2 | 1 - 3 | 4 | 50% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 6 - 40，4 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 3，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
