---
key: 视频生成/图生视频/Wan2.2-Smooth+Mix+超丝滑电影探班++多图首尾帧 64帧_2000091759243915265.json
name: Wan2.2-Smooth+Mix+超丝滑电影探班++多图首尾帧 64帧_2000091759243915265.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Smooth+Mix+超丝滑电影探班++多图首尾帧 64帧_2000091759243915265.json
hash: c0ecf6af45600930
coverage: 0.98
learned_at: 2026-10-15 22:33:39
nodes: [Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, ImpactInt, Seed (rgthree), SimpleMath+, easy cleanGpuUsed, ImageScaleBy, CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, ImpactInt, ImpactInt, CLIPVisionLoader, WanFirstLastFrameToVideo, CLIPVisionEncode, CLIPVisionEncode, UNETLoader, UNETLoader, wanBlockSwap, wanBlockSwap, Fast Bypasser (rgthree), Fast Bypasser (rgthree), VAEDecode, easy forLoopEnd, easy batchAnything, PrimitiveStringMultiline, easy anythingIndexSwitch, easy forLoopStart, JWInteger, easy anythingIndexSwitch, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, KSamplerAdvanced, KSamplerAdvanced, ImageResizeKJv2, RIFE VFI, ImageResizeKJv2, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2-Smooth+Mix+超丝滑电影探班++多图首尾帧 64帧_2000091759243915265.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2000091759243915265.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（50 个）：
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
- `SimpleMath+`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `ImpactInt`
- `ImpactInt`
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
- `VAEDecode` ★核心
- `easy forLoopEnd`
- `easy batchAnything`
- `PrimitiveStringMultiline`
- `easy anythingIndexSwitch`
- `easy forLoopStart`
- `JWInteger`
- `easy anythingIndexSwitch`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImageResizeKJv2`
- `RIFE VFI`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **98%**（49/50）

**有卡**：`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`ImpactInt`、`Seed (rgthree)`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageScaleBy`、`CLIPTextEncode`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`CLIPVisionEncode`、`UNETLoader`、`wanBlockSwap`、`VAEDecode`、`easy forLoopEnd`、`easy batchAnything`、`easy anythingIndexSwitch`、`easy forLoopStart`、`JWInteger`、`LoadImage`、`KSamplerAdvanced`、`ImageResizeKJv2`、`RIFE VFI`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
