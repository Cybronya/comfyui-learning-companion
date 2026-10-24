---
key: 图片生成/图生图/Flex.1 alpha Redux 基础工作流_1908349003488964610.json
name: Flex.1 alpha Redux 基础工作流_1908349003488964610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flex.1 alpha Redux 基础工作流_1908349003488964610.json
hash: 81fc260926b33fc9
coverage: 0.894737
learned_at: 2026-10-23 10:56:01
nodes: [StyleModelApply, SamplerCustomAdvanced, PrimitiveNode, EmptySD3LatentImage, RandomNoise, ModelSamplingFlux, BasicGuider, KSamplerSelect, CLIPTextEncode, BasicScheduler, FluxGuidance, PrimitiveNode, LoadImage, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, StyleModelLoader, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"checkpoint": "Flex.1-alpha.safetensors"}
---

# 图片生成/图生图/Flex.1 alpha Redux 基础工作流_1908349003488964610.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flex.1 alpha Redux 基础工作流_1908349003488964610.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `StyleModelApply`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveNode`
- `EmptySD3LatentImage`
- `RandomNoise`
- `ModelSamplingFlux`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `FluxGuidance`
- `PrimitiveNode`
- `LoadImage`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple` ★核心
- `StyleModelLoader`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `checkpoint` = `Flex.1-alpha.safetensors`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`StyleModelApply`、`SamplerCustomAdvanced`、`EmptySD3LatentImage`、`RandomNoise`、`ModelSamplingFlux`、`BasicGuider`、`KSamplerSelect`、`CLIPTextEncode`、`BasicScheduler`、`FluxGuidance`、`LoadImage`、`CLIPVisionEncode`、`CLIPVisionLoader`、`CheckpointLoaderSimple`、`StyleModelLoader`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、CLIPVisionEncode
