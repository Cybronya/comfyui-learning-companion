---
key: 平台全量/Cute Anime Character Converter_1864926084088164353.json
name: Cute Anime Character Converter_1864926084088164353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Cute Anime Character Converter_1864926084088164353.json
hash: b3dcf194247e0290
coverage: 0.8
learned_at: 2026-11-14 00:23:02
nodes: [ImageResize+, LayerMask: SegmentAnythingUltra V2, easy imageSize, Seed (rgthree), CLIPTextEncodeFlux, UNETLoader, DualCLIPLoader, ControlNetLoader, ControlNetInpaintingAliMamaApply, VAELoader, LoraLoaderModelOnly, easy imageSize, VAEEncode, KSamplerSelect, CFGGuider, easy imageSize, SetLatentNoiseMask, BasicScheduler, CLIPTextEncode, FluxGuidance, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, PreviewImage, VAEDecode, Reroute, Reroute, Reroute, PreviewImage, PreviewMask_, ImageScaleToTotalPixels, LoadImage, ImageCrop+, PreviewImage, PreviewImage, CR Simple Image Compare, SaveImage, PreviewImage, easy prompt, TTP_Expand_And_Mask]
patterns: []
missing: []
---

# 平台全量/Cute Anime Character Converter_1864926084088164353.json

> 来源文件 `comfyui_library/workflows/平台全量/Cute Anime Character Converter_1864926084088164353.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `ImageResize+`
- `LayerMask: SegmentAnythingUltra V2`
- `easy imageSize`
- `Seed (rgthree)`
- `CLIPTextEncodeFlux` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `ControlNetLoader`
- `ControlNetInpaintingAliMamaApply`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `easy imageSize`
- `VAEEncode` ★核心
- `KSamplerSelect` ★核心
- `CFGGuider`
- `easy imageSize`
- `SetLatentNoiseMask`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `PreviewMask_`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageCrop+`
- `PreviewImage`
- `PreviewImage`
- `CR Simple Image Compare`
- `SaveImage`
- `PreviewImage`
- `easy prompt`
- `TTP_Expand_And_Mask`

## 知识

覆盖率 **80%**（32/40）

**有卡**：`ImageResize+`、`LayerMask: SegmentAnythingUltra V2`、`easy imageSize`、`Seed (rgthree)`、`CLIPTextEncodeFlux`、`UNETLoader`、`DualCLIPLoader`、`ControlNetLoader`、`ControlNetInpaintingAliMamaApply`、`VAELoader`、`LoraLoaderModelOnly`、`VAEEncode`、`KSamplerSelect`、`CFGGuider`、`SetLatentNoiseMask`、`BasicScheduler`、`CLIPTextEncode`、`FluxGuidance`、`ModelSamplingFlux`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecode`、`PreviewMask_`、`ImageScaleToTotalPixels`、`LoadImage`、`ImageCrop+`、`CR Simple Image Compare`、`SaveImage`、`easy prompt`、`TTP_Expand_And_Mask`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、ControlNetInpaintingAliMamaApply、ControlNetLoader
