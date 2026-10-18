---
key: 视频生成/图生视频/LTX2.3单图+音频对口型无字幕_2040333916862685186.json
name: LTX2.3单图+音频对口型无字幕_2040333916862685186.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3单图+音频对口型无字幕_2040333916862685186.json
hash: 8f16eef5268ea6e9
coverage: 0.644737
learned_at: 2026-10-15 22:36:14
nodes: [LTXVCropGuides, LTXVConcatAVLatent, RandomNoise, CFGGuider, LTXVSeparateAVLatent, CheckpointLoaderSimple, GetNode, GetNode, SetNode, SetNode, GetNode, LTXVSeparateAVLatent, KSamplerSelect, BasicScheduler, CLIPTextEncode, GetNode, LTXVImgToVideoInplace, GetNode, SolidMask, PrimitiveBoolean, GetNode, ResizeImagesByLongerEdge, SimpleMath+, SimpleMath+, LTXVConcatAVLatent, SimpleMath+, EmptyLTXVLatentVideo, LatentUpscaleModelLoader, LTXVImgToVideoInplace, LTXVLatentUpsampler, VHS_VideoCombine, LTX2SamplingPreviewOverride, GetNode, GetNode, SetLatentNoiseMask, LTXVAudioVAEEncode, MelBandRoFormerSampler, GetNode, LTXAVTextEncoderLoader, CLIPTextEncode, LTX2_NAG, LoraLoaderModelOnly, LTXVConditioning, LTXVAudioVAELoader, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SetNode, PrimitiveStringMultiline, JoinStrings, SetNode, SetNode, SetNode, SetNode, DF_Int_to_Float, SetNode, SetNode, ImageResizeKJv2, MelBandRoFormerModelLoader, LayerUtility: PurgeVRAM, GetNode, GetNode, GetNode, GetNode, SamplerCustomAdvanced, VAEDecodeTiled, KSampler, NormalizeAudioLoudness, LTXVPreprocess, GetNode, LoadImage, PrimitiveInt, PrimitiveStringMultiline, LoadAudio, PrimitiveInt, Int]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 70660612994082, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/LTX2.3单图+音频对口型无字幕_2040333916862685186.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2040333916862685186.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（76 个）：
- `LTXVCropGuides`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `CheckpointLoaderSimple` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `SolidMask`
- `PrimitiveBoolean`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `SimpleMath+`
- `SimpleMath+`
- `LTXVConcatAVLatent`
- `SimpleMath+`
- `EmptyLTXVLatentVideo`
- `LatentUpscaleModelLoader`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `VHS_VideoCombine`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `GetNode`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `MelBandRoFormerSampler` ★核心
- `GetNode`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `LTXVAudioVAELoader`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `DF_Int_to_Float`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `MelBandRoFormerModelLoader`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `KSampler` ★核心
- `NormalizeAudioLoudness`
- `LTXVPreprocess`
- `GetNode`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `LoadAudio`
- `PrimitiveInt`
- `Int`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `70660612994082`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **64%**（49/76）

**有卡**：`LTXVCropGuides`、`LTXVConcatAVLatent`、`RandomNoise`、`CFGGuider`、`LTXVSeparateAVLatent`、`CheckpointLoaderSimple`、`KSamplerSelect`、`BasicScheduler`、`CLIPTextEncode`、`LTXVImgToVideoInplace`、`SolidMask`、`PrimitiveBoolean`、`ResizeImagesByLongerEdge`、`SimpleMath+`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`VHS_VideoCombine`、`LTX2SamplingPreviewOverride`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`MelBandRoFormerSampler`、`LTXAVTextEncoderLoader`、`LTX2_NAG`、`LoraLoaderModelOnly`、`LTXVConditioning`、`LTXVAudioVAELoader`、`LayerUtility: PurgeVRAM`、`JoinStrings`、`DF_Int_to_Float`、`ImageResizeKJv2`、`MelBandRoFormerModelLoader`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`KSampler`、`NormalizeAudioLoudness`、`LTXVPreprocess`、`LoadImage`、`LoadAudio`、`Int`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
