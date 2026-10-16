---
key: 视频生成/文生视频/wan2_2.14B_提示词自动优化-文生视频-加速版-KJ模型_1950557928396935169.json
name: wan2_2.14B_提示词自动优化-文生视频-加速版-KJ模型_1950557928396935169.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950557928396935169.json
hash: ef8d29de152dcf6a
coverage: 0.931034
learned_at: 2026-10-15 22:43:36
nodes: [ImpactInt, ImpactInt, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, VAELoader, EmptyHunyuanLatentVideo, SimpleMath+, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, CreateVideo, SaveVideo, ImpactInt, easy showAnything, RH_Prompter, easy showAnything, CR Text Replace, TextBox, easy cleanGpuUsed, TextBox]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/wan2_2.14B_提示词自动优化-文生视频-加速版-KJ模型_1950557928396935169.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950557928396935169.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（29 个）：
- `ImpactInt`
- `ImpactInt`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `ImpactInt`
- `easy showAnything`
- `RH_Prompter`
- `easy showAnything`
- `CR Text Replace`
- `TextBox`
- `easy cleanGpuUsed`
- `TextBox`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`ImpactInt`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`EmptyHunyuanLatentVideo`、`SimpleMath+`、`CLIPTextEncode`、`KSamplerAdvanced`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`RH_Prompter`、`CR Text Replace`、`TextBox`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
