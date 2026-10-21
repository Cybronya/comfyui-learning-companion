---
name: image_to_image_lora_sampler_unet_38
type: Image To Image
frequency: 2
level: weak
coverage: 0.6385
common_nodes: [CLIPLoader, ConditioningZeroOut, GetNode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RH_LLMAPI_NODE, SaveImage, SetNode, Text, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Edit-2511 一张图生成分镜一致性电影、短片_2003730564337311745.json, 图片生成/文生图/言刻·玉牌智造_2018934071522496514.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_38

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Qwen-Edit-2511 一张图生成分镜一致性电影、短片_2003730564337311745.json、图片生成/文生图/言刻·玉牌智造_2018934071522496514.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `GetNode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `ProcessString` —— 1/2 个有
- `QZ_ResolutionPreset` —— 1/2 个有
- `TextCombinerTwo` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/2 个有
- `easy promptLine` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 50% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 50%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
