---
name: image_to_image_sampler_unet_vae_33
type: Image To Image
frequency: 7
level: moderate
coverage: 0.872143
common_nodes: [CLIPLoader, Image Comparer (rgthree), KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX板块：FLUX.2-Klein图洗图工作流_2049795289871073281.json, 图片生成/图生图/FireRed_图生图_2029829360181583873.json, 图片生成/图生图/Flux-2-Kelin 图片编辑（PS专用）_2100760099030654978.json, 图片生成/图生图/Flux-2-Kelin 无痕扩图+图片编辑 二合一工作流_2080106637305663489.json, 图片生成/图生图/Flux-2-Kelin_二合一工作流_无痕扩图+图片编辑_2080930449978912770.json, 图片生成/图生图/Flux-2-Kelin_无痕扩图+图片编辑_二合一工作流_2085547621497794561.json, 图片生成/图生图/Flux-2-Kelin_无痕扩图+图片编辑_二合一工作流_2085562425901928450.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_33

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/FLUX板块：FLUX.2-Klein图洗图工作流_2049795289871073281.json、图片生成/图生图/FireRed_图生图_2029829360181583873.json、图片生成/图生图/Flux-2-Kelin 图片编辑（PS专用）_2100760099030654978.json、图片生成/图生图/Flux-2-Kelin 无痕扩图+图片编辑 二合一工作流_2080106637305663489.json、图片生成/图生图/Flux-2-Kelin_二合一工作流_无痕扩图+图片编辑_2080930449978912770.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 6/7 个有
- `ConditioningZeroOut` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `Any Switch (rgthree)` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `MuyeTextEditOutput` —— 5/7 个有
- `ReferenceLatent` —— 5/7 个有
- `DapaoImagePadDirectionNode` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `ImpactInt` —— 4/7 个有
- `CR Prompt Text` —— 1/7 个有
- `Int` —— 1/7 个有
- `TextEncodeQwenImageEditPlus` —— 1/7 个有
- `忽略多组孤海` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 0.3 - 1 | 7 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，7 个样本
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
