---
key: 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2075510355111006210.json
name: 首尾帧  图生视频   视频生成 wan2.2 wan22_2075510355111006210.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2075510355111006210.json
hash: cb0db81df81f3f89
coverage: 1
learned_at: 2026-10-15 22:41:25
nodes: [ImageResizeKJv2, PathchSageAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPLoader, SimpleMath+, VAELoader, INTConstant, CLIPTextEncode, LoadImage, ImageResizeKJv2, LoadImage, ModelPatchTorchSettings, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, ModelSamplingSD3, ModelPatchTorchSettings, CLIPTextEncode, WanFirstMiddleLastFrameToVideo, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2075510355111006210.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2075510355111006210.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `ImageResizeKJv2`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `SimpleMath+`
- `VAELoader`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ImageResizeKJv2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `WanFirstMiddleLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`ImageResizeKJv2`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`CLIPLoader`、`SimpleMath+`、`VAELoader`、`INTConstant`、`CLIPTextEncode`、`LoadImage`、`ModelPatchTorchSettings`、`UNETLoader`、`ModelSamplingSD3`、`WanFirstMiddleLastFrameToVideo`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
