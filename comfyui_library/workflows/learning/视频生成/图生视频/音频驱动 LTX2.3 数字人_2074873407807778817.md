---
key: 视频生成/图生视频/音频驱动 LTX2.3 数字人_2074873407807778817.json
name: 音频驱动 LTX2.3 数字人_2074873407807778817.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/音频驱动 LTX2.3 数字人_2074873407807778817.json
hash: 80b606e5fa34e6bb
coverage: 0.842105
learned_at: 2026-10-15 22:41:19
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, LTX2_NAG, SimpleMath+, INTConstant, INTConstant, LTXVPreprocess, SetNode, PreviewAudio, SimpleMath+, easy showAnything, INTConstant, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, PrimitiveBoolean, LTXVConditioning, CFGGuider, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, LTXVConcatAVLatent, LTXVImgToVideoInplace, LTX2SamplingPreviewOverride, LTXVSeparateAVLatent, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVConcatAVLatent, KSampler, LTXVSeparateAVLatent, GetNode, VAEDecodeTiled, easy cleanGpuUsed, GetNode, LatentUpscaleModelLoader, GetNode, SetLatentNoiseMask, GetNode, LTXVAudioVAEEncode, SolidMask, EmptyLTXVLatentVideo, ImageResizeKJv2, SimpleMath+, GetImageSize+, VHS_VideoCombine, LoadImage, GetNode, CM_FloatToInt, PainterAudioLength, LoadAudio]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 575730340481253, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/音频驱动 LTX2.3 数字人_2074873407807778817.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2074873407807778817.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（57 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LTX2_NAG`
- `SimpleMath+`
- `INTConstant`
- `INTConstant`
- `LTXVPreprocess`
- `SetNode`
- `PreviewAudio`
- `SimpleMath+`
- `easy showAnything`
- `INTConstant`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveBoolean`
- `LTXVConditioning`
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `LTX2SamplingPreviewOverride`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `LatentUpscaleModelLoader`
- `GetNode`
- `SetLatentNoiseMask`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `SimpleMath+`
- `GetImageSize+`
- `VHS_VideoCombine`
- `LoadImage`
- `GetNode`
- `CM_FloatToInt`
- `PainterAudioLength`
- `LoadAudio`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `575730340481253`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **84%**（48/57）

**有卡**：`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LTX2_NAG`、`SimpleMath+`、`INTConstant`、`LTXVPreprocess`、`PreviewAudio`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`PrimitiveBoolean`、`LTXVConditioning`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`KSampler`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`LatentUpscaleModelLoader`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`EmptyLTXVLatentVideo`、`ImageResizeKJv2`、`GetImageSize+`、`VHS_VideoCombine`、`LoadImage`、`CM_FloatToInt`、`PainterAudioLength`、`LoadAudio`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
