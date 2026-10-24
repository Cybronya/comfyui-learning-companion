---
name: unknown_workflow_sampler_clip_unet_345
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.906333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageSharpen, KSamplerAdvanced, KSamplerSelect, ModelSamplingAuraFlow, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/krea 2 and flux klein__文生图_2100042090527940610.json, 图片生成/文生图/Hyperrealistic_ Z-image + Flux klein_2017132941884788737.json, 图片生成/文生图/krea_2_and_flux_klein_文生图_2101080842247426049.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_345

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/krea 2 and flux klein__文生图_2100042090527940610.json、图片生成/文生图/Hyperrealistic_ Z-image + Flux klein_2017132941884788737.json、图片生成/文生图/krea_2_and_flux_klein_文生图_2101080842247426049.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageSharpen`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `DetailDaemonSamplerNode` —— 2/3 个有
- `EmptyLatentImage` —— 2/3 个有
- `FaceDetailer` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `SAMLoader` —— 2/3 个有
- `SamplerCustom` —— 2/3 个有
- `UltralyticsDetectorProvider` —— 2/3 个有
- `EmptyImage` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 12 | 3 | 80% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | er_sde | - | 3 | 67% |
| 重绘幅度 | beta | - | 3 | 67% |
| 宽度 | 2816 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 12，3 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 er_sde，3 个样本，一致性 67%
- 重绘幅度 最常用 beta，3 个样本，一致性 67%
- 宽度 中位数 2816，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
