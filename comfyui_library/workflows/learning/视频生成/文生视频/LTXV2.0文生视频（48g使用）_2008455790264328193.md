---
key: 视频生成/文生视频/LTXV2.0文生视频（48g使用）_2008455790264328193.json
name: LTXV2.0文生视频（48g使用）_2008455790264328193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTXV2.0文生视频（48g使用）_2008455790264328193.json
hash: 5ea069b6c16504d0
coverage: 0.851064
learned_at: 2026-10-11 03:07:10
nodes: [ManualSigmas, VAEDecode, CFGGuider, MarkdownNote, KSamplerSelect, KSamplerSelect, MarkdownNote, RandomNoise, LTXVConcatAVLatent, LoraLoaderModelOnly, Reroute, LTXVLatentUpsampler, LTXVCropGuides, GetImageSize, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LatentUpscaleModelLoader, ImageScaleBy, LTXVConditioning, CLIPTextEncode, SamplerCustomAdvanced, CheckpointLoaderSimple, LTXVConcatAVLatent, LTXVAudioVAEDecode, LTXVAudioVAELoader, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, PrimitiveInt, LTXAVTextEncoderLoader, RH_Translator, VHS_VideoCombine, MarkdownNote, CFGGuider, LoraLoaderModelOnly, LTXVScheduler, RandomNoise, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, VHS_VideoCombine, EmptyImage, PrimitiveInt, PrimitiveFloat, LTXVSeparateAVLatent, VAEDecode, LTXVAudioVAEDecode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTXV2.0文生视频（48g使用）_2008455790264328193.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTXV2.0文生视频（48g使用）_2008455790264328193.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（47 个）：
- `ManualSigmas`
- `VAEDecode` ★核心
- `CFGGuider`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `MarkdownNote`
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
- `RH_Translator`
- `VHS_VideoCombine`
- `MarkdownNote`
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `LTXVScheduler`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `EmptyImage`
- `PrimitiveInt`
- `PrimitiveFloat`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **85%**（40/47）

**有卡**：`ManualSigmas`、`VAEDecode`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`LTXVConcatAVLatent`、`LoraLoaderModelOnly`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`ImageScaleBy`、`LTXVConditioning`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`CheckpointLoaderSimple`、`LTXVAudioVAEDecode`、`LTXVAudioVAELoader`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXAVTextEncoderLoader`、`RH_Translator`、`VHS_VideoCombine`、`LTXVScheduler`、`EmptyImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
