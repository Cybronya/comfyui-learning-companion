---
key: 视频生成/文生视频/极速渲染优化！Wan2.2 SmoothMix+RTX+Qwen3.5提示词优化_2048029118243020801.json
name: 极速渲染优化！Wan2.2 SmoothMix+RTX+Qwen3.5提示词优化_2048029118243020801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/极速渲染优化！Wan2.2 SmoothMix+RTX+Qwen3.5提示词优化_2048029118243020801.json
hash: 5274090f7a05c163
coverage: 0.976744
learned_at: 2026-10-15 22:48:49
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, SimpleMath+, Fast Bypasser (rgthree), Fast Bypasser (rgthree), Seed (rgthree), ImageScaleBy, RTXVideoSuperResolution, ShowText, VHS_VideoCombine, llama_cpp_instruct_adv, llama_cpp_model_loader, ImpactInt, ImpactInt, ImpactInt, KSamplerAdvanced, KSamplerAdvanced, ShowText, llama_cpp_instruct_adv, VHS_VideoCombine, RTXVideoSuperResolution, UNETLoader, ModelSamplingSD3, UNETLoader, ModelSamplingSD3, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, RIFE VFI, CLIPTextEncode, CLIPTextEncode, VAEDecode, WanImageToVideo, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/极速渲染优化！Wan2.2 SmoothMix+RTX+Qwen3.5提示词优化_2048029118243020801.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/极速渲染优化！Wan2.2 SmoothMix+RTX+Qwen3.5提示词优化_2048029118243020801.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（43 个）：
- `wanBlockSwap`
- `wanBlockSwap`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Bypasser (rgthree)`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `SimpleMath+`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `Seed (rgthree)`
- `ImageScaleBy`
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
- `ShowText`
- `llama_cpp_instruct_adv`
- `VHS_VideoCombine`
- `RTXVideoSuperResolution`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RIFE VFI`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `WanImageToVideo`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **98%**（42/43）

**有卡**：`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`SimpleMath+`、`Seed (rgthree)`、`ImageScaleBy`、`RTXVideoSuperResolution`、`ShowText`、`VHS_VideoCombine`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`ImpactInt`、`KSamplerAdvanced`、`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`RIFE VFI`、`CLIPTextEncode`、`VAEDecode`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)
