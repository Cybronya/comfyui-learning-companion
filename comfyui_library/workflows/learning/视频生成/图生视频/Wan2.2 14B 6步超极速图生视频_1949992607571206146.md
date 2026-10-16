---
key: 视频生成/图生视频/Wan2.2 14B 6步超极速图生视频_1949992607571206146.json
name: Wan2.2 14B 6步超极速图生视频_1949992607571206146.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1949992607571206146.json
hash: feaaa9c32ff03ea6
coverage: 0.892857
learned_at: 2026-10-15 22:30:50
nodes: [LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, LayerUtility: PurgeVRAM, WanImageToVideo, Note, Note, VAELoader, Note, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, Int, Int, Int, Int, Int, LoadImage, VHS_VideoCombine, CLIPTextEncode, CLIPLoader, CLIPTextEncode, LayerUtility: PurgeVRAM, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 14B 6步超极速图生视频_1949992607571206146.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1949992607571206146.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（28 个）：
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `WanImageToVideo`
- `Note`
- `Note`
- `VAELoader`
- `Note`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `LoadImage`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（25/28）

**有卡**：`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`UNETLoader`、`LayerUtility: PurgeVRAM`、`WanImageToVideo`、`VAELoader`、`KSamplerAdvanced`、`Int`、`LoadImage`、`VHS_VideoCombine`、`CLIPTextEncode`、`CLIPLoader`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
