---
key: 数字人/数字人/LTX2.3-数字人-上传图片和音频生成电商带货数字人_2033156191248977921.json
name: LTX2.3-数字人-上传图片和音频生成电商带货数字人_2033156191248977921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3-数字人-上传图片和音频生成电商带货数字人_2033156191248977921.json
hash: b6943be803364239
coverage: 0.789474
learned_at: 2026-10-26 01:55:55
nodes: [KSamplerSelect, CFGGuider, BasicScheduler, SimpleMath+, easy showAnything, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, RandomNoise, LTX2SamplingPreviewOverride, LTX2_NAG, CLIPTextEncode, LTXVConditioning, PathchSageAttentionKJ, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVConcatAVLatent, LatentUpscaleModelLoader, SamplerCustomAdvanced, GetNode, LTXVImgToVideoInplace, LTXVCropGuides, LTXVLatentUpsampler, KSampler, LTXVSeparateAVLatent, GetNode, VAEDecodeTiled, easy cleanGpuUsed, ImageSharpen, SetNode, SetNode, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LTXVAudioVAELoader, SetNode, GetNode, INTConstant, INTConstant, INTConstant, SimpleMath+, GetImageSize, INTConstant, Reroute, Reroute, SimpleMath+, CM_FloatToInt, AudioDuration_wan, SolidMask, LTXVAudioVAEEncode, SetLatentNoiseMask, ResizeImageMaskNode, LTXVPreprocess, EmptyLTXVLatentVideo, INTConstant, ResizeImagesByLongerEdge, CLIPTextEncode, IndexTTS2Run, AudioPad, SetNode, ShowText, LTXVImgToVideoInplace, LoadImage, LoadAudio, Int, PrimitiveBoolean, HeartMuLa_Transcribe, AudioSeparation, PreviewAudio, GetNode, GetNode, VHS_VideoCombine, PrimitiveStringMultiline, MarkdownNote, MarkdownNote, CustomAddLabel, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 138076041682713, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 数字人/数字人/LTX2.3-数字人-上传图片和音频生成电商带货数字人_2033156191248977921.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3-数字人-上传图片和音频生成电商带货数字人_2033156191248977921.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（76 个）：
- `KSamplerSelect` ★核心
- `CFGGuider`
- `BasicScheduler`
- `SimpleMath+`
- `easy showAnything`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `PathchSageAttentionKJ`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `ImageSharpen`
- `SetNode`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `SetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `GetImageSize`
- `INTConstant`
- `Reroute`
- `Reroute`
- `SimpleMath+`
- `CM_FloatToInt`
- `AudioDuration_wan`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `ResizeImagesByLongerEdge`
- `CLIPTextEncode` ★核心
- `IndexTTS2Run`
- `AudioPad`
- `SetNode`
- `ShowText`
- `LTXVImgToVideoInplace`
- `LoadImage`
- `LoadAudio`
- `Int`
- `PrimitiveBoolean`
- `HeartMuLa_Transcribe`
- `AudioSeparation`
- `PreviewAudio`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `MarkdownNote`
- `CustomAddLabel`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `138076041682713`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **79%**（60/76）

**有卡**：`KSamplerSelect`、`CFGGuider`、`BasicScheduler`、`SimpleMath+`、`LoraLoaderModelOnly`、`RandomNoise`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`CLIPTextEncode`、`LTXVConditioning`、`PathchSageAttentionKJ`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`KSampler`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`ImageSharpen`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`INTConstant`、`GetImageSize`、`CM_FloatToInt`、`AudioDuration_wan`、`SolidMask`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`ResizeImageMaskNode`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`ResizeImagesByLongerEdge`、`IndexTTS2Run`、`AudioPad`、`ShowText`、`LoadImage`、`LoadAudio`、`Int`、`PrimitiveBoolean`、`HeartMuLa_Transcribe`、`AudioSeparation`、`PreviewAudio`、`VHS_VideoCombine`、`CustomAddLabel`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
