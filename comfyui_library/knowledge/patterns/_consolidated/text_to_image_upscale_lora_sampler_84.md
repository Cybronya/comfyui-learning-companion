---
name: text_to_image_upscale_lora_sampler_84
type: Text To Image
frequency: 3
level: strong
coverage: 0.895
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ClothesSegment, EmptyLatentImage, Flux2Scheduler, FluxKontextImageScale, GroundingDinoModelLoader_SDPose, ImageScaleBy, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SDPoseOODLoader, SDPoseOODProcessor, SamplerCustomAdvanced, SamplerEulerAncestral, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageSize, easy showAnything, easy sleep, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 Klein二次元服装真人试穿，图生图换装穿搭效果自然逼真_2114575365845897217.json, 图片生成/图生图/flux2-klein-二次元服装真人试穿｜人像写真换装一步到位_2114230623807299585.json, 图片生成/图生图/flux2-klein二次元服装真人试穿工作流｜图生图写真换装神器_2114255638078517249.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_84

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein二次元服装真人试穿，图生图换装穿搭效果自然逼真_2114575365845897217.json、图片生成/图生图/flux2-klein-二次元服装真人试穿｜人像写真换装一步到位_2114230623807299585.json、图片生成/图生图/flux2-klein二次元服装真人试穿工作流｜图生图写真换装神器_2114255638078517249.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ClothesSegment`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `FluxKontextImageScale`
- `GroundingDinoModelLoader_SDPose`
- `ImageScaleBy`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SamplerCustomAdvanced`
- `SamplerEulerAncestral`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy showAnything`
- `easy sleep`
- `solarL_SaveImagesToZip`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
