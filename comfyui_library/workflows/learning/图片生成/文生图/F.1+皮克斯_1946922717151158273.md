---
key: 图片生成/文生图/F.1+皮克斯_1946922717151158273.json
name: F.1+皮克斯_1946922717151158273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1+皮克斯_1946922717151158273.json
hash: 7a4e805bec04589e
coverage: 0.933333
learned_at: 2026-10-10 20:58:30
nodes: [RandomNoise, KSamplerSelect, SamplerCustomAdvanced, BasicGuider, Note, SaveImage, VAELoader, CLIPTextEncodeFlux, VAEDecode, UNETLoader, DualCLIPLoader, BasicScheduler, LoraLoader, SeargePromptCombiner, EmptyLatentImage]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 1280, "lora_name": "卡皮巴拉Lora.safetensors", "strength_clip": 1, "strength_model": 0.8000000000000002, "width": 720}
---

# 图片生成/文生图/F.1+皮克斯_1946922717151158273.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.1+皮克斯_1946922717151158273.json`

## 结构

**节点**（15 个）：
- `RandomNoise`
- `KSamplerSelect`
- `SamplerCustomAdvanced`
- `BasicGuider`
- `Note`
- `SaveImage`
- `VAELoader`
- `CLIPTextEncodeFlux`
- `VAEDecode`
- `UNETLoader`
- `DualCLIPLoader`
- `BasicScheduler`
- `LoraLoader`
- `SeargePromptCombiner`
- `EmptyLatentImage`

**识别到的模式**：lora

## 关键参数

- `batch_size` = `1`
- `height` = `1280`
- `lora_name` = `卡皮巴拉Lora.safetensors`
- `strength_clip` = `1`
- `strength_model` = `0.8000000000000002`
- `width` = `720`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicGuider`、`Note`、`SaveImage`、`VAELoader`、`CLIPTextEncodeFlux`、`VAEDecode`、`UNETLoader`、`DualCLIPLoader`、`BasicScheduler`、`LoraLoader`、`SeargePromptCombiner`
