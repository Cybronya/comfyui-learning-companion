---
key: 图片生成/文生图/DP小熊猫 V1.0_1897934794485878785.json
name: DP小熊猫 V1.0_1897934794485878785
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/DP小熊猫 V1.0_1897934794485878785.json
hash: 46b084daac92cd83
coverage: 1
learned_at: 2026-10-07 03:17:52
nodes: [SaveImage, VAEDecode, SamplerCustomAdvanced, VAELoader, EmptyLatentImage, BasicScheduler, KSamplerSelect, BasicGuider, RandomNoise, UNETLoader, DualCLIPLoader, LoraLoader, CLIPTextEncode]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 400, "lora_name": "flux-lora (1).safetensors", "strength_clip": 1, "strength_model": 1, "width": 400}
---

# 图片生成/文生图/DP小熊猫 V1.0_1897934794485878785.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/DP小熊猫 V1.0_1897934794485878785.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `SaveImage`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：lora

## 关键参数

- `width` = `400`
- `height` = `400`
- `batch_size` = `1`
- `lora_name` = `flux-lora (1).safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`SaveImage`、`VAEDecode`、`SamplerCustomAdvanced`、`VAELoader`、`EmptyLatentImage`、`BasicScheduler`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、EmptyLatentImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LoraLoader
