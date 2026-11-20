---
name: unknown_workflow_sampler_clip_unet_219
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.771167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, LoadImage, ReferenceMultiLatent, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux3单图编辑工作流_2111001547005054977.json, 图片生成/图生图/Flux3快速图像编辑_2110973569806192641.json, 图片生成/文生图/Flux3 kelin图像编辑_2110901954389041153.json, 图片生成/文生图/Flux3 kelin图像编辑（提示词优化）_2110918718791438338.json, 图片生成/文生图/flux3图像编辑_2111385356770828290.json, 图片生成/文生图/flux3编辑工作流_2110955588506181634.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_219

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux3单图编辑工作流_2111001547005054977.json、图片生成/图生图/Flux3快速图像编辑_2110973569806192641.json、图片生成/文生图/Flux3 kelin图像编辑_2110901954389041153.json、图片生成/文生图/Flux3 kelin图像编辑（提示词优化）_2110918718791438338.json、图片生成/文生图/flux3图像编辑_2111385356770828290.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `LoadImage`
- `ReferenceMultiLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `CreateBoundingBoxes` —— 4/6 个有
- `PreviewAny` —— 4/6 个有
- `CR Prompt Text` —— 2/6 个有
- `LayerUtility: ImageReel` —— 2/6 个有
- `LayerUtility: ImageReelComposit` —— 2/6 个有
- `ResolutionSelector` —— 2/6 个有
- `Text` —— 2/6 个有
- `ACE_TextGoogleTranslate` —— 1/6 个有
- `ImageCompare` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `TextGenerate` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 16 - 25 | 6 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 6 | 36% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 16，观测区间 16 - 25，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
