---
key: 数字人/数字人/数字人ltx2.5_2087564554460024834.json
name: 数字人ltx2.5_2087564554460024834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/数字人ltx2.5_2087564554460024834.json
hash: d486e7b07fff04c2
coverage: 0.813559
learned_at: 2026-10-18 19:07:51
nodes: [VHS_VideoCombine, KSamplerSelect, BasicScheduler, LTXVConcatAVLatent, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVLatentUpsampler, KSampler, CFGGuider, LTXVConcatAVLatent, LTXVConditioning, VAEDecodeTiled, LTX2SamplingPreviewOverride, CLIPTextEncode, CLIPTextEncode, LTXVCropGuides, easy cleanGpuUsed, SetNode, PathchSageAttentionKJ, LTXVImgToVideoInplace, GetNode, LTXVAudioVAEEncode, SetLatentNoiseMask, LTX2_NAG, easy showAnything, LTXVImgToVideoInplace, LTXVSeparateAVLatent, RTXVideoSuperResolution, SetNode, GetNode, GetNode, CLIPLoader, GetNode, GetNode, EmptyLTXVLatentVideo, LTXVPreprocess, Reroute, Reroute, SolidMask, SimpleMath+, SimpleMath+, SimpleMath+, PreviewAudio, ResizeImagesByLongerEdge, INTConstant, INTConstant, INTConstant, GetImageSize, CM_FloatToInt, PrimitiveBoolean, RandomNoise, UNETLoader, VAELoader, VAELoader, LoadImage, 1hew_AudioDuration, SetNode, LoadAudio, LatentUpscaleModelLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 544887120796468, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 数字人/数字人/数字人ltx2.5_2087564554460024834.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/数字人ltx2.5_2087564554460024834.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（59 个）：
- `VHS_VideoCombine`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `KSampler` ★核心
- `CFGGuider`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `VAEDecodeTiled` ★核心
- `LTX2SamplingPreviewOverride`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVCropGuides`
- `easy cleanGpuUsed`
- `SetNode`
- `PathchSageAttentionKJ`
- `LTXVImgToVideoInplace`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `LTX2_NAG`
- `easy showAnything`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `RTXVideoSuperResolution`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `Reroute`
- `Reroute`
- `SolidMask`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `PreviewAudio`
- `ResizeImagesByLongerEdge`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `GetImageSize`
- `CM_FloatToInt`
- `PrimitiveBoolean`
- `RandomNoise`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `LoadImage`
- `1hew_AudioDuration`
- `SetNode`
- `LoadAudio`
- `LatentUpscaleModelLoader`

## 关键参数

- `seed` = `544887120796468`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **81%**（48/59）

**有卡**：`VHS_VideoCombine`、`KSamplerSelect`、`BasicScheduler`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`KSampler`、`CFGGuider`、`LTXVConditioning`、`VAEDecodeTiled`、`LTX2SamplingPreviewOverride`、`CLIPTextEncode`、`LTXVCropGuides`、`easy cleanGpuUsed`、`PathchSageAttentionKJ`、`LTXVImgToVideoInplace`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LTX2_NAG`、`RTXVideoSuperResolution`、`CLIPLoader`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`SolidMask`、`SimpleMath+`、`PreviewAudio`、`ResizeImagesByLongerEdge`、`INTConstant`、`GetImageSize`、`CM_FloatToInt`、`PrimitiveBoolean`、`RandomNoise`、`UNETLoader`、`VAELoader`、`LoadImage`、`1hew_AudioDuration`、`LoadAudio`、`LatentUpscaleModelLoader`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider、KSamplerSelect

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
