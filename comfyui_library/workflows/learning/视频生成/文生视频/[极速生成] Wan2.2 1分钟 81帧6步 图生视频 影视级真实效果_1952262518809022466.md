---
key: 视频生成/文生视频/[极速生成] Wan2.2 1分钟 81帧6步 图生视频 影视级真实效果_1952262518809022466.json
name: [极速生成] Wan2.2 1分钟 81帧6步 图生视频 影视级真实效果_1952262518809022466.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1952262518809022466.json
hash: a0243a15bd5934ee
coverage: 1
learned_at: 2026-10-15 22:43:38
nodes: [VAELoader, LoadImage, WanImageToVideo, JWInteger, CLIPLoader, PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, KSamplerAdvanced, KSamplerAdvanced, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, VAEDecode, VHS_VideoCombine, JWInteger, JWInteger, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/[极速生成] Wan2.2 1分钟 81帧6步 图生视频 影视级真实效果_1952262518809022466.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1952262518809022466.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（23 个）：
- `VAELoader`
- `LoadImage`
- `WanImageToVideo`
- `JWInteger`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`VAELoader`、`LoadImage`、`WanImageToVideo`、`JWInteger`、`CLIPLoader`、`PathchSageAttentionKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
