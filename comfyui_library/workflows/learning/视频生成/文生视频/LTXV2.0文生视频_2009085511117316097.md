---
key: 视频生成/文生视频/LTXV2.0文生视频_2009085511117316097.json
name: LTXV2.0文生视频_2009085511117316097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTXV2.0文生视频_2009085511117316097.json
hash: 669b9bb533a82096
coverage: 0.902439
learned_at: 2026-10-15 22:45:18
nodes: [ManualSigmas, CFGGuider, KSamplerSelect, KSamplerSelect, RandomNoise, LoraLoaderModelOnly, LTXVLatentUpsampler, LTXVCropGuides, GetImageSize, LatentUpscaleModelLoader, ImageScaleBy, SamplerCustomAdvanced, CheckpointLoaderSimple, LTXVConcatAVLatent, LTXVAudioVAELoader, SamplerCustomAdvanced, LTXVSeparateAVLatent, PrimitiveInt, LTXAVTextEncoderLoader, CFGGuider, LTXVScheduler, RandomNoise, VHS_VideoCombine, PrimitiveInt, PrimitiveFloat, LTXVSeparateAVLatent, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, EmptyImage, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConcatAVLatent, Reroute, VAEDecode, LTXVAudioVAEDecode, LoraLoaderModelOnly, VAEDecodeTiled, LTXVAudioVAEDecode, VHS_VideoCombine, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTXV2.0文生视频_2009085511117316097.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTXV2.0文生视频_2009085511117316097.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（41 个）：
- `ManualSigmas`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `GetImageSize`
- `LatentUpscaleModelLoader`
- `ImageScaleBy`
- `SamplerCustomAdvanced` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVAELoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `LTXAVTextEncoderLoader`
- `CFGGuider`
- `LTXVScheduler`
- `RandomNoise`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PrimitiveFloat`
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `Reroute`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（37/41）

**有卡**：`ManualSigmas`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`LoraLoaderModelOnly`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`GetImageSize`、`LatentUpscaleModelLoader`、`ImageScaleBy`、`SamplerCustomAdvanced`、`CheckpointLoaderSimple`、`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`LTXVSeparateAVLatent`、`LTXAVTextEncoderLoader`、`LTXVScheduler`、`VHS_VideoCombine`、`CLIPTextEncode`、`LTXVConditioning`、`EmptyImage`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`VAEDecode`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
