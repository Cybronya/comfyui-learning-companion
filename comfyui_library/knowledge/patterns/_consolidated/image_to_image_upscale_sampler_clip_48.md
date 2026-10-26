---
name: image_to_image_upscale_sampler_clip_48
type: Image To Image
frequency: 2
level: weak
coverage: 0.7265
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImpactBoolean, ImpactConditionalBranch, ImpactInt, ImpactMinMax, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, PreviewImage, PrimitiveStringMultiline, RHHiddenNodes, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/迄今超强万能图片去水印+可选4K_8K高清放大（涂抹水印遮罩区）_1985533505046200321.json, 图片生成/图生图/迄今超强扩图Flux2 Klein改图几乎零偏移万物极速扩图又快又稳保留细节可选高清4K放大_1966707043744821250.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_48

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/迄今超强万能图片去水印+可选4K_8K高清放大（涂抹水印遮罩区）_1985533505046200321.json、图片生成/图生图/迄今超强扩图Flux2 Klein改图几乎零偏移万物极速扩图又快又稳保留细节可选高清4K放大_1966707043744821250.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImpactBoolean`
- `ImpactConditionalBranch`
- `ImpactInt`
- `ImpactMinMax`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `GrowMaskWithBlur` —— 1/2 个有
- `ImagePadForOutpaint` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `InpaintModelConditioning` —— 1/2 个有
- `LayerUtility: ImageReel` —— 1/2 个有
- `LayerUtility: ImageReelComposit` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有
- `SeedVR2GGUF` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
