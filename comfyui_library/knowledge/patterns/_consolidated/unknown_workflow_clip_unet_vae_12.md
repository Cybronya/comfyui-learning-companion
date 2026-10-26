---
name: unknown_workflow_clip_unet_vae_12
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.7364
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyFlux2LatentImage, PreviewAny, PrimitiveBoolean, PrimitiveStringMultiline, SaveImage, StringReplace, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1-Aiden-ernie百度文生图模型工作流（小白福音）_2096841308638900226.json, 图片生成/文生图/Ernie Image Turbo文生图_2066118202551263234.json, 图片生成/文生图/Ernie Image文生图标准版_2066340730011996162.json, 图片生成/文生图/Ernie Turbo+Z Image提示词优化组合版文生图V1_2044622121946583042.json, 图片生成/文生图/Ernie Turbo+Z Image提示词优化组合版文生图V1_2046100567373647873.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_12

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1-Aiden-ernie百度文生图模型工作流（小白福音）_2096841308638900226.json、图片生成/文生图/Ernie Image Turbo文生图_2066118202551263234.json、图片生成/文生图/Ernie Image文生图标准版_2066340730011996162.json、图片生成/文生图/Ernie Turbo+Z Image提示词优化组合版文生图V1_2044622121946583042.json、图片生成/文生图/Ernie Turbo+Z Image提示词优化组合版文生图V1_2046100567373647873.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyFlux2LatentImage`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `SaveImage`
- `StringReplace`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `KSampler` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `KSamplerAdvanced` —— 2/5 个有
- `VAEEncode` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `TTResolutionSelector` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 3 | 53% |
| Prompt 约束强度(CFG) | 4 | 1 - 9 | 5 | 25% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 9，5 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
