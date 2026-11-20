---
name: unknown_workflow_lora_sampler_unet_251
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.776
common_nodes: [CFGNorm, CLIPLoader, CR Index, CR Text, ConditioningZeroOut, GetNode, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, MuyeTextEditOutput, QwenEditConfigPreparer, SaveImage, Seed (rgthree), SetNode, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy imageScaleDownToSize, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/28photoretouching_2049469543893962754.json, 图片生成/图生图/qwen-edit-图片精修-深度优化版4.0_2013194815093084162.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_251

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/28photoretouching_2049469543893962754.json、图片生成/图生图/qwen-edit-图片精修-深度优化版4.0_2013194815093084162.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Index`
- `CR Text`
- `ConditioningZeroOut`
- `GetNode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `MuyeTextEditOutput`
- `QwenEditConfigPreparer`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy imageScaleDownToSize`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `LayerUtility: ImageReel` —— 1/2 个有
- `LayerUtility: ImageReelComposit` —— 1/2 个有
- `RTXVideoSuperResolution` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
