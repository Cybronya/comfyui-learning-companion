---
key: 视频生成/图生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 首尾帧视频🚵_1979384908328112130.json
name: 🚵Smooth Mix wan2.2 高动态电影质感模型 首尾帧视频🚵_1979384908328112130.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1979384908328112130.json
hash: 90dcd28fcaa05e8a
coverage: 0.953488
learned_at: 2026-10-15 22:32:23
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, ImpactInt, Seed (rgthree), VAEDecode, RIFE VFI, SimpleMath+, easy cleanGpuUsed, ImageScaleBy, CLIPTextEncode, easy cleanGpuUsed, Fast Bypasser (rgthree), Fast Bypasser (rgthree), CLIPTextEncode, MarkdownNote, KSamplerAdvanced, KSamplerAdvanced, PrimitiveStringMultiline, ImpactInt, ImpactInt, CLIPVisionLoader, WanFirstLastFrameToVideo, ImageResizeKJv2, ImageResizeKJv2, CLIPVisionEncode, CLIPVisionEncode, Note Plus (mtb), LoadImage, LoadImage, UNETLoader, UNETLoader, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 首尾帧视频🚵_1979384908328112130.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979384908328112130.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（43 个）：
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
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PrimitiveStringMultiline`
- `ImpactInt`
- `ImpactInt`
- `CLIPVisionLoader`
- `WanFirstLastFrameToVideo`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `Note Plus (mtb)`
- `LoadImage`
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

覆盖率 **95%**（41/43）

**有卡**：`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`ImpactInt`、`Seed (rgthree)`、`VAEDecode`、`RIFE VFI`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageScaleBy`、`CLIPTextEncode`、`KSamplerAdvanced`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`ImageResizeKJv2`、`CLIPVisionEncode`、`Note Plus (mtb)`、`LoadImage`、`UNETLoader`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
