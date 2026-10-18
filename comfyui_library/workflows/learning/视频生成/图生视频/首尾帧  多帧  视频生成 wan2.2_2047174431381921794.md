---
key: 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2_2047174431381921794.json
name: 首尾帧  多帧  视频生成 wan2.2_2047174431381921794.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2_2047174431381921794.json
hash: ceae1ae9c9854e7f
coverage: 1
learned_at: 2026-10-15 22:37:03
nodes: [INTConstant, INTConstant, INTConstant, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, LoadImage, LoadImage, LoadImage, ModelPatchTorchSettings, WanFirstMiddleLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, VAEDecode, CLIPTextEncode, CLIPTextEncode, VAELoader, CLIPLoader, SimpleMath+, UNETLoader, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2_2047174431381921794.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047174431381921794.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（29 个）：
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ModelPatchTorchSettings`
- `WanFirstMiddleLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `SimpleMath+`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`INTConstant`、`ImageResizeKJv2`、`LoadImage`、`ModelPatchTorchSettings`、`WanFirstMiddleLastFrameToVideo`、`KSamplerAdvanced`、`VHS_VideoCombine`、`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`SimpleMath+`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
