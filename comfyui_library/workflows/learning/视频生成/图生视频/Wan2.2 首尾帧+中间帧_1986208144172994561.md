---
key: 视频生成/图生视频/Wan2.2 首尾帧+中间帧_1986208144172994561.json
name: Wan2.2 首尾帧+中间帧_1986208144172994561.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 首尾帧+中间帧_1986208144172994561.json
hash: 2927e034e06a1529
coverage: 1
learned_at: 2026-10-15 22:32:54
nodes: [INTConstant, ImageScaleBy, ImageScaleBy, ImageConcatMulti, CLIPLoader, KSamplerAdvanced, INTConstant, ImageScaleBy, KSamplerAdvanced, VAELoader, UNETLoader, UNETLoader, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, Text, WanFirstMiddleLastFrameToVideo]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 首尾帧+中间帧_1986208144172994561.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1986208144172994561.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `INTConstant`
- `ImageScaleBy`
- `ImageScaleBy`
- `ImageConcatMulti`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `ImageScaleBy`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Text`
- `WanFirstMiddleLastFrameToVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `5`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`INTConstant`、`ImageScaleBy`、`ImageConcatMulti`、`CLIPLoader`、`KSamplerAdvanced`、`VAELoader`、`UNETLoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`、`Text`、`WanFirstMiddleLastFrameToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
