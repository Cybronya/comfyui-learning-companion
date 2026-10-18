---
key: 视频生成/图生视频/最佳口播数字人_LTX2.3_音频驱动_嘴型精准_高清输出_2104490779896016898.json
name: 最佳口播数字人_LTX2.3_音频驱动_嘴型精准_高清输出_2104490779896016898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/最佳口播数字人_LTX2.3_音频驱动_嘴型精准_高清输出_2104490779896016898.json
hash: f8d80b2fb5b7d5b0
coverage: 0.803571
learned_at: 2026-10-17 22:20:09
nodes: [SetNode, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVConcatAVLatent, SetNode, GetNode, GetNode, KSampler, GetNode, GetNode, GetNode, Reroute, Reroute, SolidMask, SimpleMath+, SimpleMath+, SimpleMath+, SetNode, PreviewAudio, LTXVImgToVideoInplace, INTConstant, INTConstant, EmptyLTXVLatentVideo, BasicScheduler, RandomNoise, INTConstant, KSamplerSelect, LTXVAudioVAELoader, PathchSageAttentionKJ, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, CheckpointLoaderSimple, RH_GetAudioDuration, LTXVAudioVAEEncode, ResizeImagesByLongerEdge, LTXVPreprocess, GetImageSize, CM_FloatToInt, LTX2_NAG, LTX2SamplingPreviewOverride, LTXVCropGuides, LTXVConditioning, CFGGuider, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVSeparateAVLatent, SetLatentNoiseMask, VAEDecodeTiled, easy showAnything, LoadImage, LoadAudio, CLIPTextEncode, CLIPTextEncode, easy cleanGpuUsed, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1-42.9G.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 507624643765598, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/最佳口播数字人_LTX2.3_音频驱动_嘴型精准_高清输出_2104490779896016898.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/最佳口播数字人_LTX2.3_音频驱动_嘴型精准_高清输出_2104490779896016898.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（56 个）：
- `SetNode`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `Reroute`
- `SolidMask`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SetNode`
- `PreviewAudio`
- `LTXVImgToVideoInplace`
- `INTConstant`
- `INTConstant`
- `EmptyLTXVLatentVideo`
- `BasicScheduler`
- `RandomNoise`
- `INTConstant`
- `KSamplerSelect` ★核心
- `LTXVAudioVAELoader`
- `PathchSageAttentionKJ`
- `LatentUpscaleModelLoader`
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `RH_GetAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `GetImageSize`
- `CM_FloatToInt`
- `LTX2_NAG`
- `LTX2SamplingPreviewOverride`
- `LTXVCropGuides`
- `LTXVConditioning`
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `SetLatentNoiseMask`
- `VAEDecodeTiled` ★核心
- `easy showAnything`
- `LoadImage`
- `LoadAudio`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `507624643765598`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1-42.9G.safetensors`

## 知识

覆盖率 **80%**（45/56）

**有卡**：`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`KSampler`、`SolidMask`、`SimpleMath+`、`PreviewAudio`、`LTXVImgToVideoInplace`、`INTConstant`、`EmptyLTXVLatentVideo`、`BasicScheduler`、`RandomNoise`、`KSamplerSelect`、`LTXVAudioVAELoader`、`PathchSageAttentionKJ`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`RH_GetAudioDuration`、`LTXVAudioVAEEncode`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`GetImageSize`、`CM_FloatToInt`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LTXVCropGuides`、`LTXVConditioning`、`CFGGuider`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`SetLatentNoiseMask`、`VAEDecodeTiled`、`LoadImage`、`LoadAudio`、`CLIPTextEncode`、`easy cleanGpuUsed`、`VHS_VideoCombine`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
