---
key: 平台全量/LTX2.0深度控制视频生成-48G专用_2008857194787250178.json
name: LTX2.0深度控制视频生成-48G专用_2008857194787250178
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.0深度控制视频生成-48G专用_2008857194787250178.json
hash: a95bacb21fb14214
coverage: 0.927273
learned_at: 2026-11-14 00:37:21
nodes: [MarkdownNote, CFGGuider, KSamplerSelect, ManualSigmas, LatentUpscaleModelLoader, CFGGuider, SamplerCustomAdvanced, LTXVConditioning, CLIPTextEncode, LTXVSeparateAVLatent, Reroute, KSamplerSelect, LoraLoaderModelOnly, LTXVCropGuides, LTXVScheduler, RandomNoise, SamplerCustomAdvanced, RandomNoise, LTXVSeparateAVLatent, VAEDecode, VAEDecodeTiled, LTXVAudioVAEDecode, VHS_VideoCombine, UNETLoader, BasicGuider, KSamplerSelect, ImageInvert, VAEEncode, SetFirstSigma, DisableNoise, SamplerCustomAdvanced, VAELoader, BasicScheduler, GetImageSize, LotusConditioning, LTXAVTextEncoderLoader, VAEDecode, LTXVEmptyLatentAudio, VHS_VideoCombine, LTXVConcatAVLatent, LTXVLatentUpsampler, GetVideoComponents, PreviewAny, ImageFromBatch, LTXVConcatAVLatent, LoadVideo, CLIPTextEncode, ImageResizeKJv2, ImageScaleBy, EmptyLTXVLatentVideo, LTXVAddGuide, LoraLoaderModelOnly, LTXVAudioVAELoader, CheckpointLoaderSimple, PrimitiveNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 平台全量/LTX2.0深度控制视频生成-48G专用_2008857194787250178.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.0深度控制视频生成-48G专用_2008857194787250178.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（55 个）：
- `MarkdownNote`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVSeparateAVLatent`
- `Reroute`
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVCropGuides`
- `LTXVScheduler`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ImageInvert`
- `VAEEncode` ★核心
- `SetFirstSigma`
- `DisableNoise`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `BasicScheduler`
- `GetImageSize`
- `LotusConditioning`
- `LTXAVTextEncoderLoader`
- `VAEDecode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `VHS_VideoCombine`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `GetVideoComponents`
- `PreviewAny`
- `ImageFromBatch`
- `LTXVConcatAVLatent`
- `LoadVideo`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `ImageScaleBy`
- `EmptyLTXVLatentVideo`
- `LTXVAddGuide`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveNode`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **93%**（51/55）

**有卡**：`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVSeparateAVLatent`、`LoraLoaderModelOnly`、`LTXVCropGuides`、`LTXVScheduler`、`RandomNoise`、`VAEDecode`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`UNETLoader`、`BasicGuider`、`ImageInvert`、`VAEEncode`、`SetFirstSigma`、`DisableNoise`、`VAELoader`、`BasicScheduler`、`GetImageSize`、`LotusConditioning`、`LTXAVTextEncoderLoader`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`GetVideoComponents`、`ImageFromBatch`、`LoadVideo`、`ImageResizeKJv2`、`ImageScaleBy`、`EmptyLTXVLatentVideo`、`LTXVAddGuide`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CFGGuider、KSamplerSelect
