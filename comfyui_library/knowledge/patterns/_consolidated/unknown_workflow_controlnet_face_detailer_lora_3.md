---
name: unknown_workflow_controlnet_face_detailer_lora_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.483
common_nodes: [ApplyInstantIDAdvanced, BNK_CLIPTextEncodeAdvanced, CR Text Concatenate, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, FaceDetailer, Fast Groups Bypasser (rgthree), Florence2ModelLoader, Florence2Run, GetImageSizeAndCount, GetNode, HyperLoRAApplyLoRA, HyperLoRAConfig, HyperLoRAFaceAttr, HyperLoRAGenerateIDLoRA, HyperLoRAIDCond, HyperLoRALoader, ImageScaleToMegapixels, ImpactMakeImageBatch, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, Label (rgthree), LoadImage, MinNode, OpenposePreprocessor, PreviewImage, SaveImage, SetNode, StringConstant, UltralyticsDetectorProvider, VAEDecode, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/HyperLoRA参考图片生图_1917082932597690369.json, 图片生成/文生图/2025-04-28 HyperLoRA-T2I 实现一致性人物_1916766121478000642.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_face_detailer_lora_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/HyperLoRA参考图片生图_1917082932597690369.json、图片生成/文生图/2025-04-28 HyperLoRA-T2I 实现一致性人物_1916766121478000642.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：48%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyInstantIDAdvanced`
- `BNK_CLIPTextEncodeAdvanced`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `FaceDetailer`
- `Fast Groups Bypasser (rgthree)`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetImageSizeAndCount`
- `GetNode`
- `HyperLoRAApplyLoRA`
- `HyperLoRAConfig`
- `HyperLoRAFaceAttr`
- `HyperLoRAGenerateIDLoRA`
- `HyperLoRAIDCond`
- `HyperLoRALoader`
- `ImageScaleToMegapixels`
- `ImpactMakeImageBatch`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `Label (rgthree)`
- `LoadImage`
- `MinNode`
- `OpenposePreprocessor`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `StringConstant`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 5 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| ControlNet 权重 | 0.7 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
