---
key: 视频生成/文生视频/wan2.2_14B_文生视频（预设四种动作）+sage加速 (1)_2051901085580840962.json
name: wan2.2_14B_文生视频（预设四种动作）+sage加速 (1)_2051901085580840962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2_14B_文生视频（预设四种动作）+sage加速 (1)_2051901085580840962.json
hash: 9cd52e69e6e57e46
coverage: 0.614458
learned_at: 2026-10-15 22:47:35
nodes: [SetNode, SetNode, SetNode, SetNode, Bookmark (rgthree), SetNode, GetNode, SetNode, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), StringConcatenate, StringConcatenate, GetNode, SetNode, Label (rgthree), Label (rgthree), Label (rgthree), PrimitiveString, PrimitiveString, PrimitiveString, Label (rgthree), SetNode, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, Mute / Bypass Repeater (rgthree), GetNode, GetNode, Any Switch (rgthree), ModelSamplingSD3, GetNode, GetNode, GetNode, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Relay (rgthree), WanImageToVideo, GetNode, Mute / Bypass Repeater (rgthree), Any Switch (rgthree), PathchSageAttentionKJ, Any Switch (rgthree), PathchSageAttentionKJ, LoadImage, CLIPLoader, VAELoader, UNETLoader, UNETLoader, easy seed, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, MarkdownNote, SetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, Int, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, 1hew_AnySwitchSelect, text_mul_Join, PrimitiveStringMultiline, PrimitiveStringMultiline, VAEDecode, SaveImage, GetNode, easy int, easy int, TT_img_enc_v2, VHS_VideoCombine, Int, easy int, Int, SimpleMath+, Int, Int]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/wan2.2_14B_文生视频（预设四种动作）+sage加速 (1)_2051901085580840962.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2_14B_文生视频（预设四种动作）+sage加速 (1)_2051901085580840962.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（83 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Bookmark (rgthree)`
- `SetNode`
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
- `Any Switch (rgthree)`
- `PathchSageAttentionKJ`
- `Any Switch (rgthree)`
- `PathchSageAttentionKJ`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `easy seed`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `SetNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `Int`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `1hew_AnySwitchSelect`
- `text_mul_Join`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `SaveImage`
- `GetNode`
- `easy int`
- `easy int`
- `TT_img_enc_v2`
- `VHS_VideoCombine`
- `Int`
- `easy int`
- `Int`
- `SimpleMath+`
- `Int`
- `Int`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **61%**（51/83）

**有卡**：`Bookmark (rgthree)`、`Label (rgthree)`、`StringConcatenate`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`Mute / Bypass Repeater (rgthree)`、`ModelSamplingSD3`、`Mute / Bypass Relay (rgthree)`、`WanImageToVideo`、`PathchSageAttentionKJ`、`LoadImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`easy seed`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`Int`、`1hew_AnySwitchSelect`、`text_mul_Join`、`VAEDecode`、`SaveImage`、`easy int`、`TT_img_enc_v2`、`VHS_VideoCombine`、`SimpleMath+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
