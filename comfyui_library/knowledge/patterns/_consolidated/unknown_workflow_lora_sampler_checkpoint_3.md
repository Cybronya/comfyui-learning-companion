---
name: unknown_workflow_lora_sampler_checkpoint_3
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [CR Text, CheckpointLoaderSimple, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, ModelSamplingAuraFlow, RHHiddenNodes, SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/专为SeeDance 2.0AI短剧漫剧专用超真实感资产道具库QwenRapidAIO V23_2027230287247187970.json, 图片生成/文生图/超真实感道具生成_2027209573307785218.json, 图片生成/文生图/道具库QwenRapidAIO+V23_2027221533550190594.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/专为SeeDance 2.0AI短剧漫剧专用超真实感资产道具库QwenRapidAIO V23_2027230287247187970.json、图片生成/文生图/超真实感道具生成_2027209573307785218.json、图片生成/文生图/道具库QwenRapidAIO+V23_2027221533550190594.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Text`
- `CheckpointLoaderSimple`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RHHiddenNodes`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageLoader` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta57 | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta57，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
