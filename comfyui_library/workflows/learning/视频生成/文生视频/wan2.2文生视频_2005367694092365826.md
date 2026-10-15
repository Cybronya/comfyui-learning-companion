---
key: 视频生成/文生视频/wan2.2文生视频_2005367694092365826.json
name: wan2.2文生视频_2005367694092365826
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频_2005367694092365826.json
hash: abc349cae2f2c4b5
coverage: 0.970588
learned_at: 2026-10-15 22:47:36
nodes: [KSamplerAdvanced, wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, ModelPatchTorchSettings, ImpactInt, ImpactInt, Seed (rgthree), VAEDecode, RIFE VFI, SimpleMath+, WanImageToVideo, easy cleanGpuUsed, ImageScaleBy, CLIPTextEncode, easy cleanGpuUsed, KSamplerAdvanced, Fast Bypasser (rgthree), Fast Bypasser (rgthree), CLIPTextEncode, VHS_VideoCombine, VHS_VideoCombine, UNETLoader, UNETLoader, CLIPLoader, VAELoader, ImpactInt, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/wan2.2文生视频_2005367694092365826.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频_2005367694092365826.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（34 个）：
- `KSamplerAdvanced` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Bypasser (rgthree)`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `ImpactInt`
- `ImpactInt`
- `Seed (rgthree)`
- `VAEDecode` ★核心
- `RIFE VFI`
- `SimpleMath+`
- `WanImageToVideo`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImpactInt`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（33/34）

**有卡**：`KSamplerAdvanced`、`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`ImpactInt`、`Seed (rgthree)`、`VAEDecode`、`RIFE VFI`、`SimpleMath+`、`WanImageToVideo`、`easy cleanGpuUsed`、`ImageScaleBy`、`CLIPTextEncode`、`VHS_VideoCombine`、`UNETLoader`、`CLIPLoader`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)、ImageScaleBy
