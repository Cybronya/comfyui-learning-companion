---
key: 视频生成/文生视频/wan2.2 SmoothMix V3.0高动态电影质感 文生视频+补帧_2041684980501323777.json
name: wan2.2 SmoothMix V3.0高动态电影质感 文生视频+补帧_2041684980501323777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2 SmoothMix V3.0高动态电影质感 文生视频+补帧_2041684980501323777.json
hash: 3ff5de5327502ee9
coverage: 0.972222
learned_at: 2026-10-15 22:47:34
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, VAEDecode, RIFE VFI, SimpleMath+, easy cleanGpuUsed, ImageScaleBy, CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, WanImageToVideo, KSamplerAdvanced, KSamplerAdvanced, Fast Bypasser (rgthree), Fast Bypasser (rgthree), Seed (rgthree), VHS_VideoCombine, UNETLoader, easy promptConcat, ImpactInt, ImpactInt, VHS_VideoCombine, UNETLoader, PrimitiveStringMultiline, Wan22PromptSelector, ImpactInt]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/wan2.2 SmoothMix V3.0高动态电影质感 文生视频+补帧_2041684980501323777.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2 SmoothMix V3.0高动态电影质感 文生视频+补帧_2041684980501323777.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（36 个）：
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
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `Seed (rgthree)`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `easy promptConcat`
- `ImpactInt`
- `ImpactInt`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `Wan22PromptSelector`
- `ImpactInt`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（35/36）

**有卡**：`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`RIFE VFI`、`SimpleMath+`、`easy cleanGpuUsed`、`ImageScaleBy`、`CLIPTextEncode`、`WanImageToVideo`、`KSamplerAdvanced`、`Seed (rgthree)`、`VHS_VideoCombine`、`UNETLoader`、`easy promptConcat`、`ImpactInt`、`Wan22PromptSelector`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)、Wan22PromptSelector
