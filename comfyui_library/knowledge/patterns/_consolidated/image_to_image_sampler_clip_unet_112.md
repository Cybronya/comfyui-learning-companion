---
name: image_to_image_sampler_clip_unet_112
type: Image To Image
frequency: 4
level: moderate
coverage: 0.9155
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingAuraFlow, PrimitiveFloat, RHHiddenNodes, ReferenceLatent, RunningHub Deepcleaner, SaveImage, SetNode, TTP_Image_Assy, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 Klein 8K 完美高清修复+放大_2019215002783195137.json, 图片生成/图生图/Flux2-Klein 高清修复+细节还原+8K 放大_2040437717317718018.json, 图片生成/图生图/Flux2-Klein 高清修复+细节还原+8K 放大_2041331980343713793.json, 图片生成/图生图/蒜香卡普v1 Flux2-Klein 高清修复+细节还原+8K 放大 颜色匹配_2041546360595423233.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_112

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 8K 完美高清修复+放大_2019215002783195137.json、图片生成/图生图/Flux2-Klein 高清修复+细节还原+8K 放大_2040437717317718018.json、图片生成/图生图/Flux2-Klein 高清修复+细节还原+8K 放大_2041331980343713793.json、图片生成/图生图/蒜香卡普v1 Flux2-Klein 高清修复+细节还原+8K 放大 颜色匹配_2041546360595423233.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PrimitiveFloat`
- `RHHiddenNodes`
- `ReferenceLatent`
- `RunningHub Deepcleaner`
- `SaveImage`
- `SetNode`
- `TTP_Image_Assy`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ColorMatchV2` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 8 | 4 | 22% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 4 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 8，4 个样本，取值分散，一致性仅 22%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
