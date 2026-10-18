---
key: 视频生成/图生视频/LTX2.3对口型 数字人说话唱歌 去字幕+无字幕版_2040953875372445698.json
name: LTX2.3对口型 数字人说话唱歌 去字幕+无字幕版_2040953875372445698.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3对口型 数字人说话唱歌 去字幕+无字幕版_2040953875372445698.json
hash: 04d7bdb319e4d0a2
coverage: 0.865672
learned_at: 2026-10-15 22:36:16
nodes: [RandomNoise, CFGGuider, SolidMask, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SetNode, Int, CM_FloatToInt, SoundFlow_GetLength, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ImageAndMaskResizeNode, ImageResizeKJv2, DF_Int_to_Float, DF_Int_to_Float, LatentUpscaleModelLoader, LTXVAudioVAEEncode, SetLatentNoiseMask, LTXVConditioning, SimpleMath+, LTXVImgToVideoInplace, SamplerCustomAdvanced, CFGGuider, BasicScheduler, RandomNoise, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, PrimitiveInt, CLIPTextEncode, CLIPTextEncode, LTXVImgToVideoInplace, LTXVPreprocess, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVCropGuides, LTXVSeparateAVLatent, LTX2_NAG, LoraLoaderModelOnly, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVAudioVAEDecode, LTXVConcatAVLatent, Reroute, LTXVSeparateAVLatent, GetNode, SetNode, PrimitiveBoolean, LTX2SamplingPreviewOverride, KSampler, VAEDecodeTiled, KSamplerSelect, PrimitiveInt, BasicScheduler, ManualSigmas, KSamplerSelect, PrimitiveStringMultiline, JoinStrings, PrimitiveStringMultiline, TrimAudioDuration, PrimitiveInt, VHS_VideoCombine, LoadAudio, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler_cfg_pp", "scheduler": "simple", "seed": 474776247166305, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/LTX2.3对口型 数字人说话唱歌 去字幕+无字幕版_2040953875372445698.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2040953875372445698.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（67 个）：
- `RandomNoise`
- `CFGGuider`
- `SolidMask`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `SetNode`
- `Int`
- `CM_FloatToInt`
- `SoundFlow_GetLength`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ImageAndMaskResizeNode`
- `ImageResizeKJv2`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `LatentUpscaleModelLoader`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `LTXVConditioning`
- `SimpleMath+`
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `BasicScheduler`
- `RandomNoise`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTX2_NAG`
- `LoraLoaderModelOnly` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConcatAVLatent`
- `Reroute`
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetNode`
- `PrimitiveBoolean`
- `LTX2SamplingPreviewOverride`
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `BasicScheduler`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `PrimitiveStringMultiline`
- `JoinStrings`
- `PrimitiveStringMultiline`
- `TrimAudioDuration`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `LoadAudio`
- `LoadImage`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `474776247166305`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_cfg_pp`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **87%**（58/67）

**有卡**：`RandomNoise`、`CFGGuider`、`SolidMask`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`Int`、`CM_FloatToInt`、`SoundFlow_GetLength`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`ComfyMathExpression`、`ImageAndMaskResizeNode`、`ImageResizeKJv2`、`DF_Int_to_Float`、`LatentUpscaleModelLoader`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LTXVConditioning`、`SimpleMath+`、`LTXVImgToVideoInplace`、`SamplerCustomAdvanced`、`BasicScheduler`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`LTXVPreprocess`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTX2_NAG`、`LoraLoaderModelOnly`、`LTXVAudioVAEDecode`、`PrimitiveBoolean`、`LTX2SamplingPreviewOverride`、`KSampler`、`VAEDecodeTiled`、`KSamplerSelect`、`ManualSigmas`、`JoinStrings`、`TrimAudioDuration`、`VHS_VideoCombine`、`LoadAudio`、`LoadImage`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
