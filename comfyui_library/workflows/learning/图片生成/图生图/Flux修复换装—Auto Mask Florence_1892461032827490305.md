---
key: 图片生成/图生图/Flux修复换装—Auto Mask Florence_1892461032827490305.json
name: Flux修复换装—Auto Mask Florence_1892461032827490305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux修复换装—Auto Mask Florence_1892461032827490305.json
hash: 21d53496a6ca725f
coverage: 0.794872
learned_at: 2026-10-23 11:01:56
nodes: [Reroute, Reroute, EmptySD3LatentImage, CLIPTextEncodeFlux, CLIPTextEncodeFlux, SamplerCustomAdvanced, Reroute, KSamplerSelect, VAEDecode, BasicScheduler, CFGGuider, ShowText|pysssss, Text Concatenate (JPS), MaskToImage, DownloadAndLoadSAM2Model, PreviewImage, Florence2Run, DownloadAndLoadFlorence2Model, ControlNetInpaintingAliMamaApply, ImageCompositeMasked, Image Comparer (rgthree), RandomNoise, SaveImage, ImageCompositeMasked, GrowMaskWithBlur, JjkText, StringFunction|pysssss, Florence2toCoordinates, ImageAndMaskPreview, Sam2Segmentation, easy imageSwitch, Switch mask [Crystools], ControlNetLoader, UNETLoader, DualCLIPLoader, VAELoader, LoadImage, LoadImage, PreviewImage]
patterns: []
missing: []
---

# 图片生成/图生图/Flux修复换装—Auto Mask Florence_1892461032827490305.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux修复换装—Auto Mask Florence_1892461032827490305.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `Reroute`
- `Reroute`
- `EmptySD3LatentImage`
- `CLIPTextEncodeFlux` ★核心
- `CLIPTextEncodeFlux` ★核心
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `BasicScheduler`
- `CFGGuider`
- `ShowText|pysssss`
- `Text Concatenate (JPS)`
- `MaskToImage`
- `DownloadAndLoadSAM2Model`
- `PreviewImage`
- `Florence2Run`
- `DownloadAndLoadFlorence2Model`
- `ControlNetInpaintingAliMamaApply`
- `ImageCompositeMasked`
- `Image Comparer (rgthree)`
- `RandomNoise`
- `SaveImage`
- `ImageCompositeMasked`
- `GrowMaskWithBlur`
- `JjkText`
- `StringFunction|pysssss`
- `Florence2toCoordinates`
- `ImageAndMaskPreview`
- `Sam2Segmentation`
- `easy imageSwitch`
- `Switch mask [Crystools]`
- `ControlNetLoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `PreviewImage`

## 知识

覆盖率 **79%**（31/39）

**有卡**：`EmptySD3LatentImage`、`CLIPTextEncodeFlux`、`SamplerCustomAdvanced`、`KSamplerSelect`、`VAEDecode`、`BasicScheduler`、`CFGGuider`、`Text Concatenate (JPS)`、`MaskToImage`、`DownloadAndLoadSAM2Model`、`Florence2Run`、`DownloadAndLoadFlorence2Model`、`ControlNetInpaintingAliMamaApply`、`ImageCompositeMasked`、`RandomNoise`、`SaveImage`、`GrowMaskWithBlur`、`StringFunction|pysssss`、`Florence2toCoordinates`、`ImageAndMaskPreview`、`Sam2Segmentation`、`easy imageSwitch`、`Switch mask [Crystools]`、`ControlNetLoader`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、LoadImage、ControlNetInpaintingAliMamaApply、ControlNetLoader、CFGGuider、KSamplerSelect
