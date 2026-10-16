---
key: 视频生成/图生视频/（自用）Wan2.2高质量图生视频工作流81帧50秒_1952579457632669698.json
name: （自用）Wan2.2高质量图生视频工作流81帧50秒_1952579457632669698.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952579457632669698.json
hash: 0e9c3e714e9e28c0
coverage: 0.90625
learned_at: 2026-10-15 22:31:02
nodes: [Note, LayerUtility: PurgeVRAM, PathchSageAttentionKJ, ModelSamplingSD3, JWInteger, JWInteger, LayerUtility: PurgeVRAM, JWInteger, CLIPLoader, WanImageToVideo, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, VAELoader, VAEDecode, VAELoader, LoadLatent, KSamplerAdvanced, SaveLatent, VHS_VideoCombine, LoadImage, SaveImage, UNETLoader, Note, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/（自用）Wan2.2高质量图生视频工作流81帧50秒_1952579457632669698.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952579457632669698.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（32 个）：
- `Note`
- `LayerUtility: PurgeVRAM`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `JWInteger`
- `JWInteger`
- `LayerUtility: PurgeVRAM`
- `JWInteger`
- `CLIPLoader`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `VAELoader`
- `LoadLatent`
- `KSamplerAdvanced` ★核心
- `SaveLatent`
- `VHS_VideoCombine`
- `LoadImage`
- `SaveImage`
- `UNETLoader` ★核心
- `Note`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（29/32）

**有卡**：`LayerUtility: PurgeVRAM`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`JWInteger`、`CLIPLoader`、`WanImageToVideo`、`CLIPTextEncode`、`KSamplerAdvanced`、`VAELoader`、`VAEDecode`、`LoadLatent`、`SaveLatent`、`VHS_VideoCombine`、`LoadImage`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
