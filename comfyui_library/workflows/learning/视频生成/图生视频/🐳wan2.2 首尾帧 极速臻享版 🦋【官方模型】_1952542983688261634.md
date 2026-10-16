---
key: 视频生成/图生视频/🐳wan2.2 首尾帧 极速臻享版 🦋【官方模型】_1952542983688261634.json
name: 🐳wan2.2 首尾帧 极速臻享版 🦋【官方模型】_1952542983688261634.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952542983688261634.json
hash: 169cefb91b02ea88
coverage: 0.970588
learned_at: 2026-10-15 22:31:02
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, WanVideoNAG, VAELoader, CLIPVisionLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionEncode, CLIPTextEncode, VAEDecode, WanFirstLastFrameToVideo, SimpleMath+, ImageResizeKJv2, ImageResizeKJ, ModelSamplingSD3, MarkdownNote, Note Plus (mtb), ImpactInt, ImpactInt, ImpactInt, ImpactInt, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, LoadImage, UNETLoader, UNETLoader, PathchSageAttentionKJ, CR Text, SimpleMath+, KSamplerAdvanced, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/🐳wan2.2 首尾帧 极速臻享版 🦋【官方模型】_1952542983688261634.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952542983688261634.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（34 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `WanVideoNAG`
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `WanFirstLastFrameToVideo`
- `SimpleMath+`
- `ImageResizeKJv2`
- `ImageResizeKJ`
- `ModelSamplingSD3`
- `MarkdownNote`
- `Note Plus (mtb)`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `CR Text`
- `SimpleMath+`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（33/34）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`WanVideoNAG`、`VAELoader`、`CLIPVisionLoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`VAEDecode`、`WanFirstLastFrameToVideo`、`SimpleMath+`、`ImageResizeKJv2`、`ImageResizeKJ`、`Note Plus (mtb)`、`ImpactInt`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`LoadImage`、`UNETLoader`、`CR Text`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
