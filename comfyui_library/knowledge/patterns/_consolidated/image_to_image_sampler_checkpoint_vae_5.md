---
name: image_to_image_sampler_checkpoint_vae_5
type: Image To Image
frequency: 2
level: weak
coverage: 0.5285
common_nodes: [CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), KSampler, LoadImage, SaveImage, SetNode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/(16G显存20秒出图工作流)AI代码侠土豆 Qwen-Edit-AIO(合集)_1976560992148692993.json, 图片生成/图生图/Qwen-AIO   单图&双图&三图编辑 人物一致性_2005277431428771841.json]
source: knowledge_consolidation
---

# image_to_image_sampler_checkpoint_vae_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/(16G显存20秒出图工作流)AI代码侠土豆 Qwen-Edit-AIO(合集)_1976560992148692993.json、图片生成/图生图/Qwen-AIO   单图&双图&三图编辑 人物一致性_2005277431428771841.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：53%

## 共有节点

全部 2 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `Text` —— 1/2 个有
- `TextEncodeQwenImageEdit` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | sa_solver | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（7/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
