---
key: 图片生成/文生图/F.1+流浪汉_1945170907587596289.json
name: F.1+流浪汉_1945170907587596289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1+流浪汉_1945170907587596289.json
hash: e604ac5019ac0c42
coverage: 0.933333
learned_at: 2026-10-10 20:58:30
nodes: [RandomNoise, KSamplerSelect, SamplerCustomAdvanced, BasicScheduler, BasicGuider, Note, VAELoader, CLIPTextEncodeFlux, VAEDecode, UNETLoader, DualCLIPLoader, SaveImage, EmptyLatentImage, SeargePromptCombiner, LoraLoader]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 1024, "lora_name": "lliulanghan.safetensors", "strength_clip": 1, "strength_model": 1.0000000000000002, "width": 768}
---

# 图片生成/文生图/F.1+流浪汉_1945170907587596289.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.1+流浪汉_1945170907587596289.json`

## 结构

**节点**（15 个）：
- `RandomNoise`
- `KSamplerSelect`
- `SamplerCustomAdvanced`
- `BasicScheduler`
- `BasicGuider`
- `Note`
- `VAELoader`
- `CLIPTextEncodeFlux`
- `VAEDecode`
- `UNETLoader`
- `DualCLIPLoader`
- `SaveImage`
- `EmptyLatentImage`
- `SeargePromptCombiner`
- `LoraLoader`

**识别到的模式**：lora

## 关键参数

- `batch_size` = `1`
- `height` = `1024`
- `lora_name` = `lliulanghan.safetensors`
- `strength_clip` = `1`
- `strength_model` = `1.0000000000000002`
- `width` = `768`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicScheduler`、`BasicGuider`、`Note`、`VAELoader`、`CLIPTextEncodeFlux`、`VAEDecode`、`UNETLoader`、`DualCLIPLoader`、`SaveImage`、`EmptyLatentImage`、`SeargePromptCombiner`
