---
name: image_to_image_sampler_vae_35
type: Image To Image
frequency: 2
level: weak
coverage: 0.528
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, GetNode, ImageConcatMulti, ImageScaleToTotalPixels, KSampler, LayerUtility: CropByMask V2, LoadImage, ModelSamplingAuraFlow, PreviewImage, RHHiddenNodes, SaveImage, SetNode, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader, easy imageRemBg]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物一键制作角色四视图 - 高效省力 - V1_2006398311204397058.json, 图片生成/图生图/单图一键制作角色多视角（四视图）_1987716537224204290.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_35

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/人物一键制作角色四视图 - 高效省力 - V1_2006398311204397058.json、图片生成/图生图/单图一键制作角色多视角（四视图）_1987716537224204290.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：53%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `GetNode`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: CropByMask V2`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageRemBg`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 0 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 0，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（8/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
