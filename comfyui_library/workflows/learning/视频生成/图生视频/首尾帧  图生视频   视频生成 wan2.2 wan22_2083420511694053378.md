---
key: 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2083420511694053378.json
name: 首尾帧  图生视频   视频生成 wan2.2 wan22_2083420511694053378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2083420511694053378.json
hash: b884dc5ec3f2b8a3
coverage: 1
learned_at: 2026-10-16 19:17:45
nodes: [UNETLoader, UNETLoader, VHS_VideoCombine, ImageResizeKJv2, LoadImage, LoadImage, ImageResizeKJv2, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, INTConstant, VAELoader, CLIPLoader, SimpleMath+, CLIPTextEncode, CLIPTextEncode, WanFirstMiddleLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2083420511694053378.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2083420511694053378.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `INTConstant`
- `VAELoader`
- `CLIPLoader`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanFirstMiddleLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`UNETLoader`、`VHS_VideoCombine`、`ImageResizeKJv2`、`LoadImage`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`INTConstant`、`VAELoader`、`CLIPLoader`、`SimpleMath+`、`CLIPTextEncode`、`WanFirstMiddleLastFrameToVideo`、`KSamplerAdvanced`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
