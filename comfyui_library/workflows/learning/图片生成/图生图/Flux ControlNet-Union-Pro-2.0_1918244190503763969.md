---
key: 图片生成/图生图/Flux ControlNet-Union-Pro-2.0_1918244190503763969.json
name: Flux ControlNet-Union-Pro-2.0_1918244190503763969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux ControlNet-Union-Pro-2.0_1918244190503763969.json
hash: d7374339b68e870c
coverage: 0.851852
learned_at: 2026-10-23 10:56:14
nodes: [AIO_Preprocessor, SetUnionControlNetType, CLIPTextEncode, PreviewImage, PreviewImage, AIO_Preprocessor, PreviewImage, FluxGuidance, CLIPTextEncode, CLIPTextEncode, SetUnionControlNetType, KSampler, KSampler, PreviewImage, FluxGuidance, ControlNetApplySD3, ControlNetApplySD3, EmptySD3LatentImage, EmptySD3LatentImage, LoadImage, ImpactImageInfo, VAEDecode, VAEDecode, SaveImage, ControlNetLoader, CheckpointLoaderSimple, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "flux1-dev-fp8-with_clip_vae.safetensors", "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1038878835193868, "steps": 20}
---

# 图片生成/图生图/Flux ControlNet-Union-Pro-2.0_1918244190503763969.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux ControlNet-Union-Pro-2.0_1918244190503763969.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `PreviewImage`
- `AIO_Preprocessor`
- `PreviewImage`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetUnionControlNetType`
- `KSampler` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `FluxGuidance`
- `ControlNetApplySD3` ★核心
- `ControlNetApplySD3` ★核心
- `EmptySD3LatentImage`
- `EmptySD3LatentImage`
- `LoadImage`
- `ImpactImageInfo`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ControlNetLoader`
- `CheckpointLoaderSimple` ★核心
- `SaveImage`

## 关键参数

- `seed` = `1038878835193868`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `1.0000000000000002`
- `checkpoint` = `flux1-dev-fp8-with_clip_vae.safetensors`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`AIO_Preprocessor`、`SetUnionControlNetType`、`CLIPTextEncode`、`FluxGuidance`、`KSampler`、`ControlNetApplySD3`、`EmptySD3LatentImage`、`LoadImage`、`ImpactImageInfo`、`VAEDecode`、`SaveImage`、`ControlNetLoader`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetLoader、SetUnionControlNetType、ControlNetApplySD3
