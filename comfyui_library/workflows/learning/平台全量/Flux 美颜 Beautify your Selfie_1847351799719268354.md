---
key: 平台全量/Flux 美颜 Beautify your Selfie_1847351799719268354.json
name: Flux 美颜 Beautify your Selfie_1847351799719268354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux 美颜 Beautify your Selfie_1847351799719268354.json
hash: eb44d743e788ec50
coverage: 0.71875
learned_at: 2026-11-14 00:28:22
nodes: [KSamplerSelect, BasicGuider, RandomNoise, Reroute, Reroute, Reroute, Reroute, Reroute, SetLatentNoiseMask, VAEDecode, VAEDecode, Reroute, BNK_Unsampler, SetLatentNoiseMask, BasicScheduler, LatentInterpolate, LatentInterpolate, BasicScheduler, CLIPTextEncode, PulidFluxInsightFaceLoader, PulidFluxEvaClipLoader, PulidFluxModelLoader, VAEEncode, easy imageSize, VAELoader, VAEDecode, SamplerCustomAdvanced, CLIPTextEncodeFlux, SamplerCustomAdvanced, SamplerCustomAdvanced, PreviewImage, Reroute, VAEEncode, VAEDecode, Reroute, GrowMask, ModelSamplingFlux, Reroute, ApplyPulidFlux, FluxGuidance, BasicScheduler, PreviewImage, Note, Note, UNETLoader, LoraLoaderModelOnly, DualCLIPLoader, PreviewImage, AutoCropFaces, RH_Captioner, Note, VAEDecode, PreviewImage, LayerUtility: PurgeVRAM, JWImageResizeByFactor, LayerUtility: PurgeVRAM, LayerMask: SegmentAnythingUltra V2, MaskPreview+, Image Comparer (rgthree), SaveImage, VAEDecode, ImageScaleToTotalPixels, PreviewImage, LoadImage]
patterns: []
missing: []
---

# 平台全量/Flux 美颜 Beautify your Selfie_1847351799719268354.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux 美颜 Beautify your Selfie_1847351799719268354.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetLatentNoiseMask`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `BNK_Unsampler` ★核心
- `SetLatentNoiseMask`
- `BasicScheduler`
- `LatentInterpolate`
- `LatentInterpolate`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `PulidFluxInsightFaceLoader`
- `PulidFluxEvaClipLoader`
- `PulidFluxModelLoader`
- `VAEEncode` ★核心
- `easy imageSize`
- `VAELoader`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncodeFlux` ★核心
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `Reroute`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `GrowMask`
- `ModelSamplingFlux`
- `Reroute`
- `ApplyPulidFlux`
- `FluxGuidance`
- `BasicScheduler`
- `PreviewImage`
- `Note`
- `Note`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `PreviewImage`
- `AutoCropFaces`
- `RH_Captioner`
- `Note`
- `VAEDecode` ★核心
- `PreviewImage`
- `LayerUtility: PurgeVRAM`
- `JWImageResizeByFactor`
- `LayerUtility: PurgeVRAM`
- `LayerMask: SegmentAnythingUltra V2`
- `MaskPreview+`
- `Image Comparer (rgthree)`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `LoadImage`

## 知识

覆盖率 **72%**（46/64）

**有卡**：`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`SetLatentNoiseMask`、`VAEDecode`、`BNK_Unsampler`、`BasicScheduler`、`LatentInterpolate`、`CLIPTextEncode`、`PulidFluxInsightFaceLoader`、`PulidFluxEvaClipLoader`、`PulidFluxModelLoader`、`VAEEncode`、`easy imageSize`、`VAELoader`、`SamplerCustomAdvanced`、`CLIPTextEncodeFlux`、`GrowMask`、`ModelSamplingFlux`、`ApplyPulidFlux`、`FluxGuidance`、`UNETLoader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`AutoCropFaces`、`RH_Captioner`、`LayerUtility: PurgeVRAM`、`JWImageResizeByFactor`、`LayerMask: SegmentAnythingUltra V2`、`MaskPreview+`、`SaveImage`、`ImageScaleToTotalPixels`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、BNK_Unsampler、FluxGuidance
