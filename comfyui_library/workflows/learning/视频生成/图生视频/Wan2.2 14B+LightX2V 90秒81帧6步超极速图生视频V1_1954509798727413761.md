---
key: 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1954509798727413761.json
name: Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1954509798727413761.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1954509798727413761.json
hash: 994c48f59c9d2a30
coverage: 0.92
learned_at: 2026-10-15 22:31:06
nodes: [Note, PathchSageAttentionKJ, VHS_VideoCombine, VAEDecode, UNETLoader, LoraLoaderModelOnly, WanImageToVideo, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, Note, VAELoader, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CLIPTextEncode, LoadImage, JWInteger, JWInteger, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1954509798727413761.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1954509798727413761.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（25 个）：
- `Note`
- `PathchSageAttentionKJ`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanImageToVideo`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `Note`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `JWInteger`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`PathchSageAttentionKJ`、`VHS_VideoCombine`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`WanImageToVideo`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSamplerAdvanced`、`LayerUtility: PurgeVRAM`、`LoadImage`、`JWInteger`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
