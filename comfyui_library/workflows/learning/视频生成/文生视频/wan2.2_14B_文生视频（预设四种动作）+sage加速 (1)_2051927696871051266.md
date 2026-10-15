---
key: 视频生成/文生视频/wan2.2_14B_文生视频（预设四种动作）+sage加速 (1)_2051927696871051266.json
name: wan2.2_14B_文生视频（预设四种动作）+sage加速 (1)_2051927696871051266
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2_14B_文生视频（预设四种动作）+sage加速 (1)_2051927696871051266.json
hash: 22700b8c8ea063d9
coverage: 0.636364
learned_at: 2026-10-15 22:47:35
nodes: [SetNode, SetNode, SetNode, SetNode, Bookmark (rgthree), SetNode, GetNode, SetNode, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), StringConcatenate, StringConcatenate, GetNode, SetNode, Label (rgthree), Label (rgthree), Label (rgthree), PrimitiveString, PrimitiveString, PrimitiveString, Label (rgthree), SetNode, CLIPTextEncode, CLIPTextEncode, Mute / Bypass Repeater (rgthree), GetNode, GetNode, GetNode, GetNode, GetNode, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Relay (rgthree), WanImageToVideo, GetNode, Mute / Bypass Repeater (rgthree), Any Switch (rgthree), PathchSageAttentionKJ, Any Switch (rgthree), PathchSageAttentionKJ, LoadImage, CLIPLoader, VAELoader, UNETLoader, UNETLoader, easy seed, KSamplerAdvanced, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, MarkdownNote, SetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, text_mul_Join, PrimitiveStringMultiline, PrimitiveStringMultiline, SaveImage, GetNode, easy int, TT_img_enc_v2, VHS_VideoCombine, Int, Int, VAEDecode, easy cleanGpuUsed, KSamplerAdvanced, easy cleanGpuUsed, ModelSamplingSD3, ModelSamplingSD3, easy cleanGpuUsed, easy cleanGpuUsed, UNETLoader, easy cleanGpuUsed, Int, 1hew_AnySwitchSelect, easy int, easy int, SimpleMath+, Int, Int, Any Switch (rgthree), EmptyHunyuanLatentVideo]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/wan2.2_14B_文生视频（预设四种动作）+sage加速 (1)_2051927696871051266.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2_14B_文生视频（预设四种动作）+sage加速 (1)_2051927696871051266.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（88 个）：
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
- `Mute / Bypass Repeater (rgthree)`
- `GetNode`
- `GetNode`
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
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `SetNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `text_mul_Join`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `SaveImage`
- `GetNode`
- `easy int`
- `TT_img_enc_v2`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `Int`
- `1hew_AnySwitchSelect`
- `easy int`
- `easy int`
- `SimpleMath+`
- `Int`
- `Int`
- `Any Switch (rgthree)`
- `EmptyHunyuanLatentVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **64%**（56/88）

**有卡**：`Bookmark (rgthree)`、`Label (rgthree)`、`StringConcatenate`、`CLIPTextEncode`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Relay (rgthree)`、`WanImageToVideo`、`PathchSageAttentionKJ`、`LoadImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`easy seed`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`text_mul_Join`、`SaveImage`、`easy int`、`TT_img_enc_v2`、`VHS_VideoCombine`、`Int`、`VAEDecode`、`easy cleanGpuUsed`、`ModelSamplingSD3`、`1hew_AnySwitchSelect`、`SimpleMath+`、`EmptyHunyuanLatentVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
