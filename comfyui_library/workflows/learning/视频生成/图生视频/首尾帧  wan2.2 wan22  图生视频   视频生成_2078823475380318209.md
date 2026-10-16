---
key: 视频生成/图生视频/首尾帧  wan2.2 wan22  图生视频   视频生成_2078823475380318209.json
name: 首尾帧  wan2.2 wan22  图生视频   视频生成_2078823475380318209.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2078823475380318209.json
hash: 6596e12e1105d38d
coverage: 1
learned_at: 2026-10-15 22:41:56
nodes: [CLIPTextEncode, KSamplerAdvanced, ImageResizeKJv2, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, CLIPLoader, SimpleMath+, VAELoader, INTConstant, ImageResizeKJv2, CLIPTextEncode, LoadImage, LoadImage, WanFirstMiddleLastFrameToVideo, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, VAEDecode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧  wan2.2 wan22  图生视频   视频生成_2078823475380318209.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2078823475380318209.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `SimpleMath+`
- `VAELoader`
- `INTConstant`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `WanFirstMiddleLastFrameToVideo`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
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

覆盖率 **100%**（25/25）

**有卡**：`CLIPTextEncode`、`KSamplerAdvanced`、`ImageResizeKJv2`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPLoader`、`SimpleMath+`、`VAELoader`、`INTConstant`、`LoadImage`、`WanFirstMiddleLastFrameToVideo`、`ModelSamplingSD3`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
