---
name: unknown_workflow_controlnet_lora_sampler_14
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.84625
common_nodes: [CFGNorm, CR Text, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, DWPreprocessor, EmptyLatentImage, FluxKontextMultiReferenceLatentMethod, ImageStitch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SetUnionControlNetType, TextEncodeQwenImageEditPlus, VAEDecode, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 人物换装_2026867833468100609.json, 图片生成/图生图/姿势模仿QwenEdit 2511+AnyPose+CN+F2P（多种控制加强-人脸一致性）_2007834878842249217.json, 图片生成/图生图/姿势模仿QwenEdit+2511+AnyPose+CN+F2P（控制加强-人脸一致性）_2008018964739268610.json, 图片生成/图生图/自动换装人物一致换装 完美平替_2044393544395268098.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_14

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen 人物换装_2026867833468100609.json、图片生成/图生图/姿势模仿QwenEdit 2511+AnyPose+CN+F2P（多种控制加强-人脸一致性）_2007834878842249217.json、图片生成/图生图/姿势模仿QwenEdit+2511+AnyPose+CN+F2P（控制加强-人脸一致性）_2008018964739268610.json、图片生成/图生图/自动换装人物一致换装 完美平替_2044393544395268098.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DWPreprocessor`
- `EmptyLatentImage`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageStitch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/4 个有
- `CropWithPadInfo` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ImageScaleBy` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `QwenEditAdaptiveLongestEdge` —— 2/4 个有
- `QwenEditConfigPreparer` —— 2/4 个有
- `QwenEditOutputExtractor` —— 2/4 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `VAELoader` —— 2/4 个有
- `LayerUtility: ImageReel` —— 1/4 个有
- `LayerUtility: ImageReelComposit` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
