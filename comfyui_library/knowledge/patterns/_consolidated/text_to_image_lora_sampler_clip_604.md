---
name: text_to_image_lora_sampler_clip_604
type: Text To Image
frequency: 2
level: weak
coverage: 0.865
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2, SeedVR2BlockSwap, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX3Klein高清放大 4K输出SeedVR2洗图处理工具_2113384976279490562.json, 图片生成/图生图/通用图片高清放大工作流，图生图分辨率提升细节增强工具_2103225917630935041.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_604

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/FLUX3Klein高清放大 4K输出SeedVR2洗图处理工具_2113384976279490562.json、图片生成/图生图/通用图片高清放大工作流，图生图分辨率提升细节增强工具_2103225917630935041.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `ConstrainImage|pysssss` —— 1/2 个有
- `DF_Integer` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `Flux2Scheduler` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `ManualSigmas` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有
- `ShunjingAIShade` —— 1/2 个有
- `TextGenerate` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `easy imageColorMatch` —— 1/2 个有
- `孤海图像缩放按像素` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
