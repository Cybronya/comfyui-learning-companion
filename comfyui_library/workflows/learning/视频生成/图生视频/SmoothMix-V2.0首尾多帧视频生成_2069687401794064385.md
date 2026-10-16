---
key: 视频生成/图生视频/SmoothMix-V2.0首尾多帧视频生成_2069687401794064385.json
name: SmoothMix-V2.0首尾多帧视频生成_2069687401794064385.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2069687401794064385.json
hash: bc2fd257c6e58191
coverage: 1
learned_at: 2026-10-15 22:40:32
nodes: [CLIPLoader, INTConstant, INTConstant, INTConstant, ModelSamplingSD3, ModelPatchTorchSettings, ModelPatchTorchSettings, UNETLoader, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, WanFirstMiddleLastFrameToVideo, KSamplerAdvanced, SimpleMath+, ModelSamplingSD3, VAELoader, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/SmoothMix-V2.0首尾多帧视频生成_2069687401794064385.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2069687401794064385.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（29 个）：
- `CLIPLoader`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanFirstMiddleLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `SimpleMath+`
- `ModelSamplingSD3`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`CLIPLoader`、`INTConstant`、`ModelSamplingSD3`、`ModelPatchTorchSettings`、`UNETLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`CLIPTextEncode`、`ImageResizeKJv2`、`WanFirstMiddleLastFrameToVideo`、`SimpleMath+`、`VAELoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
