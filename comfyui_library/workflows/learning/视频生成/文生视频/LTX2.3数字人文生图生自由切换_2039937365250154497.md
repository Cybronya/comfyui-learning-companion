---
key: 视频生成/文生视频/LTX2.3数字人文生图生自由切换_2039937365250154497.json
name: LTX2.3数字人文生图生自由切换_2039937365250154497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3数字人文生图生自由切换_2039937365250154497.json
hash: 747e5411b369ca31
coverage: 0.819672
learned_at: 2026-10-15 22:45:09
nodes: [KSamplerSelect, Reroute, LTXVCropGuides, INTConstant, INTConstant, Reroute, CFGGuider, BasicScheduler, INTConstant, SetNode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LatentUpscaleModelLoader, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVConcatAVLatent, SetNode, SimpleMath+, SimpleMath+, GetNode, GetNode, LTXVPreprocess, ResizeImageMaskNode, INTConstant, INTConstant, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, LTXVAudioVAELoader, ResizeImagesByLongerEdge, LTXVImgToVideoInplace, CM_FloatToInt, SimpleMath+, easy showAnything, SetNode, SolidMask, LoraLoaderModelOnly, GetNode, VHS_LoadAudioUpload, PreviewAudio, LTXVImgToVideoInplace, CLIPTextEncode, LTXVConditioning, RandomNoise, PrimitiveBoolean, LTXVAudioVAEEncode, SetLatentNoiseMask, GetNode, LTX2_NAG, LoadImage, EmptyLTXVLatentVideo, KSampler, LTXVSeparateAVLatent, VAEDecodeTiled, easy cleanGpuUsed, ImageSharpen, GetNode, CLIPTextEncode, LTX2SamplingPreviewOverride, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 67901950620255, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/LTX2.3数字人文生图生自由切换_2039937365250154497.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3数字人文生图生自由切换_2039937365250154497.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（61 个）：
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVCropGuides`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `CFGGuider`
- `BasicScheduler`
- `INTConstant`
- `SetNode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `SimpleMath+`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `INTConstant`
- `INTConstant`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LTXVAudioVAELoader`
- `ResizeImagesByLongerEdge`
- `LTXVImgToVideoInplace`
- `CM_FloatToInt`
- `SimpleMath+`
- `easy showAnything`
- `SetNode`
- `SolidMask`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `VHS_LoadAudioUpload`
- `PreviewAudio`
- `LTXVImgToVideoInplace`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `RandomNoise`
- `PrimitiveBoolean`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `GetNode`
- `LTX2_NAG`
- `LoadImage`
- `EmptyLTXVLatentVideo`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `ImageSharpen`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LTX2SamplingPreviewOverride`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `67901950620255`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **82%**（50/61）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`INTConstant`、`CFGGuider`、`BasicScheduler`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`SimpleMath+`、`LTXVPreprocess`、`ResizeImageMaskNode`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LTXVAudioVAELoader`、`ResizeImagesByLongerEdge`、`LTXVImgToVideoInplace`、`CM_FloatToInt`、`SolidMask`、`VHS_LoadAudioUpload`、`PreviewAudio`、`CLIPTextEncode`、`LTXVConditioning`、`RandomNoise`、`PrimitiveBoolean`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LTX2_NAG`、`LoadImage`、`EmptyLTXVLatentVideo`、`KSampler`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`ImageSharpen`、`LTX2SamplingPreviewOverride`、`VHS_VideoCombine`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
