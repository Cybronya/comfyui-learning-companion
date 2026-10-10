---
key: 视频生成/文生视频/LTX2.3数字人文生图生自由切换版_2031035696881864705.json
name: LTX2.3数字人文生图生自由切换版_2031035696881864705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3数字人文生图生自由切换版_2031035696881864705.json
hash: 89174331990049cc
coverage: 0.741379
learned_at: 2026-10-11 03:16:47
nodes: [KSamplerSelect, LTXVCropGuides, INTConstant, CFGGuider, BasicScheduler, easy cleanGpuUsed, INTConstant, SetNode, LTXVConcatAVLatent, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVConcatAVLatent, SetNode, GetNode, GetNode, LTXAVTextEncoderLoader, PathchSageAttentionKJ, LTXVAudioVAELoader, LTXVImgToVideoInplace, KSampler, PrimitiveBoolean, GetNode, GetNode, LatentUpscaleModelLoader, LTXVConditioning, LTXVPreprocess, VAEDecodeTiled, GetNode, INTConstant, EmptyLTXVLatentVideo, Reroute, Reroute, SolidMask, SimpleMath+, GetImageSize, LTX2SamplingPreviewOverride, LTXVAudioVAEEncode, SetLatentNoiseMask, LTX2_NAG, SimpleMath+, RH_GetAudioDuration, CM_FloatToInt, SimpleMath+, easy showAnything, SetNode, PreviewAudio, LTXVImgToVideoInplace, LoadImage, CLIPTextEncode, LoadAudio, LTXVSeparateAVLatent, RTXVideoSuperResolution, VHS_VideoCombine, CLIPTextEncode, CheckpointLoaderSimple, RandomNoise, ResizeImagesByLongerEdge]
patterns: []
missing: [SimpleMath+, SimpleMath+, SimpleMath+, easy cleanGpuUsed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1-42.9G.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 749557024577825, "steps": 4}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/LTX2.3数字人文生图生自由切换版_2031035696881864705.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3数字人文生图生自由切换版_2031035696881864705.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（58 个）：
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `INTConstant`
- `CFGGuider`
- `BasicScheduler`
- `easy cleanGpuUsed`
- `INTConstant`
- `SetNode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXAVTextEncoderLoader`
- `PathchSageAttentionKJ`
- `LTXVAudioVAELoader`
- `LTXVImgToVideoInplace`
- `KSampler` ★核心
- `PrimitiveBoolean`
- `GetNode`
- `GetNode`
- `LatentUpscaleModelLoader`
- `LTXVConditioning`
- `LTXVPreprocess`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `INTConstant`
- `EmptyLTXVLatentVideo`
- `Reroute`
- `Reroute`
- `SolidMask`
- `SimpleMath+`
- `GetImageSize`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `LTX2_NAG`
- `SimpleMath+`
- `RH_GetAudioDuration`
- `CM_FloatToInt`
- `SimpleMath+`
- `easy showAnything`
- `SetNode`
- `PreviewAudio`
- `LTXVImgToVideoInplace`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadAudio`
- `LTXVSeparateAVLatent`
- `RTXVideoSuperResolution`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `RandomNoise`
- `ResizeImagesByLongerEdge`

## 关键参数

- `seed` = `749557024577825`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1-42.9G.safetensors`

## 知识

覆盖率 **74%**（43/58）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`INTConstant`、`CFGGuider`、`BasicScheduler`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`LTXAVTextEncoderLoader`、`PathchSageAttentionKJ`、`LTXVAudioVAELoader`、`LTXVImgToVideoInplace`、`KSampler`、`PrimitiveBoolean`、`LatentUpscaleModelLoader`、`LTXVConditioning`、`LTXVPreprocess`、`VAEDecodeTiled`、`EmptyLTXVLatentVideo`、`SolidMask`、`GetImageSize`、`LTX2SamplingPreviewOverride`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LTX2_NAG`、`RH_GetAudioDuration`、`CM_FloatToInt`、`PreviewAudio`、`LoadImage`、`CLIPTextEncode`、`LoadAudio`、`RTXVideoSuperResolution`、`VHS_VideoCombine`、`CheckpointLoaderSimple`、`RandomNoise`、`ResizeImagesByLongerEdge`

**缺卡**（4）：`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`easy cleanGpuUsed`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

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
