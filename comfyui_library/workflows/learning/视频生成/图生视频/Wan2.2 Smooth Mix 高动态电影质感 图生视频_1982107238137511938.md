---
key: 视频生成/图生视频/Wan2.2 Smooth Mix 高动态电影质感 图生视频_1982107238137511938.json
name: Wan2.2 Smooth Mix 高动态电影质感 图生视频_1982107238137511938.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Smooth Mix 高动态电影质感 图生视频_1982107238137511938.json
hash: 3a6db159298b6d72
coverage: 0.973684
learned_at: 2026-10-15 22:32:40
nodes: [Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, VAELoader, RIFE VFI, CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, CLIPVisionLoader, CLIPVisionEncode, UNETLoader, KSamplerAdvanced, Seed (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), ImageResizeKJv2, ImpactInt, ModelPatchTorchSettings, easy cleanGpuUsed, SimpleMath+, VAEDecode, ImageScaleBy, ImpactInt, Fast Bypasser (rgthree), wanBlockSwap, VHS_VideoCombine, ImpactInt, PrimitiveStringMultiline, UNETLoader, ModelSamplingSD3, wanBlockSwap, PathchSageAttentionKJ, WanImageToVideo, ModelPatchTorchSettings, LoadImage, KSamplerAdvanced, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 Smooth Mix 高动态电影质感 图生视频_1982107238137511938.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1982107238137511938.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（38 个）：
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `RIFE VFI`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `Seed (rgthree)`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `ImageResizeKJv2`
- `ImpactInt`
- `ModelPatchTorchSettings`
- `easy cleanGpuUsed`
- `SimpleMath+`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `ImpactInt`
- `Fast Bypasser (rgthree)`
- `wanBlockSwap`
- `VHS_VideoCombine`
- `ImpactInt`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `WanImageToVideo`
- `ModelPatchTorchSettings`
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（37/38）

**有卡**：`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`RIFE VFI`、`CLIPTextEncode`、`easy cleanGpuUsed`、`CLIPVisionLoader`、`CLIPVisionEncode`、`UNETLoader`、`KSamplerAdvanced`、`Seed (rgthree)`、`Fast Bypasser (rgthree)`、`ImageResizeKJv2`、`ImpactInt`、`ModelPatchTorchSettings`、`SimpleMath+`、`VAEDecode`、`ImageScaleBy`、`wanBlockSwap`、`VHS_VideoCombine`、`WanImageToVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
