---
name: image_to_image_sampler_clip_checkpoint_10
type: Image To Image
frequency: 3
level: strong
coverage: 0.787
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, DualCLIPLoader, FluxSamplerParams+, Image Comparer (rgthree), Int2String, KSampler, LoadImage, SaveImage, Seed_, UNETLoader, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX图生图工作流（大全）_1946839023510020097.json, 图片生成/图生图/FLUX图生图工作流（大全）_2018483381146755073.json, 图片生成/图生图/工作流基础篇-5-FLUX图生图工作流（大全）_2013855838208790529.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_10

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX图生图工作流（大全）_1946839023510020097.json、图片生成/图生图/FLUX图生图工作流（大全）_2018483381146755073.json、图片生成/图生图/工作流基础篇-5-FLUX图生图工作流（大全）_2013855838208790529.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxSamplerParams+`
- `Image Comparer (rgthree)`
- `Int2String`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `Seed_`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 0.35 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.35，3 个样本，取值集中（一致性 100%）
