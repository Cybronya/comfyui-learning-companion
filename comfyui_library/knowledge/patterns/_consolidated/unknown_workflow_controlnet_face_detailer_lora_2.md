---
name: unknown_workflow_controlnet_face_detailer_lora_2
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.786667
common_nodes: [ApplyFBCacheOnModel, BNK_CLIPTextEncodeAdvanced, CLIPSetLastLayer, CR Text, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DeepTranslatorTextNode, FaceAnalysisModels, FaceDetailer, FaceEmbedDistance, HyperLoRAApplyLoRA, HyperLoRAConfig, HyperLoRAFaceAttr, HyperLoRAGenerateIDLoRA, HyperLoRAIDCond, HyperLoRALoader, ImpactMakeImageBatch, KSampler, LoadImage, PreviewImage, SaveImage, UltralyticsDetectorProvider, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/HyperLoRA+InstantID 换脸_1916376487573000194.json, 图片生成/图生图/HyperLoRA高效真人换脸工作流_1916327908766318593.json, 图片生成/文生图/HyperLoRA零样本真人ID一致性换脸工作流_1916141850053246977.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_face_detailer_lora_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/HyperLoRA+InstantID 换脸_1916376487573000194.json、图片生成/图生图/HyperLoRA高效真人换脸工作流_1916327908766318593.json、图片生成/文生图/HyperLoRA零样本真人ID一致性换脸工作流_1916141850053246977.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyFBCacheOnModel`
- `BNK_CLIPTextEncodeAdvanced`
- `CLIPSetLastLayer`
- `CR Text`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DeepTranslatorTextNode`
- `FaceAnalysisModels`
- `FaceDetailer`
- `FaceEmbedDistance`
- `HyperLoRAApplyLoRA`
- `HyperLoRAConfig`
- `HyperLoRAFaceAttr`
- `HyperLoRAGenerateIDLoRA`
- `HyperLoRAIDCond`
- `HyperLoRALoader`
- `ImpactMakeImageBatch`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UltralyticsDetectorProvider`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ApplyInstantIDAdvanced` —— 2/3 个有
- `EmptyLatentImage` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `InstantIDFaceAnalysis` —— 2/3 个有
- `InstantIDModelLoader` —— 2/3 个有
- `LayerMask: PersonMaskUltra V2` —— 2/3 个有
- `LayerUtility: CropByMask V2` —— 2/3 个有
- `OpenposePreprocessor` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `Text Concatenate` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `ApplyInstantID` —— 1/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `Miaoshouai_Tagger` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `SDXLEmptyLatentSizePicker+` —— 1/3 个有
- `easy showAnything` —— 1/3 个有
- `ttN concat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 5 | 3 - 5 | 3 | 78% |
| 采样算法 | dpmpp_2m | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.7 | 0.7 - 0.7 | 3 | 100% |
| 宽度 | 1064 | - | 2 | 72% |
| 高度 | 768 | 1 - 1360 | 3 | 22% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 3 - 5，3 个样本
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.7，观测区间 0.7 - 0.7，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1064，样本不足，未给区间，2 个样本
- 高度 中位数 768，观测区间 1 - 1360，3 个样本，取值分散，一致性仅 22%
