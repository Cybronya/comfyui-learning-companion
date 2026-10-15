---
key: 视频生成/文生视频/LTX 2.0 音画同步 文生视频_2013869097615888385.json
name: LTX 2.0 音画同步 文生视频_2013869097615888385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.0 音画同步 文生视频_2013869097615888385.json
hash: 4878b601502945ad
coverage: 0.765957
learned_at: 2026-10-15 22:44:31
nodes: [LTXAVTextEncoderLoader, ManualSigmas, CFGGuider, LTXVConditioning, CLIPTextEncode, LTXVConcatAVLatent, LoraLoaderModelOnly, KSamplerSelect, ImageScaleBy, CFGGuider, KSamplerSelect, LTXVScheduler, LTXVConcatAVLatent, SamplerCustomAdvanced, LatentUpscaleModelLoader, LoraLoaderModelOnly, LTXVCropGuides, LTXVLatentUpsampler, RandomNoise, VAEDecodeTiled, MarkdownNote, MarkdownNote, MarkdownNote, CheckpointLoaderSimple, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, PrimitiveInt, Note, LoraLoaderModelOnly, LTXVAudioVAEDecode, LTXVSeparateAVLatent, SamplerCustomAdvanced, Note, LTXVAudioVAELoader, Reroute, PrimitiveNode, GetImageSize, RandomNoise, PrimitiveInt, PrimitiveFloat, LTXVSeparateAVLatent, CLIPTextEncode, VHS_VideoCombine, VAEDecodeTiled, VHS_VideoCombine, EmptyImage, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX 2.0 音画同步 文生视频_2013869097615888385.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.0 音画同步 文生视频_2013869097615888385.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（47 个）：
- `LTXAVTextEncoderLoader`
- `ManualSigmas`
- `CFGGuider`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `ImageScaleBy`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `VAEDecodeTiled` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `Note`
- `LTXVAudioVAELoader`
- `Reroute`
- `PrimitiveNode`
- `GetImageSize`
- `RandomNoise`
- `PrimitiveInt`
- `PrimitiveFloat`
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `EmptyImage`
- `Note`

## 关键参数

- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（36/47）

**有卡**：`LTXAVTextEncoderLoader`、`ManualSigmas`、`CFGGuider`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`LoraLoaderModelOnly`、`KSamplerSelect`、`ImageScaleBy`、`LTXVScheduler`、`SamplerCustomAdvanced`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`RandomNoise`、`VAEDecodeTiled`、`CheckpointLoaderSimple`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`GetImageSize`、`VHS_VideoCombine`、`EmptyImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
