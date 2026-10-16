---
key: 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2_2047224792201302017.json
name: 首尾帧  多帧  视频生成 wan2.2_2047224792201302017.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2047224792201302017.json
hash: b861a18336278b77
coverage: 1
learned_at: 2026-10-15 22:37:04
nodes: [LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, KSamplerAdvanced, CLIPLoader, ModelSamplingSD3, ModelPatchTorchSettings, PathchSageAttentionKJ, LoraLoaderModelOnly, CLIPTextEncode, WanFirstMiddleLastFrameToVideo, VAELoader, SimpleMath+, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, INTConstant, INTConstant, INTConstant, ImageResizeKJv2, ImageResizeKJv2, UNETLoader, UNETLoader, LoadImage, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2_2047224792201302017.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047224792201302017.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（27 个）：
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `WanFirstMiddleLastFrameToVideo`
- `VAELoader`
- `SimpleMath+`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPLoader`、`CLIPTextEncode`、`WanFirstMiddleLastFrameToVideo`、`VAELoader`、`SimpleMath+`、`VAEDecode`、`VHS_VideoCombine`、`INTConstant`、`ImageResizeKJv2`、`UNETLoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
