---
key: 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2076181570117005314.json
name: 首尾帧  图生视频   视频生成 wan2.2 wan22_2076181570117005314.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2076181570117005314.json
hash: dc1f08ce112cecb3
coverage: 1
learned_at: 2026-10-15 22:41:29
nodes: [CLIPTextEncode, WanFirstMiddleLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, SimpleMath+, VAELoader, INTConstant, VAEDecode, VHS_VideoCombine, LoadImage, LoadImage, ImageResizeKJv2, ImageResizeKJv2, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2076181570117005314.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2076181570117005314.json`

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
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `SimpleMath+`
- `VAELoader`
- `INTConstant`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`CLIPTextEncode`、`WanFirstMiddleLastFrameToVideo`、`KSamplerAdvanced`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`CLIPLoader`、`SimpleMath+`、`VAELoader`、`INTConstant`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`、`ImageResizeKJv2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
