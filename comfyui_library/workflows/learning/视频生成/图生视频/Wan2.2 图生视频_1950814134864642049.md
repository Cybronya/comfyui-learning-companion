---
key: 视频生成/图生视频/Wan2.2 图生视频_1950814134864642049.json
name: Wan2.2 图生视频_1950814134864642049.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 图生视频_1950814134864642049.json
hash: 90a17b96fb5759f2
coverage: 1
learned_at: 2026-10-15 22:30:56
nodes: [KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, UNETLoader, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, LoadImage, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, WanImageToVideo]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 图生视频_1950814134864642049.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950814134864642049.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（20 个）：
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `WanImageToVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`KSamplerAdvanced`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`LoadImage`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
