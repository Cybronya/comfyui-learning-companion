---
key: 视频生成/文生视频/数字人直播 虚拟美女模特 LTX2.3数字人无字幕版  图生视频极速版LTX2.3 数字人话 唱歌对_2044685431765213185.json
name: 数字人直播 虚拟美女模特 LTX2.3数字人无字幕版  图生视频极速版LTX2.3 数字人话 唱歌对_2044685431765213185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/数字人直播 虚拟美女模特 LTX2.3数字人无字幕版  图生视频极速版LTX2.3 数字人话 唱歌对_2044685431765213185.json
hash: f6ca379a123f3140
coverage: 0.723077
learned_at: 2026-10-11 19:49:49
nodes: [KSamplerSelect, Reroute, LTXVCropGuides, INTConstant, INTConstant, Reroute, INTConstant, LTXVConcatAVLatent, SetNode, SimpleMath+, SimpleMath+, LTXVPreprocess, LoraLoaderModelOnly, PathchSageAttentionKJ, PrimitiveBoolean, SetLatentNoiseMask, CM_FloatToInt, SetNode, SolidMask, PreviewAudio, GetNode, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LTXVImgToVideoInplace, KSampler, RandomNoise, SoundFlow_GetLength, CFGGuider, SamplerCustomAdvanced, ResizeImagesByLongerEdge, ResizeImageMaskNode, GetNode, NormalizeAudioLoudness, EmptyLTXVLatentVideo, easy showAnything, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, LatentUpscaleModelLoader, LTXVAudioVAEEncode, RunningHub Deepcleaner, GetNode, RunningHub Deepcleaner, LTXVConcatAVLatent, SimpleMath+, SetNode, ImageCASharpening+, VAEDecodeTiled, LTXVConditioning, CheckpointLoaderSimple, LTX2SamplingPreviewOverride, GetNode, LTX2_NAG, BasicScheduler, CLIPTextEncode, GetNode, LTXVImgToVideoInplace, AudioCrop, VHS_VideoCombine, LoadAudio, Note, LoadImage, INTConstant, INTConstant, CLIPTextEncode]
patterns: []
missing: [ImageCASharpening+, RunningHub Deepcleaner, RunningHub Deepcleaner, SimpleMath+, SimpleMath+, SimpleMath+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 1106542610737212, "steps": 4}
discoveries: [次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识, 次要节点 `RunningHub Deepcleaner` 知识库中没有该节点类型的任何知识, 次要节点 `RunningHub Deepcleaner` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/数字人直播 虚拟美女模特 LTX2.3数字人无字幕版  图生视频极速版LTX2.3 数字人话 唱歌对_2044685431765213185.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/数字人直播 虚拟美女模特 LTX2.3数字人无字幕版  图生视频极速版LTX2.3 数字人话 唱歌对_2044685431765213185.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（65 个）：
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVCropGuides`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `INTConstant`
- `LTXVConcatAVLatent`
- `SetNode`
- `SimpleMath+`
- `SimpleMath+`
- `LTXVPreprocess`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `SetLatentNoiseMask`
- `CM_FloatToInt`
- `SetNode`
- `SolidMask`
- `PreviewAudio`
- `GetNode`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LTXVImgToVideoInplace`
- `KSampler` ★核心
- `RandomNoise`
- `SoundFlow_GetLength`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `ResizeImagesByLongerEdge`
- `ResizeImageMaskNode`
- `GetNode`
- `NormalizeAudioLoudness`
- `EmptyLTXVLatentVideo`
- `easy showAnything`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `LTXVAudioVAEEncode` ★核心
- `RunningHub Deepcleaner`
- `GetNode`
- `RunningHub Deepcleaner`
- `LTXVConcatAVLatent`
- `SimpleMath+`
- `SetNode`
- `ImageCASharpening+`
- `VAEDecodeTiled` ★核心
- `LTXVConditioning`
- `CheckpointLoaderSimple` ★核心
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `LTX2_NAG`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LTXVImgToVideoInplace`
- `AudioCrop`
- `VHS_VideoCombine`
- `LoadAudio`
- `Note`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `1106542610737212`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **72%**（47/65）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`INTConstant`、`LTXVConcatAVLatent`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`PrimitiveBoolean`、`SetLatentNoiseMask`、`CM_FloatToInt`、`SolidMask`、`PreviewAudio`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LTXVImgToVideoInplace`、`KSampler`、`RandomNoise`、`SoundFlow_GetLength`、`CFGGuider`、`SamplerCustomAdvanced`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`NormalizeAudioLoudness`、`EmptyLTXVLatentVideo`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`LTXVAudioVAEEncode`、`VAEDecodeTiled`、`LTXVConditioning`、`CheckpointLoaderSimple`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`BasicScheduler`、`CLIPTextEncode`、`AudioCrop`、`VHS_VideoCombine`、`LoadAudio`、`LoadImage`

**缺卡**（6）：`ImageCASharpening+`、`RunningHub Deepcleaner`、`RunningHub Deepcleaner`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- 次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识
- 次要节点 `RunningHub Deepcleaner` 知识库中没有该节点类型的任何知识
- 次要节点 `RunningHub Deepcleaner` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
