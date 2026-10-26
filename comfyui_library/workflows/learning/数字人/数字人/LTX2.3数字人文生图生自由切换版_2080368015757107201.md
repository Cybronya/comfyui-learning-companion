---
key: 数字人/数字人/LTX2.3数字人文生图生自由切换版_2080368015757107201.json
name: LTX2.3数字人文生图生自由切换版_2080368015757107201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3数字人文生图生自由切换版_2080368015757107201.json
hash: af9fa8294f18c91b
coverage: 0.810345
learned_at: 2026-10-26 01:56:06
nodes: [KSamplerSelect, INTConstant, CFGGuider, BasicScheduler, INTConstant, SetNode, SamplerCustomAdvanced, SetNode, RandomNoise, LTXAVTextEncoderLoader, LTXVAudioVAELoader, PrimitiveBoolean, GetNode, GetNode, LTXVPreprocess, INTConstant, EmptyLTXVLatentVideo, Reroute, Reroute, SolidMask, SimpleMath+, GetImageSize, ResizeImagesByLongerEdge, LTXVAudioVAEEncode, SetLatentNoiseMask, SimpleMath+, RH_GetAudioDuration, CM_FloatToInt, SimpleMath+, easy showAnything, SetNode, PreviewAudio, LoadImage, CheckpointLoaderSimple, PathchSageAttentionKJ, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVSeparateAVLatent, LTXVImgToVideoInplace, LatentUpscaleModelLoader, LTXVCropGuides, GetNode, CLIPTextEncode, LoadAudio, KSampler, LTXVSeparateAVLatent, VAEDecodeTiled, GetNode, easy cleanGpuUsed, RTXVideoSuperResolution, GetNode, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVLatentUpsampler, VHS_VideoCombine, CLIPTextEncode, LTXVConditioning, LTXVConcatAVLatent]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1-42.9G.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 1076580236777122, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 数字人/数字人/LTX2.3数字人文生图生自由切换版_2080368015757107201.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3数字人文生图生自由切换版_2080368015757107201.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（58 个）：
- `KSamplerSelect` ★核心
- `INTConstant`
- `CFGGuider`
- `BasicScheduler`
- `INTConstant`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `RandomNoise`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `PrimitiveBoolean`
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `INTConstant`
- `EmptyLTXVLatentVideo`
- `Reroute`
- `Reroute`
- `SolidMask`
- `SimpleMath+`
- `GetImageSize`
- `ResizeImagesByLongerEdge`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SimpleMath+`
- `RH_GetAudioDuration`
- `CM_FloatToInt`
- `SimpleMath+`
- `easy showAnything`
- `SetNode`
- `PreviewAudio`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `PathchSageAttentionKJ`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LoadAudio`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `easy cleanGpuUsed`
- `RTXVideoSuperResolution`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVConcatAVLatent`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1-42.9G.safetensors`
- `seed` = `1076580236777122`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **81%**（47/58）

**有卡**：`KSamplerSelect`、`INTConstant`、`CFGGuider`、`BasicScheduler`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`PrimitiveBoolean`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`SolidMask`、`SimpleMath+`、`GetImageSize`、`ResizeImagesByLongerEdge`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`RH_GetAudioDuration`、`CM_FloatToInt`、`PreviewAudio`、`LoadImage`、`CheckpointLoaderSimple`、`PathchSageAttentionKJ`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`CLIPTextEncode`、`LoadAudio`、`KSampler`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`RTXVideoSuperResolution`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`VHS_VideoCombine`、`LTXVConditioning`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
