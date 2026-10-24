---
key: 图片生成/图生图/（2图 首尾帧）LTX2.5首尾帧极速音画同出图生视频数字人_2111320761280585730.json
name: （2图 首尾帧）LTX2.5首尾帧极速音画同出图生视频数字人_2111320761280585730
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（2图 首尾帧）LTX2.5首尾帧极速音画同出图生视频数字人_2111320761280585730.json
hash: dd66f3915e9d0f0c
coverage: 0.884058
learned_at: 2026-10-23 13:36:08
nodes: [LTXVConcatAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVAddGuide, ManualSigmas, LTXVAddGuide, LTXVEmptyLatentAudio, LTXVCropGuides, EmptyLTXVLatentVideo, LTXVConditioning, SamplerEulerAncestral, LTXVDualCFGGuider, RandomNoise, CLIPTextEncode, CLIPTextEncode, LTXVPreprocess, TextGenerateLTX2Prompt, ResizeImageMaskNode, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPLoader, UNETLoader, VAELoader, VAELoader, ResizeImageMaskNode, LTXVPreprocess, GetImageSize, CLIPLoader, ComfySwitchNode, PreviewAny, PrimitiveBoolean, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, PrimitiveInt, PrimitiveStringMultiline, VHS_VideoCombine, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, LoadImage, LoadImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/（2图 首尾帧）LTX2.5首尾帧极速音画同出图生视频数字人_2111320761280585730.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（2图 首尾帧）LTX2.5首尾帧极速音画同出图生视频数字人_2111320761280585730.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVAddGuide`
- `ManualSigmas`
- `LTXVAddGuide`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVCropGuides`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `SamplerEulerAncestral` ★核心
- `LTXVDualCFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `TextGenerateLTX2Prompt`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveInt`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `GetImageSize`
- `CLIPLoader`
- `ComfySwitchNode`
- `PreviewAny`
- `PrimitiveBoolean`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoadImage`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **88%**（61/69）

**有卡**：`LTXVConcatAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVAddGuide`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`SamplerEulerAncestral`、`LTXVDualCFGGuider`、`RandomNoise`、`CLIPTextEncode`、`LTXVPreprocess`、`TextGenerateLTX2Prompt`、`ResizeImageMaskNode`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`GetImageSize`、`PrimitiveBoolean`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`KSampler`、`solarL_SaveImagesToZip`、`VAEDecode`、`EmptyLatentImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
