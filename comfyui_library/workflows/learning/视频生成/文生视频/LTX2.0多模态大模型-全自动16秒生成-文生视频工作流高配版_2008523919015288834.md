---
key: 视频生成/文生视频/LTX2.0多模态大模型-全自动16秒生成-文生视频工作流高配版_2008523919015288834.json
name: LTX2.0多模态大模型-全自动16秒生成-文生视频工作流高配版_2008523919015288834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.0多模态大模型-全自动16秒生成-文生视频工作流高配版_2008523919015288834.json
hash: c8d5c0dbae86968b
coverage: 0.551282
learned_at: 2026-10-15 22:44:51
nodes: [ManualSigmas, KSamplerSelect, EmptyImage, LTXVEmptyLatentAudio, ImageScaleBy, GetImageSize, KSamplerSelect, LTXVSeparateAVLatent, Reroute, LTXVAudioVAELoader, Reroute, PrimitiveInt, Reroute, Reroute, Reroute, Reroute, Reroute, CheckpointLoaderSimple, CFGGuider, Reroute, Reroute, Reroute, LTXVConditioning, Reroute, Reroute, EmptyLTXVLatentVideo, Reroute, Reroute, Reroute, LTXVCropGuides, RandomNoise, RandomNoise, LTXVLatentUpsampler, LTXVAudioVAEDecode, LTXVSeparateAVLatent, Reroute, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, JoinStrings, Reroute, Reroute, Reroute, Reroute, Reroute, MarkdownNote, Reroute, LTXVConcatAVLatent, Reroute, Reroute, SamplerCustomAdvanced, LTXVScheduler, Fast Groups Bypasser (rgthree), LTXAVTextEncoderLoader, LatentUpscaleModelLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, MarkdownNote, MarkdownNote, Note, PrimitiveFloat, PrimitiveInt, Int, VHS_VideoCombine, Note, TextInput_, ShowText|pysssss, TextInput_, Qwen3_VQA, MemoryCleaner, easy showAnything, JoinStrings, MemoryCleaner, Int, Int, VAEDecodeTiled, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.0多模态大模型-全自动16秒生成-文生视频工作流高配版_2008523919015288834.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.0多模态大模型-全自动16秒生成-文生视频工作流高配版_2008523919015288834.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（78 个）：
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `EmptyImage`
- `LTXVEmptyLatentAudio` ★核心
- `ImageScaleBy`
- `GetImageSize`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `Reroute`
- `LTXVAudioVAELoader`
- `Reroute`
- `PrimitiveInt`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CheckpointLoaderSimple` ★核心
- `CFGGuider`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVConditioning`
- `Reroute`
- `Reroute`
- `EmptyLTXVLatentVideo`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVCropGuides`
- `RandomNoise`
- `RandomNoise`
- `LTXVLatentUpsampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `Reroute`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `JoinStrings`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `MarkdownNote`
- `Reroute`
- `LTXVConcatAVLatent`
- `Reroute`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `LTXVScheduler`
- `Fast Groups Bypasser (rgthree)`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `Note`
- `PrimitiveFloat`
- `PrimitiveInt`
- `Int`
- `VHS_VideoCombine`
- `Note`
- `TextInput_`
- `ShowText|pysssss`
- `TextInput_`
- `Qwen3_VQA`
- `MemoryCleaner`
- `easy showAnything`
- `JoinStrings`
- `MemoryCleaner`
- `Int`
- `Int`
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **55%**（43/78）

**有卡**：`ManualSigmas`、`KSamplerSelect`、`EmptyImage`、`LTXVEmptyLatentAudio`、`ImageScaleBy`、`GetImageSize`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`CFGGuider`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVCropGuides`、`RandomNoise`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`JoinStrings`、`LTXVScheduler`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`Int`、`VHS_VideoCombine`、`TextInput_`、`Qwen3_VQA`、`MemoryCleaner`、`VAEDecodeTiled`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
