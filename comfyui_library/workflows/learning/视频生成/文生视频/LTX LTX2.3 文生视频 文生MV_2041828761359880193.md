---
key: 视频生成/文生视频/LTX LTX2.3 文生视频 文生MV_2041828761359880193.json
name: LTX LTX2.3 文生视频 文生MV_2041828761359880193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX LTX2.3 文生视频 文生MV_2041828761359880193.json
hash: aed5ca001657c309
coverage: 0.758621
learned_at: 2026-10-11 19:49:35
nodes: [KSamplerSelect, BasicScheduler, LTXAVTextEncoderLoader, CheckpointLoaderSimple, LTXVAudioVAELoader, SetNode, SetNode, CLIPTextEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVConditioning, RandomNoise, CFGGuider, LTXVCropGuides, Int, Int, LTX2SamplingPreviewOverride, VHS_VideoCombine, CLIPTextEncode, LoadAudio, MelBandRoFormerModelLoader, SoundFlow_GetLength, TrimAudioDuration, SetNode, CM_FloatToInt, PreviewAudio, MelBandRoFormerSampler, SimpleMath+, easy showAnything, SimpleMath+, SimpleMath+, INTConstant, INTConstant, Reroute, Reroute, LTXVAudioVAEEncode, GetNode, SolidMask, INTConstant, LTXVPreprocess, ResizeImagesByLongerEdge, EmptyLTXVLatentVideo, SetLatentNoiseMask, GetNode, LTXVImgToVideoInplace, easy cleanGpuUsed, GetNode, LTXVConcatAVLatent, LatentUpscaleModelLoader, LTXVLatentUpsampler, ImageSharpen, GetNode, KSampler, LTXVSeparateAVLatent, VAEDecodeTiled, LoraLoaderModelOnly, PathchSageAttentionKJ]
patterns: []
missing: [SimpleMath+, SimpleMath+, SimpleMath+, easy cleanGpuUsed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 471826633398620, "steps": 4}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/LTX LTX2.3 文生视频 文生MV_2041828761359880193.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX LTX2.3 文生视频 文生MV_2041828761359880193.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（58 个）：
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVConditioning`
- `RandomNoise`
- `CFGGuider`
- `LTXVCropGuides`
- `Int`
- `Int`
- `LTX2SamplingPreviewOverride`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `SoundFlow_GetLength`
- `TrimAudioDuration`
- `SetNode`
- `CM_FloatToInt`
- `PreviewAudio`
- `MelBandRoFormerSampler` ★核心
- `SimpleMath+`
- `easy showAnything`
- `SimpleMath+`
- `SimpleMath+`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `Reroute`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SolidMask`
- `INTConstant`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `EmptyLTXVLatentVideo`
- `SetLatentNoiseMask`
- `GetNode`
- `LTXVImgToVideoInplace`
- `easy cleanGpuUsed`
- `GetNode`
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `ImageSharpen`
- `GetNode`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `471826633398620`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **76%**（44/58）

**有卡**：`KSamplerSelect`、`BasicScheduler`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVConditioning`、`RandomNoise`、`CFGGuider`、`LTXVCropGuides`、`Int`、`LTX2SamplingPreviewOverride`、`VHS_VideoCombine`、`LoadAudio`、`MelBandRoFormerModelLoader`、`SoundFlow_GetLength`、`TrimAudioDuration`、`CM_FloatToInt`、`PreviewAudio`、`MelBandRoFormerSampler`、`INTConstant`、`LTXVAudioVAEEncode`、`SolidMask`、`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`EmptyLTXVLatentVideo`、`SetLatentNoiseMask`、`LTXVImgToVideoInplace`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`ImageSharpen`、`KSampler`、`VAEDecodeTiled`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`

**缺卡**（4）：`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`easy cleanGpuUsed`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
