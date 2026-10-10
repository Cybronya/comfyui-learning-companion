---
key: 视频生成/文生视频/LTX2.0文生视频-48G专用_2008734330729795586.json
name: LTX2.0文生视频-48G专用_2008734330729795586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.0文生视频-48G专用_2008734330729795586.json
hash: 778739a1655edd26
coverage: 0.792453
learned_at: 2026-10-11 03:07:10
nodes: [ManualSigmas, CFGGuider, MarkdownNote, KSamplerSelect, KSamplerSelect, RandomNoise, LTXVConcatAVLatent, Reroute, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXAVTextEncoderLoader, CFGGuider, LTXVScheduler, RandomNoise, LoraLoaderModelOnly, LoraLoaderModelOnly, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXVSeparateAVLatent, LTXVCropGuides, LoraLoaderModelOnly, CLIPTextEncode, MarkdownNote, EmptyImage, ImpactSwitch, MarkdownNote, RH_LLMAPI_NODE, VAEDecode, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVLatentUpsampler, LatentUpscaleModelLoader, LoraLoaderModelOnly, CLIPTextEncode, LTXVConditioning, Note, Note, PrimitiveInt, PrimitiveFloat, VHS_VideoCombine, VHS_VideoCombine, ImpactInt, GetImageSize, ImageScaleBy, MathExpression|pysssss, TextInput_, TextInput_, easy showAnything]
patterns: []
missing: [MathExpression|pysssss]
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.0文生视频-48G专用_2008734330729795586.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.0文生视频-48G专用_2008734330729795586.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（53 个）：
- `ManualSigmas`
- `CFGGuider`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVConcatAVLatent`
- `Reroute`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXAVTextEncoderLoader`
- `CFGGuider`
- `LTXVScheduler`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `EmptyImage`
- `ImpactSwitch`
- `MarkdownNote`
- `RH_LLMAPI_NODE`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `Note`
- `Note`
- `PrimitiveInt`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImpactInt`
- `GetImageSize`
- `ImageScaleBy`
- `MathExpression|pysssss`
- `TextInput_`
- `TextInput_`
- `easy showAnything`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **79%**（42/53）

**有卡**：`ManualSigmas`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXAVTextEncoderLoader`、`LTXVScheduler`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXVCropGuides`、`CLIPTextEncode`、`EmptyImage`、`RH_LLMAPI_NODE`、`VAEDecode`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`LTXVConditioning`、`VHS_VideoCombine`、`ImpactInt`、`GetImageSize`、`ImageScaleBy`、`TextInput_`

**缺卡**（1）：`MathExpression|pysssss`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
