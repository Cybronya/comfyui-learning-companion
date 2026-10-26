---
key: 数字人/数字人/Wan2.2版Infinite无限数字人_2052260635089616897.json
name: Wan2.2版Infinite无限数字人_2052260635089616897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2版Infinite无限数字人_2052260635089616897.json
hash: ab75853dbd9d83d7
coverage: 0.472868
learned_at: 2026-10-26 01:58:00
nodes: [GetNode, SetNode, SetNode, SetNode, GetNode, PreviewAny, GetNode, CLIPTextEncode, CLIPTextEncode, easy indexAnything, GetNode, easy mathInt, easy indexAnything, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, SetNode, SetNode, CM_IntToFloat, SetNode, LazySwitch1way, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, TextInput_, VHS_VideoCombine, GetNode, GetNode, ColorMatch, SetNode, easy forLoopEnd, ImageBatch, GetNode, GetNode, GetNode, GetNode, GetNode, easy showAnything, easy promptLine, Any2ListNode, SetNode, CLIPLoader, GetNode, GetNode, GetNode, GetNode, easy forLoopStart, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, SetNode, PathchSageAttentionKJ, SetNode, UNETLoader, UNETLoader, GetNode, ColorMatch, SetNode, SetNode, GetNode, GetNode, PreviewAny, GetNode, GetNode, SetNode, GetNode, LoadAudio, AudioCrop, MelBandRoFormerModelLoader, SetNode, SetNode, MelBandRoFormerSampler, AudioInfo, GetNode, GetNode, GetNode, AudioEncoderEncode, SetNode, AudioEncoderLoader, ModelPatchLoader, SetNode, SetNode, SetNode, VAELoader, SetNode, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, GetNode, easy boolean, Int, PainterAudioCut, Display Any (rgthree), MarkdownNote, GetNode, JWInteger, VAEDecode, VAEDecode, ImageFromBatch, GetNode, ImageFromBatch, VHS_VideoCombine, LoadImage, GetNode, ImpactImageInfo, ImpactImageInfo, easy mathInt, PainterAI2V, PainterAI2V, MathExpression|pysssss, Display Any (rgthree), SetNode, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, easy mathInt]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 数字人/数字人/Wan2.2版Infinite无限数字人_2052260635089616897.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2版Infinite无限数字人_2052260635089616897.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（129 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `PreviewAny`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy indexAnything`
- `GetNode`
- `easy mathInt`
- `easy indexAnything`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LazySwitch1way`
- `GetNode`
- `SetNode`
- `SetNode`
- `CM_IntToFloat`
- `SetNode`
- `LazySwitch1way`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `TextInput_`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `ColorMatch`
- `SetNode`
- `easy forLoopEnd`
- `ImageBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `easy promptLine`
- `Any2ListNode`
- `SetNode`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy forLoopStart`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `GetNode`
- `ColorMatch`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LoadAudio`
- `AudioCrop`
- `MelBandRoFormerModelLoader`
- `SetNode`
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `AudioInfo`
- `GetNode`
- `GetNode`
- `GetNode`
- `AudioEncoderEncode`
- `SetNode`
- `AudioEncoderLoader`
- `ModelPatchLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `GetNode`
- `easy boolean`
- `Int`
- `PainterAudioCut`
- `Display Any (rgthree)`
- `MarkdownNote`
- `GetNode`
- `JWInteger`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch`
- `GetNode`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `LoadImage`
- `GetNode`
- `ImpactImageInfo`
- `ImpactImageInfo`
- `easy mathInt`
- `PainterAI2V`
- `PainterAI2V`
- `MathExpression|pysssss`
- `Display Any (rgthree)`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `easy mathInt`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **47%**（61/129）

**有卡**：`CLIPTextEncode`、`easy indexAnything`、`easy mathInt`、`LazySwitch1way`、`CM_IntToFloat`、`VHS_VideoCombine`、`TextInput_`、`ColorMatch`、`easy forLoopEnd`、`ImageBatch`、`easy promptLine`、`Any2ListNode`、`CLIPLoader`、`easy forLoopStart`、`KSamplerAdvanced`、`PathchSageAttentionKJ`、`UNETLoader`、`LoadAudio`、`AudioCrop`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`AudioInfo`、`AudioEncoderEncode`、`AudioEncoderLoader`、`ModelPatchLoader`、`VAELoader`、`ModelPatchTorchSettings`、`easy boolean`、`Int`、`PainterAudioCut`、`Display Any (rgthree)`、`JWInteger`、`VAEDecode`、`ImageFromBatch`、`LoadImage`、`ImpactImageInfo`、`PainterAI2V`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、MelBandRoFormerSampler
