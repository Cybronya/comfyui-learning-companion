---
key: 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2083124131020759041.json
name: 首尾帧  图生视频   视频生成 wan2.2 wan22_2083124131020759041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2083124131020759041.json
hash: ca3880196b3ebf68
coverage: 1
learned_at: 2026-10-16 19:17:45
nodes: [CLIPTextEncode, WanFirstMiddleLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, CLIPLoader, SimpleMath+, VAELoader, INTConstant, VAEDecode, VHS_VideoCombine, CLIPTextEncode, LoadImage, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, ImageResizeKJv2, ImageResizeKJv2]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2083124131020759041.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2083124131020759041.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `CLIPTextEncode` ★核心
- `WanFirstMiddleLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `SimpleMath+`
- `VAELoader`
- `INTConstant`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ImageResizeKJv2`
- `ImageResizeKJv2`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`CLIPTextEncode`、`WanFirstMiddleLastFrameToVideo`、`KSamplerAdvanced`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPLoader`、`SimpleMath+`、`VAELoader`、`INTConstant`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`、`ModelSamplingSD3`、`ImageResizeKJv2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
