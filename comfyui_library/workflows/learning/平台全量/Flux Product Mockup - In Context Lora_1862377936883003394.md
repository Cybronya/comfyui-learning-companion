---
key: 平台全量/Flux Product Mockup - In Context Lora_1862377936883003394.json
name: Flux Product Mockup - In Context Lora_1862377936883003394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux Product Mockup - In Context Lora_1862377936883003394.json
hash: a2fa0ef57045fbc8
coverage: 0.684211
learned_at: 2026-11-14 00:28:01
nodes: [ImagePadForOutpaint, MaskToImage, Note, PreviewImage, VAEEncodeForInpaint, UNETLoader, DualCLIPLoader, VAELoader, SaveImage, CLIPTextEncodeFlux, Note, CLIPTextEncodeFlux, LoraLoader, KSampler, VAEDecode, LoadAndResizeImage, PreviewImage, Note, Note]
patterns: [lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "IC_TRY_ON_v3_e4.safetensors", "sampler_name": "euler", "scheduler": "normal", "seed": 950372244557113, "steps": 35, "strength_clip": 1, "strength_model": 1}
---

# 平台全量/Flux Product Mockup - In Context Lora_1862377936883003394.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux Product Mockup - In Context Lora_1862377936883003394.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `ImagePadForOutpaint`
- `MaskToImage`
- `Note`
- `PreviewImage`
- `VAEEncodeForInpaint` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `SaveImage`
- `CLIPTextEncodeFlux` ★核心
- `Note`
- `CLIPTextEncodeFlux` ★核心
- `LoraLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoadAndResizeImage`
- `PreviewImage`
- `Note`
- `Note`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `IC_TRY_ON_v3_e4.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `950372244557113`
- `steps` = `35`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **68%**（13/19）

**有卡**：`ImagePadForOutpaint`、`MaskToImage`、`VAEEncodeForInpaint`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`SaveImage`、`CLIPTextEncodeFlux`、`LoraLoader`、`KSampler`、`VAEDecode`、`LoadAndResizeImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncodeFlux、VAEEncodeForInpaint、LoraLoader、LoRALoader
