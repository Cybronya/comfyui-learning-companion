---
key: 视频生成/文生视频/Wan2.2 Dyno+Remix文生视频V1_1974792612945244161.json
name: Wan2.2 Dyno+Remix文生视频V1_1974792612945244161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Dyno+Remix文生视频V1_1974792612945244161.json
hash: 4de1a59318687705
coverage: 1
learned_at: 2026-10-10 23:06:48
nodes: [CLIPTextEncode, PathchSageAttentionKJ, EmptyHunyuanLatentVideo, INTConstant, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, VAELoader, CLIPLoader, INTConstant, VAEDecode, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, JWInteger, JWInteger, JWInteger, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, TT_img_enc, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2 Dyno+Remix文生视频V1_1974792612945244161.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Dyno+Remix文生视频V1_1974792612945244161.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（24 个）：
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `EmptyHunyuanLatentVideo`
- `INTConstant`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VAELoader`
- `CLIPLoader`
- `INTConstant`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `TT_img_enc`
- `SaveImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`CLIPTextEncode`、`PathchSageAttentionKJ`、`EmptyHunyuanLatentVideo`、`INTConstant`、`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`LoraLoaderModelOnly`、`UNETLoader`、`JWInteger`、`KSamplerAdvanced`、`VHS_VideoCombine`、`TT_img_enc`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
