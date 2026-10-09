---
key: 图片生成/文生图/F.1-FLUX文生图工作流（一键运行）(双LORA)_1915296194967306242.json
name: F.1-FLUX文生图工作流（一键运行）(双LORA)_1915296194967306242.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1-FLUX文生图工作流（一键运行）(双LORA)_1915296194967306242.json
hash: 8c9e8e164ea5ca0a
coverage: 1
learned_at: 2026-10-07 22:07:34
nodes: [VAELoader, KSamplerSelect, RandomNoise, BasicGuider, SamplerCustomAdvanced, VAEDecode, CLIPTextEncode, EmptyLatentImage, BasicScheduler, SaveImage, LoraLoader, LoraLoader, DualCLIPLoader, UNETLoader]
patterns: [lora]
missing: []
parameters: {"batch_size": 2, "height": 1024, "lora_name": "flux-dpgirl-mql-lora.safetensors", "strength_clip": 1, "strength_model": 0.6, "width": 768}
---

# 图片生成/文生图/F.1-FLUX文生图工作流（一键运行）(双LORA)_1915296194967306242.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1915296194967306242.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `VAELoader`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `BasicScheduler`
- `SaveImage`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心

**识别到的模式**：lora

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `2`
- `lora_name` = `flux-dpgirl-mql-lora.safetensors`
- `strength_model` = `0.6`
- `strength_clip` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`VAELoader`、`KSamplerSelect`、`RandomNoise`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`CLIPTextEncode`、`EmptyLatentImage`、`BasicScheduler`、`SaveImage`、`LoraLoader`、`DualCLIPLoader`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、EmptyLatentImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LoraLoader
