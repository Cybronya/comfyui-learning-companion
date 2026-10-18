---
key: 视频生成/图生视频/wan2.2 图生视频_2006925723407228930.json
name: wan2.2 图生视频_2006925723407228930.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 图生视频_2006925723407228930.json
hash: d338230dabc2dcdf
coverage: 0.973684
learned_at: 2026-10-15 22:34:02
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, VAEDecode, SimpleMath+, easy cleanGpuUsed, ImageScaleBy, easy cleanGpuUsed, CLIPTextEncode, WanImageToVideo, CLIPVisionLoader, CLIPVisionEncode, UNETLoader, UNETLoader, ImpactInt, KSamplerAdvanced, Fast Bypasser (rgthree), Fast Bypasser (rgthree), Seed (rgthree), ImageResizeKJv2, ImpactInt, RIFE VFI, ImpactInt, CLIPTextEncode, KSamplerAdvanced, VHS_VideoCombine, VHS_VideoCombine, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2 图生视频_2006925723407228930.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2006925723407228930.json`

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
- `SimpleMath+`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ImpactInt`
- `KSamplerAdvanced` ★核心
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `Seed (rgthree)`
- `ImageResizeKJv2`
- `ImpactInt`
- `RIFE VFI`
- `ImpactInt`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（37/38）

**有卡**：`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageScaleBy`、`CLIPTextEncode`、`WanImageToVideo`、`CLIPVisionLoader`、`CLIPVisionEncode`、`UNETLoader`、`ImpactInt`、`KSamplerAdvanced`、`Seed (rgthree)`、`ImageResizeKJv2`、`RIFE VFI`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
