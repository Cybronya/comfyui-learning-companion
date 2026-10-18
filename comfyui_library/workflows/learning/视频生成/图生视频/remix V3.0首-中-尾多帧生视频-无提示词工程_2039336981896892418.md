---
key: 视频生成/图生视频/remix V3.0首-中-尾多帧生视频-无提示词工程_2039336981896892418.json
name: remix V3.0首-中-尾多帧生视频-无提示词工程_2039336981896892418.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/remix V3.0首-中-尾多帧生视频-无提示词工程_2039336981896892418.json
hash: dfd5af8f86cef99f
coverage: 0.967742
learned_at: 2026-10-15 22:36:08
nodes: [CLIPTextEncode, VAEDecode, ModelSamplingSD3, ModelSamplingSD3, Seed (rgthree), INTConstant, INTConstant, KSamplerAdvanced, CLIPTextEncode, LatentFromBatch, VHS_VideoCombine, ImageResizeKJv2, INTConstant, WanFirstMiddleLastFrameToVideo, CLIPVisionEncode, CLIPVisionEncode, UNETLoader, UNETLoader, ImageResizeKJv2, CLIPVisionLoader, CLIPVisionEncode, ImageResizeKJv2, CLIPLoader, VAELoader, KSamplerAdvanced, PrimitiveStringMultiline, INTConstant, INTConstant, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/remix V3.0首-中-尾多帧生视频-无提示词工程_2039336981896892418.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2039336981896892418.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（31 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Seed (rgthree)`
- `INTConstant`
- `INTConstant`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `LatentFromBatch`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `INTConstant`
- `WanFirstMiddleLastFrameToVideo`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `ImageResizeKJv2`
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `PrimitiveStringMultiline`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（30/31）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`ModelSamplingSD3`、`Seed (rgthree)`、`INTConstant`、`KSamplerAdvanced`、`LatentFromBatch`、`VHS_VideoCombine`、`ImageResizeKJv2`、`WanFirstMiddleLastFrameToVideo`、`CLIPVisionEncode`、`UNETLoader`、`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
