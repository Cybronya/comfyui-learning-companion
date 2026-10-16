---
key: 视频生成/图生视频/通义万相wan2.2图生视频（lightx2v加速6步）_1949968677410136066.json
name: 通义万相wan2.2图生视频（lightx2v加速6步）_1949968677410136066.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1949968677410136066.json
hash: 6fc26a788789bd67
coverage: 0.92
learned_at: 2026-10-15 22:30:50
nodes: [CLIPTextEncode, VAELoader, Note, WanImageToVideo, ModelSamplingSD3, PathchSageAttentionKJ, CLIPLoader, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, Note, UNETLoader, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, VAEDecode, CLIPTextEncode, LoadImage, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/通义万相wan2.2图生视频（lightx2v加速6步）_1949968677410136066.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1949968677410136066.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `Note`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `Note`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`CLIPTextEncode`、`VAELoader`、`WanImageToVideo`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CLIPLoader`、`KSamplerAdvanced`、`UNETLoader`、`LoraLoaderModelOnly`、`LayerUtility: PurgeVRAM`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`VAEDecode`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
