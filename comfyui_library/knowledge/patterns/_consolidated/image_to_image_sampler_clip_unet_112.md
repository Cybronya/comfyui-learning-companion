---
name: image_to_image_sampler_clip_unet_112
type: Image To Image
frequency: 4
level: strong
coverage: 0.96675
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 Klein图像编辑API_2097018123512799234.json, 图片生成/图生图/Flux2-Klein 图片高清放大 图生图_2081675636019654657.json, 图片生成/图生图/Flux2-Klein-9B-人像迁移_2012797315538493441.json, 图片生成/图生图/图片高清放大 Flux2-Klein！_2081342617417240577.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_112

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein图像编辑API_2097018123512799234.json、图片生成/图生图/Flux2-Klein 图片高清放大 图生图_2081675636019654657.json、图片生成/图生图/Flux2-Klein-9B-人像迁移_2012797315538493441.json、图片生成/图生图/图片高清放大 Flux2-Klein！_2081342617417240577.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
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
- `EmptyFlux2LatentImage` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `ImageCASharpening+` —— 2/4 个有
- `LatentUpscaleBy` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `CR Value` —— 1/4 个有
- `FluxKontextImageScale` —— 1/4 个有
- `YC Color Match` —— 1/4 个有
- `图像缩放V2_孤海` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 6 | 4 | 80% |
| Prompt 约束强度(CFG) | 1.05 | 1 - 1.1 | 4 | 95% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 6，4 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1.05，观测区间 1 - 1.1，4 个样本，取值集中（一致性 95%）
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
