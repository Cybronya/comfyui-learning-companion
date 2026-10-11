---
key: 视频生成/文生视频/【最新加速版】数字人话 LTX2.3唱歌对口型_2043952711799934977.json
name: 【最新加速版】数字人话 LTX2.3唱歌对口型_2043952711799934977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【最新加速版】数字人话 LTX2.3唱歌对口型_2043952711799934977.json
hash: 614bad88a41eb444
coverage: 0.552632
learned_at: 2026-10-11 19:49:46
nodes: [LTXVCropGuides, LTXVConcatAVLatent, RandomNoise, CFGGuider, LTXVSeparateAVLatent, CheckpointLoaderSimple, GetNode, GetNode, SetNode, SetNode, GetNode, LTXVSeparateAVLatent, KSamplerSelect, BasicScheduler, CLIPTextEncode, GetNode, LTXVImgToVideoInplace, GetNode, SolidMask, PrimitiveBoolean, GetNode, ResizeImagesByLongerEdge, SimpleMath+, SimpleMath+, GetNode, LTXVConcatAVLatent, SimpleMath+, EmptyLTXVLatentVideo, LatentUpscaleModelLoader, LTXVImgToVideoInplace, LTXVLatentUpsampler, PrimitiveInt, Int, LTX2SamplingPreviewOverride, GetNode, GetNode, SetLatentNoiseMask, LTXVAudioVAEEncode, MelBandRoFormerSampler, GetNode, LTXAVTextEncoderLoader, CLIPTextEncode, LTX2_NAG, LoraLoaderModelOnly, LTXVConditioning, LTXVAudioVAELoader, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SetNode, PrimitiveStringMultiline, JoinStrings, SetNode, SetNode, SetNode, SetNode, DF_Int_to_Float, SetNode, SetNode, ImageResizeKJv2, MelBandRoFormerModelLoader, LayerUtility: PurgeVRAM, GetNode, GetNode, GetNode, GetNode, SamplerCustomAdvanced, VAEDecodeTiled, KSampler, NormalizeAudioLoudness, LTXVPreprocess, PrimitiveInt, VHS_VideoCombine, PrimitiveStringMultiline, LoadAudio, LoadImage]
patterns: []
missing: [LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SimpleMath+, SimpleMath+, SimpleMath+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 867362584064555, "steps": 4}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/【最新加速版】数字人话 LTX2.3唱歌对口型_2043952711799934977.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【最新加速版】数字人话 LTX2.3唱歌对口型_2043952711799934977.json`

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
- `GetNode`
- `LTXVConcatAVLatent`
- `SimpleMath+`
- `EmptyLTXVLatentVideo`
- `LatentUpscaleModelLoader`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `PrimitiveInt`
- `Int`
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
- `PrimitiveInt`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `LoadAudio`
- `LoadImage`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `867362584064555`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **55%**（42/76）

**有卡**：`LTXVCropGuides`、`LTXVConcatAVLatent`、`RandomNoise`、`CFGGuider`、`LTXVSeparateAVLatent`、`CheckpointLoaderSimple`、`KSamplerSelect`、`BasicScheduler`、`CLIPTextEncode`、`LTXVImgToVideoInplace`、`SolidMask`、`PrimitiveBoolean`、`ResizeImagesByLongerEdge`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`Int`、`LTX2SamplingPreviewOverride`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`MelBandRoFormerSampler`、`LTXAVTextEncoderLoader`、`LTX2_NAG`、`LoraLoaderModelOnly`、`LTXVConditioning`、`LTXVAudioVAELoader`、`JoinStrings`、`DF_Int_to_Float`、`ImageResizeKJv2`、`MelBandRoFormerModelLoader`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`KSampler`、`NormalizeAudioLoudness`、`LTXVPreprocess`、`VHS_VideoCombine`、`LoadAudio`、`LoadImage`

**缺卡**（7）：`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
