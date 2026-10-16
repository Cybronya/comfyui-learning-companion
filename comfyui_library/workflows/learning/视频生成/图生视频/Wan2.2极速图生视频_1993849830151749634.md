---
key: 视频生成/图生视频/Wan2.2极速图生视频_1993849830151749634.json
name: Wan2.2极速图生视频_1993849830151749634.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1993849830151749634.json
hash: fab2252750b9b151
coverage: 1
learned_at: 2026-10-15 22:33:19
nodes: [VAELoader, WanImageToVideo, ModelSamplingSD3, LayerUtility: PurgeVRAM, UNETLoader, PathchSageAttentionKJ, CLIPLoader, ModelSamplingSD3, KSamplerAdvanced, VAEDecode, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, LayerUtility: PurgeVRAM, CLIPTextEncode, LoadImage, JWInteger, JWInteger, JWInteger, VHS_VideoCombine, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2极速图生视频_1993849830151749634.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1993849830151749634.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（23 个）：
- `VAELoader`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`VAELoader`、`WanImageToVideo`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM`、`UNETLoader`、`PathchSageAttentionKJ`、`CLIPLoader`、`KSamplerAdvanced`、`VAEDecode`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LoadImage`、`JWInteger`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
