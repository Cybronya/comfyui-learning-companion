---
name: unknown_workflow_sampler_clip_unet_285
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.92925
common_nodes: [CLIPLoader, CLIPTextEncode, LanPaint_KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/LanPaint- Z-Image局部重绘_2005240517799669761.json, 图片生成/图生图/Lens-局部重绘_2067225666583617538.json, 图片生成/图生图/Z-image-base-万能局部重绘_2026265970930622466.json, 图片生成/图生图/ernie-turbo-局部重绘_2067810134981697538.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_285

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/LanPaint- Z-Image局部重绘_2005240517799669761.json、图片生成/图生图/Lens-局部重绘_2067225666583617538.json、图片生成/图生图/Z-image-base-万能局部重绘_2026265970930622466.json、图片生成/图生图/ernie-turbo-局部重绘_2067810134981697538.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `LanPaint_KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `InpaintModelConditioning` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `SetLatentNoiseMask` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `LanPaint_MaskBlend` —— 1/4 个有
- `Mask Fill Holes` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 9 | 4 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 9，4 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
