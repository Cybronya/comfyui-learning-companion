---
key: 数字人/数字人/LTX2.3 数字人 唱歌对口型！_2055660997586767874.json
name: LTX2.3 数字人 唱歌对口型！_2055660997586767874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3 数字人 唱歌对口型！_2055660997586767874.json
hash: af7e8b2a7de39f26
coverage: 0.644737
learned_at: 2026-10-26 01:55:51
nodes: [LTXVConcatAVLatent, RandomNoise, CFGGuider, LTXVSeparateAVLatent, KSamplerSelect, BasicScheduler, SolidMask, GetNode, SimpleMath+, SimpleMath+, GetNode, LTXVConcatAVLatent, LatentUpscaleModelLoader, LTXVImgToVideoInplace, CLIPTextEncode, ImageResizeKJv2, GetNode, GetNode, SamplerCustomAdvanced, PrimitiveStringMultiline, JoinStrings, SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, Int, PrimitiveInt, ResizeImagesByLongerEdge, GetNode, SetNode, LTXAVTextEncoderLoader, LTXVAudioVAELoader, CheckpointLoaderSimple, NormalizeAudioLoudness, GetNode, LTXVPreprocess, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LTXVConditioning, LayerUtility: PurgeVRAM, SetNode, PrimitiveBoolean, GetNode, LTX2_NAG, LoraLoaderModelOnly, GetNode, LTXVAudioVAEEncode, SetLatentNoiseMask, MelBandRoFormerSampler, SimpleMath+, EmptyLTXVLatentVideo, GetNode, LTXVImgToVideoInplace, CLIPTextEncode, GetNode, LTX2SamplingPreviewOverride, SetNode, LTXVSeparateAVLatent, LTXVCropGuides, LTXVLatentUpsampler, GetNode, SetNode, LayerUtility: PurgeVRAM, VAEDecodeTiled, KSampler, SetNode, SetNode, SetNode, DF_Int_to_Float, LoadImage, PrimitiveStringMultiline, PrimitiveInt, MelBandRoFormerModelLoader, LoadAudio, SetNode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 489223074181650, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 数字人/数字人/LTX2.3 数字人 唱歌对口型！_2055660997586767874.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3 数字人 唱歌对口型！_2055660997586767874.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（76 个）：
- `LTXVConcatAVLatent`
- `RandomNoise`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SolidMask`
- `GetNode`
- `SimpleMath+`
- `SimpleMath+`
- `GetNode`
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `LTXVImgToVideoInplace`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveStringMultiline`
- `JoinStrings`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `Int`
- `PrimitiveInt`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `SetNode`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `NormalizeAudioLoudness`
- `GetNode`
- `LTXVPreprocess`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LTXVConditioning`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `PrimitiveBoolean`
- `GetNode`
- `LTX2_NAG`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `MelBandRoFormerSampler` ★核心
- `SimpleMath+`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `LTXVImgToVideoInplace`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `SetNode`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `VAEDecodeTiled` ★核心
- `KSampler` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `DF_Int_to_Float`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `MelBandRoFormerModelLoader`
- `LoadAudio`
- `SetNode`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `489223074181650`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **64%**（49/76）

**有卡**：`LTXVConcatAVLatent`、`RandomNoise`、`CFGGuider`、`LTXVSeparateAVLatent`、`KSamplerSelect`、`BasicScheduler`、`SolidMask`、`SimpleMath+`、`LatentUpscaleModelLoader`、`LTXVImgToVideoInplace`、`CLIPTextEncode`、`ImageResizeKJv2`、`SamplerCustomAdvanced`、`JoinStrings`、`VHS_VideoCombine`、`Int`、`ResizeImagesByLongerEdge`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`NormalizeAudioLoudness`、`LTXVPreprocess`、`LayerUtility: PurgeVRAM`、`LTXVConditioning`、`PrimitiveBoolean`、`LTX2_NAG`、`LoraLoaderModelOnly`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`MelBandRoFormerSampler`、`EmptyLTXVLatentVideo`、`LTX2SamplingPreviewOverride`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`KSampler`、`DF_Int_to_Float`、`LoadImage`、`MelBandRoFormerModelLoader`、`LoadAudio`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
