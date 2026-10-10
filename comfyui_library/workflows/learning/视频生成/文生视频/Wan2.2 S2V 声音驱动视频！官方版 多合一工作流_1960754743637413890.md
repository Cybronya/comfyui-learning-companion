---
key: 视频生成/文生视频/Wan2.2 S2V 声音驱动视频！官方版 多合一工作流_1960754743637413890.json
name: Wan2.2 S2V 声音驱动视频！官方版 多合一工作流_1960754743637413890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 S2V 声音驱动视频！官方版 多合一工作流_1960754743637413890.json
hash: a3fa8f0d034dee5c
coverage: 0.32967
learned_at: 2026-10-10 23:06:55
nodes: [Reroute, Label (rgthree), Reroute, Reroute, Label (rgthree), Label (rgthree), Label (rgthree), Reroute, Label (rgthree), Label (rgthree), Bookmark (rgthree), Note Plus (mtb), SetNode, Label (rgthree), StringConcatenate, StringConcatenate, GetNode, SetNode, SetNode, Mute / Bypass Repeater (rgthree), Any Switch (rgthree), SetNode, SetNode, GetNode, SetNode, DepthAnythingV2Preprocessor, SetNode, Label (rgthree), GetNode, Label (rgthree), Label (rgthree), SetNode, Label (rgthree), PathchSageAttentionKJ, SetNode, DeepTranslatorTextNode, WanSoundImageToVideo, GetNode, ModelSamplingSD3, PreviewAny, GetNode, VAEDecode, SetNode, AudioEncoderEncode, GetNode, Label (rgthree), PrimitiveString, PrimitiveString, PrimitiveString, Mute / Bypass Relay (rgthree), GetNode, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SetNode, GetNode, GetNode, GetNode, CLIPTextEncode, Label (rgthree), ImageResizeKJv2, DWPreprocessor, VAELoader, AudioEncoderLoader, CLIPTextEncode, GetNode, ImageResizeKJv2, ImageResizeKJ, GetNode, GetNode, LoadImage, Fast Groups Muter (rgthree), MarkdownNote, easy int, KSampler, TorchCompileModel, TorchCompileModelWanVideoV2, easy seed, VHS_LoadVideo, easy int, easy int, PrimitiveStringMultiline, CLIPLoader, UNETLoader, LoadAudio, AudioSeparation, SaveAudioMP3, SaveAudioOpus, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: [Bookmark (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), Note Plus (mtb), easy int, easy int, easy int, easy seed]
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 666, "steps": 20}
discoveries: [次要节点 `Bookmark (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Relay (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2 S2V 声音驱动视频！官方版 多合一工作流_1960754743637413890.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 S2V 声音驱动视频！官方版 多合一工作流_1960754743637413890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（91 个）：
- `Reroute`
- `Label (rgthree)`
- `Reroute`
- `Reroute`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Reroute`
- `Label (rgthree)`
- `Label (rgthree)`
- `Bookmark (rgthree)`
- `Note Plus (mtb)`
- `SetNode`
- `Label (rgthree)`
- `StringConcatenate`
- `StringConcatenate`
- `GetNode`
- `SetNode`
- `SetNode`
- `Mute / Bypass Repeater (rgthree)`
- `Any Switch (rgthree)`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `DepthAnythingV2Preprocessor`
- `SetNode`
- `Label (rgthree)`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `Label (rgthree)`
- `PathchSageAttentionKJ`
- `SetNode`
- `DeepTranslatorTextNode`
- `WanSoundImageToVideo`
- `GetNode`
- `ModelSamplingSD3`
- `PreviewAny`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `AudioEncoderEncode`
- `GetNode`
- `Label (rgthree)`
- `PrimitiveString`
- `PrimitiveString`
- `PrimitiveString`
- `Mute / Bypass Relay (rgthree)`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `Label (rgthree)`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `VAELoader`
- `AudioEncoderLoader`
- `CLIPTextEncode` ★核心
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJ`
- `GetNode`
- `GetNode`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `MarkdownNote`
- `easy int`
- `KSampler` ★核心
- `TorchCompileModel`
- `TorchCompileModelWanVideoV2`
- `easy seed`
- `VHS_LoadVideo`
- `easy int`
- `easy int`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadAudio`
- `AudioSeparation`
- `SaveAudioMP3`
- `SaveAudioOpus`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `666`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **33%**（30/91）

**有卡**：`StringConcatenate`、`DepthAnythingV2Preprocessor`、`PathchSageAttentionKJ`、`DeepTranslatorTextNode`、`WanSoundImageToVideo`、`ModelSamplingSD3`、`VAEDecode`、`AudioEncoderEncode`、`CLIPTextEncode`、`ImageResizeKJv2`、`DWPreprocessor`、`VAELoader`、`AudioEncoderLoader`、`ImageResizeKJ`、`LoadImage`、`KSampler`、`TorchCompileModel`、`TorchCompileModelWanVideoV2`、`VHS_LoadVideo`、`CLIPLoader`、`UNETLoader`、`LoadAudio`、`AudioSeparation`、`SaveAudioMP3`、`SaveAudioOpus`、`VHS_VideoCombine`

**缺卡**（25）：`Bookmark (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Mute / Bypass Relay (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`Note Plus (mtb)`、`easy int`、`easy int`、`easy int`、`easy seed`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、DepthAnythingV2Preprocessor

## 学习发现

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
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Relay (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
