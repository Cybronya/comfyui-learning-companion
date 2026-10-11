---
key: 视频生成/文生视频/Wan2.2文生视频（优化版）_2067195635350196225.json
name: Wan2.2文生视频（优化版）_2067195635350196225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频（优化版）_2067195635350196225.json
hash: 4cf43d5f31454a5d
coverage: 1
learned_at: 2026-10-11 20:21:31
nodes: [ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, KSamplerAdvanced, VAEDecode, KSamplerAdvanced, EmptyHunyuanLatentVideo, VHS_VideoCombine, UNETLoader, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2文生视频（优化版）_2067195635350196225.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频（优化版）_2067195635350196225.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（15 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `EmptyHunyuanLatentVideo`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`ModelSamplingSD3`、`PathchSageAttentionKJ`、`KSamplerAdvanced`、`VAEDecode`、`EmptyHunyuanLatentVideo`、`VHS_VideoCombine`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、ModelSamplingSD3
