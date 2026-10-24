---
name: unknown_workflow_lora_sampler_checkpoint_14
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.944
common_nodes: [CheckpointLoaderSimple, CompressImages, CropWithPadInfo, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, QwenEditOutputExtractor, TextEncodeQwenImageEditPlusCustom_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QE2511 超高一致性换装 zip压缩_2013350144653135873.json, 图片生成/图生图/QwenEditUtils 2.2 Optional Mask (1)_1992579715970166785.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint_14

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/QE2511 超高一致性换装 zip压缩_2013350144653135873.json、图片生成/图生图/QwenEditUtils 2.2 Optional Mask (1)_1992579715970166785.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `CompressImages`
- `CropWithPadInfo`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `UNETLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
