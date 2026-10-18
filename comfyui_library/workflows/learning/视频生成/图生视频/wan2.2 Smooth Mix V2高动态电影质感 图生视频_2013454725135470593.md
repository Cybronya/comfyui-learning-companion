---
key: 视频生成/图生视频/wan2.2 Smooth Mix V2高动态电影质感 图生视频_2013454725135470593.json
name: wan2.2 Smooth Mix V2高动态电影质感 图生视频_2013454725135470593.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 Smooth Mix V2高动态电影质感 图生视频_2013454725135470593.json
hash: cfb5302342c68f40
coverage: 0.974359
learned_at: 2026-10-15 22:34:31
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, VAEDecode, RIFE VFI, SimpleMath+, easy cleanGpuUsed, ImageScaleBy, CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, CLIPVisionLoader, CLIPVisionEncode, Fast Bypasser (rgthree), Fast Bypasser (rgthree), Seed (rgthree), VHS_VideoCombine, VHS_VideoCombine, Text Concatenate, UNETLoader, UNETLoader, KSamplerAdvanced, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, WanImageToVideo, LoadImage, ImpactInt, ImpactInt, PrimitiveStringMultiline, Wan22PromptSelector]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2 Smooth Mix V2高动态电影质感 图生视频_2013454725135470593.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2013454725135470593.json`

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
- `RIFE VFI`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `Seed (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Text Concatenate`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanImageToVideo`
- `LoadImage`
- `ImpactInt`
- `ImpactInt`
- `PrimitiveStringMultiline`
- `Wan22PromptSelector`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`RIFE VFI`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageScaleBy`、`CLIPTextEncode`、`CLIPVisionLoader`、`CLIPVisionEncode`、`Seed (rgthree)`、`VHS_VideoCombine`、`Text Concatenate`、`UNETLoader`、`KSamplerAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanImageToVideo`、`LoadImage`、`ImpactInt`、`Wan22PromptSelector`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
