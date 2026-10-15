---
key: 图片生成/文生图/incontext-controlnet-home_1914936305506287617.json
name: incontext-controlnet-home_1914936305506287617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/incontext-controlnet-home_1914936305506287617.json
hash: f008fde3c92f5653
coverage: 0.789474
learned_at: 2026-10-10 20:59:21
nodes: [VAEDecode, Note, Note, BasicGuider, KSamplerSelect, VAELoader, BasicScheduler, SamplerCustomAdvanced, FluxGuidance, EmptySD3LatentImage, PrimitiveNode, PrimitiveNode, RandomNoise, ModelSamplingFlux, SaveImage, UNETLoader, DualCLIPLoader, CLIPTextEncode, LoraLoader]
patterns: [lora]
missing: []
parameters: {"lora_name": "home-decoration.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 图片生成/文生图/incontext-controlnet-home_1914936305506287617.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/incontext-controlnet-home_1914936305506287617.json`

## 结构

**节点**（19 个）：
- `VAEDecode`
- `Note`
- `Note`
- `BasicGuider`
- `KSamplerSelect`
- `VAELoader`
- `BasicScheduler`
- `SamplerCustomAdvanced`
- `FluxGuidance`
- `EmptySD3LatentImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `RandomNoise`
- `ModelSamplingFlux`
- `SaveImage`
- `UNETLoader`
- `DualCLIPLoader`
- `CLIPTextEncode`
- `LoraLoader`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `home-decoration.safetensors`
- `strength_clip` = `1`
- `strength_model` = `1`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`VAEDecode`、`Note`、`BasicGuider`、`KSamplerSelect`、`VAELoader`、`BasicScheduler`、`SamplerCustomAdvanced`、`FluxGuidance`、`EmptySD3LatentImage`、`PrimitiveNode`、`RandomNoise`、`ModelSamplingFlux`、`SaveImage`
