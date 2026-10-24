---
name: text_to_image_lora_sampler_clip_618
type: Text To Image
frequency: 2
level: weak
coverage: 0.9165
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Boogu_Turbo 文生图_2070875528814481409.json, 图片生成/文生图/Z-image-base + turbo双采样器+klein高清发大_2016542899185389569.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_618

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Boogu_Turbo 文生图_2070875528814481409.json、图片生成/文生图/Z-image-base + turbo双采样器+klein高清发大_2016542899185389569.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `EmptyFlux2LatentImage` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerUtility: ImageReel` —— 1/2 个有
- `LayerUtility: ImageReelComposit` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 40% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | euler | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |
| 宽度 | 976 | - | 2 | 95% |
| 高度 | 1600 | - | 2 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 调度器 最常用 euler，2 个样本，一致性 50%
- 宽度 中位数 976，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 高度 中位数 1600，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
