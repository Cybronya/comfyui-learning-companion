---
key: 视频生成/文生视频/Wan2.2 Smoothmix全自动提示词4步加速渲染工作流_2043337939740004354.json
name: Wan2.2 Smoothmix全自动提示词4步加速渲染工作流_2043337939740004354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Smoothmix全自动提示词4步加速渲染工作流_2043337939740004354.json
hash: 38fa5634d475a2f9
coverage: 0.804878
learned_at: 2026-10-11 19:49:43
nodes: [wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, VAELoader, ModelPatchTorchSettings, SimpleMath+, WanImageToVideo, Fast Bypasser (rgthree), VHS_VideoCombine, Fast Bypasser (rgthree), Seed (rgthree), CLIPTextEncode, RTXVideoSuperResolution, VAEDecode, ImageScaleBy, CLIPLoader, UNETLoader, UNETLoader, RTXVideoSuperResolution, llama_cpp_instruct_adv, ShowText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, llama_cpp_model_loader, VHS_VideoCombine, RIFE VFI, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, ImpactInt, ImpactInt, ImpactInt, PrimitiveStringMultiline]
patterns: []
missing: [Fast Bypasser (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), RIFE VFI, SimpleMath+, Seed (rgthree)]
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2 Smoothmix全自动提示词4步加速渲染工作流_2043337939740004354.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Smoothmix全自动提示词4步加速渲染工作流_2043337939740004354.json`

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
- `VHS_VideoCombine`
- `Fast Bypasser (rgthree)`
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `RTXVideoSuperResolution`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `RTXVideoSuperResolution`
- `llama_cpp_instruct_adv`
- `ShowText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `llama_cpp_model_loader`
- `VHS_VideoCombine`
- `RIFE VFI`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **80%**（33/41）

**有卡**：`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`VAELoader`、`WanImageToVideo`、`VHS_VideoCombine`、`CLIPTextEncode`、`RTXVideoSuperResolution`、`VAEDecode`、`ImageScaleBy`、`CLIPLoader`、`UNETLoader`、`llama_cpp_instruct_adv`、`ShowText`、`LoraLoaderModelOnly`、`llama_cpp_model_loader`、`KSamplerAdvanced`、`ImpactInt`

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
