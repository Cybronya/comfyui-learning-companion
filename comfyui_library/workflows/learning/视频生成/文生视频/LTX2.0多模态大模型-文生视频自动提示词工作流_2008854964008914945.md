---
key: 视频生成/文生视频/LTX2.0多模态大模型-文生视频自动提示词工作流_2008854964008914945.json
name: LTX2.0多模态大模型-文生视频自动提示词工作流_2008854964008914945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.0多模态大模型-文生视频自动提示词工作流_2008854964008914945.json
hash: 81550d3036f5e3c8
coverage: 0.818182
learned_at: 2026-10-15 22:44:53
nodes: [EmptyImage, LTXVEmptyLatentAudio, ImageScaleBy, GetImageSize, KSamplerSelect, LTXVSeparateAVLatent, LTXVAudioVAELoader, PrimitiveInt, CheckpointLoaderSimple, CFGGuider, LTXVConditioning, EmptyLTXVLatentVideo, Reroute, RandomNoise, LTXVAudioVAEDecode, CLIPTextEncode, SamplerCustomAdvanced, JoinStrings, JoinStrings, easy showAnything, LTXVConcatAVLatent, LTXVScheduler, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, LoraLoaderModelOnly, CLIPTextEncode, MemoryCleaner, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), MarkdownNote, Qwen3_VQA, TextInput_, ShowText|pysssss, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, LTXVLatentUpsampler, LTXVConcatAVLatent, CFGGuider, RandomNoise, ManualSigmas, KSamplerSelect, VAEDecodeTiled, VHS_VideoCombine, SimpleMath+, Int, Int, PrimitiveInt, PrimitiveFloat, Note, Int, TextInput_, TextInput_, MarkdownNote, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.0多模态大模型-文生视频自动提示词工作流_2008854964008914945.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.0多模态大模型-文生视频自动提示词工作流_2008854964008914945.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（55 个）：
- `EmptyImage`
- `LTXVEmptyLatentAudio` ★核心
- `ImageScaleBy`
- `GetImageSize`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAELoader`
- `PrimitiveInt`
- `CheckpointLoaderSimple` ★核心
- `CFGGuider`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `Reroute`
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `JoinStrings`
- `JoinStrings`
- `easy showAnything`
- `LTXVConcatAVLatent`
- `LTXVScheduler`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `MemoryCleaner`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `Qwen3_VQA`
- `TextInput_`
- `ShowText|pysssss`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `CFGGuider`
- `RandomNoise`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `SimpleMath+`
- `Int`
- `Int`
- `PrimitiveInt`
- `PrimitiveFloat`
- `Note`
- `Int`
- `TextInput_`
- `TextInput_`
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **82%**（45/55）

**有卡**：`EmptyImage`、`LTXVEmptyLatentAudio`、`ImageScaleBy`、`GetImageSize`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`CFGGuider`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`RandomNoise`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`JoinStrings`、`LTXVConcatAVLatent`、`LTXVScheduler`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`MemoryCleaner`、`Qwen3_VQA`、`TextInput_`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`ManualSigmas`、`VAEDecodeTiled`、`VHS_VideoCombine`、`SimpleMath+`、`Int`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
