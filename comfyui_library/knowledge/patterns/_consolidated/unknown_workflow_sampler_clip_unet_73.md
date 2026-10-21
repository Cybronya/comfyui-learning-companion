---
name: unknown_workflow_sampler_clip_unet_73
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.928889
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图(人像)_2006960061226164225.json, 图片生成/文生图/文生图+LoRA_2014558730028851201.json, 图片生成/文生图/文生图-Q版森林_2087797265531498498.json, 图片生成/文生图/文生图-qwen_image_2512-模板_2090689557934206978.json, 图片生成/文生图/文生图-微景观-迷你朋克工坊_2084933542248804354.json, 图片生成/文生图/文生图-微景观桃园_2088147505304395778.json, 图片生成/文生图/文生图-微景观草莓园_2085177631280029697.json, 图片生成/文生图/文生图-手机里的微景观_2084940722343600130.json, 图片生成/文生图/文生图，中英文都可以，我自己用，出图快 且准确 质量高_2026835950390747137.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_73

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/文生图(人像)_2006960061226164225.json、图片生成/文生图/文生图+LoRA_2014558730028851201.json、图片生成/文生图/文生图-Q版森林_2087797265531498498.json、图片生成/文生图/文生图-qwen_image_2512-模板_2090689557934206978.json、图片生成/文生图/文生图-微景观-迷你朋克工坊_2084933542248804354.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/9 个有
- `ConditioningCombine` —— 1/9 个有
- `ConditioningSetTimestepRange` —— 1/9 个有
- `INTConstant` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 9 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
