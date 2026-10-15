---
key: 视频生成/文生视频/wan2.2_14B_文生图生视频_lightX加速版_1950129708211027969.json
name: wan2.2_14B_文生图生视频_lightX加速版_1950129708211027969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2_14B_文生图生视频_lightX加速版_1950129708211027969.json
hash: 8fac2bbd9df56e82
coverage: 0.623188
learned_at: 2026-10-15 22:47:35
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, Bookmark (rgthree), SetNode, GetNode, GetNode, SetNode, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), StringConcatenate, StringConcatenate, GetNode, SetNode, Label (rgthree), Label (rgthree), Label (rgthree), PrimitiveString, PrimitiveString, PrimitiveString, Label (rgthree), SetNode, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, Mute / Bypass Repeater (rgthree), GetNode, GetNode, ModelSamplingSD3, Any Switch (rgthree), ModelSamplingSD3, GetNode, GetNode, GetNode, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Relay (rgthree), WanImageToVideo, GetNode, Mute / Bypass Repeater (rgthree), MarkdownNote, VAEDecode, Any Switch (rgthree), PathchSageAttentionKJ, Any Switch (rgthree), PathchSageAttentionKJ, LoadImage, UNETLoader, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, easy int, easy seed, easy int, easy int, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/wan2.2_14B_文生图生视频_lightX加速版_1950129708211027969.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2_14B_文生图生视频_lightX加速版_1950129708211027969.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（69 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Bookmark (rgthree)`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `StringConcatenate`
- `StringConcatenate`
- `GetNode`
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `PrimitiveString`
- `PrimitiveString`
- `PrimitiveString`
- `Label (rgthree)`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `Mute / Bypass Repeater (rgthree)`
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `Any Switch (rgthree)`
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `GetNode`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Relay (rgthree)`
- `WanImageToVideo`
- `GetNode`
- `Mute / Bypass Repeater (rgthree)`
- `MarkdownNote`
- `VAEDecode` ★核心
- `Any Switch (rgthree)`
- `PathchSageAttentionKJ`
- `Any Switch (rgthree)`
- `PathchSageAttentionKJ`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `easy int`
- `easy seed`
- `easy int`
- `easy int`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **62%**（43/69）

**有卡**：`Bookmark (rgthree)`、`Label (rgthree)`、`StringConcatenate`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`Mute / Bypass Repeater (rgthree)`、`ModelSamplingSD3`、`Mute / Bypass Relay (rgthree)`、`WanImageToVideo`、`VAEDecode`、`PathchSageAttentionKJ`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`VHS_VideoCombine`、`easy int`、`easy seed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
