---
key: 平台全量/Realism ➡ Anime (Flux Redux 8 step)_1897891763078811649.json
name: Realism ➡ Anime (Flux Redux 8 step)_1897891763078811649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Realism ➡ Anime (Flux Redux 8 step)_1897891763078811649.json
hash: a920c545eb25d529
coverage: 0.928571
learned_at: 2026-11-14 00:54:37
nodes: [PrimitiveNode, PrimitiveNode, SaveImage, StyleModelLoader, CLIPVisionLoader, CLIPVisionEncode, StyleModelApply, BasicGuider, FluxGuidance, SamplerCustomAdvanced, RandomNoise, EmptySD3LatentImage, KSamplerSelect, BasicScheduler, ModelSamplingFlux, DualCLIPLoader, LoadImage, ImageScale, ImageConcanate, easy imageSize, CLIPTextEncode, easy imageSize, VAELoader, VAEDecode, UNETLoader, LoraLoader, LoraLoader, SaveImage]
patterns: [lora]
missing: []
parameters: {"lora_name": "Oshi_No_Ko_LoRA_Flux_V1.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 平台全量/Realism ➡ Anime (Flux Redux 8 step)_1897891763078811649.json

> 来源文件 `comfyui_library/workflows/平台全量/Realism ➡ Anime (Flux Redux 8 step)_1897891763078811649.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `PrimitiveNode`
- `PrimitiveNode`
- `SaveImage`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `StyleModelApply`
- `BasicGuider`
- `FluxGuidance`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `EmptySD3LatentImage`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ModelSamplingFlux`
- `DualCLIPLoader`
- `LoadImage`
- `ImageScale`
- `ImageConcanate`
- `easy imageSize`
- `CLIPTextEncode` ★核心
- `easy imageSize`
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `SaveImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `Oshi_No_Ko_LoRA_Flux_V1.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`SaveImage`、`StyleModelLoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`StyleModelApply`、`BasicGuider`、`FluxGuidance`、`SamplerCustomAdvanced`、`RandomNoise`、`EmptySD3LatentImage`、`KSamplerSelect`、`BasicScheduler`、`ModelSamplingFlux`、`DualCLIPLoader`、`LoadImage`、`ImageScale`、`ImageConcanate`、`easy imageSize`、`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`UNETLoader`、`LoraLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
