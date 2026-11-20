---
key: 平台全量/photo2illustration (flux in-context lora)_1891306129174175745.json
name: photo2illustration (flux in-context lora)_1891306129174175745
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/photo2illustration (flux in-context lora)_1891306129174175745.json
hash: 2d161205797c50c4
coverage: 0.84375
learned_at: 2026-11-14 01:15:40
nodes: [DownloadAndLoadFlorence2Model, RandomNoise, BasicScheduler, KSamplerSelect, SetLatentNoiseMask, SamplerCustomAdvanced, PrimitiveNode, ModelSamplingFlux, FluxGuidance, VAEEncode, easy cleanGpuUsed, VAEDecode, Florence2Run, Replace Text _O, CR Text, ShowText|pysssss, PreviewImage, PreviewImage, MaskToImage, BasicGuider, Note, ImageResizeKJ, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageCrop+, CR Simple Image Compare, AddMaskForICLora, SaveImage, CLIPTextEncode, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"checkpoint": "flux1-dev-fp8-Comfy-Org.safetensors"}
---

# 平台全量/photo2illustration (flux in-context lora)_1891306129174175745.json

> 来源文件 `comfyui_library/workflows/平台全量/photo2illustration (flux in-context lora)_1891306129174175745.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `DownloadAndLoadFlorence2Model`
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
- `Florence2Run`
- `Replace Text _O`
- `CR Text`
- `ShowText|pysssss`
- `PreviewImage`
- `PreviewImage`
- `MaskToImage`
- `BasicGuider`
- `Note`
- `ImageResizeKJ`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageCrop+`
- `CR Simple Image Compare`
- `AddMaskForICLora`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `SaveImage`

## 关键参数

- `checkpoint` = `flux1-dev-fp8-Comfy-Org.safetensors`

## 知识

覆盖率 **84%**（27/32）

**有卡**：`DownloadAndLoadFlorence2Model`、`RandomNoise`、`BasicScheduler`、`KSamplerSelect`、`SetLatentNoiseMask`、`SamplerCustomAdvanced`、`ModelSamplingFlux`、`FluxGuidance`、`VAEEncode`、`easy cleanGpuUsed`、`VAEDecode`、`Florence2Run`、`Replace Text _O`、`CR Text`、`MaskToImage`、`BasicGuider`、`ImageResizeKJ`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`ImageCrop+`、`CR Simple Image Compare`、`AddMaskForICLora`、`SaveImage`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
