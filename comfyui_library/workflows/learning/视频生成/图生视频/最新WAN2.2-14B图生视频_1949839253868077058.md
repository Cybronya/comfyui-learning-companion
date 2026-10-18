---
key: 视频生成/图生视频/最新WAN2.2-14B图生视频_1949839253868077058.json
name: 最新WAN2.2-14B图生视频_1949839253868077058.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/最新WAN2.2-14B图生视频_1949839253868077058.json
hash: 6784134466bdf5ae
coverage: 1
learned_at: 2026-10-15 22:30:50
nodes: [VAEDecode, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, VHS_VideoCombine, ImageUpscaleWithModel, CLIPLoader, VAELoader, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, UNETLoader, UpscaleModelLoader, PathchSageAttentionKJ, CLIPTextEncode, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, RHHiddenNodes, Int, Int, Int, WanImageToVideo]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/最新WAN2.2-14B图生视频_1949839253868077058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1949839253868077058.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageUpscaleWithModel`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UpscaleModelLoader`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `RHHiddenNodes`
- `Int`
- `Int`
- `Int`
- `WanImageToVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`ImageUpscaleWithModel`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`UNETLoader`、`UpscaleModelLoader`、`LoadImage`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`RHHiddenNodes`、`Int`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
