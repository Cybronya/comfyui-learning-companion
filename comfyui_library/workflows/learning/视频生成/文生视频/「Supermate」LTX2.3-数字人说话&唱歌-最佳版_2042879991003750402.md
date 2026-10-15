---
key: 视频生成/文生视频/「Supermate」LTX2.3-数字人说话&唱歌-最佳版_2042879991003750402.json
name: 「Supermate」LTX2.3-数字人说话&唱歌-最佳版_2042879991003750402
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/「Supermate」LTX2.3-数字人说话&唱歌-最佳版_2042879991003750402.json
hash: 7088e6bc22ca12e6
coverage: 0.822581
learned_at: 2026-10-15 22:47:38
nodes: [KSamplerSelect, Reroute, CLIPTextEncode, LTXVCropGuides, INTConstant, INTConstant, Reroute, CFGGuider, BasicScheduler, easy cleanGpuUsed, INTConstant, SetNode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVConcatAVLatent, SetNode, SimpleMath+, SimpleMath+, LTXVConditioning, RandomNoise, GetNode, LTXVPreprocess, ResizeImageMaskNode, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LoraLoaderModelOnly, GetNode, PathchSageAttentionKJ, LTXVAudioVAELoader, ResizeImagesByLongerEdge, PrimitiveBoolean, SetLatentNoiseMask, CM_FloatToInt, SimpleMath+, easy showAnything, SetNode, GetNode, SolidMask, CLIPTextEncode, VHS_VideoCombine, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, GetNode, LTX2_NAG, INTConstant, INTConstant, LoadImage, LTXVImgToVideoInplace, LTXVImgToVideoInplace, ImageSharpen, VHS_LoadAudioUpload, SamplerCustomAdvanced, LTXVAudioVAEEncode, EmptyLTXVLatentVideo, PreviewAudio, KSampler, LTXVSeparateAVLatent, VAEDecodeTiled, GetNode, Label (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 1075776732574013, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/「Supermate」LTX2.3-数字人说话&唱歌-最佳版_2042879991003750402.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/「Supermate」LTX2.3-数字人说话&唱歌-最佳版_2042879991003750402.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（62 个）：
- `KSamplerSelect` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `LTXVCropGuides`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `CFGGuider`
- `BasicScheduler`
- `easy cleanGpuUsed`
- `INTConstant`
- `SetNode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `SimpleMath+`
- `SimpleMath+`
- `LTXVConditioning`
- `RandomNoise`
- `GetNode`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `PathchSageAttentionKJ`
- `LTXVAudioVAELoader`
- `ResizeImagesByLongerEdge`
- `PrimitiveBoolean`
- `SetLatentNoiseMask`
- `CM_FloatToInt`
- `SimpleMath+`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `SolidMask`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `LTX2_NAG`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplace`
- `ImageSharpen`
- `VHS_LoadAudioUpload`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEEncode` ★核心
- `EmptyLTXVLatentVideo`
- `PreviewAudio`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `Label (rgthree)`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `1075776732574013`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **82%**（51/62）

**有卡**：`KSamplerSelect`、`CLIPTextEncode`、`LTXVCropGuides`、`INTConstant`、`CFGGuider`、`BasicScheduler`、`easy cleanGpuUsed`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`SimpleMath+`、`LTXVConditioning`、`RandomNoise`、`LTXVPreprocess`、`ResizeImageMaskNode`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LTXVAudioVAELoader`、`ResizeImagesByLongerEdge`、`PrimitiveBoolean`、`SetLatentNoiseMask`、`CM_FloatToInt`、`SolidMask`、`VHS_VideoCombine`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`LoadImage`、`LTXVImgToVideoInplace`、`ImageSharpen`、`VHS_LoadAudioUpload`、`SamplerCustomAdvanced`、`LTXVAudioVAEEncode`、`EmptyLTXVLatentVideo`、`PreviewAudio`、`KSampler`、`VAEDecodeTiled`、`Label (rgthree)`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
