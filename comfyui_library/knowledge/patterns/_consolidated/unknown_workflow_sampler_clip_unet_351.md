---
name: unknown_workflow_sampler_clip_unet_351
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.729333
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux3PELoader, Flux3PromptEnhance, ImpactConditionalBranch, KSampler, PrimitiveStringMultiline, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Flux3 PE提示词强化加速版多图编辑_2111422597035552769.json, 图片生成/文生图/FLUX3 PE提示词强化加速版文生图_2111395431153496066.json, 图片生成/文生图/flux3_klein_int8 文生图_图生图功能二合一_2111428656928219137.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_351

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux3 PE提示词强化加速版多图编辑_2111422597035552769.json、图片生成/文生图/FLUX3 PE提示词强化加速版文生图_2111395431153496066.json、图片生成/文生图/flux3_klein_int8 文生图_图生图功能二合一_2111428656928219137.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux3PELoader`
- `Flux3PromptEnhance`
- `ImpactConditionalBranch`
- `KSampler`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `FastGroupsBypassSwitch` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `ReferenceMultiLatent` —— 2/3 个有
- `TextGenerateLTX2Prompt` —— 2/3 个有
- `Fast Bypasser (rgthree)` —— 1/3 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/3 个有
- `PDIMAGE_LongerSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 16 - 35 | 3 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 3 | 36% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 16，观测区间 16 - 35，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，3 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
