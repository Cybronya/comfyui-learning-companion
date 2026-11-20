---
key: 平台全量/FLUX.1 Controlnet工作流_2118259281589002241.json
name: FLUX.1 Controlnet工作流_2118259281589002241
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX.1 Controlnet工作流_2118259281589002241.json
hash: 62dbf54ae35d6c37
coverage: 0.958333
learned_at: 2026-11-14 00:25:00
nodes: [UNETLoader, DualCLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, FluxGuidance, KSampler, EmptySD3LatentImage, VAEDecode, SaveImage, ControlNetApplyAdvanced, ControlNetLoader, SetUnionControlNetType, LoadImage, AIO_Preprocessor, AIO_Preprocessor, ControlNetApplyAdvanced, LoadImage, ControlNetLoader, SetUnionControlNetType, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), Preview from image [Crystools], Preview from image [Crystools]]
patterns: []
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.6, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 640197171573554, "steps": 20}
---

# 平台全量/FLUX.1 Controlnet工作流_2118259281589002241.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX.1 Controlnet工作流_2118259281589002241.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `SaveImage`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `SetUnionControlNetType`
- `LoadImage`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `ControlNetApplyAdvanced` ★核心
- `LoadImage`
- `ControlNetLoader`
- `SetUnionControlNetType`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Preview from image [Crystools]`
- `Preview from image [Crystools]`

## 关键参数

- `seed` = `640197171573554`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.6`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`FluxGuidance`、`KSampler`、`EmptySD3LatentImage`、`VAEDecode`、`SaveImage`、`ControlNetApplyAdvanced`、`ControlNetLoader`、`SetUnionControlNetType`、`LoadImage`、`AIO_Preprocessor`、`LoraLoaderModelOnly`、`Preview from image [Crystools]`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced
