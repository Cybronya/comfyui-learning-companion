---
key: 视频生成/图生视频/Smooth wan2.2 电影质感视频生成_1983826871899070465.json
name: Smooth wan2.2 电影质感视频生成_1983826871899070465.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Smooth wan2.2 电影质感视频生成_1983826871899070465.json
hash: 3c2bf288032a8b8e
coverage: 0.969697
learned_at: 2026-10-15 22:32:46
nodes: [PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), ModelPatchTorchSettings, Seed (rgthree), VAEDecode, RIFE VFI, SimpleMath+, easy cleanGpuUsed, ImageScaleBy, CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, WanImageToVideo, CLIPVisionEncode, ImageResizeKJv2, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, VHS_VideoCombine, VHS_VideoCombine, Fast Bypasser (rgthree), UNETLoader, CLIPLoader, VAELoader, CLIPVisionLoader, PathchSageAttentionKJ, Fast Bypasser (rgthree), ImpactInt, ImpactInt, ImpactInt, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Smooth wan2.2 电影质感视频生成_1983826871899070465.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983826871899070465.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Bypasser (rgthree)`
- `ModelPatchTorchSettings`
- `Seed (rgthree)`
- `VAEDecode` ★核心
- `RIFE VFI`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `CLIPVisionEncode`
- `ImageResizeKJv2`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Fast Bypasser (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `PathchSageAttentionKJ`
- `Fast Bypasser (rgthree)`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `PrimitiveStringMultiline`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（32/33）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`Seed (rgthree)`、`VAEDecode`、`RIFE VFI`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageScaleBy`、`CLIPTextEncode`、`WanImageToVideo`、`CLIPVisionEncode`、`ImageResizeKJv2`、`KSamplerAdvanced`、`UNETLoader`、`VHS_VideoCombine`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`ImpactInt`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
