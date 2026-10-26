---
name: image_to_image_lora_sampler_clip_79
type: Image To Image
frequency: 4
level: moderate
coverage: 0.91425
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, ImageScaleBy, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RH_Captioner, ReferenceLatent, RunningHub Deepcleaner, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/遮罩局部修复放大流_2075842412131475458.json, 图片生成/图生图/高清修复细节增强去AI感flux2极速出图_2047959821852352514.json, 图片生成/文生图/Flux2 Klein控油+高清放大+增强细节_2054578014805086209.json, 图片生成/文生图/无损高清_2042903595565195265.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_79

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/遮罩局部修复放大流_2075842412131475458.json、图片生成/图生图/高清修复细节增强去AI感flux2极速出图_2047959821852352514.json、图片生成/文生图/Flux2 Klein控油+高清放大+增强细节_2054578014805086209.json、图片生成/文生图/无损高清_2042903595565195265.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `ImageScaleBy`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RH_Captioner`
- `ReferenceLatent`
- `RunningHub Deepcleaner`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GrowMaskWithBlur` —— 1/4 个有
- `ImpactInt` —— 1/4 个有
- `Int` —— 1/4 个有
- `LayerUtility: CropByMask V2` —— 1/4 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/4 个有
- `LayerUtility: RestoreCropBox` —— 1/4 个有
- `Mask Fill Holes` —— 1/4 个有
- `MaskPreview+` —— 1/4 个有
- `easy imageColorMatch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 9 | 4 | 13% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | sa_solver | - | 4 | 25% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 9，4 个样本，取值分散，一致性仅 13%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 sa_solver，4 个样本，一致性 25%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
