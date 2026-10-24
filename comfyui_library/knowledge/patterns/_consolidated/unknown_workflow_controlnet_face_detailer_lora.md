---
name: unknown_workflow_controlnet_face_detailer_lora
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8072
common_nodes: [ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, FaceAnalysisModels, FaceBoundingBox, FaceDetailer, ImageCompositeMasked, ImageResize+, ImpactMakeImageBatch, InstantIDFaceAnalysis, InstantIDModelLoader, LayerMask: MaskGrow, LoadImage, LoraLoader, MaskPreview+, PreviewImage, SAMLoader, SaveImage, UltralyticsDetectorProvider]
problems: []
missing: []
members: [图片生成/图生图/一键换脸工作流99%相似度_1934959702251872258.json, 图片生成/图生图/换脸工作流_99%相似度_带两种放大功能（二选一）_1913557262890168321.json, 图片生成/图生图/最强换脸工作流（带放大功能）V1_1898644769197740034.json, 图片生成/图生图/最自然的换脸组合InstantID+IPadapter_1911960078306504706.json, 图片生成/图生图/模特多图参考一键换脸_1985690759871508482.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_face_detailer_lora

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/一键换脸工作流99%相似度_1934959702251872258.json、图片生成/图生图/换脸工作流_99%相似度_带两种放大功能（二选一）_1913557262890168321.json、图片生成/图生图/最强换脸工作流（带放大功能）V1_1898644769197740034.json、图片生成/图生图/最自然的换脸组合InstantID+IPadapter_1911960078306504706.json、图片生成/图生图/模特多图参考一键换脸_1985690759871508482.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `FaceDetailer`
- `ImageCompositeMasked`
- `ImageResize+`
- `ImpactMakeImageBatch`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `LayerMask: MaskGrow`
- `LoadImage`
- `LoraLoader`
- `MaskPreview+`
- `PreviewImage`
- `SAMLoader`
- `SaveImage`
- `UltralyticsDetectorProvider`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `SUPIR_Upscale` —— 3/5 个有
- `UpscaleModelLoader` —— 3/5 个有
- `ColorMatch` —— 2/5 个有
- `ConstrainImage|pysssss` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `ImageScaleBy` —— 2/5 个有
- `ImageUpscaleWithModel` —— 2/5 个有
- `easy imageSize` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `IPAdapterFaceID` —— 1/5 个有
- `IPAdapterUnifiedLoaderFaceID` —— 1/5 个有
- `UltimateSDUpscale` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.6 | 0.6 - 1 | 5 | 76% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.6，观测区间 0.6 - 1，5 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
