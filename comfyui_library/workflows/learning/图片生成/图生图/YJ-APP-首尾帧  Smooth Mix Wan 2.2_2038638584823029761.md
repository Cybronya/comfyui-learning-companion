---
key: 图片生成/图生图/YJ-APP-首尾帧  Smooth Mix Wan 2.2_2038638584823029761.json
name: YJ-APP-首尾帧  Smooth Mix Wan 2.2_2038638584823029761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/YJ-APP-首尾帧  Smooth Mix Wan 2.2_2038638584823029761.json
hash: 919a3159c66f98b9
coverage: 0.967742
learned_at: 2026-10-23 11:28:49
nodes: [wanBlockSwap, ImpactInt, wanBlockSwap, ModelSamplingSD3, PathchSageAttentionKJ, ModelPatchTorchSettings, VAEDecode, ModelSamplingSD3, PathchSageAttentionKJ, ModelPatchTorchSettings, KSamplerAdvanced, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, WanFirstLastFrameToVideo, KSamplerAdvanced, CLIPVisionEncode, CLIPVisionLoader, CLIPVisionEncode, UNETLoader, UNETLoader, SimpleMath+, ImpactInt, ImpactInt, ImageResizeKJv2, ImageResizeKJv2, LoadImage, VHS_VideoCombine, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 图片生成/图生图/YJ-APP-首尾帧  Smooth Mix Wan 2.2_2038638584823029761.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/YJ-APP-首尾帧  Smooth Mix Wan 2.2_2038638584823029761.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（31 个）：
- `wanBlockSwap`
- `ImpactInt`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VAEDecode` ★核心
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
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SimpleMath+`
- `ImpactInt`
- `ImpactInt`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_VideoCombine`
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（30/31）

**有卡**：`wanBlockSwap`、`ImpactInt`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAEDecode`、`KSamplerAdvanced`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`WanFirstLastFrameToVideo`、`CLIPVisionEncode`、`CLIPVisionLoader`、`UNETLoader`、`SimpleMath+`、`ImageResizeKJv2`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode
