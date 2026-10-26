---
key: 数字人/数字人/魔改-官流infinitetalk-wan2.2_2018585403422416898.json
name: 魔改-官流infinitetalk-wan2.2_2018585403422416898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/魔改-官流infinitetalk-wan2.2_2018585403422416898.json
hash: edb032bb6eed5dbb
coverage: 0.688312
learned_at: 2026-10-26 02:06:09
nodes: [LoadAudio, Reroute, UNETLoader, Reroute, Reroute, UNETLoader, Reroute, ModelPatchLoader, LoraLoaderModelOnly, CLIPLoader, Reroute, Reroute, Reroute, WanImageToVideo, KSamplerAdvanced, WanInfiniteTalkToVideo, LatentComposite, KSamplerAdvanced, VAEDecode, ImageFromBatch, Reroute, Reroute, Reroute, Reroute, CLIPVisionLoader, LoadImage, AudioEncoderEncode, Reroute, SimpleMath+, Audio Duration (mtb), Reroute, Reroute, Reroute, Int, Int, Seed Generator, CLIPVisionEncode, Reroute, PrimitiveInt, PrimitiveInt, easy forLoopEnd, VAEDecode, AudioEncoderLoader, VHS_VideoCombine, ImageFromBatch, VAELoader, PreviewAudio, ImageFromBatch, ImageBatch, easy forLoopStart, easy showAnything, LatentComposite, KSamplerAdvanced, KSamplerAdvanced, WanInfiniteTalkToVideo, WanImageToVideo, Fast Groups Bypasser (rgthree), Int, LoadAudio, AudioEncoderEncode, MelBandRoFormerSampler, MelBandRoFormerModelLoader, MarkdownNote, MarkdownNote, LoadImage, MarkdownNote, ConditioningZeroOut, LoraLoaderModelOnly, LoraLoaderModelOnly, MathExpression|pysssss, VHS_VideoCombine, ImageFromBatch, AudioConcat, VHS_VideoCombine, MarkdownNote, AudioCrop, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 数字人/数字人/魔改-官流infinitetalk-wan2.2_2018585403422416898.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/魔改-官流infinitetalk-wan2.2_2018585403422416898.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（77 个）：
- `LoadAudio`
- `Reroute`
- `UNETLoader` ★核心
- `Reroute`
- `Reroute`
- `UNETLoader` ★核心
- `Reroute`
- `ModelPatchLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `WanInfiniteTalkToVideo`
- `LatentComposite`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPVisionLoader`
- `LoadImage`
- `AudioEncoderEncode`
- `Reroute`
- `SimpleMath+`
- `Audio Duration (mtb)`
- `Reroute`
- `Reroute`
- `Reroute`
- `Int`
- `Int`
- `Seed Generator`
- `CLIPVisionEncode`
- `Reroute`
- `PrimitiveInt`
- `PrimitiveInt`
- `easy forLoopEnd`
- `VAEDecode` ★核心
- `AudioEncoderLoader`
- `VHS_VideoCombine`
- `ImageFromBatch`
- `VAELoader`
- `PreviewAudio`
- `ImageFromBatch`
- `ImageBatch`
- `easy forLoopStart`
- `easy showAnything`
- `LatentComposite`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanInfiniteTalkToVideo`
- `WanImageToVideo`
- `Fast Groups Bypasser (rgthree)`
- `Int`
- `LoadAudio`
- `AudioEncoderEncode`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `MarkdownNote`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `ImageFromBatch`
- `AudioConcat`
- `VHS_VideoCombine`
- `MarkdownNote`
- `AudioCrop`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **69%**（53/77）

**有卡**：`LoadAudio`、`UNETLoader`、`ModelPatchLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`WanImageToVideo`、`KSamplerAdvanced`、`WanInfiniteTalkToVideo`、`LatentComposite`、`VAEDecode`、`ImageFromBatch`、`CLIPVisionLoader`、`LoadImage`、`AudioEncoderEncode`、`SimpleMath+`、`Audio Duration (mtb)`、`Int`、`Seed Generator`、`CLIPVisionEncode`、`easy forLoopEnd`、`AudioEncoderLoader`、`VHS_VideoCombine`、`VAELoader`、`PreviewAudio`、`ImageBatch`、`easy forLoopStart`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`ConditioningZeroOut`、`MathExpression|pysssss`、`AudioConcat`、`AudioCrop`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
