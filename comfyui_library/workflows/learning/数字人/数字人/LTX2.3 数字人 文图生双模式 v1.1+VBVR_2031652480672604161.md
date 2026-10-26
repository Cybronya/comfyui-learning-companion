---
key: 数字人/数字人/LTX2.3 数字人 文图生双模式 v1.1+VBVR_2031652480672604161.json
name: LTX2.3 数字人 文图生双模式 v1.1+VBVR_2031652480672604161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3 数字人 文图生双模式 v1.1+VBVR_2031652480672604161.json
hash: a517cfc0370c6de1
coverage: 0.819672
learned_at: 2026-10-26 01:55:51
nodes: [Note, Note, KSamplerSelect, Reroute, LTXVCropGuides, INTConstant, INTConstant, Reroute, CFGGuider, BasicScheduler, LTXVSeparateAVLatent, easy cleanGpuUsed, VAEDecodeTiled, INTConstant, SetNode, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVSeparateAVLatent, LatentUpscaleModelLoader, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVConcatAVLatent, SetNode, SimpleMath+, SimpleMath+, RandomNoise, GetNode, LTXVPreprocess, ResizeImageMaskNode, LTXAVTextEncoderLoader, ImageSharpen, GetNode, PathchSageAttentionKJ, LTXVAudioVAELoader, ResizeImagesByLongerEdge, LTXVImgToVideoInplace, KSampler, PrimitiveBoolean, SetLatentNoiseMask, CM_FloatToInt, SimpleMath+, easy showAnything, SetNode, LTXVAudioVAEEncode, GetNode, SolidMask, PreviewAudio, VHS_VideoCombine, LTX2SamplingPreviewOverride, LTXVImgToVideoInplace, LTX2_NAG, CLIPTextEncode, INTConstant, INTConstant, LoadImage, VHS_LoadAudioUpload, CheckpointLoaderSimple, VRAMReserver, LoraLoaderModelOnly, LTXVConditioning, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 489287399914981, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 数字人/数字人/LTX2.3 数字人 文图生双模式 v1.1+VBVR_2031652480672604161.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3 数字人 文图生双模式 v1.1+VBVR_2031652480672604161.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（61 个）：
- `Note`
- `Note`
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
- `SimpleMath+`
- `RandomNoise`
- `GetNode`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `LTXAVTextEncoderLoader`
- `ImageSharpen`
- `GetNode`
- `PathchSageAttentionKJ`
- `LTXVAudioVAELoader`
- `ResizeImagesByLongerEdge`
- `LTXVImgToVideoInplace`
- `KSampler` ★核心
- `PrimitiveBoolean`
- `SetLatentNoiseMask`
- `CM_FloatToInt`
- `SimpleMath+`
- `easy showAnything`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SolidMask`
- `PreviewAudio`
- `VHS_VideoCombine`
- `LTX2SamplingPreviewOverride`
- `LTXVImgToVideoInplace`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `VHS_LoadAudioUpload`
- `CheckpointLoaderSimple` ★核心
- `VRAMReserver`
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `489287399914981`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **82%**（50/61）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`INTConstant`、`CFGGuider`、`BasicScheduler`、`LTXVSeparateAVLatent`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`SimpleMath+`、`RandomNoise`、`LTXVPreprocess`、`ResizeImageMaskNode`、`LTXAVTextEncoderLoader`、`ImageSharpen`、`PathchSageAttentionKJ`、`LTXVAudioVAELoader`、`ResizeImagesByLongerEdge`、`LTXVImgToVideoInplace`、`KSampler`、`PrimitiveBoolean`、`SetLatentNoiseMask`、`CM_FloatToInt`、`LTXVAudioVAEEncode`、`SolidMask`、`PreviewAudio`、`VHS_VideoCombine`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`CLIPTextEncode`、`LoadImage`、`VHS_LoadAudioUpload`、`CheckpointLoaderSimple`、`VRAMReserver`、`LoraLoaderModelOnly`、`LTXVConditioning`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
