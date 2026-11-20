---
key: 平台全量/Wan2.2-Remix-首尾帧视频_1988211191065526274.json
name: Wan2.2-Remix-首尾帧视频_1988211191065526274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-Remix-首尾帧视频_1988211191065526274.json
hash: 9ea4ca4225761bd3
coverage: 1
learned_at: 2026-11-14 01:05:59
nodes: [CLIPLoader, INTConstant, VAELoader, UNETLoader, ImageResizeKJv2, INTConstant, INTConstant, SimpleMath+, ImageResizeKJv2, LoadImage, LoadImage, UNETLoader, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, CLIPVisionLoader, CLIPVisionEncode, CLIPVisionEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, WanFirstLastFrameToVideo, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 平台全量/Wan2.2-Remix-首尾帧视频_1988211191065526274.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-Remix-首尾帧视频_1988211191065526274.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `CLIPLoader`
- `INTConstant`
- `VAELoader`
- `UNETLoader` ★核心
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanFirstLastFrameToVideo`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`CLIPLoader`、`INTConstant`、`VAELoader`、`UNETLoader`、`ImageResizeKJv2`、`SimpleMath+`、`LoadImage`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`CLIPVisionLoader`、`CLIPVisionEncode`、`WanFirstLastFrameToVideo`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerAdvanced
