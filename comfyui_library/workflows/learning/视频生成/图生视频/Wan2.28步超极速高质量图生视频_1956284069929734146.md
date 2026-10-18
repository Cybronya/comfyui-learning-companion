---
key: 视频生成/图生视频/Wan2.28步超极速高质量图生视频_1956284069929734146.json
name: Wan2.28步超极速高质量图生视频_1956284069929734146.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.28步超极速高质量图生视频_1956284069929734146.json
hash: cfd06bbadeb2a2f1
coverage: 0.961538
learned_at: 2026-10-15 22:31:12
nodes: [ModelSamplingSD3, VAEDecode, LayerUtility: PurgeVRAM, CLIPTextEncode, PreviewImage, WanImageToVideo, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, CLIPTextEncode, CLIPLoader, VAELoader, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, JWInteger, JWInteger, JWInteger, UNETLoader, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, KSamplerAdvanced, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.28步超极速高质量图生视频_1956284069929734146.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956284069929734146.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（26 个）：
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `WanImageToVideo`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（25/26）

**有卡**：`ModelSamplingSD3`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`CLIPTextEncode`、`WanImageToVideo`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`LoadImage`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`JWInteger`、`UNETLoader`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
