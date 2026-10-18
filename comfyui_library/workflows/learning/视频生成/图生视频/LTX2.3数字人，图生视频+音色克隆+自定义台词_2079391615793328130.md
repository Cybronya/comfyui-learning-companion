---
key: 视频生成/图生视频/LTX2.3数字人，图生视频+音色克隆+自定义台词_2079391615793328130.json
name: LTX2.3数字人，图生视频+音色克隆+自定义台词_2079391615793328130.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3数字人，图生视频+音色克隆+自定义台词_2079391615793328130.json
hash: 0d82c3e2059acbed
coverage: 0.8
learned_at: 2026-10-15 22:42:02
nodes: [Reroute, INTConstant, INTConstant, LTXVSeparateAVLatent, SetNode, EmptyLTXVLatentVideo, SamplerCustomAdvanced, SetNode, SimpleMath+, SimpleMath+, RandomNoise, GetNode, LTXVPreprocess, ResizeImageMaskNode, LTXAVTextEncoderLoader, LTXVAudioVAELoader, KSampler, PrimitiveBoolean, SetNode, GetNode, GetNode, LatentUpscaleModelLoader, ResizeImagesByLongerEdge, VAEDecodeTiled, SolidMask, SetLatentNoiseMask, LTXVImgToVideoInplace, LTXVLatentUpsampler, CFGGuider, KSamplerSelect, LTX2_NAG, LTX2SamplingPreviewOverride, LTXVAudioVAEEncode, CLIPTextEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVCropGuides, GetNode, GetNode, LoraLoaderModelOnly, PathchSageAttentionKJ, BasicScheduler, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, Int, Divide [DVB], JWInteger, OmniVoiceWhisperLoader, SetNode, ComfyMathExpression, INTConstant, LTXVConditioning, GetNode, VHS_VideoCombine, GetNode, INTConstant, SimpleMath+, FlashVSRNode, ImageResizeKJv2, OmniVoiceVoiceCloneTTS, RH_GetAudioDuration, easy cleanGpuUsed, GetNode, Reroute, LTXVImgToVideoInplace, easy cleanGpuUsed, LTXVConcatAVLatent, easy cleanGpuUsed, CLIPTextEncode, LoadImage, PrimitiveStringMultiline, LoadAudio, INTConstant, INTConstant]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 968737738646398, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/LTX2.3数字人，图生视频+音色克隆+自定义台词_2079391615793328130.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2079391615793328130.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（75 个）：
- `Reroute`
- `INTConstant`
- `INTConstant`
- `LTXVSeparateAVLatent`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `SimpleMath+`
- `SimpleMath+`
- `RandomNoise`
- `GetNode`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `KSampler` ★核心
- `PrimitiveBoolean`
- `SetNode`
- `GetNode`
- `GetNode`
- `LatentUpscaleModelLoader`
- `ResizeImagesByLongerEdge`
- `VAEDecodeTiled` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTX2_NAG`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `BasicScheduler`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Int`
- `Divide [DVB]`
- `JWInteger`
- `OmniVoiceWhisperLoader`
- `SetNode`
- `ComfyMathExpression`
- `INTConstant`
- `LTXVConditioning`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `INTConstant`
- `SimpleMath+`
- `FlashVSRNode`
- `ImageResizeKJv2`
- `OmniVoiceVoiceCloneTTS`
- `RH_GetAudioDuration`
- `easy cleanGpuUsed`
- `GetNode`
- `Reroute`
- `LTXVImgToVideoInplace`
- `easy cleanGpuUsed`
- `LTXVConcatAVLatent`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`
- `LoadAudio`
- `INTConstant`
- `INTConstant`

## 关键参数

- `seed` = `968737738646398`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **80%**（60/75）

**有卡**：`INTConstant`、`LTXVSeparateAVLatent`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`SimpleMath+`、`RandomNoise`、`LTXVPreprocess`、`ResizeImageMaskNode`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`KSampler`、`PrimitiveBoolean`、`LatentUpscaleModelLoader`、`ResizeImagesByLongerEdge`、`VAEDecodeTiled`、`SolidMask`、`SetLatentNoiseMask`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`CFGGuider`、`KSamplerSelect`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LTXVAudioVAEEncode`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`BasicScheduler`、`CheckpointLoaderSimple`、`Int`、`Divide [DVB]`、`JWInteger`、`OmniVoiceWhisperLoader`、`ComfyMathExpression`、`LTXVConditioning`、`VHS_VideoCombine`、`FlashVSRNode`、`ImageResizeKJv2`、`OmniVoiceVoiceCloneTTS`、`RH_GetAudioDuration`、`easy cleanGpuUsed`、`LoadImage`、`LoadAudio`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
