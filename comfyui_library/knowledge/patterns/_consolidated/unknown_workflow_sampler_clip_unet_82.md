---
name: unknown_workflow_sampler_clip_unet_82
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.901
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, Image Comparer (rgthree), KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z - IMAGE - Distill loRa 速度对比工作流_2024672851546083330.json, 图片生成/文生图/Z-Image-Turbo LoRA 出图+放大_2018944118063370242.json, 图片生成/文生图/Z-distill lora对比工作流_2082076301388767234.json, 图片生成/文生图/Zimage base 4步8步Lora对比_2021782849505992705.json, 图片生成/文生图/lora生图_2_2019229829660418050.json, 图片生成/文生图/lora生图_3_api_2019356189305348098.json, 图片生成/文生图/lora生图_4_api_2019591115476836353.json, 图片生成/文生图/lora生图_5_api_2019618073682124802.json, 图片生成/文生图/太强了！最高20倍提速！最新Z-distill lora对比工作流_2028648181180928001.json, 图片生成/文生图/最高20倍提速！Z-distill lora对比工作流_2021664209846673409.json, 图片生成/文生图/最高20倍提速！Z-distill lora对比工作流_2038453840286064642.json, 图片生成/文生图/超20倍提速！Z-distill-lora效果对比_2028642862866370561.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_82

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Z - IMAGE - Distill loRa 速度对比工作流_2024672851546083330.json、图片生成/文生图/Z-Image-Turbo LoRA 出图+放大_2018944118063370242.json、图片生成/文生图/Z-distill lora对比工作流_2082076301388767234.json、图片生成/文生图/Zimage base 4步8步Lora对比_2021782849505992705.json、图片生成/文生图/lora生图_2_2019229829660418050.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/12 个有
- `LoraLoaderModelOnly` —— 9/12 个有
- `AddLabel` —— 7/12 个有
- `ImageConcatMulti` —— 7/12 个有
- `easy globalSeed` —— 7/12 个有
- `easy promptList` —— 7/12 个有
- `SeedVR2` —— 5/12 个有
- `SeedVR2BlockSwap` —— 5/12 个有
- `LoraLoader|pysssss` —— 3/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有
- `Text` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 50 | 12 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 12 | 55% |
| 采样算法 | res_multistep | - | 12 | 58% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| LoRA 模型强度 | 1 | 0 - 1 | 3 | 29% |
| LoRA 文本强度 | 1 | 0 - 1 | 3 | 29% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 50，12 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，12 个样本
- 采样算法 最常用 res_multistep，12 个样本，一致性 58%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0 - 1，3 个样本，取值分散，一致性仅 29%
- LoRA 文本强度 中位数 1，观测区间 0 - 1，3 个样本，取值分散，一致性仅 29%
- 高发问题（19/12 个样本）：Steps较低可能导致细节不足
