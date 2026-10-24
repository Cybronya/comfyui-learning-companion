---
name: unknown_workflow_lora_sampler_unet_118
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.991167
common_nodes: [CLIPLoader, GetImageSize+, GrowMask, InvertMask, JoinImageWithAlpha, KSampler, LoadImage, LoadRembgByBiRefNetModel, LoraLoaderModelOnly, PainterFluxImageEdit, ResizeImagesByLongerEdge, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/超强产品抠图 多产品高细节一键抠图工作流_2083004240590622721.json, 图片生成/图生图/超强产品抠图 多产品高细节一键抠图工作流_2083021756440334337.json, 图片生成/图生图/超强产品抠图无惧多产品，高细节_2088522672270565378.json, 图片生成/图生图/超强产品抠图无惧多产品，高细节_2092619274220298242.json, 图片生成/图生图/超强产品抠图（无惧多产品，高细节） (2)_2097256194455982081.json, 图片生成/文生图/超强产品抠图（无惧多产品，高细节）_2091785488968536065.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_118

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/超强产品抠图 多产品高细节一键抠图工作流_2083004240590622721.json、图片生成/图生图/超强产品抠图 多产品高细节一键抠图工作流_2083021756440334337.json、图片生成/图生图/超强产品抠图无惧多产品，高细节_2088522672270565378.json、图片生成/图生图/超强产品抠图无惧多产品，高细节_2092619274220298242.json、图片生成/图生图/超强产品抠图（无惧多产品，高细节） (2)_2097256194455982081.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `GetImageSize+`
- `GrowMask`
- `InvertMask`
- `JoinImageWithAlpha`
- `KSampler`
- `LoadImage`
- `LoadRembgByBiRefNetModel`
- `LoraLoaderModelOnly`
- `PainterFluxImageEdit`
- `ResizeImagesByLongerEdge`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageMaskScaleAs` —— 5/6 个有
- `RembgByBiRefNetAdvanced` —— 5/6 个有
- `孤海图像裁剪按比例` —— 5/6 个有
- `GetMaskByBiRefNet` —— 1/6 个有
- `GrowMaskWithBlur` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 2 | 2 - 5 | 6 | 53% |
| Prompt 约束强度(CFG) | 2 | 2 - 2 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 2，观测区间 2 - 5，6 个样本
- Prompt 约束强度(CFG) 中位数 2，观测区间 2 - 2，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
