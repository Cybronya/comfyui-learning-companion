---
key: 视频生成/图生视频/Wan2.2首尾帧视频加速版_1961125749866565634.json
name: Wan2.2首尾帧视频加速版_1961125749866565634.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2首尾帧视频加速版_1961125749866565634.json
hash: 234cf850a5875415
coverage: 0.965517
learned_at: 2026-10-15 22:31:28
nodes: [ModelSamplingSD3, ModelSamplingSD3, ImageScale, ImageScale, easy int, easy int, easy int, VHS_VideoCombine, UnetLoaderGGUF, CLIPLoader, UnetLoaderGGUF, VAELoader, Power Lora Loader (rgthree), Power Lora Loader (rgthree), CLIPTextEncode, CLIPTextEncode, WanVideoNAG, WanFirstLastFrameToVideo, KSamplerAdvanced, VAEDecode, WanVideoNAG, PathchSageAttentionKJ, PathchSageAttentionKJ, LoadImage, PrimitiveStringMultiline, LoadImage, ImageResizeKJ, GetImageSize, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2首尾帧视频加速版_1961125749866565634.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1961125749866565634.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（29 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ImageScale`
- `ImageScale`
- `easy int`
- `easy int`
- `easy int`
- `VHS_VideoCombine`
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `UnetLoaderGGUF` ★核心
- `VAELoader`
- `Power Lora Loader (rgthree)`
- `Power Lora Loader (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanVideoNAG`
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `WanVideoNAG`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LoadImage`
- `ImageResizeKJ`
- `GetImageSize`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（28/29）

**有卡**：`ModelSamplingSD3`、`ImageScale`、`easy int`、`VHS_VideoCombine`、`UnetLoaderGGUF`、`CLIPLoader`、`VAELoader`、`Power Lora Loader (rgthree)`、`CLIPTextEncode`、`WanVideoNAG`、`WanFirstLastFrameToVideo`、`KSamplerAdvanced`、`VAEDecode`、`PathchSageAttentionKJ`、`LoadImage`、`ImageResizeKJ`、`GetImageSize`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、Power Lora Loader (rgthree)、GetImageSize
