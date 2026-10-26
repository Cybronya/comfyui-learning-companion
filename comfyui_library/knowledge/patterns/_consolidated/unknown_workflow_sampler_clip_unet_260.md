---
name: unknown_workflow_sampler_clip_unet_260
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.8598
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MOSS_Text-to-Image_2K_Turbo_Edition_图生图2K极速版_2113466135764099073.json, 图片生成/图生图/Moss-image-文生图（8步加速）_2112146425906814977.json, 图片生成/图生图/Moss-image-文生图（提示词增强）_2112140949404082178.json, 图片生成/文生图/(贞贞Lora)Ernie Turbo文生图自动提示词优化极速版V1_2045747492465156097.json, 图片生成/文生图/Flux3-klein-文生图（提示词增强）_2111099390617280514.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_260

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/MOSS_Text-to-Image_2K_Turbo_Edition_图生图2K极速版_2113466135764099073.json、图片生成/图生图/Moss-image-文生图（8步加速）_2112146425906814977.json、图片生成/图生图/Moss-image-文生图（提示词增强）_2112140949404082178.json、图片生成/文生图/(贞贞Lora)Ernie Turbo文生图自动提示词优化极速版V1_2045747492465156097.json、图片生成/文生图/Flux3-klein-文生图（提示词增强）_2111099390617280514.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `TextGenerate` —— 4/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `easy showAnything` —— 2/5 个有
- `ConcatTextOfUtils` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `StringReplace` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 50 | 5 | 13% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 5 | 55% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 50，5 个样本，取值分散，一致性仅 13%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
