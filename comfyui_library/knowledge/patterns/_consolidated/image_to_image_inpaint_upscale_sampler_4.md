---
name: image_to_image_inpaint_upscale_sampler_4
type: Image To Image
frequency: 2
level: weak
coverage: 0.727
common_nodes: [ApplyPulidFlux, BboxDetectorSEGS, CLIPTextEncode, Crop Face, DF_Image_scale_to_side, DualCLIPLoader, Fast Groups Bypasser (rgthree), Float, FluxGuidance, GrowMask, Image Comparer (rgthree), ImageComposite+, ImageCrop+, ImageResize+, ImageResizeKJ, ImageScaleBy, ImageUpscaleWithModel, InpaintModelConditioning, KSampler, Load RetinaFace, LoadImage, Mask Crop Region, MaskBlur+, MaskToImage, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, SAMDetectorCombined, SAMLoader, SaveImage, TextBox, UltralyticsDetectorProvider, UnetLoaderGGUF, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/Flux模型快速换脸ins风滤镜_1854809437205893122.json, 平台全量/商业形象换脸_1859835761737560065.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_sampler_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Flux模型快速换脸ins风滤镜_1854809437205893122.json、平台全量/商业形象换脸_1859835761737560065.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `BboxDetectorSEGS`
- `CLIPTextEncode`
- `Crop Face`
- `DF_Image_scale_to_side`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `Float`
- `FluxGuidance`
- `GrowMask`
- `Image Comparer (rgthree)`
- `ImageComposite+`
- `ImageCrop+`
- `ImageResize+`
- `ImageResizeKJ`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `KSampler`
- `Load RetinaFace`
- `LoadImage`
- `Mask Crop Region`
- `MaskBlur+`
- `MaskToImage`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `SAMDetectorCombined`
- `SAMLoader`
- `SaveImage`
- `TextBox`
- `UltralyticsDetectorProvider`
- `UnetLoaderGGUF`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Apply Instagram Filter` —— 1/2 个有
- `BasicGuider` —— 1/2 个有
- `BasicScheduler` —— 1/2 个有
- `ControlNetApplySD3` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `DisplayText` —— 1/2 个有
- `Get resolution [Crystools]` —— 1/2 个有
- `Image Overlay` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `KSamplerSelect` —— 1/2 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/2 个有
- `Make Image Batch` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `RH_Prompter` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | - | 1 | 100% |
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 0.64 | - | 2 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 0.64，样本不足，未给区间，2 个样本，取值集中（一致性 98%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
