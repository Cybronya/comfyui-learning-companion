---
key: 视频生成/文生视频/🌈老许Gary：文生视频Wan2.2-Smooth Mix_2045834738073604098.json
name: 🌈老许Gary：文生视频Wan2.2-Smooth Mix_2045834738073604098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/🌈老许Gary：文生视频Wan2.2-Smooth Mix_2045834738073604098.json
hash: 6b14de142da4a459
coverage: 0.97561
learned_at: 2026-10-15 22:49:13
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, VAELoader, ModelPatchTorchSettings, SimpleMath+, WanImageToVideo, Fast Bypasser (rgthree), Fast Bypasser (rgthree), Seed (rgthree), CLIPTextEncode, VAEDecode, ImageScaleBy, CLIPTextEncode, CLIPLoader, UNETLoader, UNETLoader, RIFE VFI, RTXVideoSuperResolution, ShowText, VHS_VideoCombine, llama_cpp_instruct_adv, llama_cpp_model_loader, ImpactInt, ImpactInt, ImpactInt, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, ShowText, llama_cpp_instruct_adv, RTXVideoSuperResolution, PrimitiveStringMultiline, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/🌈老许Gary：文生视频Wan2.2-Smooth Mix_2045834738073604098.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/🌈老许Gary：文生视频Wan2.2-Smooth Mix_2045834738073604098.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（41 个）：
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
- `VAEDecode` ★核心
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `RIFE VFI`
- `RTXVideoSuperResolution`
- `ShowText`
- `VHS_VideoCombine`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ShowText`
- `llama_cpp_instruct_adv`
- `RTXVideoSuperResolution`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **98%**（40/41）

**有卡**：`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`ModelSamplingSD3`、`VAELoader`、`SimpleMath+`、`WanImageToVideo`、`Seed (rgthree)`、`CLIPTextEncode`、`VAEDecode`、`ImageScaleBy`、`CLIPLoader`、`UNETLoader`、`RIFE VFI`、`RTXVideoSuperResolution`、`ShowText`、`VHS_VideoCombine`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`ImpactInt`、`KSamplerAdvanced`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)
