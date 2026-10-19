---
key: 数字人/数字人/lipdub真人对口型｜Ltx2.3数字人视频生视频_2095804952722628610.json
name: lipdub真人对口型｜Ltx2.3数字人视频生视频_2095804952722628610
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/lipdub真人对口型｜Ltx2.3数字人视频生视频_2095804952722628610.json
hash: 79f1504d004b8a07
coverage: 0.945946
learned_at: 2026-10-18 22:17:13
nodes: [CFGGuider, ManualSigmas, LTXVConditioning, CLIPTextEncode, KSamplerSelect, KSamplerSelect, ManualSigmas, CFGGuider, LTXVCropGuides, LTXVSeparateAVLatent, VHS_VideoCombine, LTXVAudioVAELoader, CheckpointLoaderSimple, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXICLoRALoaderModelOnly, SamplerCustomAdvanced, RandomNoise, RandomNoise, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, LTXAddVideoICLoRAGuide, EmptyLTXVLatentVideo, LTXVAudioVAEEncode, CM_FloatToInt, LTXVEmptyLatentAudio, LTXVSetAudioRefTokens, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, LTXAddVideoICLoRAGuide, LTXVSetAudioRefTokens, LTXVLatentUpsampler, LTXVConcatAVLatent, Float, VHS_VideoInfo, LTXVTiledVAEDecode, LTXVAudioVAEDecode, VHS_VideoCombine, Text Multiline, Int, VHS_LoadVideo, GetImageSizeAndCount, ResizeImageMaskNode, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/lipdub真人对口型｜Ltx2.3数字人视频生视频_2095804952722628610.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/lipdub真人对口型｜Ltx2.3数字人视频生视频_2095804952722628610.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
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
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
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
- `LTXVTiledVAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `Text Multiline`
- `Int`
- `VHS_LoadVideo`
- `GetImageSizeAndCount`
- `ResizeImageMaskNode`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
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
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
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

覆盖率 **95%**（70/74）

**有卡**：`CFGGuider`、`ManualSigmas`、`LTXVConditioning`、`CLIPTextEncode`、`KSamplerSelect`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`VHS_VideoCombine`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LTXICLoRALoaderModelOnly`、`SamplerCustomAdvanced`、`RandomNoise`、`LTX2SamplingPreviewOverride`、`LTXAVTextEncoderLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXAddVideoICLoRAGuide`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEEncode`、`CM_FloatToInt`、`LTXVEmptyLatentAudio`、`LTXVSetAudioRefTokens`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`Float`、`VHS_VideoInfo`、`LTXVTiledVAEDecode`、`LTXVAudioVAEDecode`、`Text Multiline`、`Int`、`VHS_LoadVideo`、`GetImageSizeAndCount`、`ResizeImageMaskNode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
