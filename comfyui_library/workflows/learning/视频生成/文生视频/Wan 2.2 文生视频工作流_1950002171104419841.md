---
key: 视频生成/文生视频/Wan 2.2 文生视频工作流_1950002171104419841.json
name: Wan 2.2 文生视频工作流_1950002171104419841.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950002171104419841.json
hash: 17c1d15db0c635b1
coverage: 1
learned_at: 2026-10-15 22:43:33
nodes: [ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, CLIPLoader, EmptyHunyuanLatentVideo, UNETLoader, LoraLoaderModelOnly, KSamplerAdvanced, VAELoader, LoraLoaderModelOnly, CLIPTextEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, VHS_VideoCombine, VAEDecodeTiled, KSamplerAdvanced, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan 2.2 文生视频工作流_1950002171104419841.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950002171104419841.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（17 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `EmptyHunyuanLatentVideo`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`CLIPLoader`、`EmptyHunyuanLatentVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`VAELoader`、`PathchSageAttentionKJ`、`VHS_VideoCombine`、`VAEDecodeTiled`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、VAEDecodeTiled、EmptyHunyuanLatentVideo
