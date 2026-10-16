---
key: 视频生成/图生视频/Remix-V3.0-首尾多帧视频生成_2033890243190984706.json
name: Remix-V3.0-首尾多帧视频生成_2033890243190984706.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2033890243190984706.json
hash: 96a7d8fb5bc26783
coverage: 1
learned_at: 2026-10-15 22:35:42
nodes: [CLIPLoader, ImageResizeKJv2, LoraLoaderModelOnly, INTConstant, SimpleMath+, VAELoader, ModelSamplingSD3, VHS_VideoCombine, ImageResizeKJv2, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, LoraLoaderModelOnly, ImageResizeKJv2, INTConstant, UNETLoader, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, YC Color Match, LoadImage, LoadImage, LoadImage, INTConstant, WanFirstMiddleLastFrameToVideo, CLIPTextEncode, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Remix-V3.0-首尾多帧视频生成_2033890243190984706.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033890243190984706.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（32 个）：
- `CLIPLoader`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `SimpleMath+`
- `VAELoader`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `INTConstant`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `YC Color Match`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `INTConstant`
- `WanFirstMiddleLastFrameToVideo`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（32/32）

**有卡**：`CLIPLoader`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`INTConstant`、`SimpleMath+`、`VAELoader`、`ModelSamplingSD3`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`UNETLoader`、`CLIPTextEncode`、`KSamplerAdvanced`、`VAEDecode`、`YC Color Match`、`LoadImage`、`WanFirstMiddleLastFrameToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
