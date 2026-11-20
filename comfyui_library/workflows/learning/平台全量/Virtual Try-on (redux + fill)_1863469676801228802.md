---
key: 平台全量/Virtual Try-on (redux + fill)_1863469676801228802.json
name: Virtual Try-on (redux + fill)_1863469676801228802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Virtual Try-on (redux + fill)_1863469676801228802.json
hash: 517c2931e0ae5ccc
coverage: 0.910448
learned_at: 2026-11-14 01:03:25
nodes: [Florence2toCoordinates, Florence2toCoordinates, Florence2toCoordinates, Sam2Segmentation, Sam2Segmentation, Sam2Segmentation, GrowMask, easy imageSize, ImageCrop+, ImageResizeKJ, Image Paste Face, AutoCropFaces, DualCLIPLoader, DownloadAndLoadSAM2Model, DownloadAndLoadSAM2Model, DownloadAndLoadSAM2Model, DifferentialDiffusion, StyleModelApplyAdvanced, FluxGuidance, CLIPTextEncode, CLIPVisionEncode, ConditioningZeroOut, SubtractMask, GrowMask, LayerMask: MaskPreview, Note, SimpleMath+, SolidMask, easy imageSize, MaskToImage, easy imageSize, PreviewImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, easy imageSize, Florence2Run, Florence2Run, DownloadAndLoadFlorence2Model, Note, Florence2Run, Image Overlay, Note, LayerMask: MaskPreview, LayerMask: MaskPreview, PreviewImage, Image Overlay, SaveImage, SaveImage, LoadImage, LoadImage, LayerColor: Brightness & Contrast, ImageConcanate, LayerMask: MaskPreview, SubtractMask, GrowMask, easy imageSize, KSampler, VAEDecode, PreviewImage, CLIPVisionLoader, StyleModelLoader, VAELoader, MaskToImage, InpaintModelConditioning, easy imageSize, ImageConcanate, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 190972132810638, "steps": 30}
---

# 平台全量/Virtual Try-on (redux + fill)_1863469676801228802.json

> 来源文件 `comfyui_library/workflows/平台全量/Virtual Try-on (redux + fill)_1863469676801228802.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `Florence2toCoordinates`
- `Florence2toCoordinates`
- `Florence2toCoordinates`
- `Sam2Segmentation`
- `Sam2Segmentation`
- `Sam2Segmentation`
- `GrowMask`
- `easy imageSize`
- `ImageCrop+`
- `ImageResizeKJ`
- `Image Paste Face`
- `AutoCropFaces`
- `DualCLIPLoader`
- `DownloadAndLoadSAM2Model`
- `DownloadAndLoadSAM2Model`
- `DownloadAndLoadSAM2Model`
- `DifferentialDiffusion`
- `StyleModelApplyAdvanced`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `ConditioningZeroOut`
- `SubtractMask`
- `GrowMask`
- `LayerMask: MaskPreview`
- `Note`
- `SimpleMath+`
- `SolidMask`
- `easy imageSize`
- `MaskToImage`
- `easy imageSize`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `easy imageSize`
- `Florence2Run`
- `Florence2Run`
- `DownloadAndLoadFlorence2Model`
- `Note`
- `Florence2Run`
- `Image Overlay`
- `Note`
- `LayerMask: MaskPreview`
- `LayerMask: MaskPreview`
- `PreviewImage`
- `Image Overlay`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LayerColor: Brightness & Contrast`
- `ImageConcanate`
- `LayerMask: MaskPreview`
- `SubtractMask`
- `GrowMask`
- `easy imageSize`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `VAELoader`
- `MaskToImage`
- `InpaintModelConditioning`
- `easy imageSize`
- `ImageConcanate`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `190972132810638`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（61/67）

**有卡**：`Florence2toCoordinates`、`Sam2Segmentation`、`GrowMask`、`easy imageSize`、`ImageCrop+`、`ImageResizeKJ`、`Image Paste Face`、`AutoCropFaces`、`DualCLIPLoader`、`DownloadAndLoadSAM2Model`、`DifferentialDiffusion`、`StyleModelApplyAdvanced`、`FluxGuidance`、`CLIPTextEncode`、`CLIPVisionEncode`、`ConditioningZeroOut`、`SubtractMask`、`LayerMask: MaskPreview`、`SimpleMath+`、`SolidMask`、`MaskToImage`、`ImageScaleToTotalPixels`、`Florence2Run`、`DownloadAndLoadFlorence2Model`、`Image Overlay`、`SaveImage`、`LoadImage`、`LayerColor: Brightness & Contrast`、`ImageConcanate`、`KSampler`、`VAEDecode`、`CLIPVisionLoader`、`StyleModelLoader`、`VAELoader`、`InpaintModelConditioning`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
