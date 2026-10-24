---
key: 图片生成/图生图/FLUX 1.0 扩图工作流+高清放大+面部细化_2047001426395668481.json
name: FLUX 1.0 扩图工作流+高清放大+面部细化_2047001426395668481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX 1.0 扩图工作流+高清放大+面部细化_2047001426395668481.json
hash: 8d386db5c2898a11
coverage: 0.826087
learned_at: 2026-10-23 10:53:14
nodes: [ImpactInt, InpaintModelConditioning, DifferentialDiffusion, FluxGuidance, ConditioningZeroOut, PreviewImage, PreviewImage, MediaPipeFaceMeshDetectorProvider //Inspire, CoreMLDetailerHookProvider, PreviewImage, DualCLIPLoader, VAELoader, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SaveImage, Image Comparer (rgthree), VAEDecode, KSampler, CLIPTextEncode, MaskPreview+, MaskPreview+, SaveImage, Image Comparer (rgthree), PreviewImage, LoadImage, FaceDetailer, SAMLoader, UltralyticsDetectorProvider, UNETLoader, UNETLoader, GrowMaskWithBlur, ImageToMask, Image Padding, ImagePadForOutpaint, GrowMaskWithBlur, MaskPreview+, LayerMask: MaskPreview, ImagePadForOutpaintMasked, Fast Groups Bypasser (rgthree), easy hiresFix, LoadImage, LayerUtility: ExtendCanvas, LayerMask: MaskInvert, LayerMask: MaskPreview]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1080672194077480, "steps": 20}
---

# 图片生成/图生图/FLUX 1.0 扩图工作流+高清放大+面部细化_2047001426395668481.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX 1.0 扩图工作流+高清放大+面部细化_2047001426395668481.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `ImpactInt`
- `InpaintModelConditioning`
- `DifferentialDiffusion`
- `FluxGuidance`
- `ConditioningZeroOut`
- `PreviewImage`
- `PreviewImage`
- `MediaPipeFaceMeshDetectorProvider //Inspire`
- `CoreMLDetailerHookProvider`
- `PreviewImage`
- `DualCLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `MaskPreview+`
- `MaskPreview+`
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `LoadImage`
- `FaceDetailer`
- `SAMLoader`
- `UltralyticsDetectorProvider`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `GrowMaskWithBlur`
- `ImageToMask`
- `Image Padding`
- `ImagePadForOutpaint`
- `GrowMaskWithBlur`
- `MaskPreview+`
- `LayerMask: MaskPreview`
- `ImagePadForOutpaintMasked`
- `Fast Groups Bypasser (rgthree)`
- `easy hiresFix`
- `LoadImage`
- `LayerUtility: ExtendCanvas`
- `LayerMask: MaskInvert`
- `LayerMask: MaskPreview`

## 关键参数

- `seed` = `1080672194077480`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（38/46）

**有卡**：`ImpactInt`、`InpaintModelConditioning`、`DifferentialDiffusion`、`FluxGuidance`、`ConditioningZeroOut`、`MediaPipeFaceMeshDetectorProvider //Inspire`、`CoreMLDetailerHookProvider`、`DualCLIPLoader`、`VAELoader`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`VAEDecode`、`KSampler`、`CLIPTextEncode`、`MaskPreview+`、`FaceDetailer`、`SAMLoader`、`UltralyticsDetectorProvider`、`UNETLoader`、`GrowMaskWithBlur`、`ImageToMask`、`Image Padding`、`ImagePadForOutpaint`、`LayerMask: MaskPreview`、`ImagePadForOutpaintMasked`、`easy hiresFix`、`LayerUtility: ExtendCanvas`、`LayerMask: MaskInvert`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
