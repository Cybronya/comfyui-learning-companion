---
name: text_to_image_controlnet_inpaint_upscale
type: Text To Image
frequency: 2
level: weak
coverage: 0.589
common_nodes: [ApplyInstantID, CLIPTextEncode, CR Text, CheckpointLoaderSimple, ColorMatch, ConditioningZeroOut, ControlNetLoader, CropMask, DualCLIPLoader, EmptyLatentImage, FaceAnalysisModels, FaceBoundingBox, GrowMask, Image Comparer (rgthree), ImageResize+, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: MaskPreview, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoader, MaskBlur+, PreviewImage, RepeatLatentBatch, SUPIR_Upscale, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Aspect Ratio, CR Text, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, MaskBlur+, ImageResize+, LayerMask: MaskPreview, CR Text Concatenate, easy imageSize]
members: [图片生成/文生图/1988772214726078465.json, 图片生成/文生图/1988882107839680513.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_upscale

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1988772214726078465.json、图片生成/文生图/1988882107839680513.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：59%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ConditioningZeroOut`
- `ControlNetLoader`
- `CropMask`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `GrowMask`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoader`
- `MaskBlur+`
- `PreviewImage`
- `RepeatLatentBatch`
- `SUPIR_Upscale`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `CR Aspect Ratio` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `CannyEdgePreprocessor` —— 1/2 个有
- `ControlNetApplySD3` —— 1/2 个有
- `DepthAnythingPreprocessor` —— 1/2 个有
- `FaceDetailer` —— 1/2 个有
- `OpenposePreprocessor` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `UltralyticsDetectorProvider` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2.25 | - | 2 | 44% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 832 | - | 2 | 92% |
| 高度 | 1088 | - | 2 | 94% |
| LoRA 模型强度 | 0.7 | - | 2 | 86% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.7 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 832，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 高度 中位数 1088，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- LoRA 模型强度 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Aspect Ratio、CR Text、LayerMask: PersonMaskUltra V2、LayerUtility: CropBoxResolve、LayerUtility: CropByMask V2
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
