---
name: unknown_workflow_sampler_clip_checkpoint_31
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9335
common_nodes: [BrushNet, BrushNetLoader, CLIPTextEncode, CheckpointLoaderSimple, InvertMask, KSampler, LoadImage, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键换背景_1919008682330492929.json, 图片生成/图生图/电商产品换背景V4.1全能型_1917157794934358017.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_31

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键换背景_1919008682330492929.json、图片生成/图生图/电商产品换背景V4.1全能型_1917157794934358017.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
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
- `GrowMask` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `LayerMask: RemBgUltra` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12.5 | - | 2 | 40% |
| Prompt 约束强度(CFG) | 4.75 | - | 2 | 32% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 4.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 32%
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
