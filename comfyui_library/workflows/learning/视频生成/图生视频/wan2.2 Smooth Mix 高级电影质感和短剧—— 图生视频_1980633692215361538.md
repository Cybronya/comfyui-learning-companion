---
key: 视频生成/图生视频/wan2.2 Smooth Mix 高级电影质感和短剧—— 图生视频_1980633692215361538.json
name: wan2.2 Smooth Mix 高级电影质感和短剧—— 图生视频_1980633692215361538.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1980633692215361538.json
hash: 2d0d2f6b48cab281
coverage: 0.974359
learned_at: 2026-10-15 22:32:32
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, VAEDecode, SimpleMath+, easy cleanGpuUsed, ImageScaleBy, WanImageToVideo, CLIPVisionLoader, CLIPVisionEncode, ImageResizeKJv2, UNETLoader, UNETLoader, KSamplerAdvanced, KSamplerAdvanced, Fast Bypasser (rgthree), Fast Bypasser (rgthree), Seed (rgthree), VHS_VideoCombine, VHS_VideoCombine, LoadImage, LoadImage, PrimitiveStringMultiline, CLIPTextEncode, RHHiddenNodes, CLIPTextEncode, easy cleanGpuUsed, ImpactInt, ImpactInt, ImpactInt]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2 Smooth Mix 高级电影质感和短剧—— 图生视频_1980633692215361538.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980633692215361538.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（39 个）：
- `wanBlockSwap`
- `wanBlockSwap`
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
- `VAEDecode` ★核心
- `SimpleMath+`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `WanImageToVideo`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `Seed (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `RHHiddenNodes`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageScaleBy`、`WanImageToVideo`、`CLIPVisionLoader`、`CLIPVisionEncode`、`ImageResizeKJv2`、`UNETLoader`、`KSamplerAdvanced`、`Seed (rgthree)`、`VHS_VideoCombine`、`LoadImage`、`CLIPTextEncode`、`RHHiddenNodes`、`ImpactInt`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
