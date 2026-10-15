---
key: 视频生成/文生视频/文生视频Wan2.2 GGUF 4步采样生成1k视频_2050852999907557378.json
name: 文生视频Wan2.2 GGUF 4步采样生成1k视频_2050852999907557378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频Wan2.2 GGUF 4步采样生成1k视频_2050852999907557378.json
hash: 79621f00e6bc901c
coverage: 0.972222
learned_at: 2026-10-15 22:48:43
nodes: [PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, VAELoader, ModelPatchTorchSettings, SimpleMath+, WanImageToVideo, Seed (rgthree), CLIPTextEncode, VAEDecode, ImageScaleBy, CLIPLoader, ImpactInt, ImpactInt, ImpactInt, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, RTXVideoSuperResolution, RTXVideoSuperResolution, Fast Bypasser (rgthree), Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), wanBlockSwap, wanBlockSwap, VHS_VideoCombine, UnetLoaderGGUF, UnetLoaderGGUF, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/文生视频Wan2.2 GGUF 4步采样生成1k视频_2050852999907557378.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生视频Wan2.2 GGUF 4步采样生成1k视频_2050852999907557378.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（36 个）：
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
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ImageScaleBy`
- `CLIPLoader`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `RTXVideoSuperResolution`
- `RTXVideoSuperResolution`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `wanBlockSwap`
- `wanBlockSwap`
- `VHS_VideoCombine`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（35/36）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`VAELoader`、`SimpleMath+`、`WanImageToVideo`、`Seed (rgthree)`、`CLIPTextEncode`、`VAEDecode`、`ImageScaleBy`、`CLIPLoader`、`ImpactInt`、`LoraLoaderModelOnly`、`RTXVideoSuperResolution`、`Mute / Bypass Repeater (rgthree)`、`wanBlockSwap`、`VHS_VideoCombine`、`UnetLoaderGGUF`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、KSamplerAdvanced、Seed (rgthree)、RTXVideoSuperResolution
