---
key: 视频生成/文生视频/Wan2.2 视频生成 图生视频_文生视频工作流_1950807946525614081.json
name: Wan2.2 视频生成 图生视频_文生视频工作流_1950807946525614081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 视频生成 图生视频_文生视频工作流_1950807946525614081.json
hash: d36dc8e262184ced
coverage: 1
learned_at: 2026-10-15 22:43:37
nodes: [CLIPTextEncode, WanImageToVideo, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, ModelSamplingSD3, easy cleanGpuUsed, easy cleanGpuUsed, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, ImageResizeKJv2, LoadImage, UNETLoader, UNETLoader, CLIPLoader, VAELoader]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2 视频生成 图生视频_文生视频工作流_1950807946525614081.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950807946525614081.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（17 个）：
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`CLIPTextEncode`、`WanImageToVideo`、`ModelSamplingSD3`、`KSamplerAdvanced`、`easy cleanGpuUsed`、`VAEDecode`、`VHS_VideoCombine`、`ImageResizeKJv2`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ImageResizeKJv2
