---
key: 数字人/数字人/LTX2.3多图参考MV_2032770671985565698.json
name: LTX2.3多图参考MV_2032770671985565698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3多图参考MV_2032770671985565698.json
hash: cf6a3b379d6db985
coverage: 0.859375
learned_at: 2026-10-26 01:55:58
nodes: [SimpleMath+, SimpleMath+, CheckpointLoaderSimple, LTXVAudioVAELoader, LoraLoaderModelOnly, PathchSageAttentionKJ, LTX2_NAG, LTX2SamplingPreviewOverride, SetNode, SetNode, LTXAVTextEncoderLoader, LTXVConditioning, CFGGuider, RandomNoise, KSamplerSelect, BasicScheduler, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVCropGuides, KSampler, LTXVConcatAVLatent, GetNode, LTXVSeparateAVLatent, VAEDecodeTiled, GetNode, SetLatentNoiseMask, LTXVAudioVAEEncode, GetNode, SolidMask, EmptyLTXVLatentVideo, CM_FloatToInt, SimpleMath+, easy showAnything, INTConstant, INTConstant, GetNode, CLIPTextEncode, GetImageSize+, LTXVPreprocess, ImageResizeKJv2, LTXVPreprocess, ImageResizeKJv2, LTXVPreprocess, GetNode, LTXVLatentUpsampler, SamplerCustomAdvanced, PreviewAudio, LoraLoaderModelOnly, LatentUpscaleModelLoader, easy cleanGpuUsed, INTConstant, ImageResizeKJv2, VHS_VideoCombine, ImageResizeKJv2, LTXVPreprocess, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, CLIPTextEncode, VHS_LoadAudioUpload, LTXVImgToVideoInplaceKJ, LTXVImgToVideoInplaceKJ]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 986624366052355, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 数字人/数字人/LTX2.3多图参考MV_2032770671985565698.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3多图参考MV_2032770671985565698.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（64 个）：
- `SimpleMath+`
- `SimpleMath+`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LTX2_NAG`
- `LTX2SamplingPreviewOverride`
- `SetNode`
- `SetNode`
- `LTXAVTextEncoderLoader`
- `LTXVConditioning`
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `KSampler` ★核心
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SolidMask`
- `EmptyLTXVLatentVideo`
- `CM_FloatToInt`
- `SimpleMath+`
- `easy showAnything`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetImageSize+`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `PreviewAudio`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `easy cleanGpuUsed`
- `INTConstant`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `VHS_LoadAudioUpload`
- `LTXVImgToVideoInplaceKJ`
- `LTXVImgToVideoInplaceKJ`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `986624366052355`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **86%**（55/64）

**有卡**：`SimpleMath+`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LTXAVTextEncoderLoader`、`LTXVConditioning`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`KSampler`、`VAEDecodeTiled`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`EmptyLTXVLatentVideo`、`CM_FloatToInt`、`INTConstant`、`CLIPTextEncode`、`GetImageSize+`、`LTXVPreprocess`、`ImageResizeKJv2`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`PreviewAudio`、`LatentUpscaleModelLoader`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`LoadImage`、`VHS_LoadAudioUpload`、`LTXVImgToVideoInplaceKJ`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
