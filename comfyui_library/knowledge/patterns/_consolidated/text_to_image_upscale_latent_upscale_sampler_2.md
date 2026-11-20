---
name: text_to_image_upscale_latent_upscale_sampler_2
type: Text To Image
frequency: 4
level: strong
coverage: 0.88125
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), KSampler, KSamplerAdvanced, LatentUpscaleBy, PreviewImage, PrimitiveStringMultiline, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS-25步Spectrum加速+krea2二采_2115247989819265026.json, 图片生成/文生图/krea2 raw+turbo 双采_2078399307941761026.json, 图片生成/文生图/krea2 raw+turbo 双采微胖_2082296044741812226.json, 平台全量/MOSS-25步Spectrum加速+krea2二采_2118524711759077377.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/MOSS-25步Spectrum加速+krea2二采_2115247989819265026.json、图片生成/文生图/krea2 raw+turbo 双采_2078399307941761026.json、图片生成/文生图/krea2 raw+turbo 双采微胖_2082296044741812226.json、平台全量/MOSS-25步Spectrum加速+krea2二采_2118524711759077377.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `KSamplerAdvanced`
- `LatentUpscaleBy`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningKrea2Rebalance` —— 2/4 个有
- `ImageScaleBy` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `SpectrumMOSSImageAdaptive` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `easy imageColorMatch` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 12 | 4 | 81% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | er_sde | - | 4 | 50% |
| 重绘幅度 | beta | - | 4 | 50% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 12，4 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 er_sde，4 个样本，一致性 50%
- 重绘幅度 最常用 beta，4 个样本，一致性 50%
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
