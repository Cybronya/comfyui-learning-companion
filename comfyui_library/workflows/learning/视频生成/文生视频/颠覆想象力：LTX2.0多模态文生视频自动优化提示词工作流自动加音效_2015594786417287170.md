---
key: 视频生成/文生视频/颠覆想象力：LTX2.0多模态文生视频自动优化提示词工作流自动加音效_2015594786417287170.json
name: 颠覆想象力：LTX2.0多模态文生视频自动优化提示词工作流自动加音效_2015594786417287170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/颠覆想象力：LTX2.0多模态文生视频自动优化提示词工作流自动加音效_2015594786417287170.json
hash: fa745aa13dde9365
coverage: 0.8
learned_at: 2026-10-11 03:07:16
nodes: [EmptyImage, ImageScaleBy, KSamplerSelect, LTXVSeparateAVLatent, PrimitiveInt, CheckpointLoaderSimple, CFGGuider, Reroute, RandomNoise, LTXVAudioVAEDecode, SamplerCustomAdvanced, LTXVScheduler, LTXAVTextEncoderLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, LTXVLatentUpsampler, CFGGuider, RandomNoise, ManualSigmas, KSamplerSelect, VAEDecodeTiled, JoinStrings, ShowText|pysssss, GetImageSize, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConcatAVLatent, Qwen3VL_Advanced, TextInput_, JoinStrings, TextInput_, Fast Groups Bypasser (rgthree), LTXVAudioVAELoader, LatentUpscaleModelLoader, CLIPTextEncode, CLIPTextEncode, MemoryCleaner, LTXVConcatAVLatent, SimpleMath+, Note, Int, PrimitiveInt, PrimitiveFloat, LTXVConditioning, easy cleanGpuUsed, easy showAnything, TextInput_, Int, Int, easy cleanGpuUsed, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: [SimpleMath+, easy cleanGpuUsed, easy cleanGpuUsed]
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/颠覆想象力：LTX2.0多模态文生视频自动优化提示词工作流自动加音效_2015594786417287170.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/颠覆想象力：LTX2.0多模态文生视频自动优化提示词工作流自动加音效_2015594786417287170.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（55 个）：
- `EmptyImage`
- `ImageScaleBy`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `CheckpointLoaderSimple` ★核心
- `CFGGuider`
- `Reroute`
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVScheduler`
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `RandomNoise`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `VAEDecodeTiled` ★核心
- `JoinStrings`
- `ShowText|pysssss`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `Qwen3VL_Advanced`
- `TextInput_`
- `JoinStrings`
- `TextInput_`
- `Fast Groups Bypasser (rgthree)`
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MemoryCleaner`
- `LTXVConcatAVLatent`
- `SimpleMath+`
- `Note`
- `Int`
- `PrimitiveInt`
- `PrimitiveFloat`
- `LTXVConditioning`
- `easy cleanGpuUsed`
- `easy showAnything`
- `TextInput_`
- `Int`
- `Int`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（44/55）

**有卡**：`EmptyImage`、`ImageScaleBy`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`CheckpointLoaderSimple`、`CFGGuider`、`RandomNoise`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`LTXVScheduler`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`ManualSigmas`、`VAEDecodeTiled`、`JoinStrings`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`Qwen3VL_Advanced`、`TextInput_`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`MemoryCleaner`、`Int`、`LTXVConditioning`、`VHS_VideoCombine`

**缺卡**（3）：`SimpleMath+`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
