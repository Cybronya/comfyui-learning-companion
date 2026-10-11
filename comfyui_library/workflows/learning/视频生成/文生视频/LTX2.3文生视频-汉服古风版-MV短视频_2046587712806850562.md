---
key: 视频生成/文生视频/LTX2.3文生视频-汉服古风版-MV短视频_2046587712806850562.json
name: LTX2.3文生视频-汉服古风版-MV短视频_2046587712806850562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频-汉服古风版-MV短视频_2046587712806850562.json
hash: 7c6444f0045693db
coverage: 0.767857
learned_at: 2026-10-11 19:49:39
nodes: [INTConstant, SetLatentNoiseMask, SolidMask, SimpleMath+, easy showAnything, LTXVConditioning, CFGGuider, KSamplerSelect, BasicScheduler, LTXVConcatAVLatent, LTXVSeparateAVLatent, CM_FloatToInt, SoundFlow_GetLength, SetNode, SimpleMath+, SimpleMath+, Reroute, Reroute, INTConstant, INTConstant, LoraLoaderModelOnly, LTXVAudioVAELoader, LTXAVTextEncoderLoader, SetNode, SetNode, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, easy cleanGpuUsed, ImageSharpen, GetNode, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVCropGuides, GetNode, KSampler, EmptyLTXVLatentVideo, LTX2SamplingPreviewOverride, GetNode, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PathchSageAttentionKJ, CLIPTextEncode, CheckpointLoaderSimple, LatentUpscaleModelLoader, LoadAudio, LTXVAudioVAEEncode, CLIPTextEncode, VHS_VideoCombine, Int, Int, LoraLoaderModelOnly, LoraLoaderModelOnly, TextInputNode, TrimAudioDuration]
patterns: []
missing: [SimpleMath+, SimpleMath+, SimpleMath+, easy cleanGpuUsed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 1030910731046630, "steps": 4}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/LTX2.3文生视频-汉服古风版-MV短视频_2046587712806850562.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频-汉服古风版-MV短视频_2046587712806850562.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（56 个）：
- `INTConstant`
- `SetLatentNoiseMask`
- `SolidMask`
- `SimpleMath+`
- `easy showAnything`
- `LTXVConditioning`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `CM_FloatToInt`
- `SoundFlow_GetLength`
- `SetNode`
- `SimpleMath+`
- `SimpleMath+`
- `Reroute`
- `Reroute`
- `INTConstant`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `SetNode`
- `SetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `ImageSharpen`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `GetNode`
- `KSampler` ★核心
- `EmptyLTXVLatentVideo`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LTXVAudioVAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `Int`
- `Int`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextInputNode`
- `TrimAudioDuration`

## 关键参数

- `seed` = `1030910731046630`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **77%**（43/56）

**有卡**：`INTConstant`、`SetLatentNoiseMask`、`SolidMask`、`LTXVConditioning`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`CM_FloatToInt`、`SoundFlow_GetLength`、`LoraLoaderModelOnly`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`ImageSharpen`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`KSampler`、`EmptyLTXVLatentVideo`、`LTX2SamplingPreviewOverride`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LatentUpscaleModelLoader`、`LoadAudio`、`LTXVAudioVAEEncode`、`VHS_VideoCombine`、`Int`、`TextInputNode`、`TrimAudioDuration`

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
