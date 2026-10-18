---
key: 视频生成/图生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 图生视频🚵_1979384591175815170.json
name: 🚵Smooth Mix wan2.2 高动态电影质感模型 图生视频🚵_1979384591175815170.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 图生视频🚵_1979384591175815170.json
hash: e9e27dd65593fa3e
coverage: 0.95
learned_at: 2026-10-15 22:32:22
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, ImpactInt, Seed (rgthree), VAEDecode, RIFE VFI, SimpleMath+, easy cleanGpuUsed, ImageScaleBy, CLIPTextEncode, easy cleanGpuUsed, Fast Bypasser (rgthree), Fast Bypasser (rgthree), CLIPTextEncode, MarkdownNote, ImpactInt, ImpactInt, PrimitiveStringMultiline, Note Plus (mtb), WanImageToVideo, CLIPVisionLoader, CLIPVisionEncode, ImageResizeKJv2, KSamplerAdvanced, KSamplerAdvanced, LoadImage, UNETLoader, UNETLoader, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 图生视频🚵_1979384591175815170.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979384591175815170.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（40 个）：
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
- `ImpactInt`
- `Seed (rgthree)`
- `VAEDecode` ★核心
- `RIFE VFI`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `ImpactInt`
- `ImpactInt`
- `PrimitiveStringMultiline`
- `Note Plus (mtb)`
- `WanImageToVideo`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `ImageResizeKJv2`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`ImpactInt`、`Seed (rgthree)`、`VAEDecode`、`RIFE VFI`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageScaleBy`、`CLIPTextEncode`、`Note Plus (mtb)`、`WanImageToVideo`、`CLIPVisionLoader`、`CLIPVisionEncode`、`ImageResizeKJv2`、`KSamplerAdvanced`、`LoadImage`、`UNETLoader`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
