---
name: unknown_workflow_sampler_clip_unet_389
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.922667
common_nodes: [CLIPLoader, CLIPTextEncode, CreateBoundingBoxes, EmptyFlux2LatentImage, KSampler, MOSSImageLayoutPrompt, ResolutionSelector, SaveImage, SkipLayerGuidanceDiTSimple, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS-IMAGE-SFT-4-Steps-KJ_2112398936735576066.json, 图片生成/文生图/MOSS-IMAGE-SFT-加速合集_2112422905622646785.json, 图片生成/文生图/Moss 文生图_2111394608352681986.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_389

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/MOSS-IMAGE-SFT-4-Steps-KJ_2112398936735576066.json、图片生成/文生图/MOSS-IMAGE-SFT-加速合集_2112422905622646785.json、图片生成/文生图/Moss 文生图_2111394608352681986.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateBoundingBoxes`
- `EmptyFlux2LatentImage`
- `KSampler`
- `MOSSImageLayoutPrompt`
- `ResolutionSelector`
- `SaveImage`
- `SkipLayerGuidanceDiTSimple`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `LayerUtility: TextBox` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 50 | 3 | 38% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 3 | 3 | 61% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 50，3 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 3，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
