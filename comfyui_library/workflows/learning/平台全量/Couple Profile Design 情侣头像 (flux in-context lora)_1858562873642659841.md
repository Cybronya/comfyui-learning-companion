---
key: 平台全量/Couple Profile Design 情侣头像 (flux in-context lora)_1858562873642659841.json
name: Couple Profile Design 情侣头像 (flux in-context lora)_1858562873642659841
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Couple Profile Design 情侣头像 (flux in-context lora)_1858562873642659841.json
hash: 67f8e6448fe8c787
coverage: 0.909091
learned_at: 2026-11-14 00:22:59
nodes: [CLIPTextEncode, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, BasicGuider, RandomNoise, FluxGuidance, ModelSamplingFlux, easy cleanGpuUsed, PrimitiveNode, EmptyLatentImage, ImageCrop+, VAEDecode, ImageCrop+, SaveImage, SaveImage, SaveImage, CR Text, Note, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "flux1-dev-fp8-Comfy-Org.safetensors", "height": 1024, "width": 2048}
---

# 平台全量/Couple Profile Design 情侣头像 (flux in-context lora)_1858562873642659841.json

> 来源文件 `comfyui_library/workflows/平台全量/Couple Profile Design 情侣头像 (flux in-context lora)_1858562873642659841.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `RandomNoise`
- `FluxGuidance`
- `ModelSamplingFlux`
- `easy cleanGpuUsed`
- `PrimitiveNode`
- `EmptyLatentImage` ★核心
- `ImageCrop+`
- `VAEDecode` ★核心
- `ImageCrop+`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `CR Text`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `2048`
- `height` = `1024`
- `batch_size` = `1`
- `checkpoint` = `flux1-dev-fp8-Comfy-Org.safetensors`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`CLIPTextEncode`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`RandomNoise`、`FluxGuidance`、`ModelSamplingFlux`、`easy cleanGpuUsed`、`EmptyLatentImage`、`ImageCrop+`、`VAEDecode`、`SaveImage`、`CR Text`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
