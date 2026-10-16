---
key: 视频生成/文生视频/【美女跳舞】Wan2.2 14B+LightX2V 图片生成视频_1955111888410460162.json
name: 【美女跳舞】Wan2.2 14B+LightX2V 图片生成视频_1955111888410460162.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1955111888410460162.json
hash: 481ee976d9c6684c
coverage: 1
learned_at: 2026-10-15 22:43:39
nodes: [CLIPTextEncode, WanImageToVideo, ModelSamplingSD3, LayerUtility: PurgeVRAM, PathchSageAttentionKJ, ModelSamplingSD3, VHS_VideoCombine, KSamplerAdvanced, VAEDecode, PathchSageAttentionKJ, KSamplerAdvanced, LayerUtility: PurgeVRAM, JWInteger, JWInteger, VAELoader, JWInteger, LoadImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, LoraLoader, UNETLoader, CLIPLoader, LoraLoader]
patterns: [lora]
missing: []
parameters: {"cfg": 6, "denoise": "simple", "lora_name": "dbc.safetensors", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed", "strength_clip": 1, "strength_model": 1}
---

# 视频生成/文生视频/【美女跳舞】Wan2.2 14B+LightX2V 图片生成视频_1955111888410460162.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1955111888410460162.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（25 个）：
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `JWInteger`
- `JWInteger`
- `VAELoader`
- `JWInteger`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoader` ★核心

**识别到的模式**：lora

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`
- `lora_name` = `dbc.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`CLIPTextEncode`、`WanImageToVideo`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM`、`PathchSageAttentionKJ`、`VHS_VideoCombine`、`KSamplerAdvanced`、`VAEDecode`、`JWInteger`、`VAELoader`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`LoraLoader`、`CLIPLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
