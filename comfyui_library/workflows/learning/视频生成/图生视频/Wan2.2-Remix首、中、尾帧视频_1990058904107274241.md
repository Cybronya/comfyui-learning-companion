---
key: 视频生成/图生视频/Wan2.2-Remix首、中、尾帧视频_1990058904107274241.json
name: Wan2.2-Remix首、中、尾帧视频_1990058904107274241.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1990058904107274241.json
hash: 8ea6208a99585102
coverage: 1
learned_at: 2026-10-15 22:33:09
nodes: [PathchSageAttentionKJ, CLIPLoader, INTConstant, ImageResizeKJv2, ImageResizeKJv2, LoraLoaderModelOnly, INTConstant, INTConstant, SimpleMath+, CLIPTextEncode, VAELoader, CLIPTextEncode, UNETLoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, KSamplerAdvanced, VAEDecode, LoadImage, LoadImage, ImageResizeKJv2, LoadImage, WanFirstMiddleLastFrameToVideo, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2-Remix首、中、尾帧视频_1990058904107274241.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1990058904107274241.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（29 个）：
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `LoadImage`
- `WanFirstMiddleLastFrameToVideo`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`PathchSageAttentionKJ`、`CLIPLoader`、`INTConstant`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`SimpleMath+`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`ModelSamplingSD3`、`VHS_VideoCombine`、`KSamplerAdvanced`、`VAEDecode`、`LoadImage`、`WanFirstMiddleLastFrameToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
