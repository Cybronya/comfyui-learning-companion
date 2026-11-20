---
name: unknown_workflow_controlnet_lora_sampler_31
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9285
common_nodes: [CFGNorm, CR Text, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, DWPreprocessor, EmptyLatentImage, FluxKontextMultiReferenceLatentMethod, HAIGC_SaveImagesToZip, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SetUnionControlNetType, TextEncodeQwenImageEditPlus, VAEDecode, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/姿势模仿QwenEdit+RAPID-AIO_2057809610521792514.json, 图片生成/图生图/姿势模仿V3_2058745138565967874.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_31

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/姿势模仿QwenEdit+RAPID-AIO_2057809610521792514.json、图片生成/图生图/姿势模仿V3_2058745138565967874.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DWPreprocessor`
- `EmptyLatentImage`
- `FluxKontextMultiReferenceLatentMethod`
- `HAIGC_SaveImagesToZip`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SetUnionControlNetType`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| ControlNet 权重 | 0.935 | - | 2 | 93% |
| 采样步数 | 12 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 50% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 0.91 | - | 2 | 90% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.935，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 采样步数 中位数 12，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 0.91，样本不足，未给区间，2 个样本，取值集中（一致性 90%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
