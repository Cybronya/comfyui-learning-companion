---
key: 视频生成/图生视频/DaSiWaWan2.2-动漫多帧视频生成_2007811222472761345.json
name: DaSiWaWan2.2-动漫多帧视频生成_2007811222472761345.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2007811222472761345.json
hash: bc3c47f789ea26a3
coverage: 1
learned_at: 2026-10-15 22:34:05
nodes: [INTConstant, PathchSageAttentionKJ, CLIPLoader, ModelPatchTorchSettings, VHS_VideoCombine, VAELoader, INTConstant, INTConstant, UNETLoader, UNETLoader, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, LoadImage, LoadImage, LoadImage, ImageResizeKJv2, ImageResizeKJv2, WanFirstMiddleLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, ImageResizeKJv2, SimpleMath+]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/DaSiWaWan2.2-动漫多帧视频生成_2007811222472761345.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2007811222472761345.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（27 个）：
- `INTConstant`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `ModelPatchTorchSettings`
- `VHS_VideoCombine`
- `VAELoader`
- `INTConstant`
- `INTConstant`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanFirstMiddleLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `SimpleMath+`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`INTConstant`、`PathchSageAttentionKJ`、`CLIPLoader`、`ModelPatchTorchSettings`、`VHS_VideoCombine`、`VAELoader`、`UNETLoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`LoadImage`、`ImageResizeKJv2`、`WanFirstMiddleLastFrameToVideo`、`KSamplerAdvanced`、`VAEDecode`、`SimpleMath+`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ImageResizeKJv2
