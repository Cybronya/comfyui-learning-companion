---
name: unknown_workflow_lora_sampler_unet_294
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5115
common_nodes: [AddLabel, CFGNorm, CLIPLoader, Create Grid Image from Batch, GetNode, ImpactMakeImageList, Int, JoinStrings, KSampler, LoadImage, Lora Loader, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, PrimitiveInt, PrimitiveString, ReActorImageDublicator, SaveImage, Seed_, SetNode, TextEncodeQwenImageEditPlus_lrzjason, TextInput_, UNETLoader, VAEDecode, VAELoader, easy convertAnything, easy imageListToImageBatch, easy rangeFloat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/蜡笔画转绘_2007739845896052738.json, 图片生成/文生图/Qwen Image Edit Lora-xy测试工作流_2073327775062249474.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_294

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/蜡笔画转绘_2007739845896052738.json、图片生成/文生图/Qwen Image Edit Lora-xy测试工作流_2073327775062249474.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 2 个 workflow 都包含：
- `AddLabel`
- `CFGNorm`
- `CLIPLoader`
- `Create Grid Image from Batch`
- `GetNode`
- `ImpactMakeImageList`
- `Int`
- `JoinStrings`
- `KSampler`
- `LoadImage`
- `Lora Loader`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveInt`
- `PrimitiveString`
- `ReActorImageDublicator`
- `SaveImage`
- `Seed_`
- `SetNode`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy convertAnything`
- `easy imageListToImageBatch`
- `easy rangeFloat`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `SeedVR2LoadDiTModel` —— 1/2 个有
- `SeedVR2LoadVAEModel` —— 1/2 个有
- `SeedVR2VideoUpscaler` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 40% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（10/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
