---
key: 视频生成/图生视频/首尾帧图生视频社区模型Smooth Mix i2V v2.0工作流_2050542650729746434.json
name: 首尾帧图生视频社区模型Smooth Mix i2V v2.0工作流_2050542650729746434.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2050542650729746434.json
hash: b5faedf40d75493e
coverage: 1
learned_at: 2026-10-15 22:37:18
nodes: [CLIPLoader, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, VAELoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, ImageResize+, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, WanFirstLastFrameToVideo, VAEDecode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧图生视频社区模型Smooth Mix i2V v2.0工作流_2050542650729746434.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2050542650729746434.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（19 个）：
- `CLIPLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResize+`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `WanFirstLastFrameToVideo`
- `VAEDecode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`CLIPLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResize+`、`CLIPTextEncode`、`WanFirstLastFrameToVideo`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
