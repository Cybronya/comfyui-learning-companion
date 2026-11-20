---
key: 平台全量/LTX2.3多国语言翻译+视频对口型_2054034912080080898.json
name: LTX2.3多国语言翻译+视频对口型_2054034912080080898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3多国语言翻译+视频对口型_2054034912080080898.json
hash: e34bb0fae46a3d60
coverage: 0.903846
learned_at: 2026-11-14 00:38:39
nodes: [LatentUpscaleModelLoader, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, MarkdownNote, DeepTranslatorTextNode, easy promptConcat, easy showAnything, Text Multiline, Apply Whisper, ManualSigmas, KSamplerSelect, CFGGuider, RandomNoise, LTXVCropGuides, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, SaveVideo, LTXVConditioning, LTX2SamplingPreviewOverride, CLIPTextEncode, CLIPTextEncode, LTXAVTextEncoderLoader, LayerUtility: ImageScaleByAspectRatio V2, LTXAddVideoICLoRAGuide, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVSetAudioRefTokens, LTXVConcatAVLatent, LTXVSetAudioRefTokens, LTXVLatentUpsampler, LTXVAudioVAEDecode, CreateVideo, CheckpointLoaderSimple, GetImageSizeAndCount, ComfyMathExpression, SamplerCustomAdvanced, LTXVTiledVAEDecode, LTXVAudioVAEEncode, LTXVSeparateAVLatent, LTXAddVideoICLoRAGuide, ResizeImageMaskNode, MarkdownNote, MarkdownNote, MarkdownNote, LoadVideoUI]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 24, "width": 97}
---

# 平台全量/LTX2.3多国语言翻译+视频对口型_2054034912080080898.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3多国语言翻译+视频对口型_2054034912080080898.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `MarkdownNote`
- `DeepTranslatorTextNode`
- `easy promptConcat`
- `easy showAnything`
- `Text Multiline`
- `Apply Whisper`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `LTXVCropGuides`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `SaveVideo`
- `LTXVConditioning`
- `LTX2SamplingPreviewOverride`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXAVTextEncoderLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXAddVideoICLoRAGuide`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSetAudioRefTokens`
- `LTXVConcatAVLatent`
- `LTXVSetAudioRefTokens`
- `LTXVLatentUpsampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `CheckpointLoaderSimple` ★核心
- `GetImageSizeAndCount`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `LTXVTiledVAEDecode` ★核心
- `LTXVAudioVAEEncode` ★核心
- `LTXVSeparateAVLatent`
- `LTXAddVideoICLoRAGuide`
- `ResizeImageMaskNode`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LoadVideoUI`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **90%**（47/52）

**有卡**：`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`LTXVAudioVAELoader`、`DeepTranslatorTextNode`、`easy promptConcat`、`Text Multiline`、`Apply Whisper`、`ManualSigmas`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`SaveVideo`、`LTXVConditioning`、`LTX2SamplingPreviewOverride`、`CLIPTextEncode`、`LTXAVTextEncoderLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXAddVideoICLoRAGuide`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVSetAudioRefTokens`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`CreateVideo`、`CheckpointLoaderSimple`、`GetImageSizeAndCount`、`ComfyMathExpression`、`LTXVTiledVAEDecode`、`LTXVAudioVAEEncode`、`ResizeImageMaskNode`、`LoadVideoUI`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、LTXVLatentUpsampler、SamplerCustomAdvanced
