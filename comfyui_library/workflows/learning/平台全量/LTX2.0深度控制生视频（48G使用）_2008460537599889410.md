---
key: 平台全量/LTX2.0深度控制生视频（48G使用）_2008460537599889410.json
name: LTX2.0深度控制生视频（48G使用）_2008460537599889410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.0深度控制生视频（48G使用）_2008460537599889410.json
hash: a5d1d0a86b55913a
coverage: 0.924528
learned_at: 2026-11-14 00:37:20
nodes: [CFGGuider, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVConditioning, CLIPTextEncode, LTXVConcatAVLatent, Reroute, KSamplerSelect, LTXVCropGuides, LTXVScheduler, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, RandomNoise, BasicGuider, KSamplerSelect, VAEEncode, SetFirstSigma, UNETLoader, LoraLoaderModelOnly, BasicScheduler, LotusConditioning, MarkdownNote, MarkdownNote, GetImageSize, LTXVAddGuide, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVConcatAVLatent, PreviewAny, VAELoader, SamplerCustomAdvanced, ImageInvert, EmptyLTXVLatentVideo, VAEDecode, DisableNoise, LTXVEmptyLatentAudio, CLIPTextEncode, LTXVSeparateAVLatent, ImageScaleBy, ImageResizeKJv2, CheckpointLoaderSimple, LoraLoaderModelOnly, LTXVAudioVAELoader, LTXAVTextEncoderLoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, VAEDecode, VAEDecodeTiled, LTXVAudioVAEDecode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 平台全量/LTX2.0深度控制生视频（48G使用）_2008460537599889410.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.0深度控制生视频（48G使用）_2008460537599889410.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（53 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `Reroute`
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `LTXVScheduler`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAEEncode` ★核心
- `SetFirstSigma`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `LotusConditioning`
- `MarkdownNote`
- `MarkdownNote`
- `GetImageSize`
- `LTXVAddGuide`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `PreviewAny`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `ImageInvert`
- `EmptyLTXVLatentVideo`
- `VAEDecode` ★核心
- `DisableNoise`
- `LTXVEmptyLatentAudio` ★核心
- `CLIPTextEncode` ★核心
- `LTXVSeparateAVLatent`
- `ImageScaleBy`
- `ImageResizeKJv2`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **92%**（49/53）

**有卡**：`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`LTXVScheduler`、`RandomNoise`、`LTXVSeparateAVLatent`、`BasicGuider`、`VAEEncode`、`SetFirstSigma`、`UNETLoader`、`LoraLoaderModelOnly`、`BasicScheduler`、`LotusConditioning`、`GetImageSize`、`LTXVAddGuide`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`VAELoader`、`ImageInvert`、`EmptyLTXVLatentVideo`、`VAEDecode`、`DisableNoise`、`LTXVEmptyLatentAudio`、`ImageScaleBy`、`ImageResizeKJv2`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`VHS_LoadVideo`、`VHS_VideoCombine`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CFGGuider、KSamplerSelect
