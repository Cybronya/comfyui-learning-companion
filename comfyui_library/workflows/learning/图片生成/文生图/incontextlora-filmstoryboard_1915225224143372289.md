---
key: 图片生成/文生图/incontextlora-filmstoryboard_1915225224143372289.json
name: incontextlora-filmstoryboard_1915225224143372289.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/incontextlora-filmstoryboard_1915225224143372289.json
hash: 9fa57dc686ab016b
coverage: 0.789474
learned_at: 2026-10-07 22:07:31
nodes: [VAEDecode, Note, Note, BasicGuider, KSamplerSelect, VAELoader, BasicScheduler, SamplerCustomAdvanced, FluxGuidance, EmptySD3LatentImage, PrimitiveNode, PrimitiveNode, RandomNoise, ModelSamplingFlux, SaveImage, CLIPTextEncode, UNETLoader, LoraLoader, DualCLIPLoader]
patterns: [lora]
missing: []
parameters: {"lora_name": "film-storyboard.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 图片生成/文生图/incontextlora-filmstoryboard_1915225224143372289.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1915225224143372289.json`

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
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `DualCLIPLoader`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `film-storyboard.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`VAEDecode`、`BasicGuider`、`KSamplerSelect`、`VAELoader`、`BasicScheduler`、`SamplerCustomAdvanced`、`FluxGuidance`、`EmptySD3LatentImage`、`RandomNoise`、`ModelSamplingFlux`、`SaveImage`、`CLIPTextEncode`、`UNETLoader`、`LoraLoader`、`DualCLIPLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、LoraLoader
