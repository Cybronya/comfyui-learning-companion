---
key: 视频生成/文生视频/LTX2.3数字人 音频驱动_2082129889662160897.json
name: LTX2.3数字人 音频驱动_2082129889662160897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3数字人 音频驱动_2082129889662160897.json
hash: 35320bc7e3184efc
coverage: 0.810345
learned_at: 2026-10-15 22:45:08
nodes: [KSamplerSelect, LTXVCropGuides, INTConstant, CFGGuider, BasicScheduler, easy cleanGpuUsed, INTConstant, SetNode, LTXVConcatAVLatent, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVConcatAVLatent, SetNode, GetNode, GetNode, LTXAVTextEncoderLoader, PathchSageAttentionKJ, LTXVAudioVAELoader, LTXVImgToVideoInplace, KSampler, PrimitiveBoolean, GetNode, GetNode, LatentUpscaleModelLoader, LTXVConditioning, LTXVPreprocess, VAEDecodeTiled, GetNode, INTConstant, EmptyLTXVLatentVideo, Reroute, Reroute, SolidMask, SimpleMath+, GetImageSize, LTX2SamplingPreviewOverride, LTXVAudioVAEEncode, SetLatentNoiseMask, LTX2_NAG, SimpleMath+, RH_GetAudioDuration, CM_FloatToInt, SimpleMath+, easy showAnything, SetNode, PreviewAudio, LTXVImgToVideoInplace, CLIPTextEncode, LTXVSeparateAVLatent, RTXVideoSuperResolution, VHS_VideoCombine, CLIPTextEncode, CheckpointLoaderSimple, RandomNoise, ResizeImagesByLongerEdge, LoadAudio, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1-42.9G.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 372289123277222, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/LTX2.3数字人 音频驱动_2082129889662160897.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3数字人 音频驱动_2082129889662160897.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（58 个）：
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `INTConstant`
- `CFGGuider`
- `BasicScheduler`
- `easy cleanGpuUsed`
- `INTConstant`
- `SetNode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXAVTextEncoderLoader`
- `PathchSageAttentionKJ`
- `LTXVAudioVAELoader`
- `LTXVImgToVideoInplace`
- `KSampler` ★核心
- `PrimitiveBoolean`
- `GetNode`
- `GetNode`
- `LatentUpscaleModelLoader`
- `LTXVConditioning`
- `LTXVPreprocess`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `INTConstant`
- `EmptyLTXVLatentVideo`
- `Reroute`
- `Reroute`
- `SolidMask`
- `SimpleMath+`
- `GetImageSize`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `LTX2_NAG`
- `SimpleMath+`
- `RH_GetAudioDuration`
- `CM_FloatToInt`
- `SimpleMath+`
- `easy showAnything`
- `SetNode`
- `PreviewAudio`
- `LTXVImgToVideoInplace`
- `CLIPTextEncode` ★核心
- `LTXVSeparateAVLatent`
- `RTXVideoSuperResolution`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `LoadAudio`
- `LoadImage`

## 关键参数

- `seed` = `372289123277222`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1-42.9G.safetensors`

## 知识

覆盖率 **81%**（47/58）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`INTConstant`、`CFGGuider`、`BasicScheduler`、`easy cleanGpuUsed`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`LTXAVTextEncoderLoader`、`PathchSageAttentionKJ`、`LTXVAudioVAELoader`、`LTXVImgToVideoInplace`、`KSampler`、`PrimitiveBoolean`、`LatentUpscaleModelLoader`、`LTXVConditioning`、`LTXVPreprocess`、`VAEDecodeTiled`、`EmptyLTXVLatentVideo`、`SolidMask`、`SimpleMath+`、`GetImageSize`、`LTX2SamplingPreviewOverride`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LTX2_NAG`、`RH_GetAudioDuration`、`CM_FloatToInt`、`PreviewAudio`、`CLIPTextEncode`、`RTXVideoSuperResolution`、`VHS_VideoCombine`、`CheckpointLoaderSimple`、`RandomNoise`、`ResizeImagesByLongerEdge`、`LoadAudio`、`LoadImage`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
