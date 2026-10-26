---
name: image_to_image_sampler_clip_unet_133
type: Image To Image
frequency: 3
level: strong
coverage: 0.979333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 Klein图像编辑API_2097018123512799234.json, 图片生成/图生图/Flux2-Klein-9B-人像迁移_2012797315538493441.json, 图片生成/图生图/Qwen-klein-9B-局部重绘_2014309614954745857.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_133

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein图像编辑API_2097018123512799234.json、图片生成/图生图/Flux2-Klein-9B-人像迁移_2012797315538493441.json、图片生成/图生图/Qwen-klein-9B-局部重绘_2014309614954745857.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `YC Color Match` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `CR Value` —— 1/3 个有
- `FluxKontextImageScale` —— 1/3 个有
- `InpaintModelConditioning` —— 1/3 个有
- `Mask Fill Holes` —— 1/3 个有
- `图像缩放V2_孤海` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
