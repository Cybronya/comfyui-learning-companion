---
key: 视频生成/文生视频/很强的文生视频-LTXV2.0你就是导演_2008866865359097857.json
name: 很强的文生视频-LTXV2.0你就是导演_2008866865359097857
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/很强的文生视频-LTXV2.0你就是导演_2008866865359097857.json
hash: c5106932715ccd9a
coverage: 0.758621
learned_at: 2026-10-15 22:48:36
nodes: [CFGGuider, LTXVEmptyLatentAudio, LatentUpscaleModelLoader, ImageScaleBy, CFGGuider, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, MemoryCleaner, EmptyLTXVLatentVideo, VHS_VideoCombine, VAEDecode, CLIPTextEncode, SamplerCustomAdvanced, Reroute, LoraLoaderModelOnly, LoraLoaderModelOnly, Reroute, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVConditioning, KSamplerSelect, Reroute, LTXVScheduler, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXVLatentUpsampler, RandomNoise, Reroute, PrimitiveFloat, LTXAVTextEncoderLoader, PrimitiveInt, Int, SimpleMath+, PrimitiveInt, GetImageSize, MarkdownNote, MarkdownNote, MarkdownNote, LTXVAudioVAEDecode, VHS_VideoCombine, SetNode, CLIPTextEncode, GetNode, MarkdownNote, LTXVCropGuides, MemoryCleaner, MarkdownNote, LTXVAudioVAEDecode, EmptyImage, Int, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/很强的文生视频-LTXV2.0你就是导演_2008866865359097857.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/很强的文生视频-LTXV2.0你就是导演_2008866865359097857.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（58 个）：
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `LatentUpscaleModelLoader`
- `ImageScaleBy`
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `MemoryCleaner`
- `EmptyLTXVLatentVideo`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVScheduler`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `Reroute`
- `PrimitiveFloat`
- `LTXAVTextEncoderLoader`
- `PrimitiveInt`
- `Int`
- `SimpleMath+`
- `PrimitiveInt`
- `GetImageSize`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `MarkdownNote`
- `LTXVCropGuides`
- `MemoryCleaner`
- `MarkdownNote`
- `LTXVAudioVAEDecode` ★核心
- `EmptyImage`
- `Int`
- `CR Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **76%**（44/58）

**有卡**：`CFGGuider`、`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`ImageScaleBy`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`MemoryCleaner`、`EmptyLTXVLatentVideo`、`VHS_VideoCombine`、`VAEDecode`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`LTXVConditioning`、`KSamplerSelect`、`LTXVScheduler`、`LTXVConcatAVLatent`、`ManualSigmas`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXVLatentUpsampler`、`LTXAVTextEncoderLoader`、`Int`、`SimpleMath+`、`GetImageSize`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`EmptyImage`、`CR Text`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
