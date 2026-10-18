---
key: 视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_1980432616040148994.json
name: wan2.2 Smooth Mix 高动态电影质感 图生视频_1980432616040148994.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_1980432616040148994.json
hash: 4f527fe7b0b6f304
coverage: 0.973684
learned_at: 2026-10-15 22:32:30
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, VAEDecode, RIFE VFI, SimpleMath+, easy cleanGpuUsed, ImageScaleBy, CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, WanImageToVideo, CLIPVisionLoader, CLIPVisionEncode, ImageResizeKJv2, UNETLoader, UNETLoader, ImpactInt, ImpactInt, KSamplerAdvanced, KSamplerAdvanced, Fast Bypasser (rgthree), Fast Bypasser (rgthree), Seed (rgthree), LoadImage, VHS_VideoCombine, VHS_VideoCombine, PrimitiveStringMultiline, ImpactInt]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_1980432616040148994.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980432616040148994.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（38 个）：
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
- `RIFE VFI`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ImpactInt`
- `ImpactInt`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `Seed (rgthree)`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `ImpactInt`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（37/38）

**有卡**：`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`RIFE VFI`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageScaleBy`、`CLIPTextEncode`、`WanImageToVideo`、`CLIPVisionLoader`、`CLIPVisionEncode`、`ImageResizeKJv2`、`UNETLoader`、`ImpactInt`、`KSamplerAdvanced`、`Seed (rgthree)`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
