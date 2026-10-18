---
key: 视频生成/图生视频/Wan2.2 14B+LightX2V 12步超极速高质量图生视频V1_1949874955704033281.json
name: Wan2.2 14B+LightX2V 12步超极速高质量图生视频V1_1949874955704033281.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 14B+LightX2V 12步超极速高质量图生视频V1_1949874955704033281.json
hash: f3a5c5e80e2dabf7
coverage: 0.92
learned_at: 2026-10-15 22:30:50
nodes: [CLIPTextEncode, VAELoader, Note, LoadImage, VAEDecode, ModelSamplingSD3, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CLIPTextEncode, Note, UNETLoader, PathchSageAttentionKJ, CLIPLoader, ModelSamplingSD3, VHS_VideoCombine, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, KSamplerAdvanced, KSamplerAdvanced, WanImageToVideo, JWInteger, JWInteger, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 14B+LightX2V 12步超极速高质量图生视频V1_1949874955704033281.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1949874955704033281.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（25 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `Note`
- `LoadImage`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `Note`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `JWInteger`
- `JWInteger`
- `JWInteger`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`CLIPTextEncode`、`VAELoader`、`LoadImage`、`VAEDecode`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM`、`UNETLoader`、`PathchSageAttentionKJ`、`CLIPLoader`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`WanImageToVideo`、`JWInteger`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
