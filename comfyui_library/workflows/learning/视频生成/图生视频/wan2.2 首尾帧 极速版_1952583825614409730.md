---
key: 视频生成/图生视频/wan2.2 首尾帧 极速版_1952583825614409730.json
name: wan2.2 首尾帧 极速版_1952583825614409730.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952583825614409730.json
hash: 7f212d29d8eb198c
coverage: 1
learned_at: 2026-10-15 22:31:02
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, WanVideoNAG, VAELoader, CLIPVisionLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionEncode, VAEDecode, WanFirstLastFrameToVideo, SimpleMath+, ImageResizeKJv2, ImageResizeKJ, ModelSamplingSD3, ImpactInt, ImpactInt, ImpactInt, ImpactInt, VHS_VideoCombine, LoraLoaderModelOnly, UNETLoader, UNETLoader, SimpleMath+, KSamplerAdvanced, KSamplerAdvanced, PathchSageAttentionKJ, LoraLoaderModelOnly, LoadImage, LoadImage, CR Text, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2 首尾帧 极速版_1952583825614409730.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952583825614409730.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（32 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `WanVideoNAG`
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `VAEDecode` ★核心
- `WanFirstLastFrameToVideo`
- `SimpleMath+`
- `ImageResizeKJv2`
- `ImageResizeKJ`
- `ModelSamplingSD3`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SimpleMath+`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `CR Text`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（32/32）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`WanVideoNAG`、`VAELoader`、`CLIPVisionLoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`VAEDecode`、`WanFirstLastFrameToVideo`、`SimpleMath+`、`ImageResizeKJv2`、`ImageResizeKJ`、`ImpactInt`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`UNETLoader`、`KSamplerAdvanced`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
