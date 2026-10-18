---
key: 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063714093613281281.json
name: 首尾帧  多帧  视频生成 wan2.2 wan22_2063714093613281281.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063714093613281281.json
hash: 70b27a06e7c00a4a
coverage: 0.878788
learned_at: 2026-10-15 22:39:17
nodes: [ImageResizeKJv2, ModelPatchTorchSettings, VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, GetNode, GetNode, ImageResizeKJv2, SetNode, INTConstant, SimpleMath+, CLIPTextEncode, WanFirstMiddleLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, UNETLoader, ImageResizeKJv2, LoadImage, LoadImage, LoadImage, INTConstant, INTConstant, SetNode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063714093613281281.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063714093613281281.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `ImageResizeKJv2`
- `ModelPatchTorchSettings`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `INTConstant`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `WanFirstMiddleLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`ImageResizeKJv2`、`ModelPatchTorchSettings`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`INTConstant`、`SimpleMath+`、`CLIPTextEncode`、`WanFirstMiddleLastFrameToVideo`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
