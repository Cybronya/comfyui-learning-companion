---
key: 视频生成/文生视频/文生视频Wan2.2 GGUF 4步采样生成1k视频_2050852999907557378.json
name: 文生视频Wan2.2 GGUF 4步采样生成1k视频_2050852999907557378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频Wan2.2 GGUF 4步采样生成1k视频_2050852999907557378.json
hash: 79621f00e6bc901c
coverage: 0.805556
learned_at: 2026-10-11 19:49:49
nodes: [PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, VAELoader, ModelPatchTorchSettings, SimpleMath+, WanImageToVideo, Seed (rgthree), CLIPTextEncode, VAEDecode, ImageScaleBy, CLIPLoader, ImpactInt, ImpactInt, ImpactInt, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, RTXVideoSuperResolution, RTXVideoSuperResolution, Fast Bypasser (rgthree), Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), wanBlockSwap, wanBlockSwap, VHS_VideoCombine, UnetLoaderGGUF, UnetLoaderGGUF, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, PrimitiveStringMultiline]
patterns: []
missing: [Fast Bypasser (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), SimpleMath+, Seed (rgthree)]
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **81%**（29/36）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`VAELoader`、`WanImageToVideo`、`CLIPTextEncode`、`VAEDecode`、`ImageScaleBy`、`CLIPLoader`、`ImpactInt`、`LoraLoaderModelOnly`、`RTXVideoSuperResolution`、`wanBlockSwap`、`VHS_VideoCombine`、`UnetLoaderGGUF`、`KSamplerAdvanced`

**缺卡**（6）：`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`SimpleMath+`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、KSamplerAdvanced、RTXVideoSuperResolution、ImageScaleBy

## 学习发现

- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
