---
name: unknown_workflow_lora_sampler_checkpoint_6
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9735
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, FluxKontextMultiReferenceLatentMethod, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, QwenMultiangleCameraNode, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/002.Qwen编辑之王021.单人角度控制_2034853239019016193.json, 图片生成/图生图/002.Qwen编辑之王022.单人多角度控制_2034854397078933505.json, 图片生成/图生图/5.其他类型-6.NSF+-08.Qwen_2511生图004.Qwen_2511单人角度控制.js_2021976998549131266.json, 图片生成/图生图/5.其他类型-6.NSF+-08.Qwen_2511生图005.Qwen_2511多角度控制.jso_2021977065486032898.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint_6

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/002.Qwen编辑之王021.单人角度控制_2034853239019016193.json、图片生成/图生图/002.Qwen编辑之王022.单人多角度控制_2034854397078933505.json、图片生成/图生图/5.其他类型-6.NSF+-08.Qwen_2511生图004.Qwen_2511单人角度控制.js_2021976998549131266.json、图片生成/图生图/5.其他类型-6.NSF+-08.Qwen_2511生图005.Qwen_2511多角度控制.jso_2021977065486032898.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 2/4 个有
- `easy promptList` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
