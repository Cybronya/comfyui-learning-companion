---
key: 视频生成/文生视频/wan2.2-14B 官方文生视频+自动提示词_1949825598320459778.json
name: wan2.2-14B 官方文生视频+自动提示词_1949825598320459778.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1949825598320459778.json
hash: a30d9a262deaf5c6
coverage: 0.931034
learned_at: 2026-10-15 22:43:33
nodes: [DF_Integer, easy showAnything, CLIPLoader, CLIPTextEncode, easy cleanGpuUsed, easy showAnything, RH_Prompter, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, TextBox, KSamplerAdvanced, CR Text Replace, LayerUtility: PurgeVRAM, ModelSamplingSD3, VAELoader, CLIPTextEncode, EmptyHunyuanLatentVideo, ModelSamplingSD3, EmptyImage, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, easy imageSize, UNETLoader, UNETLoader, TextBox]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/wan2.2-14B 官方文生视频+自动提示词_1949825598320459778.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1949825598320459778.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（29 个）：
- `DF_Integer`
- `easy showAnything`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `easy showAnything`
- `RH_Prompter`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `TextBox`
- `KSamplerAdvanced` ★核心
- `CR Text Replace`
- `LayerUtility: PurgeVRAM`
- `ModelSamplingSD3`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `EmptyImage`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `easy imageSize`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
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

**有卡**：`DF_Integer`、`CLIPLoader`、`CLIPTextEncode`、`easy cleanGpuUsed`、`RH_Prompter`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`TextBox`、`CR Text Replace`、`LayerUtility: PurgeVRAM`、`ModelSamplingSD3`、`VAELoader`、`EmptyHunyuanLatentVideo`、`EmptyImage`、`SimpleMath+`、`easy imageSize`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、RH_Prompter
