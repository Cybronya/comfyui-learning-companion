---
key: 平台全量/【首发最强】FLUX_fill+ACE + Redux 换脸1.0_1931952044364464129.json
name: 【首发最强】FLUX_fill+ACE + Redux 换脸1.0_1931952044364464129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【首发最强】FLUX_fill+ACE + Redux 换脸1.0_1931952044364464129.json
hash: bd3ebb550de89ad4
coverage: 0.839286
learned_at: 2026-11-14 01:26:38
nodes: [ConditioningZeroOut, LayerMask: PersonMaskUltra V2, GrowMaskWithBlur, MaskPreview+, FaceAnalysisModels, FaceBoundingBox, LayerMask: PersonMaskUltra V2, PreviewImage, GrowMaskWithBlur, MaskPreview+, ReduxAdvanced, VAEDecode, InpaintModelConditioning, PreviewImage, LayerUtility: CropByMask V2, ImageResize+, EmptyImage, ImageConcanate, ImpactGaussianBlurMask, ImageToMask, ImageAndMaskPreview, PreviewImage, LayerUtility: RestoreCropBox, PreviewImage, LayerMask: PersonMaskUltra V2, MaskToSEGS, MaskPreview+, GrowMaskWithBlur, PreviewImage, RepeatLatentBatch, ResizeMask, ImageConcanate, MaskToImage, PreviewImage, CLIPTextEncode, SaveImage, PreviewImage, ImageResize+, ImageCrop, FluxGuidance, Image Comparer (rgthree), PreviewImage, easy cleanGpuUsed, DetailerForEach, KSampler, FloatConstant, LoadImage, LoadImage, UNETLoader, DualCLIPLoader, UNETLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, StyleModelLoader, CLIPVisionLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.6000000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 69339421205380, "steps": 25}
---

# 平台全量/【首发最强】FLUX_fill+ACE + Redux 换脸1.0_1931952044364464129.json

> 来源文件 `comfyui_library/workflows/平台全量/【首发最强】FLUX_fill+ACE + Redux 换脸1.0_1931952044364464129.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `ConditioningZeroOut`
- `LayerMask: PersonMaskUltra V2`
- `GrowMaskWithBlur`
- `MaskPreview+`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `LayerMask: PersonMaskUltra V2`
- `PreviewImage`
- `GrowMaskWithBlur`
- `MaskPreview+`
- `ReduxAdvanced`
- `VAEDecode` ★核心
- `InpaintModelConditioning`
- `PreviewImage`
- `LayerUtility: CropByMask V2`
- `ImageResize+`
- `EmptyImage`
- `ImageConcanate`
- `ImpactGaussianBlurMask`
- `ImageToMask`
- `ImageAndMaskPreview`
- `PreviewImage`
- `LayerUtility: RestoreCropBox`
- `PreviewImage`
- `LayerMask: PersonMaskUltra V2`
- `MaskToSEGS`
- `MaskPreview+`
- `GrowMaskWithBlur`
- `PreviewImage`
- `RepeatLatentBatch`
- `ResizeMask`
- `ImageConcanate`
- `MaskToImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `PreviewImage`
- `ImageResize+`
- `ImageCrop`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `easy cleanGpuUsed`
- `DetailerForEach`
- `KSampler` ★核心
- `FloatConstant`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `StyleModelLoader`
- `CLIPVisionLoader`

## 关键参数

- `seed` = `69339421205380`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.6000000000000001`

## 知识

覆盖率 **84%**（47/56）

**有卡**：`ConditioningZeroOut`、`LayerMask: PersonMaskUltra V2`、`GrowMaskWithBlur`、`MaskPreview+`、`FaceAnalysisModels`、`FaceBoundingBox`、`ReduxAdvanced`、`VAEDecode`、`InpaintModelConditioning`、`LayerUtility: CropByMask V2`、`ImageResize+`、`EmptyImage`、`ImageConcanate`、`ImpactGaussianBlurMask`、`ImageToMask`、`ImageAndMaskPreview`、`LayerUtility: RestoreCropBox`、`MaskToSEGS`、`RepeatLatentBatch`、`ResizeMask`、`MaskToImage`、`CLIPTextEncode`、`SaveImage`、`ImageCrop`、`FluxGuidance`、`easy cleanGpuUsed`、`DetailerForEach`、`KSampler`、`FloatConstant`、`LoadImage`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`StyleModelLoader`、`CLIPVisionLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
