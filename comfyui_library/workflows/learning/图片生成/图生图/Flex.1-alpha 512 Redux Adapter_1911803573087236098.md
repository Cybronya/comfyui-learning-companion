---
key: 图片生成/图生图/Flex.1-alpha 512 Redux Adapter_1911803573087236098.json
name: Flex.1-alpha 512 Redux Adapter_1911803573087236098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flex.1-alpha 512 Redux Adapter_1911803573087236098.json
hash: 4a26692d1e7c0b98
coverage: 0.894737
learned_at: 2026-10-23 10:56:01
nodes: [StyleModelApply, SamplerCustomAdvanced, PrimitiveNode, EmptySD3LatentImage, RandomNoise, CheckpointLoaderSimple, ModelSamplingFlux, BasicGuider, KSamplerSelect, CLIPTextEncode, StyleModelLoader, BasicScheduler, FluxGuidance, PrimitiveNode, CLIPVisionEncode, AdvancedVisionLoader, LoadImage, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"checkpoint": "Flex.1-alpha.safetensors"}
---

# 图片生成/图生图/Flex.1-alpha 512 Redux Adapter_1911803573087236098.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flex.1-alpha 512 Redux Adapter_1911803573087236098.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `StyleModelApply`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveNode`
- `EmptySD3LatentImage`
- `RandomNoise`
- `CheckpointLoaderSimple` ★核心
- `ModelSamplingFlux`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `StyleModelLoader`
- `BasicScheduler`
- `FluxGuidance`
- `PrimitiveNode`
- `CLIPVisionEncode`
- `AdvancedVisionLoader`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `checkpoint` = `Flex.1-alpha.safetensors`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`StyleModelApply`、`SamplerCustomAdvanced`、`EmptySD3LatentImage`、`RandomNoise`、`CheckpointLoaderSimple`、`ModelSamplingFlux`、`BasicGuider`、`KSamplerSelect`、`CLIPTextEncode`、`StyleModelLoader`、`BasicScheduler`、`FluxGuidance`、`CLIPVisionEncode`、`AdvancedVisionLoader`、`LoadImage`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、CLIPVisionEncode
