---
key: 中文直出---F.1-FLUX文生图工作流+LORA（一键运行）_1929761113691340801.json
name: 中文直出---F.1-FLUX文生图工作流+LORA（一键运行）_1929761113691340801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/中文直出---F.1-FLUX文生图工作流+LORA（一键运行）_1929761113691340801.json
hash: f2917a2c394cc3e4
coverage: 1
learned_at: 2026-10-10 20:59:34
nodes: [KSamplerSelect, RandomNoise, BasicGuider, SamplerCustomAdvanced, VAEDecode, UNETLoader, DualCLIPLoader, VAELoader, EmptyLatentImage, BasicScheduler, CLIPTextEncode, SaveImage, ShowText, LoraLoader, RH_Translator]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 1024, "lora_name": "flat childrenXX.safetensors", "strength_clip": 1, "strength_model": 0.8, "width": 768}
---

# 中文直出---F.1-FLUX文生图工作流+LORA（一键运行）_1929761113691340801.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/中文直出---F.1-FLUX文生图工作流+LORA（一键运行）_1929761113691340801.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `KSamplerSelect` ★核心
- `RandomNoise`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `ShowText`
- `LoraLoader` ★核心
- `RH_Translator`

**识别到的模式**：lora

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `lora_name` = `flat childrenXX.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`KSamplerSelect`、`RandomNoise`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`EmptyLatentImage`、`BasicScheduler`、`CLIPTextEncode`、`SaveImage`、`ShowText`、`LoraLoader`、`RH_Translator`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、EmptyLatentImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LoraLoader
