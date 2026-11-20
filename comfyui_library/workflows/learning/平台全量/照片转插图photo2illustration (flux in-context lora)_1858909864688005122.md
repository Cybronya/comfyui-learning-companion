---
key: 平台全量/照片转插图photo2illustration (flux in-context lora)_1858909864688005122.json
name: 照片转插图photo2illustration (flux in-context lora)_1858909864688005122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/照片转插图photo2illustration (flux in-context lora)_1858909864688005122.json
hash: b27fe9455becd644
coverage: 0.848485
learned_at: 2026-11-14 02:21:31
nodes: [RandomNoise, BasicScheduler, KSamplerSelect, SetLatentNoiseMask, SamplerCustomAdvanced, PrimitiveNode, ModelSamplingFlux, FluxGuidance, VAEEncode, easy cleanGpuUsed, VAEDecode, PreviewImage, PreviewImage, MaskToImage, BasicGuider, Note, CR Simple Image Compare, AddMaskForICLora, ImageResizeKJ, ImageCrop+, CLIPTextEncode, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage, SaveImage, LoadImage, Replace Text _O, RH_Captioner, CR Text, ShowText|pysssss, Florence2Run, DownloadAndLoadFlorence2Model]
patterns: []
missing: []
parameters: {"checkpoint": "flux1-dev-fp8.safetensors"}
---

# 平台全量/照片转插图photo2illustration (flux in-context lora)_1858909864688005122.json

> 来源文件 `comfyui_library/workflows/平台全量/照片转插图photo2illustration (flux in-context lora)_1858909864688005122.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `RandomNoise`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `SetLatentNoiseMask`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveNode`
- `ModelSamplingFlux`
- `FluxGuidance`
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `PreviewImage`
- `PreviewImage`
- `MaskToImage`
- `BasicGuider`
- `Note`
- `CR Simple Image Compare`
- `AddMaskForICLora`
- `ImageResizeKJ`
- `ImageCrop+`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `Replace Text _O`
- `RH_Captioner`
- `CR Text`
- `ShowText|pysssss`
- `Florence2Run`
- `DownloadAndLoadFlorence2Model`

## 关键参数

- `checkpoint` = `flux1-dev-fp8.safetensors`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`RandomNoise`、`BasicScheduler`、`KSamplerSelect`、`SetLatentNoiseMask`、`SamplerCustomAdvanced`、`ModelSamplingFlux`、`FluxGuidance`、`VAEEncode`、`easy cleanGpuUsed`、`VAEDecode`、`MaskToImage`、`BasicGuider`、`CR Simple Image Compare`、`AddMaskForICLora`、`ImageResizeKJ`、`ImageCrop+`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`SaveImage`、`LoadImage`、`Replace Text _O`、`RH_Captioner`、`CR Text`、`Florence2Run`、`DownloadAndLoadFlorence2Model`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
