---
key: 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1949877835465932801.json
name: Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1949877835465932801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1949877835465932801.json
hash: 6b283ad82985aea5
coverage: 0.92
learned_at: 2026-10-15 22:42:57
nodes: [CLIPTextEncode, VAELoader, Note, LoadImage, WanImageToVideo, ModelSamplingSD3, LayerUtility: PurgeVRAM, Note, UNETLoader, PathchSageAttentionKJ, CLIPLoader, ModelSamplingSD3, VHS_VideoCombine, KSamplerAdvanced, VAEDecode, JWInteger, JWInteger, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, CLIPTextEncode, LoraLoaderModelOnly, KSamplerAdvanced, LayerUtility: PurgeVRAM, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1949877835465932801.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1949877835465932801.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（25 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `Note`
- `LoadImage`
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

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`CLIPTextEncode`、`VAELoader`、`LoadImage`、`WanImageToVideo`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM`、`UNETLoader`、`PathchSageAttentionKJ`、`CLIPLoader`、`VHS_VideoCombine`、`KSamplerAdvanced`、`VAEDecode`、`JWInteger`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
