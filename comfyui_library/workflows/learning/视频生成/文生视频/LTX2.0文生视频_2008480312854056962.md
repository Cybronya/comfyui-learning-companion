---
key: 视频生成/文生视频/LTX2.0文生视频_2008480312854056962.json
name: LTX2.0文生视频_2008480312854056962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.0文生视频_2008480312854056962.json
hash: 512a4e88d6e9fa80
coverage: 0.782609
learned_at: 2026-10-15 22:44:53
nodes: [MarkdownNote, SaveVideo, LTXVScheduler, LTXAVTextEncoderLoader, ManualSigmas, LatentUpscaleModelLoader, LTXVCropGuides, CFGGuider, ImageScaleBy, GetImageSize, LTXVEmptyLatentAudio, LTXVConditioning, EmptyLTXVLatentVideo, LTXVConcatAVLatent, CLIPTextEncode, EmptyImage, PrimitiveInt, SamplerCustomAdvanced, RandomNoise, RandomNoise, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVLatentUpsampler, SamplerCustomAdvanced, Reroute, CLIPTextEncode, CreateVideo, PrimitiveNode, LTXVAudioVAELoader, LTXVSeparateAVLatent, VAEDecode, VAEDecodeTiled, LTXVAudioVAEDecode, CFGGuider, PrimitiveFloat, PrimitiveInt, MarkdownNote, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerSelect, KSamplerSelect, MarkdownNote, MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.0文生视频_2008480312854056962.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.0文生视频_2008480312854056962.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `MarkdownNote`
- `SaveVideo`
- `LTXVScheduler`
- `LTXAVTextEncoderLoader`
- `ManualSigmas`
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `CFGGuider`
- `ImageScaleBy`
- `GetImageSize`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `EmptyImage`
- `PrimitiveInt`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `PrimitiveNode`
- `LTXVAudioVAELoader`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CFGGuider`
- `PrimitiveFloat`
- `PrimitiveInt`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **78%**（36/46）

**有卡**：`SaveVideo`、`LTXVScheduler`、`LTXAVTextEncoderLoader`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`CFGGuider`、`ImageScaleBy`、`GetImageSize`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`EmptyImage`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`CreateVideo`、`LTXVAudioVAELoader`、`VAEDecode`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`KSamplerSelect`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
