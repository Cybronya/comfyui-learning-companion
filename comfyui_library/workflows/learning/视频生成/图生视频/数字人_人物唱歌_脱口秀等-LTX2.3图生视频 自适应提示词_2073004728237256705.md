---
key: 视频生成/图生视频/数字人_人物唱歌_脱口秀等-LTX2.3图生视频 自适应提示词_2073004728237256705.json
name: 数字人_人物唱歌_脱口秀等-LTX2.3图生视频 自适应提示词_2073004728237256705.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2073004728237256705.json
hash: 4608fc2f6c0b9026
coverage: 0.814286
learned_at: 2026-10-15 22:41:00
nodes: [SimpleMath+, SetNode, INTConstant, INTConstant, INTConstant, Reroute, Reroute, EmptyLTXVLatentVideo, CFGGuider, SimpleMath+, PreviewAudio, SetNode, SetLatentNoiseMask, CLIPTextEncode, KSamplerSelect, BasicScheduler, GetNode, GetNode, GetNode, GetNode, SetNode, LTX2SamplingPreviewOverride, LTXVConditioning, GetNode, easy showAnything, Textbox, RHLLMChatNode, PreviewAny, LoadAudio, CM_FloatToInt, RH_GetAudioDuration, SimpleMath+, SolidMask, INTConstant, INTConstant, LoadImage, PrimitiveBoolean, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVImgToVideoInplace, LTXVAudioVAEEncode, RandomNoise, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVConcatAVLatent, KSampler, VHS_VideoCombine, VAEDecodeTiled, easy cleanGpuUsed, GetNode, SamplerCustomAdvanced, LTXVConcatAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, RTXVideoSuperResolution, VAEDecodeTiled, LTXVSeparateAVLatent, VHS_VideoCombine, VHS_VideoCombine, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, LTX2_NAG, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 256389699239973, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/数字人_人物唱歌_脱口秀等-LTX2.3图生视频 自适应提示词_2073004728237256705.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073004728237256705.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（70 个）：
- `SimpleMath+`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `Reroute`
- `EmptyLTXVLatentVideo`
- `CFGGuider`
- `SimpleMath+`
- `PreviewAudio`
- `SetNode`
- `SetLatentNoiseMask`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `LTXVConditioning`
- `GetNode`
- `easy showAnything`
- `Textbox`
- `RHLLMChatNode`
- `PreviewAny`
- `LoadAudio`
- `CM_FloatToInt`
- `RH_GetAudioDuration`
- `SimpleMath+`
- `SolidMask`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `PrimitiveBoolean`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEEncode` ★核心
- `RandomNoise`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `RTXVideoSuperResolution`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `256389699239973`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **81%**（57/70）

**有卡**：`SimpleMath+`、`INTConstant`、`EmptyLTXVLatentVideo`、`CFGGuider`、`PreviewAudio`、`SetLatentNoiseMask`、`CLIPTextEncode`、`KSamplerSelect`、`BasicScheduler`、`LTX2SamplingPreviewOverride`、`LTXVConditioning`、`Textbox`、`RHLLMChatNode`、`LoadAudio`、`CM_FloatToInt`、`RH_GetAudioDuration`、`SolidMask`、`LoadImage`、`PrimitiveBoolean`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`LTXVAudioVAEEncode`、`RandomNoise`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`KSampler`、`VHS_VideoCombine`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`RTXVideoSuperResolution`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LTX2_NAG`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
