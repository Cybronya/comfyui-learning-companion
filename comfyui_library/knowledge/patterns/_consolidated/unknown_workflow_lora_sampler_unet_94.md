---
name: unknown_workflow_lora_sampler_unet_94
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.800286
common_nodes: [Any Switch (rgthree), CFGNorm, CLIPLoader, CR Text, CR Text Concatenate, ConditioningZeroOut, CropWithPadInfo, FluxKontextMultiReferenceLatentMethod, GetImageSize, ImpactMinMax, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, Qwen3_VQA, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit2511+AnyPose免骨架姿态迁移lora，4 步高效出图_2021113810890788866.json, 图片生成/图生图/Qwen-Image-Edit2511+AnyPose免骨架姿态迁移lora，4 步高效出图_2007712919701692418.json, 图片生成/图生图/Qwen-Image-Edit2511+AnyPose免骨架姿态迁移lora，4 步高效出图_2008718061972496385.json, 图片生成/图生图/Qwen-Image-Edit2511+AnyPose免骨架姿态迁移lora，4 步高效出图_2043108574913634305.json, 图片生成/图生图/Qwen-Image免骨架姿态迁移l_2021760534307147778.json, 图片生成/图生图/人物姿态迁移Qwen-Image-Edit2511+AnyPose_2008786454448709634.json, 图片生成/图生图/参考人物姿势迁移_2010268614363979778.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_94

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit2511+AnyPose免骨架姿态迁移lora，4 步高效出图_2021113810890788866.json、图片生成/图生图/Qwen-Image-Edit2511+AnyPose免骨架姿态迁移lora，4 步高效出图_2007712919701692418.json、图片生成/图生图/Qwen-Image-Edit2511+AnyPose免骨架姿态迁移lora，4 步高效出图_2008718061972496385.json、图片生成/图生图/Qwen-Image-Edit2511+AnyPose免骨架姿态迁移lora，4 步高效出图_2043108574913634305.json、图片生成/图生图/Qwen-Image免骨架姿态迁移l_2021760534307147778.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `FluxKontextMultiReferenceLatentMethod`
- `GetImageSize`
- `ImpactMinMax`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `Qwen3_VQA`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 5/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 7 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，7 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
