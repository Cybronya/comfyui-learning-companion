---
key: 音频生成/音频生成/LTX2.3数字人_2031246027176546305.json
name: LTX2.3数字人_2031246027176546305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/LTX2.3数字人_2031246027176546305.json
hash: 5337702b00444071
coverage: 0.770492
learned_at: 2026-10-18 02:28:41
nodes: [KSamplerSelect, Reroute, CLIPTextEncode, INTConstant, INTConstant, Reroute, CFGGuider, BasicScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVConcatAVLatent, LTXVConditioning, RandomNoise, LTXAVTextEncoderLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, LTXVAudioVAELoader, LTXVImgToVideoInplace, KSampler, SetLatentNoiseMask, SimpleMath+, easy showAnything, SetNode, LTXVAudioVAEEncode, GetNode, SolidMask, CLIPTextEncode, LTX2SamplingPreviewOverride, LTXVImgToVideoInplace, GetNode, CM_FloatToInt, SetNode, SetNode, GetNode, SimpleMath+, SimpleMath+, LTXVPreprocess, ResizeImageMaskNode, ResizeImagesByLongerEdge, CheckpointLoaderSimple, LTXVConcatAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, GetNode, VAEDecodeTiled, easy cleanGpuUsed, ImageSharpen, GetNode, VHS_VideoCombine, LoadImage, INTConstant, INTConstant, Note, Note, Note, VHS_LoadAudioUpload, PreviewAudio, EmptyLTXVLatentVideo, INTConstant]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 456193948717802, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/LTX2.3数字人_2031246027176546305.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/LTX2.3数字人_2031246027176546305.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（61 个）：
- `KSamplerSelect` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `INTConstant`
- `Reroute`
- `CFGGuider`
- `BasicScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `RandomNoise`
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LTXVAudioVAELoader`
- `LTXVImgToVideoInplace`
- `KSampler` ★核心
- `SetLatentNoiseMask`
- `SimpleMath+`
- `easy showAnything`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SolidMask`
- `CLIPTextEncode` ★核心
- `LTX2SamplingPreviewOverride`
- `LTXVImgToVideoInplace`
- `GetNode`
- `CM_FloatToInt`
- `SetNode`
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `SimpleMath+`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `CheckpointLoaderSimple` ★核心
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `ImageSharpen`
- `GetNode`
- `VHS_VideoCombine`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `Note`
- `Note`
- `Note`
- `VHS_LoadAudioUpload`
- `PreviewAudio`
- `EmptyLTXVLatentVideo`
- `INTConstant`

## 关键参数

- `seed` = `456193948717802`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **77%**（47/61）

**有卡**：`KSamplerSelect`、`CLIPTextEncode`、`INTConstant`、`CFGGuider`、`BasicScheduler`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`LTXVConditioning`、`RandomNoise`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LTXVAudioVAELoader`、`LTXVImgToVideoInplace`、`KSampler`、`SetLatentNoiseMask`、`SimpleMath+`、`LTXVAudioVAEEncode`、`SolidMask`、`LTX2SamplingPreviewOverride`、`CM_FloatToInt`、`LTXVPreprocess`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`CheckpointLoaderSimple`、`LTXVCropGuides`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`ImageSharpen`、`VHS_VideoCombine`、`LoadImage`、`VHS_LoadAudioUpload`、`PreviewAudio`、`EmptyLTXVLatentVideo`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
