---
key: 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063711056727461890.json
name: 首尾帧  多帧  视频生成 wan2.2 wan22_2063711056727461890.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2063711056727461890.json
hash: d25d9073a82e3317
coverage: 0.878788
learned_at: 2026-10-15 22:39:17
nodes: [ImageResizeKJv2, ModelPatchTorchSettings, CLIPLoader, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, GetNode, GetNode, ImageResizeKJv2, UNETLoader, LoadImage, LoadImage, LoadImage, SetNode, INTConstant, SetNode, INTConstant, INTConstant, ImageResizeKJv2, VHS_VideoCombine, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, WanFirstMiddleLastFrameToVideo, CLIPTextEncode, CLIPTextEncode, VAELoader, SimpleMath+]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063711056727461890.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063711056727461890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `ImageResizeKJv2`
- `ModelPatchTorchSettings`
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
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanFirstMiddleLastFrameToVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SimpleMath+`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`ImageResizeKJv2`、`ModelPatchTorchSettings`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LoadImage`、`INTConstant`、`VHS_VideoCombine`、`VAEDecode`、`KSamplerAdvanced`、`WanFirstMiddleLastFrameToVideo`、`CLIPTextEncode`、`VAELoader`、`SimpleMath+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
