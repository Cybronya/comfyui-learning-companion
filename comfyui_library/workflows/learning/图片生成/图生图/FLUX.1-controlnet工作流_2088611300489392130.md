---
key: 图片生成/图生图/FLUX.1-controlnet工作流_2088611300489392130.json
name: FLUX.1-controlnet工作流_2088611300489392130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.1-controlnet工作流_2088611300489392130.json
hash: da10895a6a70160d
coverage: 0.954545
learned_at: 2026-10-23 10:54:01
nodes: [VAEDecode, SaveImage, SetUnionControlNetType, AIO_Preprocessor, LoadImage, ControlNetLoader, LoadImage, SetUnionControlNetType, AIO_Preprocessor, KSampler, EmptySD3LatentImage, ControlNetLoader, CLIPTextEncode, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetApplyAdvanced, LoraLoaderModelOnly, UNETLoader, DualCLIPLoader, VAELoader, FluxGuidance, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.6000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 786845563956807, "steps": 20}
---

# 图片生成/图生图/FLUX.1-controlnet工作流_2088611300489392130.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.1-controlnet工作流_2088611300489392130.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `VAEDecode` ★核心
- `SaveImage`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `LoadImage`
- `ControlNetLoader`
- `LoadImage`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `FluxGuidance`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `786845563956807`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.6000000000000001`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`VAEDecode`、`SaveImage`、`SetUnionControlNetType`、`AIO_Preprocessor`、`LoadImage`、`ControlNetLoader`、`KSampler`、`EmptySD3LatentImage`、`CLIPTextEncode`、`ControlNetApplyAdvanced`、`LoraLoaderModelOnly`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`FluxGuidance`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced
