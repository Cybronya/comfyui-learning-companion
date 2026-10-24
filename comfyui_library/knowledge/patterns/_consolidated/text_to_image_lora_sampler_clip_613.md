---
name: text_to_image_lora_sampler_clip_613
type: Text To Image
frequency: 2
level: weak
coverage: 0.8805
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/通用图片高清放大工作流，图生图分辨率提升细节增强工具_2103225917630935041.json, 图片生成/文生图/Super Z-image 3.0+真实感Lora文生图批量跑 浮云2.9_2020686279058399234.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_613

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/通用图片高清放大工作流，图生图分辨率提升细节增强工具_2103225917630935041.json、图片生成/文生图/Super Z-image 3.0+真实感Lora文生图批量跑 浮云2.9_2020686279058399234.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `ConstrainImage|pysssss` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy imageColorMatch` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9.5 | - | 2 | 42% |
| Prompt 约束强度(CFG) | 2.75 | - | 2 | 36% |
| 采样算法 | er_sde | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 580 | - | 2 | 14% |
| 高度 | 1000 | - | 2 | 8% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 2.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 580，样本不足，未给区间，2 个样本，取值分散，一致性仅 14%
- 高度 中位数 1000，样本不足，未给区间，2 个样本，取值分散，一致性仅 8%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
