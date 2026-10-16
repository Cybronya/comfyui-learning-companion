---
key: 视频生成/图生视频/Wan2.2  图生视频_2018573357712674817.json
name: Wan2.2  图生视频_2018573357712674817.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2018573357712674817.json
hash: aa877cf82eaa0fd9
coverage: 0.896552
learned_at: 2026-10-15 22:34:58
nodes: [WanImageToVideo, UNETLoader, PathchSageAttentionKJ, VAEDecode, PathchSageAttentionKJ, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, JWInteger, PreviewAny, MathExpression|pysssss, VHS_VideoCombine, LoraLoaderModelOnly, JWInteger, JWInteger, CLIPTextEncode, LayerUtility: PurgeVRAM, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, Note, UNETLoader, CLIPLoader, Note, LoadImage, VAELoader, Int, CLIPTextEncode, Int]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2  图生视频_2018573357712674817.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2018573357712674817.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（29 个）：
- `WanImageToVideo`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `JWInteger`
- `PreviewAny`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Note`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Note`
- `LoadImage`
- `VAELoader`
- `Int`
- `CLIPTextEncode` ★核心
- `Int`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`WanImageToVideo`、`UNETLoader`、`PathchSageAttentionKJ`、`VAEDecode`、`LoraLoaderModelOnly`、`LayerUtility: PurgeVRAM`、`JWInteger`、`MathExpression|pysssss`、`VHS_VideoCombine`、`CLIPTextEncode`、`KSamplerAdvanced`、`ModelSamplingSD3`、`CLIPLoader`、`LoadImage`、`VAELoader`、`Int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
