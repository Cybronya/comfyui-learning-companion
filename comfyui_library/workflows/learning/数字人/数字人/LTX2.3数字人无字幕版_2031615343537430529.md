---
key: 数字人/数字人/LTX2.3数字人无字幕版_2031615343537430529.json
name: LTX2.3数字人无字幕版_2031615343537430529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3数字人无字幕版_2031615343537430529.json
hash: 79a90c92399b1f75
coverage: 0.815385
learned_at: 2026-10-26 01:56:06
nodes: [KSamplerSelect, Reroute, LTXVCropGuides, INTConstant, INTConstant, Reroute, INTConstant, LTXVConcatAVLatent, SetNode, SimpleMath+, SimpleMath+, LTXVPreprocess, INTConstant, INTConstant, LoraLoaderModelOnly, GetNode, PathchSageAttentionKJ, PrimitiveBoolean, SetLatentNoiseMask, CM_FloatToInt, SetNode, SolidMask, PreviewAudio, GetNode, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LTXVImgToVideoInplace, KSampler, RandomNoise, LoadImage, SoundFlow_GetLength, CFGGuider, SamplerCustomAdvanced, LTXVImgToVideoInplace, ResizeImagesByLongerEdge, ResizeImageMaskNode, GetNode, NormalizeAudioLoudness, EmptyLTXVLatentVideo, easy showAnything, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, LatentUpscaleModelLoader, LTXVAudioVAEEncode, RunningHub Deepcleaner, GetNode, RunningHub Deepcleaner, LTXVConcatAVLatent, LoadAudio, AudioCrop, SimpleMath+, VHS_VideoCombine, SetNode, ImageCASharpening+, VAEDecodeTiled, LTXVConditioning, CheckpointLoaderSimple, LTX2SamplingPreviewOverride, GetNode, LTX2_NAG, CLIPTextEncode, BasicScheduler, CLIPTextEncode, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 1106542610737212, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 数字人/数字人/LTX2.3数字人无字幕版_2031615343537430529.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3数字人无字幕版_2031615343537430529.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（65 个）：
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVCropGuides`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `INTConstant`
- `LTXVConcatAVLatent`
- `SetNode`
- `SimpleMath+`
- `SimpleMath+`
- `LTXVPreprocess`
- `INTConstant`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `SetLatentNoiseMask`
- `CM_FloatToInt`
- `SetNode`
- `SolidMask`
- `PreviewAudio`
- `GetNode`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LTXVImgToVideoInplace`
- `KSampler` ★核心
- `RandomNoise`
- `LoadImage`
- `SoundFlow_GetLength`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `ResizeImagesByLongerEdge`
- `ResizeImageMaskNode`
- `GetNode`
- `NormalizeAudioLoudness`
- `EmptyLTXVLatentVideo`
- `easy showAnything`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `LTXVAudioVAEEncode` ★核心
- `RunningHub Deepcleaner`
- `GetNode`
- `RunningHub Deepcleaner`
- `LTXVConcatAVLatent`
- `LoadAudio`
- `AudioCrop`
- `SimpleMath+`
- `VHS_VideoCombine`
- `SetNode`
- `ImageCASharpening+`
- `VAEDecodeTiled` ★核心
- `LTXVConditioning`
- `CheckpointLoaderSimple` ★核心
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `Note`

## 关键参数

- `seed` = `1106542610737212`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **82%**（53/65）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`INTConstant`、`LTXVConcatAVLatent`、`SimpleMath+`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`PrimitiveBoolean`、`SetLatentNoiseMask`、`CM_FloatToInt`、`SolidMask`、`PreviewAudio`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LTXVImgToVideoInplace`、`KSampler`、`RandomNoise`、`LoadImage`、`SoundFlow_GetLength`、`CFGGuider`、`SamplerCustomAdvanced`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`NormalizeAudioLoudness`、`EmptyLTXVLatentVideo`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`LTXVAudioVAEEncode`、`RunningHub Deepcleaner`、`LoadAudio`、`AudioCrop`、`VHS_VideoCombine`、`ImageCASharpening+`、`VAEDecodeTiled`、`LTXVConditioning`、`CheckpointLoaderSimple`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`CLIPTextEncode`、`BasicScheduler`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
