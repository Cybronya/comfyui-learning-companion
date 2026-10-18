---
key: 视频生成/图生视频/Wan2.2-Smooth Mix 超丝滑动态电影感画质极速渲染 图生视频工作流_1981294713347145729.json
name: Wan2.2-Smooth Mix 超丝滑动态电影感画质极速渲染 图生视频工作流_1981294713347145729.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Smooth Mix 超丝滑动态电影感画质极速渲染 图生视频工作流_1981294713347145729.json
hash: 1f03aa919d6e3dbc
coverage: 0.973684
learned_at: 2026-10-15 22:32:37
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, ImpactInt, Seed (rgthree), VAEDecode, RIFE VFI, SimpleMath+, easy cleanGpuUsed, ImageScaleBy, CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, ImpactInt, WanImageToVideo, CLIPVisionLoader, CLIPVisionEncode, ImageResizeKJv2, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, UNETLoader, Fast Bypasser (rgthree), Fast Bypasser (rgthree), LoadImage, ImpactInt, VHS_VideoCombine, VHS_VideoCombine, PrimitiveStringMultiline, Fast Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2-Smooth Mix 超丝滑动态电影感画质极速渲染 图生视频工作流_1981294713347145729.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981294713347145729.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（38 个）：
- `wanBlockSwap`
- `wanBlockSwap`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `ModelPatchTorchSettings`
- `ImpactInt`
- `Seed (rgthree)`
- `VAEDecode` ★核心
- `RIFE VFI`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `ImpactInt`
- `WanImageToVideo`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `ImageResizeKJv2`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `LoadImage`
- `ImpactInt`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `Fast Bypasser (rgthree)`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（37/38）

**有卡**：`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`ImpactInt`、`Seed (rgthree)`、`VAEDecode`、`RIFE VFI`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageScaleBy`、`CLIPTextEncode`、`WanImageToVideo`、`CLIPVisionLoader`、`CLIPVisionEncode`、`ImageResizeKJv2`、`KSamplerAdvanced`、`UNETLoader`、`Fast Bypasser (rgthree)`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
