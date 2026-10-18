---
key: 视频生成/图生视频/Wan2.2-吸入漫画-前半部分工作流_2010234636823175169.json
name: Wan2.2-吸入漫画-前半部分工作流_2010234636823175169.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-吸入漫画-前半部分工作流_2010234636823175169.json
hash: b4c6b18ce082e414
coverage: 0.946429
learned_at: 2026-10-15 22:34:16
nodes: [Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, SimpleMath+, easy cleanGpuUsed, CLIPVisionLoader, WanFirstLastFrameToVideo, CLIPVisionEncode, CLIPVisionEncode, UNETLoader, UNETLoader, wanBlockSwap, wanBlockSwap, Fast Bypasser (rgthree), Fast Bypasser (rgthree), easy batchAnything, ImageResizeKJv2, ImageResizeKJv2, LoadImage, VAEDecode, LoadAudio, easy cleanGpuUsed, ImageScaleBy, easy forLoopEnd, RIFE VFI, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, ImpactInt, ImpactInt, LoadImage, VHS_VideoCombine, LoadImage, ImpactInt, easy anythingIndexSwitch, easy anythingIndexSwitch, CLIPTextEncode, easy forLoopStart, JWInteger, Seed (rgthree), easy anythingIndexSwitch, Seed (rgthree), LoadImage, LoadImage, easy anythingIndexSwitch, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 16, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2-吸入漫画-前半部分工作流_2010234636823175169.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2010234636823175169.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（56 个）：
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
- `SimpleMath+`
- `easy cleanGpuUsed`
- `CLIPVisionLoader`
- `WanFirstLastFrameToVideo`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `easy batchAnything`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoadImage`
- `VAEDecode` ★核心
- `LoadAudio`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `easy forLoopEnd`
- `RIFE VFI`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `ImpactInt`
- `ImpactInt`
- `LoadImage`
- `VHS_VideoCombine`
- `LoadImage`
- `ImpactInt`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `CLIPTextEncode` ★核心
- `easy forLoopStart`
- `JWInteger`
- `Seed (rgthree)`
- `easy anythingIndexSwitch`
- `Seed (rgthree)`
- `LoadImage`
- `LoadImage`
- `easy anythingIndexSwitch`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `16`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（53/56）

**有卡**：`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`SimpleMath+`、`easy cleanGpuUsed`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`CLIPVisionEncode`、`UNETLoader`、`wanBlockSwap`、`easy batchAnything`、`ImageResizeKJv2`、`LoadImage`、`VAEDecode`、`LoadAudio`、`ImageScaleBy`、`easy forLoopEnd`、`RIFE VFI`、`KSamplerAdvanced`、`CLIPTextEncode`、`ImpactInt`、`VHS_VideoCombine`、`easy anythingIndexSwitch`、`easy forLoopStart`、`JWInteger`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
