---
key: 数字人/数字人/LTX2.3数字人=首尾帧+台本+参考音频_2046018270754508801.json
name: LTX2.3数字人=首尾帧+台本+参考音频_2046018270754508801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3数字人=首尾帧+台本+参考音频_2046018270754508801.json
hash: 15c4078aa6d76a62
coverage: 0.816901
learned_at: 2026-10-26 01:56:03
nodes: [KSamplerSelect, Reroute, LTXVCropGuides, INTConstant, INTConstant, Reroute, CFGGuider, BasicScheduler, LTXVSeparateAVLatent, easy cleanGpuUsed, VAEDecodeTiled, SetNode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LatentUpscaleModelLoader, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVConcatAVLatent, SetNode, SimpleMath+, RandomNoise, GetNode, GetNode, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LoraLoaderModelOnly, ImageSharpen, GetNode, PathchSageAttentionKJ, LTXVAudioVAELoader, LTXVImgToVideoInplace, KSampler, SetLatentNoiseMask, SetNode, GetNode, SolidMask, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, GetNode, LTX2_NAG, CLIPTextEncode, INTConstant, SimpleMath+, AudioDuration_wan, easy showAnything, SimpleMath+, CM_FloatToInt, SaveAudio, AudioPad, LTXVConditioning, CLIPTextEncode, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVFirstLastFrameControl_TTP, LTXVImgToVideoInplace, LTXVPreprocess, GetImageSizeAndCount, ImageResizeKJv2, INTConstant, PrimitiveBoolean, LTXVAudioVAEEncode, LoadAudio, IndexTTS2Run, PrimitiveStringMultiline, LoadImage, PrimitiveStringMultiline, GetImageSize, EmptyLTXVLatentVideo, INTConstant, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 358691681335852, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 数字人/数字人/LTX2.3数字人=首尾帧+台本+参考音频_2046018270754508801.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3数字人=首尾帧+台本+参考音频_2046018270754508801.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVCropGuides`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `CFGGuider`
- `BasicScheduler`
- `LTXVSeparateAVLatent`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `SimpleMath+`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `ImageSharpen`
- `GetNode`
- `PathchSageAttentionKJ`
- `LTXVAudioVAELoader`
- `LTXVImgToVideoInplace`
- `KSampler` ★核心
- `SetLatentNoiseMask`
- `SetNode`
- `GetNode`
- `SolidMask`
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `SimpleMath+`
- `AudioDuration_wan`
- `easy showAnything`
- `SimpleMath+`
- `CM_FloatToInt`
- `SaveAudio`
- `AudioPad`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVFirstLastFrameControl_TTP`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `INTConstant`
- `PrimitiveBoolean`
- `LTXVAudioVAEEncode` ★核心
- `LoadAudio`
- `IndexTTS2Run`
- `PrimitiveStringMultiline`
- `LoadImage`
- `PrimitiveStringMultiline`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `VHS_VideoCombine`
- `LoadImage`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `358691681335852`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **82%**（58/71）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`INTConstant`、`CFGGuider`、`BasicScheduler`、`LTXVSeparateAVLatent`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`LTXVConcatAVLatent`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`SimpleMath+`、`RandomNoise`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`ImageSharpen`、`PathchSageAttentionKJ`、`LTXVAudioVAELoader`、`LTXVImgToVideoInplace`、`KSampler`、`SetLatentNoiseMask`、`SolidMask`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`CLIPTextEncode`、`AudioDuration_wan`、`CM_FloatToInt`、`SaveAudio`、`AudioPad`、`LTXVConditioning`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LTXVFirstLastFrameControl_TTP`、`LTXVPreprocess`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`PrimitiveBoolean`、`LTXVAudioVAEEncode`、`LoadAudio`、`IndexTTS2Run`、`LoadImage`、`GetImageSize`、`EmptyLTXVLatentVideo`、`VHS_VideoCombine`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
