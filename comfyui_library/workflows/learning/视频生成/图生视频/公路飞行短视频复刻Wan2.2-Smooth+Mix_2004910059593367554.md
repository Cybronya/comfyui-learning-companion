---
key: 视频生成/图生视频/公路飞行短视频复刻Wan2.2-Smooth+Mix_2004910059593367554.json
name: 公路飞行短视频复刻Wan2.2-Smooth+Mix_2004910059593367554.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/公路飞行短视频复刻Wan2.2-Smooth+Mix_2004910059593367554.json
hash: a3937563d7a2a69b
coverage: 0.971429
learned_at: 2026-10-15 22:33:55
nodes: [Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, VAELoader, ModelPatchTorchSettings, Seed (rgthree), easy cleanGpuUsed, CLIPTextEncode, CLIPTextEncode, UNETLoader, UNETLoader, wanBlockSwap, wanBlockSwap, Fast Bypasser (rgthree), Fast Bypasser (rgthree), LoadImage, SimpleMath+, VAEDecode, ImpactInt, ImpactInt, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, PrimitiveStringMultiline, VHS_VideoCombine, ImpactInt, KSamplerAdvanced, KSamplerAdvanced, ImageResizeKJv2, WanFirstLastFrameToVideo, CLIPVisionEncode, CLIPVisionLoader, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/公路飞行短视频复刻Wan2.2-Smooth+Mix_2004910059593367554.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2004910059593367554.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Bypasser (rgthree)`
- `PathchSageAttentionKJ`
- `VAELoader`
- `ModelPatchTorchSettings`
- `Seed (rgthree)`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `LoadImage`
- `SimpleMath+`
- `VAEDecode` ★核心
- `ImpactInt`
- `ImpactInt`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `ImpactInt`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImageResizeKJv2`
- `WanFirstLastFrameToVideo`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（34/35）

**有卡**：`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`VAELoader`、`Seed (rgthree)`、`easy cleanGpuUsed`、`CLIPTextEncode`、`UNETLoader`、`wanBlockSwap`、`LoadImage`、`SimpleMath+`、`VAEDecode`、`ImpactInt`、`ModelSamplingSD3`、`CLIPLoader`、`VHS_VideoCombine`、`KSamplerAdvanced`、`ImageResizeKJv2`、`WanFirstLastFrameToVideo`、`CLIPVisionEncode`、`CLIPVisionLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
