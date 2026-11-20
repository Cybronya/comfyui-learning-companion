---
key: 平台全量/LTX2.3翻译+重新对口型_2054451736919724033.json
name: LTX2.3翻译+重新对口型_2054451736919724033
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3翻译+重新对口型_2054451736919724033.json
hash: 178c07c26edf7acd
coverage: 0.921569
learned_at: 2026-11-14 00:38:48
nodes: [RandomNoise, CFGGuider, ManualSigmas, LTXVConcatAVLatent, LTXVAudioVAEDecode, LTXVTiledVAEDecode, LTXAddVideoICLoRAGuide, LatentUpscaleModelLoader, LTXVConditioning, LTXVEmptyLatentAudio, CLIPTextEncode, CheckpointLoaderSimple, LTXVCropGuides, LTXVSeparateAVLatent, LTXVSetAudioRefTokens, LTXVLatentUpsampler, LTX2SamplingPreviewOverride, EmptyLTXVLatentVideo, KSamplerSelect, LTXAddVideoICLoRAGuide, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, RandomNoise, CFGGuider, LTXVCropGuides, easy showAnything, CLIPTextEncode, CreateVideo, SamplerCustomAdvanced, SaveVideo, LayerUtility: ImageScaleByAspectRatio V2, ComfyMathExpression, LTXVAudioVAELoader, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LTXAVTextEncoderLoader, Apply Whisper, LTXVSetAudioRefTokens, GetImageSizeAndCount, SamplerCustomAdvanced, LTXVSeparateAVLatent, easy promptConcat, ResizeImageMaskNode, LTXVAudioVAEEncode, LoadVideoUI, MarkdownNote, MarkdownNote, Note, Text Multiline, DeepTranslatorTextNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 24, "width": 97}
---

# 平台全量/LTX2.3翻译+重新对口型_2054451736919724033.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3翻译+重新对口型_2054451736919724033.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `RandomNoise`
- `CFGGuider`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVTiledVAEDecode` ★核心
- `LTXAddVideoICLoRAGuide`
- `LatentUpscaleModelLoader`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVSetAudioRefTokens`
- `LTXVLatentUpsampler` ★核心
- `LTX2SamplingPreviewOverride`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect` ★核心
- `LTXAddVideoICLoRAGuide`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `CFGGuider`
- `LTXVCropGuides`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `SamplerCustomAdvanced` ★核心
- `SaveVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ComfyMathExpression`
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `Apply Whisper`
- `LTXVSetAudioRefTokens`
- `GetImageSizeAndCount`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `easy promptConcat`
- `ResizeImageMaskNode`
- `LTXVAudioVAEEncode` ★核心
- `LoadVideoUI`
- `MarkdownNote`
- `MarkdownNote`
- `Note`
- `Text Multiline`
- `DeepTranslatorTextNode`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **92%**（47/51）

**有卡**：`RandomNoise`、`CFGGuider`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`LTXVTiledVAEDecode`、`LTXAddVideoICLoRAGuide`、`LatentUpscaleModelLoader`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVSetAudioRefTokens`、`LTXVLatentUpsampler`、`LTX2SamplingPreviewOverride`、`EmptyLTXVLatentVideo`、`KSamplerSelect`、`CreateVideo`、`SamplerCustomAdvanced`、`SaveVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`ComfyMathExpression`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`LTXAVTextEncoderLoader`、`Apply Whisper`、`GetImageSizeAndCount`、`easy promptConcat`、`ResizeImageMaskNode`、`LTXVAudioVAEEncode`、`LoadVideoUI`、`Text Multiline`、`DeepTranslatorTextNode`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、LTXVLatentUpsampler、SamplerCustomAdvanced
