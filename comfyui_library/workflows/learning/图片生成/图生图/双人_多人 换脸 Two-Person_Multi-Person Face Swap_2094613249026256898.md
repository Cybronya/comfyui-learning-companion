---
key: 图片生成/图生图/双人_多人 换脸 Two-Person_Multi-Person Face Swap_2094613249026256898.json
name: 双人_多人 换脸 Two-Person_Multi-Person Face Swap_2094613249026256898
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/双人_多人 换脸 Two-Person_Multi-Person Face Swap_2094613249026256898.json
hash: 61ee9d3a62695a05
coverage: 0.910714
learned_at: 2026-10-21 00:50:55
nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, CLIPTextEncode, DifferentialDiffusion, UNETLoader, easy imageCount, CLIPTextEncode, ControlNetLoader, CLIPTextEncode, InstantIDFaceAnalysis, ControlNetLoader, ApplyInstantID, ControlNetApplyAdvanced, VAEEncode, KSampler, PreviewImage, LayerMask: MaskStroke, VAELoader, CheckpointLoaderSimple, InstantIDModelLoader, InpaintModelConditioning, KSampler, VAEDecode, VAEDecode, ColorMatch, WarpFacesBack, ColorMatch, easy forLoopEnd, UltralyticsDetectorProvider, LayerUtility: ImageScaleByAspectRatio V2, SAMLoader, ImpactSEGSToMaskBatch, MaskToImage, CropFaces, DetectFaces, MaskListSelect(FaceParsing), LayerMask: MaskPreview, easy forLoopStart, Mask Invert, SEGSPreview, ImpactMakeImageBatch, ImageFromBatch, CropFace, ImpactSimpleDetectorSEGS, SaveImage, Image Comparer (rgthree), LoadImage, Note, Note, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "dreamshaperXL_lightningDPMSDE.safetensors", "controlnet_strength": 0.5000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 324708950411102, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/双人_多人 换脸 Two-Person_Multi-Person Face Swap_2094613249026256898.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/双人_多人 换脸 Two-Person_Multi-Person Face Swap_2094613249026256898.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `DifferentialDiffusion`
- `UNETLoader` ★核心
- `easy imageCount`
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `InstantIDFaceAnalysis`
- `ControlNetLoader`
- `ApplyInstantID`
- `ControlNetApplyAdvanced` ★核心
- `VAEEncode` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `LayerMask: MaskStroke`
- `VAELoader`
- `CheckpointLoaderSimple` ★核心
- `InstantIDModelLoader`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ColorMatch`
- `WarpFacesBack`
- `ColorMatch`
- `easy forLoopEnd`
- `UltralyticsDetectorProvider`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SAMLoader`
- `ImpactSEGSToMaskBatch`
- `MaskToImage`
- `CropFaces`
- `DetectFaces`
- `MaskListSelect(FaceParsing)`
- `LayerMask: MaskPreview`
- `easy forLoopStart`
- `Mask Invert`
- `SEGSPreview`
- `ImpactMakeImageBatch`
- `ImageFromBatch`
- `CropFace`
- `ImpactSimpleDetectorSEGS`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `0.5000000000000001`
- `seed` = `324708950411102`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `dreamshaperXL_lightningDPMSDE.safetensors`

## 知识

覆盖率 **91%**（51/56）

**有卡**：`CLIPTextEncode`、`DualCLIPLoader`、`FluxGuidance`、`DifferentialDiffusion`、`UNETLoader`、`easy imageCount`、`ControlNetLoader`、`InstantIDFaceAnalysis`、`ApplyInstantID`、`ControlNetApplyAdvanced`、`VAEEncode`、`KSampler`、`LayerMask: MaskStroke`、`VAELoader`、`CheckpointLoaderSimple`、`InstantIDModelLoader`、`InpaintModelConditioning`、`VAEDecode`、`ColorMatch`、`WarpFacesBack`、`easy forLoopEnd`、`UltralyticsDetectorProvider`、`LayerUtility: ImageScaleByAspectRatio V2`、`SAMLoader`、`ImpactSEGSToMaskBatch`、`MaskToImage`、`CropFaces`、`DetectFaces`、`MaskListSelect(FaceParsing)`、`LayerMask: MaskPreview`、`easy forLoopStart`、`Mask Invert`、`SEGSPreview`、`ImpactMakeImageBatch`、`ImageFromBatch`、`CropFace`、`ImpactSimpleDetectorSEGS`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
