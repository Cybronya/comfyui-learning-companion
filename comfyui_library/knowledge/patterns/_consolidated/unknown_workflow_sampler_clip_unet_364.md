---
name: unknown_workflow_sampler_clip_unet_364
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.854667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, PrimitiveStringMultiline, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/(贞贞Lora)Ernie Turbo文生图自动提示词优化极速版V1_2045747492465156097.json, 图片生成/文生图/Flux3-klein-文生图（提示词增强）_2111099390617280514.json, 图片生成/文生图/flux3_image_klein文生图_2111012203712311297.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_364

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/(贞贞Lora)Ernie Turbo文生图自动提示词优化极速版V1_2045747492465156097.json、图片生成/文生图/Flux3-klein-文生图（提示词增强）_2111099390617280514.json、图片生成/文生图/flux3_image_klein文生图_2111012203712311297.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `ConcatTextOfUtils` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `StringReplace` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 8 - 20 | 3 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
