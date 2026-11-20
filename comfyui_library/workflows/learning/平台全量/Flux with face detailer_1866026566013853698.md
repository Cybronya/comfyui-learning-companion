---
key: 平台全量/Flux with face detailer_1866026566013853698.json
name: Flux with face detailer_1866026566013853698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux with face detailer_1866026566013853698.json
hash: b8a4a40c90f73853
coverage: 0.931034
learned_at: 2026-11-14 00:28:12
nodes: [CLIPTextEncode, BasicScheduler, RandomNoise, EmptyLatentImage, KSamplerSelect, BasicGuider, SamplerCustomAdvanced, ModelSamplingFlux, Int Literal, Int Literal, FluxGuidance, CLIPTextEncode, CLIPTextEncode, CR Apply LoRA Stack, CR LoRA Stack, UNETLoader, DualCLIPLoader, VAELoader, CheckpointLoaderSimple, SAMLoader, UltralyticsDetectorProvider, LoadImage, SaveImage, VAEDecode, FaceDetailer, SaveImage, PreviewImage, PreviewImage, String Literal]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "juggernautXL_v9Rdphoto2Lightning.safetensors", "height": 1216, "width": 832}
---

# 平台全量/Flux with face detailer_1866026566013853698.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux with face detailer_1866026566013853698.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（29 个）：
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `RandomNoise`
- `EmptyLatentImage` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `ModelSamplingFlux`
- `Int Literal`
- `Int Literal`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Apply LoRA Stack`
- `CR LoRA Stack`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `CheckpointLoaderSimple` ★核心
- `SAMLoader`
- `UltralyticsDetectorProvider`
- `LoadImage`
- `SaveImage`
- `VAEDecode` ★核心
- `FaceDetailer`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `String Literal`

## 关键参数

- `width` = `832`
- `height` = `1216`
- `batch_size` = `1`
- `checkpoint` = `juggernautXL_v9Rdphoto2Lightning.safetensors`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`CLIPTextEncode`、`BasicScheduler`、`RandomNoise`、`EmptyLatentImage`、`KSamplerSelect`、`BasicGuider`、`SamplerCustomAdvanced`、`ModelSamplingFlux`、`Int Literal`、`FluxGuidance`、`CR Apply LoRA Stack`、`CR LoRA Stack`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`CheckpointLoaderSimple`、`SAMLoader`、`UltralyticsDetectorProvider`、`LoadImage`、`SaveImage`、`VAEDecode`、`FaceDetailer`、`String Literal`

**用到的条目**：VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、FluxGuidance
