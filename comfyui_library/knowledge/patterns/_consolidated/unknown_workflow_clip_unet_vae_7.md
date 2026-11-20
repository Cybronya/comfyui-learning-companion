---
name: unknown_workflow_clip_unet_vae_7
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.736
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyFlux2LatentImage, PreviewAny, PrimitiveBoolean, PrimitiveStringMultiline, SaveImage, StringReplace, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1-Aiden-ernie百度文生图模型工作流（小白福音）_2096841308638900226.json, 图片生成/文生图/Ernie Image Turbo文生图_2066118202551263234.json, 图片生成/文生图/Ernie Image文生图标准版_2066340730011996162.json, 图片生成/文生图/Ernie Turbo+Z Image提示词优化组合版文生图V1_2044622121946583042.json, 图片生成/文生图/Ernie Turbo+Z Image提示词优化组合版文生图V1_2046100567373647873.json, 图片生成/文生图/Ernie Turbo文生图自动提示词优化极速版V1_2044590644466814977.json, 图片生成/文生图/Ernie Turbo文生图自动提示词优化极速版V1_2046109277659602945.json, 图片生成/文生图/Ernie-Image-8步快速出图_2046183724303261698.json, 图片生成/文生图/本地部署ERNIE-Image模型：24G 显存可跑，8 步快速出图！_2044965223928438786.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_7

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1-Aiden-ernie百度文生图模型工作流（小白福音）_2096841308638900226.json、图片生成/文生图/Ernie Image Turbo文生图_2066118202551263234.json、图片生成/文生图/Ernie Image文生图标准版_2066340730011996162.json、图片生成/文生图/Ernie Turbo+Z Image提示词优化组合版文生图V1_2044622121946583042.json、图片生成/文生图/Ernie Turbo+Z Image提示词优化组合版文生图V1_2046100567373647873.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 9 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 8/9 个有
- `KSampler` —— 7/9 个有
- `PreviewImage` —— 4/9 个有
- `easy showAnything` —— 3/9 个有
- `Int` —— 2/9 个有
- `KSamplerAdvanced` —— 2/9 个有
- `VAEEncode` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `Label (rgthree)` —— 1/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `TTResolutionSelector` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 7 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 9 | 9 | 0% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | simple | - | 9 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 9，9 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（6/9 个样本）：Steps较低可能导致细节不足
