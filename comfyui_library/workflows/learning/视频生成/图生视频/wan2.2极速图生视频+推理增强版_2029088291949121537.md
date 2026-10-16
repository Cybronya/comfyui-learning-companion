---
key: 视频生成/图生视频/wan2.2极速图生视频+推理增强版_2029088291949121537.json
name: wan2.2极速图生视频+推理增强版_2029088291949121537.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2029088291949121537.json
hash: 279a8fb005062640
coverage: 1
learned_at: 2026-10-15 22:35:21
nodes: [PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, UNETLoader, PathchSageAttentionKJ, VAELoader, LoraLoaderModelOnly, WanImageToVideo, KSamplerAdvanced, KSamplerAdvanced, JWInteger, JWInteger, LoraLoaderModelOnly, CLIPLoader, ModelSamplingSD3, ModelSamplingSD3, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LoadImage, CLIPTextEncode, VAEDecode, VHS_VideoCombine, FL_RIFE, SimpleMath+, JWInteger, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2极速图生视频+推理增强版_2029088291949121537.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2029088291949121537.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（27 个）：
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `JWInteger`
- `JWInteger`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `FL_RIFE`
- `SimpleMath+`
- `JWInteger`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`PathchSageAttentionKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`VAELoader`、`WanImageToVideo`、`KSamplerAdvanced`、`JWInteger`、`CLIPLoader`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM`、`LoadImage`、`VAEDecode`、`VHS_VideoCombine`、`FL_RIFE`、`SimpleMath+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
