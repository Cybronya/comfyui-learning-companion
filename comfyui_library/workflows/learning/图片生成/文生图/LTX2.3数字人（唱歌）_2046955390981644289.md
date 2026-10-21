---
key: 图片生成/文生图/LTX2.3数字人（唱歌）_2046955390981644289.json
name: LTX2.3数字人（唱歌）_2046955390981644289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/LTX2.3数字人（唱歌）_2046955390981644289.json
hash: 30e93d6150c6c509
coverage: 0.822581
learned_at: 2026-10-21 02:53:29
nodes: [Reroute, INTConstant, INTConstant, Reroute, SimpleMath+, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVCropGuides, LTXVConcatAVLatent, KSampler, LTXVSeparateAVLatent, VAEDecodeTiled, ImageSharpen, easy cleanGpuUsed, GetNode, SimpleMath+, LTX2_NAG, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, SetNode, SolidMask, easy showAnything, LTXVAudioVAEEncode, SetLatentNoiseMask, INTConstant, CM_FloatToInt, GetNode, PreviewAudio, SimpleMath+, PrimitiveBoolean, INTConstant, GetNode, GetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, INTConstant, VHS_LoadAudioUpload, LatentUpscaleModelLoader, RandomNoise, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVImgToVideoInplace, CFGGuider, GetNode, LoadImage, EmptyLTXVLatentVideo, VHS_VideoCombine, ResizeImagesByLongerEdge, ResizeImageMaskNode, CLIPTextEncode, LTX2SamplingPreviewOverride, LTXVConditioning, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, LTXVPreprocess]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 384805116003596, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 图片生成/文生图/LTX2.3数字人（唱歌）_2046955390981644289.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/LTX2.3数字人（唱歌）_2046955390981644289.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（62 个）：
- `Reroute`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `SimpleMath+`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVCropGuides`
- `LTXVConcatAVLatent`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `ImageSharpen`
- `easy cleanGpuUsed`
- `GetNode`
- `SimpleMath+`
- `LTX2_NAG`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `SetNode`
- `SolidMask`
- `easy showAnything`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `INTConstant`
- `CM_FloatToInt`
- `GetNode`
- `PreviewAudio`
- `SimpleMath+`
- `PrimitiveBoolean`
- `INTConstant`
- `GetNode`
- `GetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `INTConstant`
- `VHS_LoadAudioUpload`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `GetNode`
- `LoadImage`
- `EmptyLTXVLatentVideo`
- `VHS_VideoCombine`
- `ResizeImagesByLongerEdge`
- `ResizeImageMaskNode`
- `CLIPTextEncode` ★核心
- `LTX2SamplingPreviewOverride`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LTXVPreprocess`

## 关键参数

- `seed` = `384805116003596`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **82%**（51/62）

**有卡**：`INTConstant`、`SimpleMath+`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`KSampler`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`ImageSharpen`、`easy cleanGpuUsed`、`LTX2_NAG`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`SolidMask`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`CM_FloatToInt`、`PreviewAudio`、`PrimitiveBoolean`、`LoraLoaderModelOnly`、`VHS_LoadAudioUpload`、`LatentUpscaleModelLoader`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`CFGGuider`、`LoadImage`、`EmptyLTXVLatentVideo`、`VHS_VideoCombine`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`CLIPTextEncode`、`LTX2SamplingPreviewOverride`、`LTXVConditioning`、`PathchSageAttentionKJ`、`LTXVPreprocess`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
