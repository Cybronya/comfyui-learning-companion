---
key: 视频生成/文生视频/DNR-wan2.2-官方文生视频_1952913163996041218.json
name: DNR-wan2.2-官方文生视频_1952913163996041218.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/DNR-wan2.2-官方文生视频_1952913163996041218.json
hash: 2701fc2b2dcf1075
coverage: 1
learned_at: 2026-10-15 22:43:38
nodes: [CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, VHS_VideoCombine, CLIPLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, VAELoader, VAEDecode, LayerUtility: PurgeVRAM, TextBox, EmptyHunyuanLatentVideo, KSamplerAdvanced, UNETLoader, UNETLoader, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/DNR-wan2.2-官方文生视频_1952913163996041218.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1952913163996041218.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（18 个）：
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAELoader`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `TextBox`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`CLIPTextEncode`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`CLIPLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAELoader`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`TextBox`、`EmptyHunyuanLatentVideo`、`KSamplerAdvanced`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、ModelSamplingSD3
