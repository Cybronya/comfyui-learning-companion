---
name: unknown_workflow_controlnet_inpaint_face_detailer
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.922
common_nodes: [Any Switch (rgthree), Anything Everywhere3, ApplyInstantID, CLIPLoader, ColorMatch, ControlNetLoader, CropFace, DifferentialDiffusion, EG_LJ_JZTXDZ, FaceDetailer, Image Comparer (rgthree), ImageBatchMulti, ImageFromBatch, ImpactInt, ImpactSEGSConcat, ImpactSEGSOrderedFilter, ImpactSEGSToMaskBatch, ImpactSimpleDetectorSEGS, InpaintCrop, InpaintModelConditioning, InpaintStitch, InstantIDFaceAnalysis, InstantIDModelLoader, LayerMask: MaskGrow, LoadImage, MaskFromBatch+, MaskToImage, Pipe from any [Crystools], Pipe to/edit any [Crystools], ReActorFaceSwap, SAMLoader, SEGSPreview, SaveImage, Switch image [Crystools], UltralyticsDetectorProvider, easy a1111Loader, easy forLoopEnd, easy forLoopStart, easy fullkSampler, easy getNode, easy imageCount, easy pipeOut, easy setNode]
problems: []
missing: []
members: [图片生成/图生图/多人换脸_1911652331983728642.json, 平台全量/旅拍机-淘汰-多人换脸普通候选-运行失败_2071278485066309633.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_face_detailer

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/多人换脸_1911652331983728642.json、平台全量/旅拍机-淘汰-多人换脸普通候选-运行失败_2071278485066309633.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Anything Everywhere3`
- `ApplyInstantID`
- `CLIPLoader`
- `ColorMatch`
- `ControlNetLoader`
- `CropFace`
- `DifferentialDiffusion`
- `EG_LJ_JZTXDZ`
- `FaceDetailer`
- `Image Comparer (rgthree)`
- `ImageBatchMulti`
- `ImageFromBatch`
- `ImpactInt`
- `ImpactSEGSConcat`
- `ImpactSEGSOrderedFilter`
- `ImpactSEGSToMaskBatch`
- `ImpactSimpleDetectorSEGS`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `LayerMask: MaskGrow`
- `LoadImage`
- `MaskFromBatch+`
- `MaskToImage`
- `Pipe from any [Crystools]`
- `Pipe to/edit any [Crystools]`
- `ReActorFaceSwap`
- `SAMLoader`
- `SEGSPreview`
- `SaveImage`
- `Switch image [Crystools]`
- `UltralyticsDetectorProvider`
- `easy a1111Loader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy fullkSampler`
- `easy getNode`
- `easy imageCount`
- `easy pipeOut`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
