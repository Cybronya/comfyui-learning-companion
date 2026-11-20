---
key: 平台全量/图生图sd3.5模型 +SUPIR高清放大修复_1848917154883158018.json
name: 图生图sd3.5模型 +SUPIR高清放大修复_1848917154883158018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/图生图sd3.5模型 +SUPIR高清放大修复_1848917154883158018.json
hash: 895ad356a71db2a6
coverage: 0.556962
learned_at: 2026-11-14 01:56:13
nodes: [CLIPLoader, DualCLIPLoader, Note, Note, SeargePromptText, RH_Captioner, TripleCLIPLoader, SUPIR_first_stage, SUPIR_sample, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, ColorMatch, SetNode, GetNode, SetNode, GetNode, SUPIR_model_loader_v2, CheckpointLoaderSimple, Display Int (rgthree), Display Int (rgthree), UpscaleModelLoader, CLIPTextEncode, Seed (rgthree), CLIPTextEncode, ImpactInt, Image Comparer (rgthree), ImpactInt, ImpactInt, ImageResize+, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, PreviewImage, VAEDecode, PreviewImage, PreviewImage, LoadImage, LoadImage, RH_Captioner, KSampler, VAEDecode, SaveImage, PreviewImage, easy cleanGpuUsed, CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, KSampler, VAEDecode, SaveImage, PreviewImage, EmptySD3LatentImage, CLIPTextEncode, KSampler, CheckpointLoaderSimple, CLIPTextEncode, PreviewImage, GetNode, GetNode, HD UltimateSDUpscale, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 5.45, "checkpoint": "sd3.5_large.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 361963662467122, "steps": 20}
---

# 平台全量/图生图sd3.5模型 +SUPIR高清放大修复_1848917154883158018.json

> 来源文件 `comfyui_library/workflows/平台全量/图生图sd3.5模型 +SUPIR高清放大修复_1848917154883158018.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `CLIPLoader`
- `DualCLIPLoader`
- `Note`
- `Note`
- `SeargePromptText`
- `RH_Captioner`
- `TripleCLIPLoader`
- `SUPIR_first_stage`
- `SUPIR_sample`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `ColorMatch`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SUPIR_model_loader_v2`
- `CheckpointLoaderSimple` ★核心
- `Display Int (rgthree)`
- `Display Int (rgthree)`
- `UpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `ImpactInt`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `ImpactInt`
- `ImageResize+`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `RH_Captioner`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `GetNode`
- `GetNode`
- `HD UltimateSDUpscale`
- `SaveImage`

## 关键参数

- `checkpoint` = `sd3.5_large.safetensors`
- `seed` = `361963662467122`
- `steps` = `20`
- `cfg` = `5.45`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **56%**（44/79）

**有卡**：`CLIPLoader`、`DualCLIPLoader`、`SeargePromptText`、`RH_Captioner`、`TripleCLIPLoader`、`SUPIR_first_stage`、`SUPIR_sample`、`SUPIR_conditioner`、`SUPIR_decode`、`SUPIR_encode`、`ColorMatch`、`SUPIR_model_loader_v2`、`CheckpointLoaderSimple`、`Display Int (rgthree)`、`UpscaleModelLoader`、`CLIPTextEncode`、`Seed (rgthree)`、`ImpactInt`、`ImageResize+`、`VAEDecode`、`LoadImage`、`KSampler`、`SaveImage`、`easy cleanGpuUsed`、`EmptySD3LatentImage`、`HD UltimateSDUpscale`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPLoader、CLIPTextEncode、LoadImage、Seed (rgthree)、SUPIR_decode
