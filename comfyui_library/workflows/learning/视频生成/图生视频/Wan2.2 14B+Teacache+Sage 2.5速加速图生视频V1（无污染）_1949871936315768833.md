---
key: 视频生成/图生视频/Wan2.2 14B+Teacache+Sage 2.5速加速图生视频V1（无污染）_1949871936315768833.json
name: Wan2.2 14B+Teacache+Sage 2.5速加速图生视频V1（无污染）_1949871936315768833.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1949871936315768833.json
hash: 90b0f757f2499043
coverage: 0.92
learned_at: 2026-10-15 22:30:50
nodes: [CLIPTextEncode, CLIPLoader, VAELoader, Note, LoadImage, WanImageToVideo, VAEDecode, ModelSamplingSD3, ModelSamplingSD3, TeaCache, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, KSamplerAdvanced, UNETLoader, CLIPTextEncode, Note, VHS_VideoCombine, PathchSageAttentionKJ, UNETLoader, KSamplerAdvanced, PathchSageAttentionKJ, TeaCache, JWInteger, JWInteger, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 14B+Teacache+Sage 2.5速加速图生视频V1（无污染）_1949871936315768833.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1949871936315768833.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（25 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `LoadImage`
- `WanImageToVideo`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `TeaCache`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `TeaCache`
- `JWInteger`
- `JWInteger`
- `JWInteger`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`LoadImage`、`WanImageToVideo`、`VAEDecode`、`ModelSamplingSD3`、`TeaCache`、`LayerUtility: PurgeVRAM`、`KSamplerAdvanced`、`UNETLoader`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`JWInteger`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ModelSamplingSD3
