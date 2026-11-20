---
name: text_to_image_sampler_clip_unet_199
type: Text To Image
frequency: 3
level: strong
coverage: 0.907333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, PrimitiveStringMultiline, ResolutionSelector, SaveImage, Seed (rgthree), SpectrumMOSSImageAdaptive, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/MOSS Image 25步 + SeedVR2高质量高清放大文生图 ｜Spectrum加速版_2117092348516724738.json, 图片生成/文生图/MOSS Image 25步 高质量文生图 ｜Spectrum加速版_2116372587663155202.json, 平台全量/MOSS Image  25步 Spectrum加速版｜高质量文生图_2117436993285218306.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_199

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/MOSS Image 25步 + SeedVR2高质量高清放大文生图 ｜Spectrum加速版_2117092348516724738.json、图片生成/文生图/MOSS Image 25步 高质量文生图 ｜Spectrum加速版_2116372587663155202.json、平台全量/MOSS Image  25步 Spectrum加速版｜高质量文生图_2117436993285218306.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `SpectrumMOSSImageAdaptive`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `孤海注释` —— 1/3 个有
- `忽略多组孤海` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
