---
key: 视频生成/文生视频/wan2.2_14B官方版本_全功能_1954176509042946049.json
name: wan2.2_14B官方版本_全功能_1954176509042946049
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2_14B官方版本_全功能_1954176509042946049.json
hash: 076a119ad2a8842f
coverage: 0.351648
learned_at: 2026-10-10 23:09:43
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, Label (rgthree), StringConcatenate, StringConcatenate, GetNode, SetNode, PrimitiveString, PrimitiveString, Any Switch (rgthree), CLIPLoader, SetNode, SetNode, SetNode, Label (rgthree), ModelSamplingSD3, GetNode, SetNode, GetNode, ModelSamplingSD3, Mute / Bypass Relay (rgthree), Any Switch (rgthree), EmptyHunyuanLatentVideo, GetNode, GetNode, PathchSageAttentionKJ, TorchCompileModelWanVideoV2, PathchSageAttentionKJ, TorchCompileModelWanVideoV2, Bookmark (rgthree), Bookmark (rgthree), Label (rgthree), Mute / Bypass Repeater (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), PrimitiveString, SetNode, GetNode, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), Label (rgthree), GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, VAEDecodeTiled, VAEDecode, GetNode, KSamplerAdvanced, KSamplerAdvanced, GetNode, GetNode, Any Switch (rgthree), Any Switch (rgthree), Any Switch (rgthree), VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, UNETLoader, Label (rgthree), Label (rgthree), WanImageToVideo, WanFirstLastFrameToVideo, MarkdownNote, LoadImage, PrimitiveFloat, LoadImage, Fast Groups Muter (rgthree), easy int, easy int, PrimitiveStringMultiline, easy int, UNETLoader, VHS_VideoCombine, easy int, easy int, easy seed, LoraLoaderModelOnly, ImageResizeKJv2, ImageResizeKJv2, LoraLoaderModelOnly]
patterns: []
missing: [Bookmark (rgthree), Bookmark (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Mute / Bypass Relay (rgthree), Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), easy int, easy int, easy int, easy int, easy int, easy seed]
parameters: {"cfg": 9, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `Bookmark (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Bookmark (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Relay (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Relay (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/wan2.2_14B官方版本_全功能_1954176509042946049.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2_14B官方版本_全功能_1954176509042946049.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（91 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Label (rgthree)`
- `StringConcatenate`
- `StringConcatenate`
- `GetNode`
- `SetNode`
- `PrimitiveString`
- `PrimitiveString`
- `Any Switch (rgthree)`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `Label (rgthree)`
- `ModelSamplingSD3`
- `GetNode`
- `SetNode`
- `GetNode`
- `ModelSamplingSD3`
- `Mute / Bypass Relay (rgthree)`
- `Any Switch (rgthree)`
- `EmptyHunyuanLatentVideo`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `TorchCompileModelWanVideoV2`
- `PathchSageAttentionKJ`
- `TorchCompileModelWanVideoV2`
- `Bookmark (rgthree)`
- `Bookmark (rgthree)`
- `Label (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `PrimitiveString`
- `SetNode`
- `GetNode`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Label (rgthree)`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `WanImageToVideo`
- `WanFirstLastFrameToVideo`
- `MarkdownNote`
- `LoadImage`
- `PrimitiveFloat`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `easy int`
- `easy int`
- `PrimitiveStringMultiline`
- `easy int`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `easy int`
- `easy int`
- `easy seed`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `9`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **35%**（32/91）

**有卡**：`StringConcatenate`、`CLIPLoader`、`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`PathchSageAttentionKJ`、`TorchCompileModelWanVideoV2`、`CLIPTextEncode`、`VAEDecodeTiled`、`VAEDecode`、`KSamplerAdvanced`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`WanImageToVideo`、`WanFirstLastFrameToVideo`、`LoadImage`、`VHS_VideoCombine`、`ImageResizeKJv2`

**缺卡**（21）：`Bookmark (rgthree)`、`Bookmark (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Mute / Bypass Relay (rgthree)`、`Mute / Bypass Relay (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`easy int`、`easy int`、`easy int`、`easy int`、`easy int`、`easy seed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `Bookmark (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Bookmark (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Relay (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Relay (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
