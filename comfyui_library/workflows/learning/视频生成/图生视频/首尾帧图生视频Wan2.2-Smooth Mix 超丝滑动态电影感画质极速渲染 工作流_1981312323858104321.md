---
key: 视频生成/图生视频/首尾帧图生视频Wan2.2-Smooth Mix 超丝滑动态电影感画质极速渲染 工作流_1981312323858104321.json
name: 首尾帧图生视频Wan2.2-Smooth Mix 超丝滑动态电影感画质极速渲染 工作流_1981312323858104321.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧图生视频Wan2.2-Smooth Mix 超丝滑动态电影感画质极速渲染 工作流_1981312323858104321.json
hash: 0054f51d1090db5c
coverage: 0.976744
learned_at: 2026-10-15 22:32:37
nodes: [Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, ImpactInt, Seed (rgthree), VAEDecode, RIFE VFI, SimpleMath+, easy cleanGpuUsed, ImageScaleBy, CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, ImpactInt, ImpactInt, CLIPVisionLoader, WanFirstLastFrameToVideo, ImageResizeKJv2, ImageResizeKJv2, CLIPVisionEncode, CLIPVisionEncode, LoadImage, UNETLoader, UNETLoader, wanBlockSwap, wanBlockSwap, Fast Bypasser (rgthree), PrimitiveStringMultiline, Fast Bypasser (rgthree), VHS_VideoCombine, VHS_VideoCombine, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/首尾帧图生视频Wan2.2-Smooth Mix 超丝滑动态电影感画质极速渲染 工作流_1981312323858104321.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981312323858104321.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（43 个）：
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Bypasser (rgthree)`
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
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImpactInt`
- `ImpactInt`
- `CLIPVisionLoader`
- `WanFirstLastFrameToVideo`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `Fast Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `Fast Bypasser (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **98%**（42/43）

**有卡**：`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`ImpactInt`、`Seed (rgthree)`、`VAEDecode`、`RIFE VFI`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageScaleBy`、`CLIPTextEncode`、`KSamplerAdvanced`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`ImageResizeKJv2`、`CLIPVisionEncode`、`LoadImage`、`UNETLoader`、`wanBlockSwap`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
