---
key: 视频生成/文生视频/wan2.2万相文生视频_1987538580979519489.json
name: wan2.2万相文生视频_1987538580979519489
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2万相文生视频_1987538580979519489.json
hash: 9b5fe6cb5bf312d6
coverage: 1
learned_at: 2026-10-15 22:47:36
nodes: [easy int, CLIPLoader, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, CM_IntToFloat, SimpleMath+, VHS_VideoCombine, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, UNETLoader, UNETLoader, VAEDecode, VAELoader, easy int, CLIPTextEncode, EmptyHunyuanLatentVideo, easy int, easy int]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/wan2.2万相文生视频_1987538580979519489.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2万相文生视频_1987538580979519489.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（21 个）：
- `easy int`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CM_IntToFloat`
- `SimpleMath+`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `easy int`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `easy int`
- `easy int`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`easy int`、`CLIPLoader`、`CLIPTextEncode`、`KSamplerAdvanced`、`CM_IntToFloat`、`SimpleMath+`、`VHS_VideoCombine`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`UNETLoader`、`VAEDecode`、`VAELoader`、`EmptyHunyuanLatentVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、CM_IntToFloat
