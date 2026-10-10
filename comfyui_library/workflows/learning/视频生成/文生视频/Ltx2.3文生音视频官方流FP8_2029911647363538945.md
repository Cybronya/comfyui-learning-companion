---
key: 视频生成/文生视频/Ltx2.3文生音视频官方流FP8_2029911647363538945.json
name: Ltx2.3文生音视频官方流FP8_2029911647363538945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Ltx2.3文生音视频官方流FP8_2029911647363538945.json
hash: d3c32cac82dc8557
coverage: 0.822222
learned_at: 2026-10-11 03:16:48
nodes: [MarkdownNote, LTXVCropGuides, ImageScaleBy, LTXVEmptyLatentAudio, LTXVConditioning, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SamplerCustomAdvanced, VAEDecodeTiled, PrimitiveFloat, PrimitiveInt, MarkdownNote, LoraLoaderModelOnly, KSamplerSelect, KSamplerSelect, MarkdownNote, LTXVConcatAVLatent, LTXVLatentUpsampler, Reroute, LTXVAudioVAEDecode, VHS_VideoCombine, MarkdownNote, EmptyImage, GetImageSize, PrimitiveInt, CFGGuider, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVSeparateAVLatent, VHS_VideoCombine, RandomNoise, RandomNoise, CFGGuider, SamplerCustomAdvanced, LoraLoaderModelOnly, LTXVScheduler, LoraLoaderModelOnly, CLIPTextEncode, ManualSigmas, CLIPTextEncode, LTXVAudioVAELoader, LatentUpscaleModelLoader, CheckpointLoaderSimple, LTXAVTextEncoderLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/Ltx2.3文生音视频官方流FP8_2029911647363538945.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Ltx2.3文生音视频官方流FP8_2029911647363538945.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（45 个）：
- `MarkdownNote`
- `LTXVCropGuides`
- `ImageScaleBy`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `PrimitiveFloat`
- `PrimitiveInt`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `MarkdownNote`
- `EmptyImage`
- `GetImageSize`
- `PrimitiveInt`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `RandomNoise`
- `RandomNoise`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVScheduler`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ManualSigmas`
- `CLIPTextEncode` ★核心
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **82%**（37/45）

**有卡**：`LTXVCropGuides`、`ImageScaleBy`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`LoraLoaderModelOnly`、`KSamplerSelect`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`EmptyImage`、`GetImageSize`、`CFGGuider`、`LTXVSeparateAVLatent`、`RandomNoise`、`LTXVScheduler`、`CLIPTextEncode`、`ManualSigmas`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
