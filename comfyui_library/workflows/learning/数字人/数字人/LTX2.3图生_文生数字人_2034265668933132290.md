---
key: 数字人/数字人/LTX2.3图生_文生数字人_2034265668933132290.json
name: LTX2.3图生_文生数字人_2034265668933132290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3图生_文生数字人_2034265668933132290.json
hash: 0e19922514f09504
coverage: 0.819672
learned_at: 2026-10-26 01:55:58
nodes: [KSamplerSelect, Reroute, CLIPTextEncode, LTXVCropGuides, INTConstant, CFGGuider, BasicScheduler, LTXVSeparateAVLatent, easy cleanGpuUsed, VAEDecodeTiled, INTConstant, SetNode, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVSeparateAVLatent, LatentUpscaleModelLoader, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVConcatAVLatent, SetNode, SimpleMath+, LTXVConditioning, RandomNoise, GetNode, GetNode, LTXVPreprocess, ResizeImageMaskNode, INTConstant, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LoraLoaderModelOnly, ImageSharpen, GetNode, PathchSageAttentionKJ, LTXVAudioVAELoader, ResizeImagesByLongerEdge, LTXVImgToVideoInplace, KSampler, SetLatentNoiseMask, CM_FloatToInt, SimpleMath+, easy showAnything, SetNode, LTXVAudioVAEEncode, GetNode, SolidMask, PreviewAudio, CLIPTextEncode, VHS_VideoCombine, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, LTXVImgToVideoInplace, GetNode, LTX2_NAG, PrimitiveBoolean, LoadImage, VHS_LoadAudioUpload, INTConstant, SimpleMath+, INTConstant, Reroute]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 1083582520300267, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 数字人/数字人/LTX2.3图生_文生数字人_2034265668933132290.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3图生_文生数字人_2034265668933132290.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（61 个）：
- `KSamplerSelect` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `LTXVCropGuides`
- `INTConstant`
- `CFGGuider`
- `BasicScheduler`
- `LTXVSeparateAVLatent`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `INTConstant`
- `SetNode`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `SimpleMath+`
- `LTXVConditioning`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `INTConstant`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `ImageSharpen`
- `GetNode`
- `PathchSageAttentionKJ`
- `LTXVAudioVAELoader`
- `ResizeImagesByLongerEdge`
- `LTXVImgToVideoInplace`
- `KSampler` ★核心
- `SetLatentNoiseMask`
- `CM_FloatToInt`
- `SimpleMath+`
- `easy showAnything`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SolidMask`
- `PreviewAudio`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoInplace`
- `GetNode`
- `LTX2_NAG`
- `PrimitiveBoolean`
- `LoadImage`
- `VHS_LoadAudioUpload`
- `INTConstant`
- `SimpleMath+`
- `INTConstant`
- `Reroute`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `1083582520300267`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **82%**（50/61）

**有卡**：`KSamplerSelect`、`CLIPTextEncode`、`LTXVCropGuides`、`INTConstant`、`CFGGuider`、`BasicScheduler`、`LTXVSeparateAVLatent`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`SimpleMath+`、`LTXVConditioning`、`RandomNoise`、`LTXVPreprocess`、`ResizeImageMaskNode`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`ImageSharpen`、`PathchSageAttentionKJ`、`LTXVAudioVAELoader`、`ResizeImagesByLongerEdge`、`LTXVImgToVideoInplace`、`KSampler`、`SetLatentNoiseMask`、`CM_FloatToInt`、`LTXVAudioVAEEncode`、`SolidMask`、`PreviewAudio`、`VHS_VideoCombine`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`PrimitiveBoolean`、`LoadImage`、`VHS_LoadAudioUpload`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
