---
key: 视频生成/文生视频/Wan2.2文生视频_1997925759635324929.json
name: Wan2.2文生视频_1997925759635324929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频_1997925759635324929.json
hash: edcdf663141c74d2
coverage: 1
learned_at: 2026-10-15 22:47:15
nodes: [ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPLoader, VAELoader, UNETLoader, UNETLoader, KSamplerAdvanced, VAEDecode, KSamplerAdvanced, EmptyHunyuanLatentVideo, CLIPTextEncode, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2文生视频_1997925759635324929.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频_1997925759635324929.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（15 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSamplerAdvanced`、`VAEDecode`、`EmptyHunyuanLatentVideo`、`CLIPTextEncode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、ModelSamplingSD3
