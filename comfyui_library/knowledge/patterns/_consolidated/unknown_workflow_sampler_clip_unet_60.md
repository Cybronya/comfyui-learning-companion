---
name: unknown_workflow_sampler_clip_unet_60
type: Unknown Workflow
frequency: 14
level: weak
coverage: 0.954286
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图(人像)_2006960061226164225.json, 图片生成/文生图/文生图++Z-image多图猫咪 真实感_2048956527746224129.json, 图片生成/文生图/文生图+LoRA_2014558730028851201.json, 图片生成/文生图/文生图-Q版森林_2087797265531498498.json, 图片生成/文生图/文生图-qwen_image_2512-模板_2090689557934206978.json, 图片生成/文生图/文生图-微景观-迷你朋克工坊_2084933542248804354.json, 图片生成/文生图/文生图-微景观桃园_2088147505304395778.json, 图片生成/文生图/文生图-微景观草莓园_2085177631280029697.json, 图片生成/文生图/文生图-手机里的微景观_2084940722343600130.json, 图片生成/文生图/文生图合集_2038775252657905666.json, 图片生成/文生图/文生图合集_2049394125358764034.json, 图片生成/文生图/文生图合集（3种风格）_2038265960213258242.json, 图片生成/文生图/文生图，中英文都可以，我自己用，出图快 且准确 质量高_2026835950390747137.json, 图片生成/文生图/本地专用 Z-Image 文生图_2005279973143445506.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_60

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/文生图(人像)_2006960061226164225.json、图片生成/文生图/文生图++Z-image多图猫咪 真实感_2048956527746224129.json、图片生成/文生图/文生图+LoRA_2014558730028851201.json、图片生成/文生图/文生图-Q版森林_2087797265531498498.json、图片生成/文生图/文生图-qwen_image_2512-模板_2090689557934206978.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 12/14 个有
- `ConditioningZeroOut` —— 10/14 个有
- `ConditioningCombine` —— 1/14 个有
- `ConditioningSetTimestepRange` —— 1/14 个有
- `DuckHideNode` —— 1/14 个有
- `INTConstant` —— 1/14 个有
- `PrimitiveStringMultiline` —— 1/14 个有
- `easy bookmark` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 50 | 14 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 14 | 65% |
| 采样算法 | euler | - | 14 | 79% |
| 调度器 | simple | - | 14 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 50，14 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，14 个样本
- 采样算法 最常用 euler，14 个样本，一致性 79%
- 调度器 最常用 simple，14 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（15/14 个样本）：Steps较低可能导致细节不足
