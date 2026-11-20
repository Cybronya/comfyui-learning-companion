---
name: unknown_workflow_inpaint_upscale_lora_9
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.859
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Simple Image Compare, CheckpointLoaderSimple, ConditioningZeroOut, DetailerForEach, DifferentialDiffusion, DualCLIPLoader, FaceAnalysisModels, FaceBoundingBox, Florence2ModelLoader, Florence2Run, FluxGuidance, GetImageSizeAndCount, GetImage_(Width&Height) _O, GrowMask, INPAINT_ExpandMask, ImageCompositeMasked, ImageConcanate, ImageScale, ImageScaleBy, ImageUpscaleWithModel, ImpactGaussianBlurMask, ImpactSimpleDetectorSEGS, InpaintModelConditioning, InvertMask, KSampler, LayerColor: ColorAdapter, LayerMask: PersonMaskUltra V2, LoadImage, LoraLoaderModelOnly, MaskFromColor+, MaskPreview+, MaskToImage, MaskToSEGS, ModelSamplingFlux, PreviewImage, SEGSPreview, SaveImage, SegsToCombinedMask, StyleModelApply, StyleModelLoader, SubtractMask, UNETLoader, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageInsetCrop]
problems: [Steps较低可能导致细节不足]
missing: []
members: ["平台全量/100% facial consistency change face, photo_1863459986448822274.json", 平台全量/一键换脸100%相似度（fill+redux+ACE方案）_1926278872659316738.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_lora_9

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/100% facial consistency change face, photo_1863459986448822274.json、平台全量/一键换脸100%相似度（fill+redux+ACE方案）_1926278872659316738.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Simple Image Compare`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DetailerForEach`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `GetImageSizeAndCount`
- `GetImage_(Width&Height) _O`
- `GrowMask`
- `INPAINT_ExpandMask`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageScale`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImpactGaussianBlurMask`
- `ImpactSimpleDetectorSEGS`
- `InpaintModelConditioning`
- `InvertMask`
- `KSampler`
- `LayerColor: ColorAdapter`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskFromColor+`
- `MaskPreview+`
- `MaskToImage`
- `MaskToSEGS`
- `ModelSamplingFlux`
- `PreviewImage`
- `SEGSPreview`
- `SaveImage`
- `SegsToCombinedMask`
- `StyleModelApply`
- `StyleModelLoader`
- `SubtractMask`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageInsetCrop`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
