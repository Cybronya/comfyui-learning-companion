---
key: 视频生成/图生视频/Smooth Mix i2V v2.0图生视频8步加速版_2026835055515017218.json
name: Smooth Mix i2V v2.0图生视频8步加速版_2026835055515017218.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Smooth Mix i2V v2.0图生视频8步加速版_2026835055515017218.json
hash: 16e88cd013fe1b35
coverage: 0.68
learned_at: 2026-10-15 22:35:14
nodes: [ModelSamplingSD3, ModelSamplingSD3, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, VHS_VideoCombine, UNETLoader, LoraLoaderModelOnly, UNETLoader, Note, LoadImage, Reroute, WanImageToVideo, Reroute, Reroute, VAELoader, Reroute, Reroute, Reroute, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, MarkdownNote, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Smooth Mix i2V v2.0图生视频8步加速版_2026835055515017218.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2026835055515017218.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Note`
- `LoadImage`
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

**有卡**：`ModelSamplingSD3`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`VHS_VideoCombine`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`WanImageToVideo`、`VAELoader`、`KSamplerAdvanced`、`CLIPLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
