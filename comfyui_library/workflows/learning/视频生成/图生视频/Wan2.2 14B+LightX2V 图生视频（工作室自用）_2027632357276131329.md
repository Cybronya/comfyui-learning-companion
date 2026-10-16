---
key: 视频生成/图生视频/Wan2.2 14B+LightX2V 图生视频（工作室自用）_2027632357276131329.json
name: Wan2.2 14B+LightX2V 图生视频（工作室自用）_2027632357276131329.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2027632357276131329.json
hash: e068d6e9cdb39d0c
coverage: 0.92
learned_at: 2026-10-15 22:35:17
nodes: [CLIPTextEncode, VAELoader, Note, WanImageToVideo, ModelSamplingSD3, LayerUtility: PurgeVRAM, Note, UNETLoader, PathchSageAttentionKJ, CLIPLoader, ModelSamplingSD3, VHS_VideoCombine, KSamplerAdvanced, VAEDecode, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, JWInteger, LoadImage, CLIPTextEncode, KSamplerAdvanced, JWInteger, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 14B+LightX2V 图生视频（工作室自用）_2027632357276131329.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2027632357276131329.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（25 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `Note`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `Note`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `JWInteger`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `JWInteger`
- `JWInteger`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`CLIPTextEncode`、`VAELoader`、`WanImageToVideo`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM`、`UNETLoader`、`PathchSageAttentionKJ`、`CLIPLoader`、`VHS_VideoCombine`、`KSamplerAdvanced`、`VAEDecode`、`LoraLoaderModelOnly`、`JWInteger`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
