---
name: image_to_image_lora_sampler_clip_78
type: Image To Image
frequency: 4
level: strong
coverage: 0.954
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, FluxKontextMultiReferenceLatentMethod, KSampler, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwenedit+zimage图片编辑_2004600121633505281.json, 图片生成/图生图/人物场景一致套图，IP打造神器_2004016489734782978.json, 图片生成/图生图/人物场景一致套图，IP打造神器_2018876124696154114.json, 图片生成/图生图/🦄人物一致性IP神器🎯天下无腰_2022270208706093058.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_78

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/qwenedit+zimage图片编辑_2004600121633505281.json、图片生成/图生图/人物场景一致套图，IP打造神器_2004016489734782978.json、图片生成/图生图/人物场景一致套图，IP打造神器_2018876124696154114.json、图片生成/图生图/🦄人物一致性IP神器🎯天下无腰_2022270208706093058.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 3/4 个有
- `CR Text` —— 3/4 个有
- `CR Text Replace` —— 3/4 个有
- `JDCN_StringToList` —— 3/4 个有
- `ProcessString` —— 3/4 个有
- `RunningHub Deepcleaner` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `ResizeImagesByLongerEdge` —— 1/4 个有
- `easy promptLine` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 10 | 10 - 10 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler_ancestral | - | 4 | 100% |
| 重绘幅度 | FlowMatchEulerDiscreteScheduler | - | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 10，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，4 个样本，一致性 100%
- 重绘幅度 最常用 FlowMatchEulerDiscreteScheduler，4 个样本，一致性 100%
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
