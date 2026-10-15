---
key: 视频生成/文生视频/LTX2.3数字人 数字人直播+虚拟美女模特 图生视频极速版LTX2.3+数字人话+唱歌_2049691978417352705.json
name: LTX2.3数字人 数字人直播+虚拟美女模特 图生视频极速版LTX2.3+数字人话+唱歌_2049691978417352705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3数字人 数字人直播+虚拟美女模特 图生视频极速版LTX2.3+数字人话+唱歌_2049691978417352705.json
hash: 02894e1866a740dd
coverage: 0.815385
learned_at: 2026-10-15 22:45:08
nodes: [KSamplerSelect, Reroute, LTXVCropGuides, INTConstant, INTConstant, Reroute, INTConstant, LTXVConcatAVLatent, SetNode, SimpleMath+, SimpleMath+, LTXVPreprocess, LoraLoaderModelOnly, PathchSageAttentionKJ, PrimitiveBoolean, SetLatentNoiseMask, CM_FloatToInt, SetNode, SolidMask, PreviewAudio, GetNode, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LTXVImgToVideoInplace, KSampler, RandomNoise, SoundFlow_GetLength, CFGGuider, SamplerCustomAdvanced, ResizeImagesByLongerEdge, ResizeImageMaskNode, GetNode, NormalizeAudioLoudness, EmptyLTXVLatentVideo, easy showAnything, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, LatentUpscaleModelLoader, LTXVAudioVAEEncode, RunningHub Deepcleaner, GetNode, RunningHub Deepcleaner, LTXVConcatAVLatent, SimpleMath+, SetNode, ImageCASharpening+, VAEDecodeTiled, LTXVConditioning, CheckpointLoaderSimple, LTX2SamplingPreviewOverride, GetNode, LTX2_NAG, BasicScheduler, CLIPTextEncode, GetNode, LTXVImgToVideoInplace, AudioCrop, VHS_VideoCombine, LoadAudio, Note, INTConstant, INTConstant, CLIPTextEncode, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 675314036187023, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/LTX2.3数字人 数字人直播+虚拟美女模特 图生视频极速版LTX2.3+数字人话+唱歌_2049691978417352705.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3数字人 数字人直播+虚拟美女模特 图生视频极速版LTX2.3+数字人话+唱歌_2049691978417352705.json`

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
- `LoraLoaderModelOnly` ★核心
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
- `SoundFlow_GetLength`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
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
- `SimpleMath+`
- `SetNode`
- `ImageCASharpening+`
- `VAEDecodeTiled` ★核心
- `LTXVConditioning`
- `CheckpointLoaderSimple` ★核心
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `LTX2_NAG`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LTXVImgToVideoInplace`
- `AudioCrop`
- `VHS_VideoCombine`
- `LoadAudio`
- `Note`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `LoadImage`

## 关键参数

- `seed` = `675314036187023`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **82%**（53/65）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`INTConstant`、`LTXVConcatAVLatent`、`SimpleMath+`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`PrimitiveBoolean`、`SetLatentNoiseMask`、`CM_FloatToInt`、`SolidMask`、`PreviewAudio`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LTXVImgToVideoInplace`、`KSampler`、`RandomNoise`、`SoundFlow_GetLength`、`CFGGuider`、`SamplerCustomAdvanced`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`NormalizeAudioLoudness`、`EmptyLTXVLatentVideo`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`LTXVAudioVAEEncode`、`RunningHub Deepcleaner`、`ImageCASharpening+`、`VAEDecodeTiled`、`LTXVConditioning`、`CheckpointLoaderSimple`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`BasicScheduler`、`CLIPTextEncode`、`AudioCrop`、`VHS_VideoCombine`、`LoadAudio`、`LoadImage`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
