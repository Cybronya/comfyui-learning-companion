---
key: 视频生成/文生视频/文生视频Wan2.2-Smooth Mix_2051648863991279617.json
name: 文生视频Wan2.2-Smooth Mix_2051648863991279617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频Wan2.2-Smooth Mix_2051648863991279617.json
hash: 69725aa52d462782
coverage: 0.971429
learned_at: 2026-10-15 22:48:43
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, VAELoader, ModelPatchTorchSettings, SimpleMath+, WanImageToVideo, Fast Bypasser (rgthree), Fast Bypasser (rgthree), Seed (rgthree), CLIPTextEncode, CLIPLoader, UNETLoader, RTXVideoSuperResolution, VHS_VideoCombine, ImpactInt, ImpactInt, ImpactInt, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, CLIPTextEncode, PrimitiveStringMultiline, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageScaleBy, VAEDecode, RIFE VFI]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/文生视频Wan2.2-Smooth Mix_2051648863991279617.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生视频Wan2.2-Smooth Mix_2051648863991279617.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
- `wanBlockSwap`
- `wanBlockSwap`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Bypasser (rgthree)`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAELoader`
- `ModelPatchTorchSettings`
- `SimpleMath+`
- `WanImageToVideo`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `RTXVideoSuperResolution`
- `VHS_VideoCombine`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageScaleBy`
- `VAEDecode` ★核心
- `RIFE VFI`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（34/35）

**有卡**：`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`VAELoader`、`SimpleMath+`、`WanImageToVideo`、`Seed (rgthree)`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`RTXVideoSuperResolution`、`VHS_VideoCombine`、`ImpactInt`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`ImageScaleBy`、`VAEDecode`、`RIFE VFI`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)
