---
key: 视频生成/图生视频/WAN2.2 图生视频女孩微笑_1950190982249799682.json
name: WAN2.2 图生视频女孩微笑_1950190982249799682.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950190982249799682.json
hash: 9f9b6edaa03466b8
coverage: 1
learned_at: 2026-10-15 22:30:54
nodes: [VAEDecode, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, VHS_VideoCombine, VAEDecode, KSamplerAdvanced, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, CLIPLoader, VAELoader, ModelSamplingSD3, EmptyHunyuanLatentVideo, PathchSageAttentionKJ, UNETLoader, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, VHS_VideoCombine, CLIPLoader, CLIPTextEncode, VAELoader, ModelSamplingSD3, LoadImage, WanImageToVideo, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/WAN2.2 图生视频女孩微笑_1950190982249799682.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950190982249799682.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（31 个）：
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `LoadImage`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（31/31）

**有卡**：`VAEDecode`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VHS_VideoCombine`、`KSamplerAdvanced`、`CLIPLoader`、`VAELoader`、`EmptyHunyuanLatentVideo`、`CLIPTextEncode`、`LoadImage`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
