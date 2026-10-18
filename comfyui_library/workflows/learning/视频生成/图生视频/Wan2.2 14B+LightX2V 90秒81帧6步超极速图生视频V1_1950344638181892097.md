---
key: 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1950344638181892097.json
name: Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1950344638181892097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1950344638181892097.json
hash: a9da2b7318db4e7c
coverage: 0.892857
learned_at: 2026-10-15 22:30:54
nodes: [CLIPTextEncode, VAELoader, Note, ModelSamplingSD3, LayerUtility: PurgeVRAM, UNETLoader, PathchSageAttentionKJ, CLIPLoader, ModelSamplingSD3, VHS_VideoCombine, KSamplerAdvanced, VAEDecode, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, LayerUtility: PurgeVRAM, JWInteger, Note, WanImageToVideo, JWInteger, MathExpression|pysssss, CLIPTextEncode, LoadImagesFromURL, LoadImage, Primitive integer [Crystools], Note]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1950344638181892097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950344638181892097.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（28 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `Note`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
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
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `JWInteger`
- `Note`
- `WanImageToVideo`
- `JWInteger`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `LoadImagesFromURL`
- `LoadImage`
- `Primitive integer [Crystools]`
- `Note`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（25/28）

**有卡**：`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM`、`UNETLoader`、`PathchSageAttentionKJ`、`CLIPLoader`、`VHS_VideoCombine`、`KSamplerAdvanced`、`VAEDecode`、`LoraLoaderModelOnly`、`JWInteger`、`WanImageToVideo`、`MathExpression|pysssss`、`LoadImagesFromURL`、`LoadImage`、`Primitive integer [Crystools]`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
