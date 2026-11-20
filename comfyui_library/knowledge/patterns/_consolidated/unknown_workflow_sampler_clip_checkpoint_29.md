---
name: unknown_workflow_sampler_clip_checkpoint_29
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.955667
common_nodes: [BrushNet, BrushNetLoader, CLIPTextEncode, CheckpointLoaderSimple, InvertMask, KSampler, LoadImage, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键换背景_1919008682330492929.json, 图片生成/图生图/电商产品换背景V4.1全能型_1917157794934358017.json, 平台全量/XL产品换背景_1916790763789946881.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_29

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/一键换背景_1919008682330492929.json、图片生成/图生图/电商产品换背景V4.1全能型_1917157794934358017.json、平台全量/XL产品换背景_1916790763789946881.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `InvertMask`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LayerMask: RemBgUltra` —— 2/3 个有
- `GrowMask` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 20 | 3 | 29% |
| Prompt 约束强度(CFG) | 1.5 | 1.5 - 8 | 3 | 16% |
| 采样算法 | dpmpp_sde_gpu | - | 3 | 67% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 20，3 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1.5 - 8，3 个样本，取值分散，一致性仅 16%
- 采样算法 最常用 dpmpp_sde_gpu，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
