---
key: 图片生成/文生图/incontext-controlnet-home_1914936305506287617.json
name: incontext-controlnet-home_1914936305506287617.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/incontext-controlnet-home_1914936305506287617.json
hash: f008fde3c92f5653
coverage: 0.789474
learned_at: 2026-10-07 19:46:24
nodes: [VAEDecode, Note, Note, BasicGuider, KSamplerSelect, VAELoader, BasicScheduler, SamplerCustomAdvanced, FluxGuidance, EmptySD3LatentImage, PrimitiveNode, PrimitiveNode, RandomNoise, ModelSamplingFlux, SaveImage, UNETLoader, DualCLIPLoader, CLIPTextEncode, LoraLoader]
patterns: [lora]
missing: []
parameters: {"lora_name": "home-decoration.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 图片生成/文生图/incontext-controlnet-home_1914936305506287617.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1914936305506287617.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `VAEDecode` ★核心
- `Note`
- `Note`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAELoader`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `FluxGuidance`
- `EmptySD3LatentImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `RandomNoise`
- `ModelSamplingFlux`
- `SaveImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心

**识别到的模式**：lora

## 关键参数

- `lora_name` = `home-decoration.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`VAEDecode`、`BasicGuider`、`KSamplerSelect`、`VAELoader`、`BasicScheduler`、`SamplerCustomAdvanced`、`FluxGuidance`、`EmptySD3LatentImage`、`RandomNoise`、`ModelSamplingFlux`、`SaveImage`、`UNETLoader`、`DualCLIPLoader`、`CLIPTextEncode`、`LoraLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、LoraLoader
