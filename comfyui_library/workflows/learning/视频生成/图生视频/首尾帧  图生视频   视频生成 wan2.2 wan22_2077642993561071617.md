---
key: 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2077642993561071617.json
name: 首尾帧  图生视频   视频生成 wan2.2 wan22_2077642993561071617.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2077642993561071617.json
hash: f930ce39cd69bfc8
coverage: 0.962963
learned_at: 2026-10-15 22:41:42
nodes: [WanFirstMiddleLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, ImageResizeKJv2, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, SimpleMath+, VAELoader, INTConstant, ImageResizeKJv2, VAEDecode, VHS_VideoCombine, VHS_SelectFilename, PreviewAny, LoadImage, LoadImage, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2077642993561071617.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2077642993561071617.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（27 个）：
- `WanFirstMiddleLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImageResizeKJv2`
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
- `ImageResizeKJv2`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VHS_SelectFilename`
- `PreviewAny`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **96%**（26/27）

**有卡**：`WanFirstMiddleLastFrameToVideo`、`KSamplerAdvanced`、`ImageResizeKJv2`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`CLIPLoader`、`SimpleMath+`、`VAELoader`、`INTConstant`、`VAEDecode`、`VHS_VideoCombine`、`VHS_SelectFilename`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
