---
name: unknown_workflow_lora_sampler_unet_66
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8545
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptySD3LatentImage, Int, JjkConcat, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, SizeSelector, Text, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy setNode]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, easy boolean, easy getNode, easy setNode]
members: [图片生成/图生图/2087508775061254145.json, 数字人/数字人/真人参考生成基础演员资产_2094427436439134210.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_66

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2087508775061254145.json、数字人/数字人/真人参考生成基础演员资产_2094427436439134210.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `Int`
- `JjkConcat`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SizeSelector`
- `Text`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `GODMT_BatchToList` —— 1/2 个有
- `GODMT_SplitString` —— 1/2 个有
- `ImageMergeNode` —— 1/2 个有
- `easy boolean` —— 1/2 个有
- `easy getNode` —— 1/2 个有
- `easy ifElse` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | sa_solver | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerUtility: ImageScaleByAspectRatio V2、easy boolean、easy getNode、easy setNode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
