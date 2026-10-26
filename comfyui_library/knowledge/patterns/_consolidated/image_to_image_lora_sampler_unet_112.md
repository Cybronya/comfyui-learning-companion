---
name: image_to_image_lora_sampler_unet_112
type: Image To Image
frequency: 6
level: moderate
coverage: 0.9425
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwenedit+zimage图片编辑_2004600121633505281.json, 图片生成/图生图/【AI播草机】QWEN图像参考_2031297541442113537.json, 图片生成/图生图/【AI播草机】QWEN图像编辑_2031303437199085569.json, 图片生成/图生图/人物场景一致套图，IP打造神器_2004016489734782978.json, 图片生成/图生图/人物场景一致套图，IP打造神器_2018876124696154114.json, 图片生成/图生图/🦄人物一致性IP神器🎯天下无腰_2022270208706093058.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_112

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/qwenedit+zimage图片编辑_2004600121633505281.json、图片生成/图生图/【AI播草机】QWEN图像参考_2031297541442113537.json、图片生成/图生图/【AI播草机】QWEN图像编辑_2031303437199085569.json、图片生成/图生图/人物场景一致套图，IP打造神器_2004016489734782978.json、图片生成/图生图/人物场景一致套图，IP打造神器_2018876124696154114.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEditPlus` —— 5/6 个有
- `CLIPTextEncode` —— 4/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `FluxKontextMultiReferenceLatentMethod` —— 4/6 个有
- `KSamplerAdvanced` —— 4/6 个有
- `AILab_QwenVL` —— 3/6 个有
- `CR Text` —— 3/6 个有
- `CR Text Replace` —— 3/6 个有
- `JDCN_StringToList` —— 3/6 个有
- `ProcessString` —— 3/6 个有
- `RunningHub Deepcleaner` —— 2/6 个有
- `StringConcatenate` —— 2/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `ResizeImagesByLongerEdge` —— 1/6 个有
- `easy promptLine` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 67% |
| Prompt 约束强度(CFG) | 10 | 1 - 10 | 6 | 39% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler_ancestral | - | 6 | 67% |
| 重绘幅度 | FlowMatchEulerDiscreteScheduler | - | 6 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 10，观测区间 1 - 10，6 个样本，取值分散，一致性仅 39%
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，6 个样本，一致性 67%
- 重绘幅度 最常用 FlowMatchEulerDiscreteScheduler，6 个样本，一致性 67%
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
