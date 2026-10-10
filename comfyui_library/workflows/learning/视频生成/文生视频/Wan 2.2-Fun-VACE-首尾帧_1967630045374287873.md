---
key: 视频生成/文生视频/Wan 2.2-Fun-VACE-首尾帧_1967630045374287873.json
name: Wan 2.2-Fun-VACE-首尾帧_1967630045374287873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.2-Fun-VACE-首尾帧_1967630045374287873.json
hash: c5c57ad16e30ab4c
coverage: 1
learned_at: 2026-10-10 23:06:12
nodes: [TrimVideoLatent, VAEDecode, CLIPTextEncode, VHS_VideoCombine, WanVaceToVideo, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, INTConstant, ImageResizeKJv2, GetImageSizeAndCount, WanVideoVACEStartToEndFrame, INTConstant, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, LoadImage, ImageResizeKJv2, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan 2.2-Fun-VACE-首尾帧_1967630045374287873.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan 2.2-Fun-VACE-首尾帧_1967630045374287873.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `INTConstant`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `WanVideoVACEStartToEndFrame`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ImageResizeKJv2`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`TrimVideoLatent`、`VAEDecode`、`CLIPTextEncode`、`VHS_VideoCombine`、`WanVaceToVideo`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`INTConstant`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`WanVideoVACEStartToEndFrame`、`LoraLoaderModelOnly`、`UNETLoader`、`KSamplerAdvanced`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
