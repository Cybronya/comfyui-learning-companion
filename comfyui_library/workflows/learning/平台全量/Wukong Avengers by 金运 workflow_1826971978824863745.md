---
key: 平台全量/Wukong Avengers by 金运 workflow_1826971978824863745.json
name: Wukong Avengers by 金运 workflow_1826971978824863745
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wukong Avengers by 金运 workflow_1826971978824863745.json
hash: c84a1fb3f0f48357
coverage: 1
learned_at: 2026-11-14 01:07:31
nodes: [KSampler, VAEDecode, LoraLoader, CLIPTextEncode, FluxGuidance, CheckpointLoaderSimple, SDXLEmptyLatentSizePicker+, CLIPTextEncode, PlaySound|pysssss, SaveImage]
patterns: [lora]
missing: []
parameters: {"batch_size": 0, "cfg": 1, "checkpoint": "flux1-dev-fp8-Comfy-Org.safetensors", "denoise": 1, "height": 4, "lora_name": "FLUX1-超写实逼真黑悟空-支持在线生图_FLUX-超写实黑悟空--V1.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 558566680526941, "steps": 20, "strength_clip": 1, "strength_model": 1.2, "width": "896x1152 (0.78)"}
---

# 平台全量/Wukong Avengers by 金运 workflow_1826971978824863745.json

> 来源文件 `comfyui_library/workflows/平台全量/Wukong Avengers by 金运 workflow_1826971978824863745.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（10 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `CheckpointLoaderSimple` ★核心
- `SDXLEmptyLatentSizePicker+` ★核心
- `CLIPTextEncode` ★核心
- `PlaySound|pysssss`
- `SaveImage`

**识别到的模式**：lora

## 关键参数

- `seed` = `558566680526941`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `FLUX1-超写实逼真黑悟空-支持在线生图_FLUX-超写实黑悟空--V1.safetensors`
- `strength_model` = `1.2`
- `strength_clip` = `1`
- `checkpoint` = `flux1-dev-fp8-Comfy-Org.safetensors`
- `width` = `896x1152 (0.78)`
- `height` = `4`
- `batch_size` = `0`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`KSampler`、`VAEDecode`、`LoraLoader`、`CLIPTextEncode`、`FluxGuidance`、`CheckpointLoaderSimple`、`SDXLEmptyLatentSizePicker+`、`PlaySound|pysssss`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、FluxGuidance、SDXLEmptyLatentSizePicker+、LoraLoader、LoRALoader
