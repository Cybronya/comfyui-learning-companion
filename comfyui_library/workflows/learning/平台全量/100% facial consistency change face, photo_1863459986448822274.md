---
key: 平台全量/100% facial consistency change face, photo_1863459986448822274.json
name: 100% facial consistency change face, photo_1863459986448822274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/100% facial consistency change face, photo_1863459986448822274.json
hash: 2b885f33bdf5458d
coverage: 0.864865
learned_at: 2026-11-14 00:10:32
nodes: [LoadImage, ImageScale, GetImage_(Width&Height) _O, LoadImage, FaceBoundingBox, FaceAnalysisModels, PreviewImage, FaceAnalysisModels, FaceBoundingBox, PreviewImage, ImageScale, UpscaleModelLoader, LayerColor: ColorAdapter, ImageUpscaleWithModel, ImageScaleBy, ImageCompositeMasked, PreviewImage, PreviewImage, ImageConcanate, PreviewImage, MaskFromColor+, LayerMask: PersonMaskUltra V2, ImageConcanate, ImpactSimpleDetectorSEGS, UltralyticsDetectorProvider, SegsToCombinedMask, SEGSPreview, MaskPreview+, PreviewImage, MaskPreview+, INPAINT_ExpandMask, ImpactGaussianBlurMask, MaskToImage, InvertMask, SubtractMask, MaskPreview+, MaskPreview+, GrowMask, MaskToSEGS, DualCLIPLoader, CLIPTextEncode, VAELoader, CLIPVisionLoader, GetImageSizeAndCount, LoraLoaderModelOnly, UNETLoader, ModelSamplingFlux, DifferentialDiffusion, CLIPVisionEncode, FluxGuidance, ConditioningZeroOut, StyleModelLoader, StyleModelApply, InpaintModelConditioning, KSampler, VAEDecode, PreviewImage, easy cleanGpuUsed, easy imageInsetCrop, Florence2ModelLoader, Florence2Run, CLIPTextEncode, CheckpointLoaderSimple, DetailerForEach, FluxGuidance, ConditioningZeroOut, GetImage_(Width&Height) _O, ImageScale, PreviewImage, ImageScale, PreviewImage, PreviewImage, CR Simple Image Compare, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "STOIQONewrealityFLUXSD_F1DPreAlpha.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 279988365337062, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/100% facial consistency change face, photo_1863459986448822274.json

> 来源文件 `comfyui_library/workflows/平台全量/100% facial consistency change face, photo_1863459986448822274.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `LoadImage`
- `ImageScale`
- `GetImage_(Width&Height) _O`
- `LoadImage`
- `FaceBoundingBox`
- `FaceAnalysisModels`
- `PreviewImage`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `PreviewImage`
- `ImageScale`
- `UpscaleModelLoader`
- `LayerColor: ColorAdapter`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `ImageCompositeMasked`
- `PreviewImage`
- `PreviewImage`
- `ImageConcanate`
- `PreviewImage`
- `MaskFromColor+`
- `LayerMask: PersonMaskUltra V2`
- `ImageConcanate`
- `ImpactSimpleDetectorSEGS`
- `UltralyticsDetectorProvider`
- `SegsToCombinedMask`
- `SEGSPreview`
- `MaskPreview+`
- `PreviewImage`
- `MaskPreview+`
- `INPAINT_ExpandMask`
- `ImpactGaussianBlurMask`
- `MaskToImage`
- `InvertMask`
- `SubtractMask`
- `MaskPreview+`
- `MaskPreview+`
- `GrowMask`
- `MaskToSEGS`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingFlux`
- `DifferentialDiffusion`
- `CLIPVisionEncode`
- `FluxGuidance`
- `ConditioningZeroOut`
- `StyleModelLoader`
- `StyleModelApply`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `easy cleanGpuUsed`
- `easy imageInsetCrop`
- `Florence2ModelLoader`
- `Florence2Run`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `DetailerForEach`
- `FluxGuidance`
- `ConditioningZeroOut`
- `GetImage_(Width&Height) _O`
- `ImageScale`
- `PreviewImage`
- `ImageScale`
- `PreviewImage`
- `PreviewImage`
- `CR Simple Image Compare`
- `SaveImage`

## 关键参数

- `seed` = `279988365337062`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `STOIQONewrealityFLUXSD_F1DPreAlpha.safetensors`

## 知识

覆盖率 **86%**（64/74）

**有卡**：`LoadImage`、`ImageScale`、`GetImage_(Width&Height) _O`、`FaceBoundingBox`、`FaceAnalysisModels`、`UpscaleModelLoader`、`LayerColor: ColorAdapter`、`ImageUpscaleWithModel`、`ImageScaleBy`、`ImageCompositeMasked`、`ImageConcanate`、`MaskFromColor+`、`LayerMask: PersonMaskUltra V2`、`ImpactSimpleDetectorSEGS`、`UltralyticsDetectorProvider`、`SegsToCombinedMask`、`SEGSPreview`、`MaskPreview+`、`INPAINT_ExpandMask`、`ImpactGaussianBlurMask`、`MaskToImage`、`InvertMask`、`SubtractMask`、`GrowMask`、`MaskToSEGS`、`DualCLIPLoader`、`CLIPTextEncode`、`VAELoader`、`CLIPVisionLoader`、`GetImageSizeAndCount`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingFlux`、`DifferentialDiffusion`、`CLIPVisionEncode`、`FluxGuidance`、`ConditioningZeroOut`、`StyleModelLoader`、`StyleModelApply`、`InpaintModelConditioning`、`KSampler`、`VAEDecode`、`easy cleanGpuUsed`、`easy imageInsetCrop`、`Florence2ModelLoader`、`Florence2Run`、`CheckpointLoaderSimple`、`DetailerForEach`、`CR Simple Image Compare`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
