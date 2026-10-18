---
key: 视频生成/图生视频/Smooth Mix i2V v2.0首尾帧生视频8步加速版_2038172701340213249.json
name: Smooth Mix i2V v2.0首尾帧生视频8步加速版_2038172701340213249.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Smooth Mix i2V v2.0首尾帧生视频8步加速版_2038172701340213249.json
hash: b7b75011c36611c7
coverage: 0.730769
learned_at: 2026-10-15 22:36:00
nodes: [ModelSamplingSD3, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, UNETLoader, LoraLoaderModelOnly, UNETLoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, VAELoader, CLIPTextEncode, ImageResize+, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, CLIPTextEncode, Note, WanFirstLastFrameToVideo]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Smooth Mix i2V v2.0首尾帧生视频8步加速版_2038172701340213249.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038172701340213249.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（26 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ImageResize+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Note`
- `WanFirstLastFrameToVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **73%**（19/26）

**有卡**：`ModelSamplingSD3`、`VAEDecode`、`VHS_VideoCombine`、`UNETLoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ImageResize+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`WanFirstLastFrameToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
