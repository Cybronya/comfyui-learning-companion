---
key: 图片生成/图生图/Flux.1+ controlnet工作流_2109991263348019202.json
name: Flux.1+ controlnet工作流_2109991263348019202
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1+ controlnet工作流_2109991263348019202.json
hash: 70829724bbbf7846
coverage: 1
learned_at: 2026-10-23 10:58:41
nodes: [AIO_Preprocessor, VAEDecode, LoadImage, LoadImage, EmptySD3LatentImage, FluxGuidance, VAELoader, KSampler, UNETLoader, DualCLIPLoader, ControlNetLoader, CLIPTextEncode, CLIPTextEncode, SaveImage, AIO_Preprocessor, LoraLoaderModelOnly, ControlNetApplyAdvanced, ControlNetApplyAdvanced, SetUnionControlNetType, ControlNetLoader, SetUnionControlNetType]
patterns: []
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.6000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 675035935141472, "steps": 20}
---

# 图片生成/图生图/Flux.1+ controlnet工作流_2109991263348019202.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1+ controlnet工作流_2109991263348019202.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `AIO_Preprocessor`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `VAELoader`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `AIO_Preprocessor`
- `LoraLoaderModelOnly` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `SetUnionControlNetType`
- `ControlNetLoader`
- `SetUnionControlNetType`

## 关键参数

- `seed` = `675035935141472`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.6000000000000001`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`AIO_Preprocessor`、`VAEDecode`、`LoadImage`、`EmptySD3LatentImage`、`FluxGuidance`、`VAELoader`、`KSampler`、`UNETLoader`、`DualCLIPLoader`、`ControlNetLoader`、`CLIPTextEncode`、`SaveImage`、`LoraLoaderModelOnly`、`ControlNetApplyAdvanced`、`SetUnionControlNetType`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced
