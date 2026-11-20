---
key: 平台全量/Flux Virtual Try-on (in-context lora)_1861694610878681090.json
name: Flux Virtual Try-on (in-context lora)_1861694610878681090
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux Virtual Try-on (in-context lora)_1861694610878681090.json
hash: d1cf32135b0400f9
coverage: 0.818182
learned_at: 2026-11-14 00:28:05
nodes: [PreviewImage, GetImageSize+, ImageResizeKJ, LayerUtility: ColorImage V2, SimpleMath+, PreviewImage, ConditioningZeroOut, CLIPTextEncode, CFGGuider, KSamplerSelect, SetLatentNoiseMask, VAEEncode, ControlNetInpaintingAliMamaApply, ModelSamplingFlux, easy cleanGpuUsed, RandomNoise, SamplerCustomAdvanced, SDXLAspectRatioSelector, LayerUtility: ExtendCanvasV2, MaskPreview+, FluxGuidance, Florence2Run, ShowText|pysssss, Note, Replace Text _O, BasicScheduler, PrimitiveNode, Note, Note, VAEDecode, LoadImage, easy float, Florence2toCoordinates, DownloadAndLoadSAM2Model, PreviewImage, LayerUtility: ImageBlend, Florence2Run, DownloadAndLoadFlorence2Model, Sam2Segmentation, Mask Invert, PreviewImage, PrepareImageAndMaskForInpaint, ImageResizeKJ, LoraLoader, ControlNetLoader, CheckpointLoaderSimple, LoraLoaderModelOnly, SaveImage, CR Simple Image Compare, SaveImage, PreviewImage, ImageCrop+, ImageCrop+, AddMaskForICLora, easy imageSize]
patterns: [lora]
missing: []
parameters: {"checkpoint": "flux1-dev-fp8-Comfy-Org.safetensors", "lora_name": "FLUX.1-Turbo-Alpha.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 平台全量/Flux Virtual Try-on (in-context lora)_1861694610878681090.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux Virtual Try-on (in-context lora)_1861694610878681090.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `PreviewImage`
- `GetImageSize+`
- `ImageResizeKJ`
- `LayerUtility: ColorImage V2`
- `SimpleMath+`
- `PreviewImage`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SetLatentNoiseMask`
- `VAEEncode` ★核心
- `ControlNetInpaintingAliMamaApply`
- `ModelSamplingFlux`
- `easy cleanGpuUsed`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `SDXLAspectRatioSelector`
- `LayerUtility: ExtendCanvasV2`
- `MaskPreview+`
- `FluxGuidance`
- `Florence2Run`
- `ShowText|pysssss`
- `Note`
- `Replace Text _O`
- `BasicScheduler`
- `PrimitiveNode`
- `Note`
- `Note`
- `VAEDecode` ★核心
- `LoadImage`
- `easy float`
- `Florence2toCoordinates`
- `DownloadAndLoadSAM2Model`
- `PreviewImage`
- `LayerUtility: ImageBlend`
- `Florence2Run`
- `DownloadAndLoadFlorence2Model`
- `Sam2Segmentation`
- `Mask Invert`
- `PreviewImage`
- `PrepareImageAndMaskForInpaint`
- `ImageResizeKJ`
- `LoraLoader` ★核心
- `ControlNetLoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `CR Simple Image Compare`
- `SaveImage`
- `PreviewImage`
- `ImageCrop+`
- `ImageCrop+`
- `AddMaskForICLora`
- `easy imageSize`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `FLUX.1-Turbo-Alpha.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `checkpoint` = `flux1-dev-fp8-Comfy-Org.safetensors`

## 知识

覆盖率 **82%**（45/55）

**有卡**：`GetImageSize+`、`ImageResizeKJ`、`LayerUtility: ColorImage V2`、`SimpleMath+`、`ConditioningZeroOut`、`CLIPTextEncode`、`CFGGuider`、`KSamplerSelect`、`SetLatentNoiseMask`、`VAEEncode`、`ControlNetInpaintingAliMamaApply`、`ModelSamplingFlux`、`easy cleanGpuUsed`、`RandomNoise`、`SamplerCustomAdvanced`、`SDXLAspectRatioSelector`、`LayerUtility: ExtendCanvasV2`、`MaskPreview+`、`FluxGuidance`、`Florence2Run`、`Replace Text _O`、`BasicScheduler`、`VAEDecode`、`LoadImage`、`easy float`、`Florence2toCoordinates`、`DownloadAndLoadSAM2Model`、`LayerUtility: ImageBlend`、`DownloadAndLoadFlorence2Model`、`Sam2Segmentation`、`Mask Invert`、`PrepareImageAndMaskForInpaint`、`LoraLoader`、`ControlNetLoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`SaveImage`、`CR Simple Image Compare`、`ImageCrop+`、`AddMaskForICLora`、`easy imageSize`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetInpaintingAliMamaApply、ControlNetLoader
