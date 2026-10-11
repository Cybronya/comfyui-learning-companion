---
key: 视频生成/文生视频/极速渲染优化！Wan2.2 SmoothMix+RTX+Qwen3.5提示词优化_2048029118243020801.json
name: 极速渲染优化！Wan2.2 SmoothMix+RTX+Qwen3.5提示词优化_2048029118243020801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/极速渲染优化！Wan2.2 SmoothMix+RTX+Qwen3.5提示词优化_2048029118243020801.json
hash: 5274090f7a05c163
coverage: 0.813953
learned_at: 2026-10-11 19:49:50
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, SimpleMath+, Fast Bypasser (rgthree), Fast Bypasser (rgthree), Seed (rgthree), ImageScaleBy, RTXVideoSuperResolution, ShowText, VHS_VideoCombine, llama_cpp_instruct_adv, llama_cpp_model_loader, ImpactInt, ImpactInt, ImpactInt, KSamplerAdvanced, KSamplerAdvanced, ShowText, llama_cpp_instruct_adv, VHS_VideoCombine, RTXVideoSuperResolution, UNETLoader, ModelSamplingSD3, UNETLoader, ModelSamplingSD3, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, RIFE VFI, CLIPTextEncode, CLIPTextEncode, VAEDecode, WanImageToVideo, PrimitiveStringMultiline]
patterns: []
missing: [Fast Bypasser (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), RIFE VFI, SimpleMath+, Seed (rgthree)]
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **81%**（35/43）

**有卡**：`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ImageScaleBy`、`RTXVideoSuperResolution`、`ShowText`、`VHS_VideoCombine`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`ImpactInt`、`KSamplerAdvanced`、`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`VAEDecode`、`WanImageToVideo`

**缺卡**（7）：`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`RIFE VFI`、`SimpleMath+`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、RTXVideoSuperResolution

## 学习发现

- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
