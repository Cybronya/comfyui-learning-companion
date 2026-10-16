---
key: 视频生成/图生视频/Wan2.2 14B+Teacache+Sage 2.5图生视频加速版+视频放大_1950019885810278402.json
name: Wan2.2 14B+Teacache+Sage 2.5图生视频加速版+视频放大_1950019885810278402.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950019885810278402.json
hash: 09025a4f82b9b08a
coverage: 1
learned_at: 2026-10-15 22:30:51
nodes: [UNETLoader, PathchSageAttentionKJ, VAELoader, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, TeaCache, TeaCache, VAEDecode, UpscaleModelLoader, ImageUpscaleWithModel, LoadImage, WanImageToVideo, VHS_VideoCombine, RIFE VFI, VHS_VideoCombine, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 14B+Teacache+Sage 2.5图生视频加速版+视频放大_1950019885810278402.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950019885810278402.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（24 个）：
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `VAELoader`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `TeaCache`
- `TeaCache`
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `LoadImage`
- `WanImageToVideo`
- `VHS_VideoCombine`
- `RIFE VFI`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`UNETLoader`、`PathchSageAttentionKJ`、`VAELoader`、`ModelSamplingSD3`、`CLIPLoader`、`CLIPTextEncode`、`KSamplerAdvanced`、`LayerUtility: PurgeVRAM`、`TeaCache`、`VAEDecode`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`LoadImage`、`WanImageToVideo`、`VHS_VideoCombine`、`RIFE VFI`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ImageUpscaleWithModel
