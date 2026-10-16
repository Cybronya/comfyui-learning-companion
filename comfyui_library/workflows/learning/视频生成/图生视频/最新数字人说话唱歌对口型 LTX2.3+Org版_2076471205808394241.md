---
key: 视频生成/图生视频/最新数字人说话唱歌对口型 LTX2.3+Org版_2076471205808394241.json
name: 最新数字人说话唱歌对口型 LTX2.3+Org版_2076471205808394241.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2076471205808394241.json
hash: b782c088fff8e0f7
coverage: 0.864865
learned_at: 2026-10-15 22:41:30
nodes: [RandomNoise, CFGGuider, EmptyLTXVLatentVideo, LTXVConcatAVLatent, CM_FloatToInt, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ImageAndMaskResizeNode, ImageResizeKJv2, LTXVConditioning, LTXVImgToVideoInplace, SamplerCustomAdvanced, CFGGuider, BasicScheduler, RandomNoise, CheckpointLoaderSimple, LTXVAudioVAELoader, PrimitiveInt, CLIPTextEncode, CLIPTextEncode, LTXVPreprocess, SamplerCustomAdvanced, LTX2_NAG, LoraLoaderModelOnly, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVConcatAVLatent, Reroute, LTXVSeparateAVLatent, GetNode, SetNode, PrimitiveBoolean, VAEDecodeTiled, KSamplerSelect, BasicScheduler, ManualSigmas, KSamplerSelect, JoinStrings, LTXVCropGuides, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, SetNode, KSampler, LTXVAudioVAEDecode, PrimitiveStringMultiline, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, LTX2SamplingPreviewOverride, LTXVAudioVAEEncode, SoundFlow_GetLength, SetLatentNoiseMask, SolidMask, DF_Int_to_Float, SoundFlow_GetLength, TrimAudioDuration, DF_Int_to_Float, SimpleMath+, TrimAudioDuration, MelBandRoFormerSampler, MelBandRoFormerModelLoader, Compare, InversionDemoLazySwitch, Int, VHS_VideoCombine, PreviewAudio, LoadImage, PrimitiveStringMultiline, LoadAudio, PrimitiveFloat, Int, PrimitiveInt, PrimitiveInt]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler_cfg_pp", "scheduler": "simple", "seed": 956351432869863, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/最新数字人说话唱歌对口型 LTX2.3+Org版_2076471205808394241.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2076471205808394241.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（74 个）：
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
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `SetNode`
- `KSampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveStringMultiline`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEEncode` ★核心
- `SoundFlow_GetLength`
- `SetLatentNoiseMask`
- `SolidMask`
- `DF_Int_to_Float`
- `SoundFlow_GetLength`
- `TrimAudioDuration`
- `DF_Int_to_Float`
- `SimpleMath+`
- `TrimAudioDuration`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `Compare`
- `InversionDemoLazySwitch`
- `Int`
- `VHS_VideoCombine`
- `PreviewAudio`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LoadAudio`
- `PrimitiveFloat`
- `Int`
- `PrimitiveInt`
- `PrimitiveInt`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `956351432869863`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_cfg_pp`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **86%**（64/74）

**有卡**：`RandomNoise`、`CFGGuider`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`CM_FloatToInt`、`ComfyMathExpression`、`ImageAndMaskResizeNode`、`ImageResizeKJv2`、`LTXVConditioning`、`LTXVImgToVideoInplace`、`SamplerCustomAdvanced`、`BasicScheduler`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`CLIPTextEncode`、`LTXVPreprocess`、`LTX2_NAG`、`LoraLoaderModelOnly`、`LTXVSeparateAVLatent`、`PrimitiveBoolean`、`VAEDecodeTiled`、`KSamplerSelect`、`ManualSigmas`、`JoinStrings`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`KSampler`、`LTXVAudioVAEDecode`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`LTX2SamplingPreviewOverride`、`LTXVAudioVAEEncode`、`SoundFlow_GetLength`、`SetLatentNoiseMask`、`SolidMask`、`DF_Int_to_Float`、`TrimAudioDuration`、`SimpleMath+`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`Compare`、`InversionDemoLazySwitch`、`Int`、`VHS_VideoCombine`、`PreviewAudio`、`LoadImage`、`LoadAudio`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
