---
key: 图片生成/文生图/incontextlora-filmstoryboard_1915225224143372289.json
name: incontextlora-filmstoryboard_1915225224143372289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/incontextlora-filmstoryboard_1915225224143372289.json
hash: 9fa57dc686ab016b
coverage: 0.789474
learned_at: 2026-10-10 20:59:21
nodes: [VAEDecode, Note, Note, BasicGuider, KSamplerSelect, VAELoader, BasicScheduler, SamplerCustomAdvanced, FluxGuidance, EmptySD3LatentImage, PrimitiveNode, PrimitiveNode, RandomNoise, ModelSamplingFlux, SaveImage, CLIPTextEncode, UNETLoader, LoraLoader, DualCLIPLoader]
patterns: [lora]
missing: []
parameters: {"lora_name": "film-storyboard.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 图片生成/文生图/incontextlora-filmstoryboard_1915225224143372289.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/incontextlora-filmstoryboard_1915225224143372289.json`

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
- `CLIPTextEncode`
- `UNETLoader`
- `LoraLoader`
- `DualCLIPLoader`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `film-storyboard.safetensors`
- `strength_clip` = `1`
- `strength_model` = `1`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`VAEDecode`、`Note`、`BasicGuider`、`KSamplerSelect`、`VAELoader`、`BasicScheduler`、`SamplerCustomAdvanced`、`FluxGuidance`、`EmptySD3LatentImage`、`PrimitiveNode`、`RandomNoise`、`ModelSamplingFlux`、`SaveImage`
