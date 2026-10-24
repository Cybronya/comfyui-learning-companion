---
key: 图片生成/图生图/FLUX+Fill+redux+control生图+换脸保持人物和场景一致性_1922083596960727042.json
name: FLUX+Fill+redux+control生图+换脸保持人物和场景一致性_1922083596960727042
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX+Fill+redux+control生图+换脸保持人物和场景一致性_1922083596960727042.json
hash: 1cea851750df2f06
coverage: 0.83908
learned_at: 2026-10-23 10:53:40
nodes: [SetUnionControlNetType, StyleModelLoader, CLIPVisionEncode, PreviewImage, CLIPTextEncode, VAEDecode, ImageResize+, MaskPreview+, InpaintModelConditioning, VAEDecode, DualCLIPLoader, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, InstantIDFaceAnalysis, ControlNetLoader, CLIPVisionLoader, PreviewImage, PreviewImage, AIO_Preprocessor, ControlNetApplySD3, VAEDecode, CLIPTextEncode, CLIPTextEncode, KSampler, PreviewImage, PreviewImage, PreviewImage, SaveImage, InstantIDModelLoader, LayerMask: LoadFlorence2Model, LayerUtility: Florence2Image2Prompt, ImageScaleToMegapixels, easy imageCropFromMask, CheckpointLoaderSimple, ControlNetLoader, VAEEncode, KSampler, InpaintResize, ApplyInstantID, LayerMask: SegmentAnythingUltra V2, GrowMaskWithBlur, FaceSegmentation, LoadImage, AutoCropFaces, PreviewImage, FaceAnalysisModels, LoadImage, FaceSegmentation, PreviewImage, ImageResizeKJv2, PreviewImage, Hina.PoseEditor3D, PreviewImage, Image To Mask, PreviewImage, CLIPTextEncode, ConditioningZeroOut, VAELoader, PreviewImage, ImageConcanate, ImageInvert, ImageConcanate, ControlNetLoader, StyleModelApply, KSampler, FluxGuidance, LoadImage, InpaintModelConditioning, ControlNetApplySD3, ImageConcanate, EmptyImage, Load RetinaFace, Crop Face, DifferentialDiffusion, Get Image Size, PlaySound|pysssss, easy cleanGpuUsed, PreviewImage, InpaintStitch, InpaintCrop, FaceAnalysisModels, MaskPreview+, LoadImage, ImageResizeKJv2, AIO_Preprocessor, PreviewImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "juggernautXL_juggXILightningByRD.safetensors", "controlnet_strength": 0.9500000000000002, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 666, "steps": 28}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FLUX+Fill+redux+control生图+换脸保持人物和场景一致性_1922083596960727042.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX+Fill+redux+control生图+换脸保持人物和场景一致性_1922083596960727042.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（87 个）：
- `SetUnionControlNetType`
- `StyleModelLoader`
- `CLIPVisionEncode`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ImageResize+`
- `MaskPreview+`
- `InpaintModelConditioning`
- `VAEDecode` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `InstantIDFaceAnalysis`
- `ControlNetLoader`
- `CLIPVisionLoader`
- `PreviewImage`
- `PreviewImage`
- `AIO_Preprocessor`
- `ControlNetApplySD3` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `InstantIDModelLoader`
- `LayerMask: LoadFlorence2Model`
- `LayerUtility: Florence2Image2Prompt`
- `ImageScaleToMegapixels`
- `easy imageCropFromMask`
- `CheckpointLoaderSimple` ★核心
- `ControlNetLoader`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `InpaintResize`
- `ApplyInstantID`
- `LayerMask: SegmentAnythingUltra V2`
- `GrowMaskWithBlur`
- `FaceSegmentation`
- `LoadImage`
- `AutoCropFaces`
- `PreviewImage`
- `FaceAnalysisModels`
- `LoadImage`
- `FaceSegmentation`
- `PreviewImage`
- `ImageResizeKJv2`
- `PreviewImage`
- `Hina.PoseEditor3D`
- `PreviewImage`
- `Image To Mask`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `PreviewImage`
- `ImageConcanate`
- `ImageInvert`
- `ImageConcanate`
- `ControlNetLoader`
- `StyleModelApply`
- `KSampler` ★核心
- `FluxGuidance`
- `LoadImage`
- `InpaintModelConditioning`
- `ControlNetApplySD3` ★核心
- `ImageConcanate`
- `EmptyImage`
- `Load RetinaFace`
- `Crop Face`
- `DifferentialDiffusion`
- `Get Image Size`
- `PlaySound|pysssss`
- `easy cleanGpuUsed`
- `PreviewImage`
- `InpaintStitch`
- `InpaintCrop`
- `FaceAnalysisModels`
- `MaskPreview+`
- `LoadImage`
- `ImageResizeKJv2`
- `AIO_Preprocessor`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `0.9500000000000002`
- `seed` = `666`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `juggernautXL_juggXILightningByRD.safetensors`

## 知识

覆盖率 **84%**（73/87）

**有卡**：`SetUnionControlNetType`、`StyleModelLoader`、`CLIPVisionEncode`、`CLIPTextEncode`、`VAEDecode`、`ImageResize+`、`MaskPreview+`、`InpaintModelConditioning`、`DualCLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`InstantIDFaceAnalysis`、`ControlNetLoader`、`CLIPVisionLoader`、`AIO_Preprocessor`、`ControlNetApplySD3`、`KSampler`、`SaveImage`、`InstantIDModelLoader`、`LayerMask: LoadFlorence2Model`、`LayerUtility: Florence2Image2Prompt`、`ImageScaleToMegapixels`、`easy imageCropFromMask`、`CheckpointLoaderSimple`、`VAEEncode`、`InpaintResize`、`ApplyInstantID`、`LayerMask: SegmentAnythingUltra V2`、`GrowMaskWithBlur`、`FaceSegmentation`、`LoadImage`、`AutoCropFaces`、`FaceAnalysisModels`、`ImageResizeKJv2`、`Hina.PoseEditor3D`、`Image To Mask`、`ConditioningZeroOut`、`VAELoader`、`ImageConcanate`、`ImageInvert`、`StyleModelApply`、`FluxGuidance`、`EmptyImage`、`Load RetinaFace`、`Crop Face`、`DifferentialDiffusion`、`Get Image Size`、`PlaySound|pysssss`、`easy cleanGpuUsed`、`InpaintStitch`、`InpaintCrop`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
