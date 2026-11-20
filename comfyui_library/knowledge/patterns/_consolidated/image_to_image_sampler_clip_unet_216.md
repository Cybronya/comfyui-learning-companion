---
name: image_to_image_sampler_clip_unet_216
type: Image To Image
frequency: 2
level: weak
coverage: 0.6545
common_nodes: [AILab_QwenVL, Any Switch (rgthree), CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Muter (rgthree), FloatConstant, Flux2KleinEnhancer, Flux2Scheduler, GetImageSize, GetNode, INTConstant, Image Comparer (rgthree), ImageConcanate, ImpactSwitch, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LazyCache, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SetNode, ShowText, UNETLoader, VAEDecode, VAEEncode, VAELoader, ZML_ImageMemory]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动漫转真人 Flux.2 Klein 生成 文心Ernie细节重绘输出_2060985217950769154.json, 平台全量/动漫转真人 Flux.2 Klein 生成 Z-imag写实重绘输出_2005675192120737793.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_216

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/动漫转真人 Flux.2 Klein 生成 文心Ernie细节重绘输出_2060985217950769154.json、平台全量/动漫转真人 Flux.2 Klein 生成 Z-imag写实重绘输出_2005675192120737793.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `Any Switch (rgthree)`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Muter (rgthree)`
- `FloatConstant`
- `Flux2KleinEnhancer`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImpactSwitch`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazyCache`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `ShowText`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZML_ImageMemory`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1.6 | - | 2 | 100% |
| 采样算法 | dpm_2 | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.4 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpm_2，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
