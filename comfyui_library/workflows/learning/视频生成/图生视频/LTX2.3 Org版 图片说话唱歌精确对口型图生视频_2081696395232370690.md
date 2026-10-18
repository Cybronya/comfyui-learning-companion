---
key: 视频生成/图生视频/LTX2.3 Org版 图片说话唱歌精确对口型图生视频_2081696395232370690.json
name: LTX2.3 Org版 图片说话唱歌精确对口型图生视频_2081696395232370690.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 Org版 图片说话唱歌精确对口型图生视频_2081696395232370690.json
hash: b12c9923a751efc5
coverage: 0.859155
learned_at: 2026-10-15 22:42:24
nodes: [RandomNoise, CFGGuider, EmptyLTXVLatentVideo, LTXVConcatAVLatent, CM_FloatToInt, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ImageAndMaskResizeNode, ImageResizeKJv2, LTXVConditioning, LTXVImgToVideoInplace, SamplerCustomAdvanced, CFGGuider, BasicScheduler, RandomNoise, CheckpointLoaderSimple, LTXVAudioVAELoader, PrimitiveInt, CLIPTextEncode, CLIPTextEncode, LTXVPreprocess, SamplerCustomAdvanced, LTX2_NAG, LoraLoaderModelOnly, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVConcatAVLatent, Reroute, LTXVSeparateAVLatent, GetNode, SetNode, PrimitiveBoolean, VAEDecodeTiled, KSamplerSelect, BasicScheduler, ManualSigmas, KSamplerSelect, JoinStrings, PrimitiveInt, SoundFlow_GetLength, LTXVCropGuides, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, TrimAudioDuration, SetNode, KSampler, LTXVAudioVAEDecode, PrimitiveStringMultiline, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, LTX2SamplingPreviewOverride, PreviewAudio, SimpleMath+, Int, PrimitiveFloat, VHS_VideoCombine, TrimAudioDuration, LTXVAudioVAEEncode, MelBandRoFormerSampler, MelBandRoFormerModelLoader, SoundFlow_GetLength, SetLatentNoiseMask, SolidMask, DF_Int_to_Float, DF_Int_to_Float, LoadAudio, PrimitiveInt, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler_cfg_pp", "scheduler": "simple", "seed": 758440895793162, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/LTX2.3 Org版 图片说话唱歌精确对口型图生视频_2081696395232370690.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2081696395232370690.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（71 个）：
- `RandomNoise`
- `CFGGuider`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `CM_FloatToInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ImageAndMaskResizeNode`
- `ImageResizeKJv2`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `BasicScheduler`
- `RandomNoise`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `SamplerCustomAdvanced` ★核心
- `LTX2_NAG`
- `LoraLoaderModelOnly` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `Reroute`
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetNode`
- `PrimitiveBoolean`
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `JoinStrings`
- `PrimitiveInt`
- `SoundFlow_GetLength`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `TrimAudioDuration`
- `SetNode`
- `KSampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveStringMultiline`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `LTX2SamplingPreviewOverride`
- `PreviewAudio`
- `SimpleMath+`
- `Int`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `SoundFlow_GetLength`
- `SetLatentNoiseMask`
- `SolidMask`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `LoadAudio`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `LoadImage`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `758440895793162`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_cfg_pp`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **86%**（61/71）

**有卡**：`RandomNoise`、`CFGGuider`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`CM_FloatToInt`、`ComfyMathExpression`、`ImageAndMaskResizeNode`、`ImageResizeKJv2`、`LTXVConditioning`、`LTXVImgToVideoInplace`、`SamplerCustomAdvanced`、`BasicScheduler`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`CLIPTextEncode`、`LTXVPreprocess`、`LTX2_NAG`、`LoraLoaderModelOnly`、`LTXVSeparateAVLatent`、`PrimitiveBoolean`、`VAEDecodeTiled`、`KSamplerSelect`、`ManualSigmas`、`JoinStrings`、`SoundFlow_GetLength`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`TrimAudioDuration`、`KSampler`、`LTXVAudioVAEDecode`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`LTX2SamplingPreviewOverride`、`PreviewAudio`、`SimpleMath+`、`Int`、`VHS_VideoCombine`、`LTXVAudioVAEEncode`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`SetLatentNoiseMask`、`SolidMask`、`DF_Int_to_Float`、`LoadAudio`、`LoadImage`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
