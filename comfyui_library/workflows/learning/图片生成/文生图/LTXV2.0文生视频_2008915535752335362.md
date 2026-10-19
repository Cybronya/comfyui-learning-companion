---
key: 图片生成/文生图/LTXV2.0文生视频_2008915535752335362.json
name: LTXV2.0文生视频_2008915535752335362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/LTXV2.0文生视频_2008915535752335362.json
hash: 71255fbb8e725e1f
coverage: 0.847826
learned_at: 2026-10-19 22:00:35
nodes: [ManualSigmas, VAEDecode, CFGGuider, MarkdownNote, KSamplerSelect, KSamplerSelect, RandomNoise, LTXVConcatAVLatent, LoraLoaderModelOnly, Reroute, LTXVLatentUpsampler, LTXVCropGuides, GetImageSize, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LatentUpscaleModelLoader, ImageScaleBy, LTXVConditioning, CLIPTextEncode, SamplerCustomAdvanced, CheckpointLoaderSimple, LTXVConcatAVLatent, LTXVAudioVAEDecode, LTXVAudioVAELoader, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, PrimitiveInt, LTXAVTextEncoderLoader, CFGGuider, LoraLoaderModelOnly, LTXVScheduler, RandomNoise, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveInt, PrimitiveFloat, LTXVSeparateAVLatent, VAEDecode, LTXVAudioVAEDecode, MarkdownNote, MarkdownNote, EmptyImage, CLIPTextEncode, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 图片生成/文生图/LTXV2.0文生视频_2008915535752335362.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/LTXV2.0文生视频_2008915535752335362.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（46 个）：
- `ManualSigmas`
- `VAEDecode` ★核心
- `CFGGuider`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVConcatAVLatent`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LatentUpscaleModelLoader`
- `ImageScaleBy`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAELoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `PrimitiveInt`
- `LTXAVTextEncoderLoader`
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `LTXVScheduler`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `PrimitiveFloat`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `EmptyImage`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **85%**（39/46）

**有卡**：`ManualSigmas`、`VAEDecode`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`LTXVConcatAVLatent`、`LoraLoaderModelOnly`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`ImageScaleBy`、`LTXVConditioning`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`CheckpointLoaderSimple`、`LTXVAudioVAEDecode`、`LTXVAudioVAELoader`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXAVTextEncoderLoader`、`LTXVScheduler`、`EmptyImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
