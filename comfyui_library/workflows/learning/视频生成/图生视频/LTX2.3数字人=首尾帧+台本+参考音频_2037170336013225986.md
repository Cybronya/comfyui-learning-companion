---
key: 视频生成/图生视频/LTX2.3数字人=首尾帧+台本+参考音频_2037170336013225986.json
name: LTX2.3数字人=首尾帧+台本+参考音频_2037170336013225986.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2037170336013225986.json
hash: 93bc4f6b3f3a8c4e
coverage: 0.816901
learned_at: 2026-10-15 22:35:56
nodes: [KSamplerSelect, Reroute, LTXVCropGuides, INTConstant, INTConstant, Reroute, CFGGuider, BasicScheduler, LTXVSeparateAVLatent, easy cleanGpuUsed, VAEDecodeTiled, INTConstant, SetNode, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVSeparateAVLatent, LatentUpscaleModelLoader, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVConcatAVLatent, SetNode, SimpleMath+, RandomNoise, GetNode, GetNode, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LoraLoaderModelOnly, ImageSharpen, GetNode, PathchSageAttentionKJ, LTXVAudioVAELoader, LTXVImgToVideoInplace, KSampler, PrimitiveBoolean, SetLatentNoiseMask, SetNode, LTXVAudioVAEEncode, GetNode, SolidMask, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, GetNode, LTX2_NAG, CLIPTextEncode, INTConstant, INTConstant, SimpleMath+, LoadAudio, IndexTTS2Run, AudioDuration_wan, easy showAnything, SimpleMath+, CM_FloatToInt, SaveAudio, AudioPad, LTXVConditioning, CLIPTextEncode, VHS_VideoCombine, ResizeImageMaskNode, ResizeImagesByLongerEdge, GetImageSize, LTXVFirstLastFrameControl_TTP, LTXVImgToVideoInplace, LTXVPreprocess, GetImageSizeAndCount, ImageResizeKJv2, PrimitiveStringMultiline, PrimitiveStringMultiline, LoadImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 156027950272284, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/LTX2.3数字人=首尾帧+台本+参考音频_2037170336013225986.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037170336013225986.json`

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
- `PrimitiveBoolean`
- `SetLatentNoiseMask`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SolidMask`
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `LoadAudio`
- `IndexTTS2Run`
- `AudioDuration_wan`
- `easy showAnything`
- `SimpleMath+`
- `CM_FloatToInt`
- `SaveAudio`
- `AudioPad`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `GetImageSize`
- `LTXVFirstLastFrameControl_TTP`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `156027950272284`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **82%**（58/71）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`INTConstant`、`CFGGuider`、`BasicScheduler`、`LTXVSeparateAVLatent`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`SimpleMath+`、`RandomNoise`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`ImageSharpen`、`PathchSageAttentionKJ`、`LTXVAudioVAELoader`、`LTXVImgToVideoInplace`、`KSampler`、`PrimitiveBoolean`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`CLIPTextEncode`、`LoadAudio`、`IndexTTS2Run`、`AudioDuration_wan`、`CM_FloatToInt`、`SaveAudio`、`AudioPad`、`LTXVConditioning`、`VHS_VideoCombine`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`GetImageSize`、`LTXVFirstLastFrameControl_TTP`、`LTXVPreprocess`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`LoadImage`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
