---
key: 视频生成/图生视频/LTX2.3多参数字人 口播带货生视频（图片+参考音频+台词）_2094393909978943489.json
name: LTX2.3多参数字人 口播带货生视频（图片+参考音频+台词）_2094393909978943489
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3多参数字人 口播带货生视频（图片+参考音频+台词）_2094393909978943489.json
hash: f88883b1b2679ba7
coverage: 0.785714
learned_at: 2026-10-17 00:02:14
nodes: [KSamplerSelect, CFGGuider, BasicScheduler, GetNode, GetNode, SimpleMath+, easy showAnything, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, RandomNoise, LTX2SamplingPreviewOverride, LTX2_NAG, CLIPTextEncode, LTXVConditioning, PathchSageAttentionKJ, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVConcatAVLatent, LatentUpscaleModelLoader, SamplerCustomAdvanced, GetNode, LTXVImgToVideoInplace, LTXVCropGuides, LTXVLatentUpsampler, KSampler, LTXVSeparateAVLatent, GetNode, VAEDecodeTiled, easy cleanGpuUsed, ImageSharpen, SetNode, SetNode, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LTXVAudioVAELoader, SetNode, LTXVImgToVideoInplace, GetNode, INTConstant, INTConstant, INTConstant, SimpleMath+, GetImageSize, INTConstant, Reroute, Reroute, SimpleMath+, CM_FloatToInt, AudioDuration_wan, SolidMask, LTXVAudioVAEEncode, SetLatentNoiseMask, LTXVPreprocess, EmptyLTXVLatentVideo, PrimitiveBoolean, INTConstant, CLIPTextEncode, IndexTTS2Run, PrimitiveStringMultiline, VHS_VideoCombine, AudioPad, SetNode, PreviewAudio, ResizeImageMaskNode, ResizeImagesByLongerEdge, LoadAudio, Int, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 887398371304596, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/LTX2.3多参数字人 口播带货生视频（图片+参考音频+台词）_2094393909978943489.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3多参数字人 口播带货生视频（图片+参考音频+台词）_2094393909978943489.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（70 个）：
- `KSamplerSelect` ★核心
- `CFGGuider`
- `BasicScheduler`
- `GetNode`
- `GetNode`
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
- `LTXVImgToVideoInplace`
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
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `PrimitiveBoolean`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `IndexTTS2Run`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `AudioPad`
- `SetNode`
- `PreviewAudio`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LoadAudio`
- `Int`
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `887398371304596`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **79%**（55/70）

**有卡**：`KSamplerSelect`、`CFGGuider`、`BasicScheduler`、`SimpleMath+`、`LoraLoaderModelOnly`、`RandomNoise`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`CLIPTextEncode`、`LTXVConditioning`、`PathchSageAttentionKJ`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`KSampler`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`ImageSharpen`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`INTConstant`、`GetImageSize`、`CM_FloatToInt`、`AudioDuration_wan`、`SolidMask`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`PrimitiveBoolean`、`IndexTTS2Run`、`VHS_VideoCombine`、`AudioPad`、`PreviewAudio`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LoadAudio`、`Int`、`LoadImage`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
