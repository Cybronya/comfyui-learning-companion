---
key: 数字人/数字人/真人对口型 Ltx2.3 lipdub_2054752281408614401.json
name: 真人对口型 Ltx2.3 lipdub_2054752281408614401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/真人对口型 Ltx2.3 lipdub_2054752281408614401.json
hash: c696a07d6c7f5802
coverage: 0.941176
learned_at: 2026-10-18 19:07:52
nodes: [CFGGuider, ManualSigmas, LTXVConditioning, CLIPTextEncode, KSamplerSelect, KSamplerSelect, ManualSigmas, CFGGuider, LTXVCropGuides, LTXVSeparateAVLatent, VHS_VideoCombine, Note, LTXVAudioVAELoader, CheckpointLoaderSimple, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXICLoRALoaderModelOnly, SamplerCustomAdvanced, MarkdownNote, RandomNoise, RandomNoise, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, LTXAddVideoICLoRAGuide, EmptyLTXVLatentVideo, LTXVAudioVAEEncode, CM_FloatToInt, LTXVEmptyLatentAudio, LTXVSetAudioRefTokens, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, LTXAddVideoICLoRAGuide, LTXVSetAudioRefTokens, LTXVLatentUpsampler, LTXVConcatAVLatent, Float, VHS_VideoInfo, LoadVideoUI, MarkdownNote, LTXVTiledVAEDecode, LTXVAudioVAEDecode, VHS_VideoCombine, Text Multiline, Int, VHS_LoadVideo, GetImageSizeAndCount, ResizeImageMaskNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 24, "width": 97}
---

# 数字人/数字人/真人对口型 Ltx2.3 lipdub_2054752281408614401.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/真人对口型 Ltx2.3 lipdub_2054752281408614401.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

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
- `VHS_VideoCombine`
- `Note`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `MarkdownNote`
- `RandomNoise`
- `RandomNoise`
- `LTX2SamplingPreviewOverride`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `LTXVConcatAVLatent`
- `Float`
- `VHS_VideoInfo`
- `LoadVideoUI`
- `MarkdownNote`
- `LTXVTiledVAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `Text Multiline`
- `Int`
- `VHS_LoadVideo`
- `GetImageSizeAndCount`
- `ResizeImageMaskNode`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（48/51）

**有卡**：`CFGGuider`、`ManualSigmas`、`LTXVConditioning`、`CLIPTextEncode`、`KSamplerSelect`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`VHS_VideoCombine`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LTXICLoRALoaderModelOnly`、`SamplerCustomAdvanced`、`RandomNoise`、`LTX2SamplingPreviewOverride`、`LTXAVTextEncoderLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXAddVideoICLoRAGuide`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEEncode`、`CM_FloatToInt`、`LTXVEmptyLatentAudio`、`LTXVSetAudioRefTokens`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`Float`、`VHS_VideoInfo`、`LoadVideoUI`、`LTXVTiledVAEDecode`、`LTXVAudioVAEDecode`、`Text Multiline`、`Int`、`VHS_LoadVideo`、`GetImageSizeAndCount`、`ResizeImageMaskNode`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
