---
key: 视频生成/图生视频/首尾帧  Smooth Mix Wan 2.2_1979526029473648642.json
name: 首尾帧  Smooth Mix Wan 2.2_1979526029473648642.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧  Smooth Mix Wan 2.2_1979526029473648642.json
hash: 777a7b5f0c673290
coverage: 0.967742
learned_at: 2026-10-15 22:32:24
nodes: [wanBlockSwap, ImpactInt, ImpactInt, wanBlockSwap, ModelSamplingSD3, PathchSageAttentionKJ, ModelPatchTorchSettings, VAEDecode, UNETLoader, UNETLoader, ModelSamplingSD3, PathchSageAttentionKJ, ModelPatchTorchSettings, KSamplerAdvanced, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, WanFirstLastFrameToVideo, KSamplerAdvanced, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJv2, ImageResizeKJv2, SimpleMath+, CLIPVisionEncode, PrimitiveStringMultiline, VHS_VideoCombine, LoadImage, ImpactInt, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/首尾帧  Smooth Mix Wan 2.2_1979526029473648642.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979526029473648642.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（31 个）：
- `wanBlockSwap`
- `ImpactInt`
- `ImpactInt`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SimpleMath+`
- `CLIPVisionEncode`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `LoadImage`
- `ImpactInt`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（30/31）

**有卡**：`wanBlockSwap`、`ImpactInt`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAEDecode`、`UNETLoader`、`KSamplerAdvanced`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`WanFirstLastFrameToVideo`、`CLIPVisionEncode`、`CLIPVisionLoader`、`ImageResizeKJv2`、`SimpleMath+`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode
