---
name: image_to_image_lora_sampler_unet_170
type: Image To Image
frequency: 3
level: strong
coverage: 0.644333
common_nodes: [CLIPLoader, ConditioningZeroOut, GetNode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RH_LLMAPI_NODE, SaveImage, SetNode, Text, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit-2511图生分镜_电影、短片人物一致性_2043969511224778753.json, 图片生成/文生图/Qwen-Edit-2511 一张图生成分镜一致性电影、短片_2003730564337311745.json, 图片生成/文生图/言刻·玉牌智造_2018934071522496514.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_170

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit-2511图生分镜_电影、短片人物一致性_2043969511224778753.json、图片生成/文生图/Qwen-Edit-2511 一张图生成分镜一致性电影、短片_2003730564337311745.json、图片生成/文生图/言刻·玉牌智造_2018934071522496514.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
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
- `CFGNorm` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `ProcessString` —— 2/3 个有
- `QZ_ResolutionPreset` —— 2/3 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/3 个有
- `easy promptLine` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `TextCombinerTwo` —— 1/3 个有
- `TextEncodeQwenImageEditPlus` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
