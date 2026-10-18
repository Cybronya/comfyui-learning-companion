---
key: 视频生成/图生视频/LTX2.0 图生音画同步视频+提示词自动润色_2009276516399583233.json
name: LTX2.0 图生音画同步视频+提示词自动润色_2009276516399583233.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.0 图生音画同步视频+提示词自动润色_2009276516399583233.json
hash: cbcdba5402511ec6
coverage: 0.945455
learned_at: 2026-10-15 22:34:12
nodes: [KSamplerSelect, KSamplerSelect, ManualSigmas, CFGGuider, LTXVEmptyLatentAudio, CLIPTextEncode, RandomNoise, SamplerCustomAdvanced, ImageScaleBy, EmptyLTXVLatentVideo, CFGGuider, LoraLoaderModelOnly, LTXVAudioVAELoader, LTXAVTextEncoderLoader, EmptyImage, VAEDecode, LTXVAudioVAEDecode, LTXVConditioning, LTXVScheduler, LTXVImgToVideoInplace, LTXVCropGuides, LTXVSeparateAVLatent, RandomNoise, CLIPTextEncode, GetImageSize, GetImageSize, MathExpression|pysssss, LTXVConcatAVLatent, CM_IntToFloat, LTXVSeparateAVLatent, VAEDecode, LTXVAudioVAEDecode, SamplerCustomAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVConcatAVLatent, easy int, Int, VHS_VideoCombine, Text Multiline, VHS_VideoCombine, VRAMReserver, CheckpointLoaderSimple, Note, Int, LayerUtility: ImageScaleByAspectRatio V2, LTXVPreprocess, LoadImage, RH_LLMAPI_NODE, easy ifElse, easy showAnything, easy boolean]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.0 图生音画同步视频+提示词自动润色_2009276516399583233.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2009276516399583233.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（55 个）：
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleBy`
- `EmptyLTXVLatentVideo`
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `EmptyImage`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `LTXVScheduler`
- `LTXVImgToVideoInplace`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `GetImageSize`
- `MathExpression|pysssss`
- `LTXVConcatAVLatent`
- `CM_IntToFloat`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `easy int`
- `Int`
- `VHS_VideoCombine`
- `Text Multiline`
- `VHS_VideoCombine`
- `VRAMReserver`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVPreprocess`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `easy ifElse`
- `easy showAnything`
- `easy boolean`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **95%**（52/55）

**有卡**：`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`LTXVEmptyLatentAudio`、`CLIPTextEncode`、`RandomNoise`、`SamplerCustomAdvanced`、`ImageScaleBy`、`EmptyLTXVLatentVideo`、`LoraLoaderModelOnly`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`EmptyImage`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`LTXVScheduler`、`LTXVImgToVideoInplace`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`GetImageSize`、`MathExpression|pysssss`、`LTXVConcatAVLatent`、`CM_IntToFloat`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`easy int`、`Int`、`VHS_VideoCombine`、`Text Multiline`、`VRAMReserver`、`CheckpointLoaderSimple`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVPreprocess`、`LoadImage`、`RH_LLMAPI_NODE`、`easy boolean`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
