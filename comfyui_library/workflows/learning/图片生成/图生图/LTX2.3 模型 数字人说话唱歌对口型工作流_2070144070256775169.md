---
key: 图片生成/图生图/LTX2.3 模型 数字人说话唱歌对口型工作流_2070144070256775169.json
name: LTX2.3 模型 数字人说话唱歌对口型工作流_2070144070256775169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/LTX2.3 模型 数字人说话唱歌对口型工作流_2070144070256775169.json
hash: 8b598ad7e8271341
coverage: 0.847458
learned_at: 2026-10-23 11:08:49
nodes: [PrimitiveInt, PrimitiveInt, PrimitiveInt, LoadAudio, PrimitiveFloat, PrimitiveStringMultiline, LoadImage, Int, GetNode, LTXVAudioVAELoader, LoraLoaderModelOnly, LTXAVTextEncoderLoader, CLIPTextEncode, JoinStrings, PrimitiveStringMultiline, CLIPTextEncode, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, MelBandRoFormerModelLoader, SetLatentNoiseMask, SolidMask, LTXVConcatAVLatent, LTXVAudioVAEEncode, RandomNoise, CFGGuider, KSamplerSelect, LTXVSeparateAVLatent, LTXVCropGuides, LTX2_NAG, KSampler, LTXVSeparateAVLatent, VAEDecodeTiled, SetNode, ImageAndMaskResizeNode, LTXVPreprocess, LTXVConditioning, SimpleMath+, DF_Int_to_Float, DF_Int_to_Float, PreviewAudio, CM_FloatToInt, SoundFlow_GetLength, ImageResizeKJv2, LTX2SamplingPreviewOverride, VHS_VideoCombine, LatentUpscaleModelLoader, TrimAudioDuration, LTXVLatentUpsampler, LTXVImgToVideoInplace, SamplerCustomAdvanced, LTXVConcatAVLatent, MelBandRoFormerSampler, TrimAudioDuration, CheckpointLoaderSimple, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, ComfyMathExpression, BasicScheduler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4000000000000001, "sampler_name": "euler_cfg_pp", "scheduler": "simple", "seed": 1059139935925191, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 图片生成/图生图/LTX2.3 模型 数字人说话唱歌对口型工作流_2070144070256775169.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/LTX2.3 模型 数字人说话唱歌对口型工作流_2070144070256775169.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（59 个）：
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadAudio`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `LoadImage`
- `Int`
- `GetNode`
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `JoinStrings`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MelBandRoFormerModelLoader`
- `SetLatentNoiseMask`
- `SolidMask`
- `LTXVConcatAVLatent`
- `LTXVAudioVAEEncode` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTX2_NAG`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `ImageAndMaskResizeNode`
- `LTXVPreprocess`
- `LTXVConditioning`
- `SimpleMath+`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `PreviewAudio`
- `CM_FloatToInt`
- `SoundFlow_GetLength`
- `ImageResizeKJv2`
- `LTX2SamplingPreviewOverride`
- `VHS_VideoCombine`
- `LatentUpscaleModelLoader`
- `TrimAudioDuration`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `MelBandRoFormerSampler` ★核心
- `TrimAudioDuration`
- `CheckpointLoaderSimple` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `ComfyMathExpression`
- `BasicScheduler`

## 关键参数

- `seed` = `1059139935925191`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_cfg_pp`
- `scheduler` = `simple`
- `denoise` = `0.4000000000000001`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **85%**（50/59）

**有卡**：`LoadAudio`、`LoadImage`、`Int`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`JoinStrings`、`ComfyMathExpression`、`MelBandRoFormerModelLoader`、`SetLatentNoiseMask`、`SolidMask`、`LTXVConcatAVLatent`、`LTXVAudioVAEEncode`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTX2_NAG`、`KSampler`、`VAEDecodeTiled`、`ImageAndMaskResizeNode`、`LTXVPreprocess`、`LTXVConditioning`、`SimpleMath+`、`DF_Int_to_Float`、`PreviewAudio`、`CM_FloatToInt`、`SoundFlow_GetLength`、`ImageResizeKJv2`、`LTX2SamplingPreviewOverride`、`VHS_VideoCombine`、`LatentUpscaleModelLoader`、`TrimAudioDuration`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`SamplerCustomAdvanced`、`MelBandRoFormerSampler`、`CheckpointLoaderSimple`、`EmptyLTXVLatentVideo`、`BasicScheduler`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
