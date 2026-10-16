---
key: 视频生成/图生视频/Smooth Mix i2V v2.0图生视频8步加速版_2056759291427778562.json
name: Smooth Mix i2V v2.0图生视频8步加速版_2056759291427778562.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2056759291427778562.json
hash: 81bc37e04d0c89f6
coverage: 0.68
learned_at: 2026-10-15 22:38:05
nodes: [ModelSamplingSD3, ModelSamplingSD3, VAEDecode, CLIPTextEncode, VHS_VideoCombine, UNETLoader, LoraLoaderModelOnly, UNETLoader, Note, Reroute, WanImageToVideo, Reroute, Reroute, VAELoader, Reroute, Reroute, Reroute, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, MarkdownNote, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Smooth Mix i2V v2.0图生视频8步加速版_2056759291427778562.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2056759291427778562.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Note`
- `Reroute`
- `WanImageToVideo`
- `Reroute`
- `Reroute`
- `VAELoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `MarkdownNote`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **68%**（17/25）

**有卡**：`ModelSamplingSD3`、`VAEDecode`、`CLIPTextEncode`、`VHS_VideoCombine`、`UNETLoader`、`LoraLoaderModelOnly`、`WanImageToVideo`、`VAELoader`、`KSamplerAdvanced`、`CLIPLoader`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
