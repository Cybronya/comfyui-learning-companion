---
key: 视频生成/图生视频/remix V3.0 单图生视频&首尾帧_2034945354898083841.json
name: remix V3.0 单图生视频&首尾帧_2034945354898083841.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2034945354898083841.json
hash: 88d7bfc3d2d82f6a
coverage: 0.9
learned_at: 2026-10-15 22:35:47
nodes: [CLIPTextEncode, KSamplerAdvanced, Seed (rgthree), ModelSamplingSD3, KSamplerAdvanced, INTConstant, INTConstant, ModelSamplingSD3, INTConstant, INTConstant, VHS_VideoCombine, VAEDecode, INTConstant, WanFunInpaintToVideo, CLIPTextEncode, ImageResizeKJv2, ImageResizeKJv2, llama_cpp_parameters, ImageStitch, easy showAnything, llama_cpp_instruct_adv, PreviewImage, PrimitiveStringMultiline, LoadImage, LoadImage, UNETLoader, UNETLoader, CLIPLoader, VAELoader, llama_cpp_model_loader]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/remix V3.0 单图生视频&首尾帧_2034945354898083841.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2034945354898083841.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `Seed (rgthree)`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `INTConstant`
- `ModelSamplingSD3`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `INTConstant`
- `WanFunInpaintToVideo`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `llama_cpp_parameters`
- `ImageStitch`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `llama_cpp_model_loader`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（27/30）

**有卡**：`CLIPTextEncode`、`KSamplerAdvanced`、`Seed (rgthree)`、`ModelSamplingSD3`、`INTConstant`、`VHS_VideoCombine`、`VAEDecode`、`WanFunInpaintToVideo`、`ImageResizeKJv2`、`llama_cpp_parameters`、`ImageStitch`、`llama_cpp_instruct_adv`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`llama_cpp_model_loader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
