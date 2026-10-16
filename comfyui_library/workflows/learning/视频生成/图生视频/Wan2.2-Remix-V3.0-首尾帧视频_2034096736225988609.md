---
key: 视频生成/图生视频/Wan2.2-Remix-V3.0-首尾帧视频_2034096736225988609.json
name: Wan2.2-Remix-V3.0-首尾帧视频_2034096736225988609.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2034096736225988609.json
hash: 2aa15b32c0d2bdaf
coverage: 1
learned_at: 2026-10-15 22:35:43
nodes: [ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, LoraLoaderModelOnly, KSamplerAdvanced, VAELoader, SimpleMath+, VAEDecode, INTConstant, INTConstant, INTConstant, ImageResizeKJv2, ImageResizeKJv2, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, CLIPTextEncode, KSamplerAdvanced, WanFirstLastFrameToVideo, CLIPVisionLoader, UNETLoader, UNETLoader, CLIPVisionEncode, CLIPVisionEncode, VHS_VideoCombine, LoadImage, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2-Remix-V3.0-首尾帧视频_2034096736225988609.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2034096736225988609.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（32 个）：
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `SimpleMath+`
- `VAEDecode` ★核心
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `WanFirstLastFrameToVideo`
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `VHS_VideoCombine`
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

覆盖率 **100%**（32/32）

**有卡**：`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`KSamplerAdvanced`、`VAELoader`、`SimpleMath+`、`VAEDecode`、`INTConstant`、`ImageResizeKJv2`、`CLIPLoader`、`CLIPTextEncode`、`WanFirstLastFrameToVideo`、`CLIPVisionLoader`、`UNETLoader`、`CLIPVisionEncode`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
