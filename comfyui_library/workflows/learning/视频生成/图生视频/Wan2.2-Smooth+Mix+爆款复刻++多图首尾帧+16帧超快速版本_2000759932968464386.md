---
key: 视频生成/图生视频/Wan2.2-Smooth+Mix+爆款复刻++多图首尾帧+16帧超快速版本_2000759932968464386.json
name: Wan2.2-Smooth+Mix+爆款复刻++多图首尾帧+16帧超快速版本_2000759932968464386.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2000759932968464386.json
hash: e1e62d89c8a47779
coverage: 0.979167
learned_at: 2026-10-15 22:33:42
nodes: [Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, ModelPatchTorchSettings, Seed (rgthree), SimpleMath+, CLIPVisionLoader, CLIPVisionEncode, UNETLoader, UNETLoader, wanBlockSwap, wanBlockSwap, Fast Bypasser (rgthree), Fast Bypasser (rgthree), easy forLoopEnd, easy batchAnything, easy forLoopStart, ImageResizeKJv2, LoadImage, ImpactInt, ImpactInt, CLIPTextEncode, ImageScaleBy, VHS_VideoCombine, RIFE VFI, WanFirstLastFrameToVideo, easy cleanGpuUsed, CLIPVisionEncode, VAEDecode, VAELoader, ImpactInt, LoadImage, LoadImage, LoadImage, JWInteger, CLIPTextEncode, easy anythingIndexSwitch, easy anythingIndexSwitch, ImageResizeKJv2, KSamplerAdvanced, KSamplerAdvanced, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2-Smooth+Mix+爆款复刻++多图首尾帧+16帧超快速版本_2000759932968464386.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2000759932968464386.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（48 个）：
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Bypasser (rgthree)`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `ModelPatchTorchSettings`
- `Seed (rgthree)`
- `SimpleMath+`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `easy forLoopEnd`
- `easy batchAnything`
- `easy forLoopStart`
- `ImageResizeKJv2`
- `LoadImage`
- `ImpactInt`
- `ImpactInt`
- `CLIPTextEncode` ★核心
- `ImageScaleBy`
- `VHS_VideoCombine`
- `RIFE VFI`
- `WanFirstLastFrameToVideo`
- `easy cleanGpuUsed`
- `CLIPVisionEncode`
- `VAEDecode` ★核心
- `VAELoader`
- `ImpactInt`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `ImageResizeKJv2`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PrimitiveStringMultiline`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **98%**（47/48）

**有卡**：`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`Seed (rgthree)`、`SimpleMath+`、`CLIPVisionLoader`、`CLIPVisionEncode`、`UNETLoader`、`wanBlockSwap`、`easy forLoopEnd`、`easy batchAnything`、`easy forLoopStart`、`ImageResizeKJv2`、`LoadImage`、`ImpactInt`、`CLIPTextEncode`、`ImageScaleBy`、`VHS_VideoCombine`、`RIFE VFI`、`WanFirstLastFrameToVideo`、`easy cleanGpuUsed`、`VAEDecode`、`VAELoader`、`JWInteger`、`easy anythingIndexSwitch`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
