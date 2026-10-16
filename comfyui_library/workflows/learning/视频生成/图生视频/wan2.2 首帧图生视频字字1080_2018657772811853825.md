---
key: 视频生成/图生视频/wan2.2 首帧图生视频字字1080_2018657772811853825.json
name: wan2.2 首帧图生视频字字1080_2018657772811853825.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2018657772811853825.json
hash: 55b892751d1cc595
coverage: 0.965517
learned_at: 2026-10-15 22:34:58
nodes: [KSamplerAdvanced, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, Seed (rgthree), VAEDecode, SimpleMath+, WanImageToVideo, easy cleanGpuUsed, CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, ImageResizeKJv2, CLIPVisionEncode, CLIPVisionLoader, ImpactInt, ModelPatchTorchSettings, UNETLoader, UNETLoader, VAELoader, KSamplerAdvanced, CLIPLoader, VHS_VideoCombine, LoadImage, PrimitiveStringMultiline, ImpactInt, ImpactInt]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2 首帧图生视频字字1080_2018657772811853825.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2018657772811853825.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（29 个）：
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Seed (rgthree)`
- `VAEDecode` ★核心
- `SimpleMath+`
- `WanImageToVideo`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImpactInt`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VHS_VideoCombine`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ImpactInt`
- `ImpactInt`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（28/29）

**有卡**：`KSamplerAdvanced`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`Seed (rgthree)`、`VAEDecode`、`SimpleMath+`、`WanImageToVideo`、`easy cleanGpuUsed`、`CLIPTextEncode`、`ImageResizeKJv2`、`CLIPVisionEncode`、`CLIPVisionLoader`、`ImpactInt`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
