---
key: 平台全量/wan2.2视频延长_1979179407367639042.json
name: wan2.2视频延长_1979179407367639042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2视频延长_1979179407367639042.json
hash: 08fba2fbd010b36f
coverage: 0.97561
learned_at: 2026-11-14 01:19:51
nodes: [ModelSamplingSD3, CLIPTextEncode, MathExpression|pysssss, easy convertAnything, VHS_SelectImages, ModelSamplingSD3, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, UNETLoader, CLIPTextEncode, WanImageToVideo, RIFE VFI, VAEDecode, WanVideoBlender, VHS_VideoCombine, VHS_LoadVideo, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, ModelSamplingSD3, CLIPTextEncode, MathExpression|pysssss, easy convertAnything, VHS_SelectImages, ModelSamplingSD3, CLIPLoader, VAELoader, UNETLoader, CLIPTextEncode, WanImageToVideo, RIFE VFI, VAEDecode, WanVideoBlender, VHS_VideoCombine, VHS_LoadVideo, UNETLoader, KSamplerAdvanced, KSamplerAdvanced, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 平台全量/wan2.2视频延长_1979179407367639042.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2视频延长_1979179407367639042.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（41 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `easy convertAnything`
- `VHS_SelectImages`
- `ModelSamplingSD3`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `RIFE VFI`
- `VAEDecode` ★核心
- `WanVideoBlender`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `easy convertAnything`
- `VHS_SelectImages`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `RIFE VFI`
- `VAEDecode` ★核心
- `WanVideoBlender`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **98%**（40/41）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`MathExpression|pysssss`、`easy convertAnything`、`VHS_SelectImages`、`CLIPLoader`、`LoraLoaderModelOnly`、`VAELoader`、`UNETLoader`、`WanImageToVideo`、`RIFE VFI`、`VAEDecode`、`WanVideoBlender`、`VHS_VideoCombine`、`VHS_LoadVideo`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、KSamplerAdvanced、easy convertAnything
