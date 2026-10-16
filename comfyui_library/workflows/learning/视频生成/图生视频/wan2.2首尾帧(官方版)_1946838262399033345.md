---
key: 视频生成/图生视频/wan2.2首尾帧(官方版)_1946838262399033345.json
name: wan2.2首尾帧(官方版)_1946838262399033345.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1946838262399033345.json
hash: a0e4864dcdfac8b3
coverage: 1
learned_at: 2026-10-15 22:30:44
nodes: [ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAEDecode, VHS_VideoCombine, CLIPVisionEncode, CLIPVisionLoader, VAELoader, CLIPVisionEncode, ImageScale, CLIPTextEncode, UNETLoader, CLIPTextEncode, ImageScale, WanFirstLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, RIFE VFI, VHS_VideoCombine, LoadImage, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, Text, Text, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2首尾帧(官方版)_1946838262399033345.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1946838262399033345.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（26 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPVisionEncode`
- `ImageScale`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ImageScale`
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `RIFE VFI`
- `VHS_VideoCombine`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text`
- `Text`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（26/26）

**有卡**：`ModelSamplingSD3`、`CLIPLoader`、`VAEDecode`、`VHS_VideoCombine`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`ImageScale`、`CLIPTextEncode`、`UNETLoader`、`WanFirstLastFrameToVideo`、`KSamplerAdvanced`、`RIFE VFI`、`LoadImage`、`LoraLoaderModelOnly`、`Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
