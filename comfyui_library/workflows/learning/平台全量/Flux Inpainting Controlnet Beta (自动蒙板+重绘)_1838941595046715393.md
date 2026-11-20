---
key: 平台全量/Flux Inpainting Controlnet Beta (自动蒙板+重绘)_1838941595046715393.json
name: Flux Inpainting Controlnet Beta (自动蒙板+重绘)_1838941595046715393
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux Inpainting Controlnet Beta (自动蒙板+重绘)_1838941595046715393.json
hash: 4c592745eda3858f
coverage: 0.761905
learned_at: 2026-11-14 00:27:41
nodes: [Reroute, Reroute, EmptySD3LatentImage, CLIPTextEncodeFlux, Reroute, KSamplerSelect, VAEDecode, BasicScheduler, CFGGuider, ShowText|pysssss, DownloadAndLoadSAM2Model, ImageCompositeMasked, RandomNoise, ImageAndMaskPreview, Sam2Segmentation, ControlNetLoader, DualCLIPLoader, VAELoader, UNETLoader, easy imageSwitch, Florence2toCoordinates, Text Concatenate (JPS), PreviewImage, Image Comparer (rgthree), MaskToImage, ControlNetInpaintingAliMamaApply, CLIPTextEncodeFlux, StringFunction|pysssss, SamplerCustomAdvanced, SaveImage, PreviewImage, ImageCompositeMasked, GrowMaskWithBlur, Switch mask [Crystools], PreviewImage, JjkText, DownloadAndLoadFlorence2Model, Florence2Run, LoadImage, LoadImage, RH_Prompter, JjkText]
patterns: []
missing: []
---

# 平台全量/Flux Inpainting Controlnet Beta (自动蒙板+重绘)_1838941595046715393.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux Inpainting Controlnet Beta (自动蒙板+重绘)_1838941595046715393.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `Reroute`
- `Reroute`
- `EmptySD3LatentImage`
- `CLIPTextEncodeFlux` ★核心
- `Reroute`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `BasicScheduler`
- `CFGGuider`
- `ShowText|pysssss`
- `DownloadAndLoadSAM2Model`
- `ImageCompositeMasked`
- `RandomNoise`
- `ImageAndMaskPreview`
- `Sam2Segmentation`
- `ControlNetLoader`
- `DualCLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `easy imageSwitch`
- `Florence2toCoordinates`
- `Text Concatenate (JPS)`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `MaskToImage`
- `ControlNetInpaintingAliMamaApply`
- `CLIPTextEncodeFlux` ★核心
- `StringFunction|pysssss`
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `PreviewImage`
- `ImageCompositeMasked`
- `GrowMaskWithBlur`
- `Switch mask [Crystools]`
- `PreviewImage`
- `JjkText`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `LoadImage`
- `LoadImage`
- `RH_Prompter`
- `JjkText`

## 知识

覆盖率 **76%**（32/42）

**有卡**：`EmptySD3LatentImage`、`CLIPTextEncodeFlux`、`KSamplerSelect`、`VAEDecode`、`BasicScheduler`、`CFGGuider`、`DownloadAndLoadSAM2Model`、`ImageCompositeMasked`、`RandomNoise`、`ImageAndMaskPreview`、`Sam2Segmentation`、`ControlNetLoader`、`DualCLIPLoader`、`VAELoader`、`UNETLoader`、`easy imageSwitch`、`Florence2toCoordinates`、`Text Concatenate (JPS)`、`MaskToImage`、`ControlNetInpaintingAliMamaApply`、`StringFunction|pysssss`、`SamplerCustomAdvanced`、`SaveImage`、`GrowMaskWithBlur`、`Switch mask [Crystools]`、`DownloadAndLoadFlorence2Model`、`Florence2Run`、`LoadImage`、`RH_Prompter`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、LoadImage、ControlNetInpaintingAliMamaApply、ControlNetLoader、CFGGuider、KSamplerSelect
