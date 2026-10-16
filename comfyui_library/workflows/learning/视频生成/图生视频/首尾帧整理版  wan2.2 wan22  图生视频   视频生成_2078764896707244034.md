---
key: 视频生成/图生视频/首尾帧整理版  wan2.2 wan22  图生视频   视频生成_2078764896707244034.json
name: 首尾帧整理版  wan2.2 wan22  图生视频   视频生成_2078764896707244034.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2078764896707244034.json
hash: b237c25e3be990ae
coverage: 0.925926
learned_at: 2026-10-15 22:41:55
nodes: [UNETLoader, LoraLoaderModelOnly, WanFirstMiddleLastFrameToVideo, UNETLoader, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, INTConstant, SimpleMath+, VAELoader, LoadImage, LoadImage, ImageResizeKJv2, ImageResizeKJv2, GetNode, KSamplerAdvanced, SetNode, ModelSamplingSD3, CLIPLoader]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧整理版  wan2.2 wan22  图生视频   视频生成_2078764896707244034.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2078764896707244034.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（27 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanFirstMiddleLastFrameToVideo`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `INTConstant`
- `SimpleMath+`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `SetNode`
- `ModelSamplingSD3`
- `CLIPLoader`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`WanFirstMiddleLastFrameToVideo`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`CLIPTextEncode`、`INTConstant`、`SimpleMath+`、`VAELoader`、`LoadImage`、`ImageResizeKJv2`、`CLIPLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
