---
key: 平台全量/音频生视频 LTX2.3文生MV_2053017927036751874.json
name: 音频生视频 LTX2.3文生MV_2053017927036751874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/音频生视频 LTX2.3文生MV_2053017927036751874.json
hash: 7a8311548dc143b4
coverage: 0.827586
learned_at: 2026-11-14 02:50:24
nodes: [SetNode, KSamplerSelect, GetNode, Reroute, LatentUpscaleModelLoader, INTConstant, SetNode, GetNode, GetNode, SetNode, MelBandRoFormerSampler, PathchSageAttentionKJ, LTXVCropGuides, INTConstant, INTConstant, Reroute, LTXVLatentUpsampler, CFGGuider, BasicScheduler, LTXVConcatAVLatent, LTXVAudioVAEEncode, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, KSampler, LTXVSeparateAVLatent, GetNode, LTXVSeparateAVLatent, VAEDecodeTiled, SamplerCustomAdvanced, Int, SimpleMath+, MelBandRoFormerModelLoader, LoraLoaderModelOnly, SimpleMath+, Int, LTXVPreprocess, ImageSharpen, ResizeImagesByLongerEdge, LoadAudio, CLIPTextEncode, TrimAudioDuration, PreviewAudio, easy cleanGpuUsed, VHS_VideoCombine, SoundFlow_GetLength, CM_FloatToInt, SimpleMath+, SetLatentNoiseMask, SolidMask, easy showAnything, LTXVConcatAVLatent, CLIPTextEncode, CheckpointLoaderSimple, LTXVAudioVAELoader, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXVConditioning, RandomNoise]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 938560255108736, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/音频生视频 LTX2.3文生MV_2053017927036751874.json

> 来源文件 `comfyui_library/workflows/平台全量/音频生视频 LTX2.3文生MV_2053017927036751874.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（58 个）：
- `SetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `Reroute`
- `LatentUpscaleModelLoader`
- `INTConstant`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `PathchSageAttentionKJ`
- `LTXVCropGuides`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `LTXVAudioVAEEncode` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `SamplerCustomAdvanced` ★核心
- `Int`
- `SimpleMath+`
- `MelBandRoFormerModelLoader`
- `LoraLoaderModelOnly` ★核心
- `SimpleMath+`
- `Int`
- `LTXVPreprocess`
- `ImageSharpen`
- `ResizeImagesByLongerEdge`
- `LoadAudio`
- `CLIPTextEncode` ★核心
- `TrimAudioDuration`
- `PreviewAudio`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `SoundFlow_GetLength`
- `CM_FloatToInt`
- `SimpleMath+`
- `SetLatentNoiseMask`
- `SolidMask`
- `easy showAnything`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTX2SamplingPreviewOverride`
- `LTXAVTextEncoderLoader`
- `LTXVConditioning`
- `RandomNoise`

## 关键参数

- `seed` = `938560255108736`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **83%**（48/58）

**有卡**：`KSamplerSelect`、`LatentUpscaleModelLoader`、`INTConstant`、`MelBandRoFormerSampler`、`PathchSageAttentionKJ`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`CFGGuider`、`BasicScheduler`、`LTXVConcatAVLatent`、`LTXVAudioVAEEncode`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`KSampler`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`SamplerCustomAdvanced`、`Int`、`SimpleMath+`、`MelBandRoFormerModelLoader`、`LoraLoaderModelOnly`、`LTXVPreprocess`、`ImageSharpen`、`ResizeImagesByLongerEdge`、`LoadAudio`、`CLIPTextEncode`、`TrimAudioDuration`、`PreviewAudio`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`SoundFlow_GetLength`、`CM_FloatToInt`、`SetLatentNoiseMask`、`SolidMask`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTX2SamplingPreviewOverride`、`LTXAVTextEncoderLoader`、`LTXVConditioning`、`RandomNoise`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、LTXVLatentUpsampler、MelBandRoFormerSampler

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
