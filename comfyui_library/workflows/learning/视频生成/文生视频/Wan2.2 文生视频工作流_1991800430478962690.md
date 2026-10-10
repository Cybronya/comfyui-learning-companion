---
key: 视频生成/文生视频/Wan2.2 文生视频工作流_1991800430478962690.json
name: Wan2.2 文生视频工作流_1991800430478962690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 文生视频工作流_1991800430478962690.json
hash: 304de73b31a42c44
coverage: 1
learned_at: 2026-10-11 02:57:38
nodes: [UNETLoader, UNETLoader, CLIPLoader, PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, VAEDecode, VHS_VideoCombine, EmptyHunyuanLatentVideo, VAELoader, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 30, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "increment"}
---

# 视频生成/文生视频/Wan2.2 文生视频工作流_1991800430478962690.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 文生视频工作流_1991800430478962690.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（15 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `increment`
- `cfg` = `30`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`UNETLoader`、`CLIPLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAEDecode`、`VHS_VideoCombine`、`EmptyHunyuanLatentVideo`、`VAELoader`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、ModelSamplingSD3
