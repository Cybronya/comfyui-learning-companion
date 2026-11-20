---
key: 平台全量/Inspiration finder for Jewelry-makers & Clients_1887383424712204290.json
name: Inspiration finder for Jewelry-makers & Clients_1887383424712204290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Inspiration finder for Jewelry-makers & Clients_1887383424712204290.json
hash: 6fbc68c5dac4d103
coverage: 0.75
learned_at: 2026-11-14 00:32:47
nodes: [PlaySound|pysssss, VAEDecode, SaveImage, IterativeLatentUpscale, PixelKSampleUpscalerProvider, Reroute, Reroute, Reroute, ShowText|pysssss, Note, KSampler, Text Random Line, Text Concatenate, Text Concatenate, CR SDXL Aspect Ratio, VAEDecode, CheckpointLoaderSimple, CLIPSetLastLayer, LoraLoader, Text Concatenate, Bus Node, Bus Node, Reroute, UpscaleModelLoader, Seed (rgthree), Reroute, Fast Groups Muter (rgthree), CLIPTextEncode, CLIPTextEncode, Bus Node, PrimitiveNode, TextBox, TextBox, TextBox, TextBox, SaveImage]
patterns: [lora]
missing: []
parameters: {"cfg": 6.5, "checkpoint": "crystalClearXL_ccxl.safetensors", "denoise": 1, "lora_name": "add-detail-xl.safetensors", "sampler_name": "dpmpp_2m_sde_gpu", "scheduler": "karras", "seed": 477780103124987, "steps": 40, "strength_clip": 0.7000000000000001, "strength_model": 0.7000000000000001}
---

# 平台全量/Inspiration finder for Jewelry-makers & Clients_1887383424712204290.json

> 来源文件 `comfyui_library/workflows/平台全量/Inspiration finder for Jewelry-makers & Clients_1887383424712204290.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `PlaySound|pysssss`
- `VAEDecode` ★核心
- `SaveImage`
- `IterativeLatentUpscale`
- `PixelKSampleUpscalerProvider`
- `Reroute`
- `Reroute`
- `Reroute`
- `ShowText|pysssss`
- `Note`
- `KSampler` ★核心
- `Text Random Line`
- `Text Concatenate`
- `Text Concatenate`
- `CR SDXL Aspect Ratio`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPSetLastLayer`
- `LoraLoader` ★核心
- `Text Concatenate`
- `Bus Node`
- `Bus Node`
- `Reroute`
- `UpscaleModelLoader`
- `Seed (rgthree)`
- `Reroute`
- `Fast Groups Muter (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Bus Node`
- `PrimitiveNode`
- `TextBox`
- `TextBox`
- `TextBox`
- `TextBox`
- `SaveImage`

**识别到的模式**：lora

## 关键参数

- `seed` = `477780103124987`
- `steps` = `40`
- `cfg` = `6.5`
- `sampler_name` = `dpmpp_2m_sde_gpu`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `crystalClearXL_ccxl.safetensors`
- `lora_name` = `add-detail-xl.safetensors`
- `strength_model` = `0.7000000000000001`
- `strength_clip` = `0.7000000000000001`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`PlaySound|pysssss`、`VAEDecode`、`SaveImage`、`IterativeLatentUpscale`、`PixelKSampleUpscalerProvider`、`KSampler`、`Text Random Line`、`Text Concatenate`、`CR SDXL Aspect Ratio`、`CheckpointLoaderSimple`、`CLIPSetLastLayer`、`LoraLoader`、`Bus Node`、`UpscaleModelLoader`、`Seed (rgthree)`、`CLIPTextEncode`、`TextBox`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、Seed (rgthree)、IterativeLatentUpscale、LoraLoader、LoRALoader
