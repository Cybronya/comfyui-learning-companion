---
key: 视频生成/图生视频/Remix-V2.1-首尾多帧视频生成_2011657248396808193.json
name: Remix-V2.1-首尾多帧视频生成_2011657248396808193.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Remix-V2.1-首尾多帧视频生成_2011657248396808193.json
hash: e818b8627e5aaef8
coverage: 1
learned_at: 2026-10-15 22:34:24
nodes: [CLIPLoader, INTConstant, ImageResizeKJv2, LoraLoaderModelOnly, INTConstant, INTConstant, SimpleMath+, CLIPTextEncode, VAELoader, CLIPTextEncode, ModelSamplingSD3, VHS_VideoCombine, LoadImage, LoadImage, ImageResizeKJv2, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, UNETLoader, LoadImage, LoraLoaderModelOnly, UNETLoader, WanFirstMiddleLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, ImageResizeKJv2, VAEDecode, YC Color Match]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Remix-V2.1-首尾多帧视频生成_2011657248396808193.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2011657248396808193.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（32 个）：
- `CLIPLoader`
- `INTConstant`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `WanFirstMiddleLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImageResizeKJv2`
- `VAEDecode` ★核心
- `YC Color Match`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（32/32）

**有卡**：`CLIPLoader`、`INTConstant`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`SimpleMath+`、`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`VHS_VideoCombine`、`LoadImage`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`UNETLoader`、`WanFirstMiddleLastFrameToVideo`、`KSamplerAdvanced`、`VAEDecode`、`YC Color Match`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
