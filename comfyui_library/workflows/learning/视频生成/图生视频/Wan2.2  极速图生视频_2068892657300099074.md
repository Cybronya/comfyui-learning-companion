---
key: 视频生成/图生视频/Wan2.2  极速图生视频_2068892657300099074.json
name: Wan2.2  极速图生视频_2068892657300099074.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2  极速图生视频_2068892657300099074.json
hash: 4aaf75e70f2fe5e6
coverage: 0.92
learned_at: 2026-10-15 22:40:22
nodes: [VAELoader, Note, WanImageToVideo, ModelSamplingSD3, LayerUtility: PurgeVRAM, Note, PathchSageAttentionKJ, CLIPLoader, ModelSamplingSD3, KSamplerAdvanced, VAEDecode, JWInteger, JWInteger, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, CLIPTextEncode, LoraLoaderModelOnly, KSamplerAdvanced, LayerUtility: PurgeVRAM, JWInteger, UNETLoader, VHS_VideoCombine, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2  极速图生视频_2068892657300099074.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2068892657300099074.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（25 个）：
- `VAELoader`
- `Note`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `Note`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `JWInteger`
- `JWInteger`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `JWInteger`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`VAELoader`、`WanImageToVideo`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM`、`PathchSageAttentionKJ`、`CLIPLoader`、`KSamplerAdvanced`、`VAEDecode`、`JWInteger`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
