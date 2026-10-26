---
key: 数字人/数字人/人物对口型 LTX2.3_2054520449886900225.json
name: 人物对口型 LTX2.3_2054520449886900225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/人物对口型 LTX2.3_2054520449886900225.json
hash: 9c18462c9954bb6d
coverage: 0.941176
learned_at: 2026-10-26 02:00:15
nodes: [CFGGuider, ManualSigmas, LTXVConditioning, CLIPTextEncode, KSamplerSelect, KSamplerSelect, ManualSigmas, CFGGuider, LTXVCropGuides, LTXVSeparateAVLatent, LTXVTiledVAEDecode, VHS_VideoCombine, Note, LTXVAudioVAELoader, CheckpointLoaderSimple, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, SamplerCustomAdvanced, CreateVideo, MarkdownNote, RandomNoise, RandomNoise, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, LTXAddVideoICLoRAGuide, EmptyLTXVLatentVideo, LTXVAudioVAEEncode, CM_FloatToInt, LTXVEmptyLatentAudio, LTXVSetAudioRefTokens, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, LTXAddVideoICLoRAGuide, LTXVSetAudioRefTokens, LTXVLatentUpsampler, ResizeImageMaskNode, LTXVConcatAVLatent, SaveVideo, Float, Int, MarkdownNote, LoadVideoUI, VHS_LoadVideo, Text Multiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 24, "width": 97}
---

# 数字人/数字人/人物对口型 LTX2.3_2054520449886900225.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/人物对口型 LTX2.3_2054520449886900225.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `CFGGuider`
- `ManualSigmas`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVTiledVAEDecode` ★核心
- `VHS_VideoCombine`
- `Note`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `MarkdownNote`
- `RandomNoise`
- `RandomNoise`
- `LTX2SamplingPreviewOverride`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSizeAndCount`
- `LTXAddVideoICLoRAGuide`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEEncode` ★核心
- `CM_FloatToInt`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSetAudioRefTokens`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXAddVideoICLoRAGuide`
- `LTXVSetAudioRefTokens`
- `LTXVLatentUpsampler` ★核心
- `ResizeImageMaskNode`
- `LTXVConcatAVLatent`
- `SaveVideo`
- `Float`
- `Int`
- `MarkdownNote`
- `LoadVideoUI`
- `VHS_LoadVideo`
- `Text Multiline`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（48/51）

**有卡**：`CFGGuider`、`ManualSigmas`、`LTXVConditioning`、`CLIPTextEncode`、`KSamplerSelect`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVTiledVAEDecode`、`VHS_VideoCombine`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LTXICLoRALoaderModelOnly`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`CreateVideo`、`RandomNoise`、`LTX2SamplingPreviewOverride`、`LTXAVTextEncoderLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSizeAndCount`、`LTXAddVideoICLoRAGuide`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEEncode`、`CM_FloatToInt`、`LTXVEmptyLatentAudio`、`LTXVSetAudioRefTokens`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`ResizeImageMaskNode`、`SaveVideo`、`Float`、`Int`、`LoadVideoUI`、`VHS_LoadVideo`、`Text Multiline`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
