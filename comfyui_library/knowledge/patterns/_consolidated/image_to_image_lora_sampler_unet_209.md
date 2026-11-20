---
name: image_to_image_lora_sampler_unet_209
type: Image To Image
frequency: 2
level: weak
coverage: 0.6145
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, Fast Groups Bypasser (rgthree), GetNode, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SetNode, Text, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/AI代码侠土豆-Qwen-Edit-2511   单图+双图编辑_2002677750794186754.json, 图片生成/图生图/Qwen-Edit-2511   单图+双图编辑_2044987054626447361.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_209

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/AI代码侠土豆-Qwen-Edit-2511   单图+双图编辑_2002677750794186754.json、图片生成/图生图/Qwen-Edit-2511   单图+双图编辑_2044987054626447361.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `Text`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DrawMaskOnImage` —— 1/2 个有
- `MuyeSizeSelector` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
