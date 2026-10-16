---
key: 视频生成/图生视频/Remix Wan2.2-i2V 6步极速版版-官方版_2018238424574070785.json
name: Remix Wan2.2-i2V 6步极速版版-官方版_2018238424574070785.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2018238424574070785.json
hash: e105f2a14cfa91d6
coverage: 0.944444
learned_at: 2026-10-15 22:34:55
nodes: [CLIPLoader, WanImageToVideo, ModelSamplingSD3, VAELoader, KSamplerAdvanced, VAEDecode, CLIPTextEncode, LoadImage, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, VHS_VideoCombine, ModelSamplingSD3, UNETLoader, UNETLoader, UNETLoader, UNETLoader, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Remix Wan2.2-i2V 6步极速版版-官方版_2018238424574070785.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2018238424574070785.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（18 个）：
- `CLIPLoader`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MarkdownNote`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`CLIPLoader`、`WanImageToVideo`、`ModelSamplingSD3`、`VAELoader`、`KSamplerAdvanced`、`VAEDecode`、`CLIPTextEncode`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ModelSamplingSD3
