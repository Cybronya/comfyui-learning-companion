---
name: image_to_image_sampler_clip_unet_17
type: Image To Image
frequency: 2
level: weak
coverage: 0.907
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, SeedVR2, SeedVR2BlockSwap, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/图生图/2102231252593102849.json, 图片生成/文生图/Flux2_All_In_One-黑森林最新生图模型_1993542560188661762.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_17

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2102231252593102849.json、图片生成/文生图/Flux2_All_In_One-黑森林最新生图模型_1993542560188661762.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageCrop` —— 1/2 个有
- `ImageScaleToMaxDimension` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | - | 2 | 33% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
