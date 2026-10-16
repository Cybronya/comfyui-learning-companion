---
key: 视频生成/图生视频/首尾帧新版本   wan2.2 wan22  图生视频   视频生成_2078441258510536706.json
name: 首尾帧新版本   wan2.2 wan22  图生视频   视频生成_2078441258510536706.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2078441258510536706.json
hash: 86a2529b02329db6
coverage: 1
learned_at: 2026-10-15 22:41:53
nodes: [CLIPTextEncode, KSamplerAdvanced, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, SimpleMath+, VAELoader, INTConstant, LoadImage, LoadImage, VHS_VideoCombine, VHS_VideoCombine, ImageResizeKJv2, ImageResizeKJv2, CLIPTextEncode, WanFirstMiddleLastFrameToVideo, KSamplerAdvanced, VAEDecode, ImageConcatMulti, ImageConcatMulti]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧新版本   wan2.2 wan22  图生视频   视频生成_2078441258510536706.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2078441258510536706.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `SimpleMath+`
- `VAELoader`
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `WanFirstMiddleLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `ImageConcatMulti`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`CLIPTextEncode`、`KSamplerAdvanced`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`CLIPLoader`、`SimpleMath+`、`VAELoader`、`INTConstant`、`LoadImage`、`VHS_VideoCombine`、`ImageResizeKJv2`、`WanFirstMiddleLastFrameToVideo`、`VAEDecode`、`ImageConcatMulti`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
