---
key: 视频生成/文生视频/LTX2.3文生MV工作流_2030727534442188801.json
name: LTX2.3文生MV工作流_2030727534442188801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文生MV工作流_2030727534442188801.json
hash: e49b6350e30d4696
coverage: 0.758621
learned_at: 2026-10-10 23:00:26
nodes: [SetNode, KSamplerSelect, GetNode, Reroute, SolidMask, LatentUpscaleModelLoader, INTConstant, SetNode, GetNode, GetNode, SetNode, MelBandRoFormerSampler, PathchSageAttentionKJ, CLIPTextEncode, LTXVConditioning, LTXVCropGuides, INTConstant, INTConstant, Reroute, LTXVLatentUpsampler, ResizeImagesByLongerEdge, CFGGuider, BasicScheduler, LTXVConcatAVLatent, SetLatentNoiseMask, LTXVAudioVAEEncode, LTXVPreprocess, SoundFlow_GetLength, easy showAnything, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConcatAVLatent, KSampler, LTXVSeparateAVLatent, easy cleanGpuUsed, GetNode, ImageSharpen, LTXVSeparateAVLatent, VHS_VideoCombine, VAEDecodeTiled, SamplerCustomAdvanced, RandomNoise, TrimAudioDuration, PreviewAudio, CLIPTextEncode, CM_FloatToInt, SimpleMath+, Int, SimpleMath+, SimpleMath+, Int, LoadAudio, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, MelBandRoFormerModelLoader, CheckpointLoaderSimple, LTXVAudioVAELoader, LoraLoaderModelOnly]
patterns: []
missing: [SimpleMath+, SimpleMath+, SimpleMath+, easy cleanGpuUsed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 472325667833915, "steps": 4}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/LTX2.3文生MV工作流_2030727534442188801.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文生MV工作流_2030727534442188801.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（58 个）：
- `SetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `Reroute`
- `SolidMask`
- `LatentUpscaleModelLoader`
- `INTConstant`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVCropGuides`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `ResizeImagesByLongerEdge`
- `CFGGuider`
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `LTXVPreprocess`
- `SoundFlow_GetLength`
- `easy showAnything`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `easy cleanGpuUsed`
- `GetNode`
- `ImageSharpen`
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `TrimAudioDuration`
- `PreviewAudio`
- `CLIPTextEncode` ★核心
- `CM_FloatToInt`
- `SimpleMath+`
- `Int`
- `SimpleMath+`
- `SimpleMath+`
- `Int`
- `LoadAudio`
- `LTX2SamplingPreviewOverride`
- `LTXAVTextEncoderLoader`
- `MelBandRoFormerModelLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `472325667833915`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **76%**（44/58）

**有卡**：`KSamplerSelect`、`SolidMask`、`LatentUpscaleModelLoader`、`INTConstant`、`MelBandRoFormerSampler`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`ResizeImagesByLongerEdge`、`CFGGuider`、`BasicScheduler`、`LTXVConcatAVLatent`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`LTXVPreprocess`、`SoundFlow_GetLength`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`KSampler`、`LTXVSeparateAVLatent`、`ImageSharpen`、`VHS_VideoCombine`、`VAEDecodeTiled`、`SamplerCustomAdvanced`、`RandomNoise`、`TrimAudioDuration`、`PreviewAudio`、`CM_FloatToInt`、`Int`、`LoadAudio`、`LTX2SamplingPreviewOverride`、`LTXAVTextEncoderLoader`、`MelBandRoFormerModelLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`

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
