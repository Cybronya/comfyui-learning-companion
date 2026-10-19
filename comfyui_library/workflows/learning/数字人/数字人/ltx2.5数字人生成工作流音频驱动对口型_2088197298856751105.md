---
key: 数字人/数字人/ltx2.5数字人生成工作流音频驱动对口型_2088197298856751105.json
name: ltx2.5数字人生成工作流音频驱动对口型_2088197298856751105
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/ltx2.5数字人生成工作流音频驱动对口型_2088197298856751105.json
hash: f234697f84e19c0b
coverage: 0.829545
learned_at: 2026-10-18 19:07:47
nodes: [VHS_VideoCombine, KSamplerSelect, BasicScheduler, LTXVConcatAVLatent, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVLatentUpsampler, KSampler, CFGGuider, LTXVConcatAVLatent, LTXVConditioning, VAEDecodeTiled, LTX2SamplingPreviewOverride, CLIPTextEncode, CLIPTextEncode, LTXVCropGuides, easy cleanGpuUsed, SetNode, PathchSageAttentionKJ, LTXVImgToVideoInplace, GetNode, LTXVAudioVAEEncode, SetLatentNoiseMask, LTX2_NAG, easy showAnything, LTXVImgToVideoInplace, LTXVSeparateAVLatent, RTXVideoSuperResolution, SetNode, GetNode, GetNode, CLIPLoader, GetNode, GetNode, EmptyLTXVLatentVideo, LTXVPreprocess, Reroute, Reroute, SolidMask, SimpleMath+, SimpleMath+, SimpleMath+, PreviewAudio, ResizeImagesByLongerEdge, INTConstant, INTConstant, INTConstant, GetImageSize, CM_FloatToInt, PrimitiveBoolean, RandomNoise, UNETLoader, VAELoader, VAELoader, LoadImage, 1hew_AudioDuration, SetNode, LoadAudio, LatentUpscaleModelLoader, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/ltx2.5数字人生成工作流音频驱动对口型_2088197298856751105.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/ltx2.5数字人生成工作流音频驱动对口型_2088197298856751105.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
- `VHS_VideoCombine`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `KSampler` ★核心
- `CFGGuider`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `VAEDecodeTiled` ★核心
- `LTX2SamplingPreviewOverride`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVCropGuides`
- `easy cleanGpuUsed`
- `SetNode`
- `PathchSageAttentionKJ`
- `LTXVImgToVideoInplace`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `LTX2_NAG`
- `easy showAnything`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `RTXVideoSuperResolution`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `Reroute`
- `Reroute`
- `SolidMask`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `PreviewAudio`
- `ResizeImagesByLongerEdge`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `GetImageSize`
- `CM_FloatToInt`
- `PrimitiveBoolean`
- `RandomNoise`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `LoadImage`
- `1hew_AudioDuration`
- `SetNode`
- `LoadAudio`
- `LatentUpscaleModelLoader`
- `孤海注释`
- `孤海注释`
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

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（73/88）

**有卡**：`VHS_VideoCombine`、`KSamplerSelect`、`BasicScheduler`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`KSampler`、`CFGGuider`、`LTXVConditioning`、`VAEDecodeTiled`、`LTX2SamplingPreviewOverride`、`CLIPTextEncode`、`LTXVCropGuides`、`easy cleanGpuUsed`、`PathchSageAttentionKJ`、`LTXVImgToVideoInplace`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LTX2_NAG`、`RTXVideoSuperResolution`、`CLIPLoader`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`SolidMask`、`SimpleMath+`、`PreviewAudio`、`ResizeImagesByLongerEdge`、`INTConstant`、`GetImageSize`、`CM_FloatToInt`、`PrimitiveBoolean`、`RandomNoise`、`UNETLoader`、`VAELoader`、`LoadImage`、`1hew_AudioDuration`、`LoadAudio`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`solarL_SaveImagesToZip`、`VAEDecode`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
