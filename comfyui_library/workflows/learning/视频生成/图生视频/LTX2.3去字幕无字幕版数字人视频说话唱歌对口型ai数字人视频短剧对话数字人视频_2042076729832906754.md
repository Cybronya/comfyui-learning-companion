---
key: 视频生成/图生视频/LTX2.3去字幕无字幕版数字人视频说话唱歌对口型ai数字人视频短剧对话数字人视频_2042076729832906754.json
name: LTX2.3去字幕无字幕版数字人视频说话唱歌对口型ai数字人视频短剧对话数字人视频_2042076729832906754.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3去字幕无字幕版数字人视频说话唱歌对口型ai数字人视频短剧对话数字人视频_2042076729832906754.json
hash: 22aba26935533640
coverage: 0.644737
learned_at: 2026-10-15 22:36:24
nodes: [LTXVCropGuides, LTXVConcatAVLatent, RandomNoise, CFGGuider, LTXVSeparateAVLatent, CheckpointLoaderSimple, GetNode, GetNode, SetNode, SetNode, GetNode, LTXVSeparateAVLatent, KSamplerSelect, BasicScheduler, CLIPTextEncode, GetNode, LTXVImgToVideoInplace, GetNode, SolidMask, PrimitiveBoolean, GetNode, ResizeImagesByLongerEdge, SimpleMath+, SimpleMath+, GetNode, LTXVConcatAVLatent, SimpleMath+, EmptyLTXVLatentVideo, LatentUpscaleModelLoader, LTXVImgToVideoInplace, LTXVLatentUpsampler, PrimitiveInt, Int, VHS_VideoCombine, LTX2SamplingPreviewOverride, GetNode, GetNode, SetLatentNoiseMask, LTXVAudioVAEEncode, MelBandRoFormerSampler, GetNode, LTXAVTextEncoderLoader, CLIPTextEncode, LTX2_NAG, LoraLoaderModelOnly, LTXVConditioning, LTXVAudioVAELoader, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SetNode, PrimitiveStringMultiline, JoinStrings, SetNode, SetNode, SetNode, SetNode, DF_Int_to_Float, SetNode, SetNode, ImageResizeKJv2, MelBandRoFormerModelLoader, LayerUtility: PurgeVRAM, GetNode, GetNode, GetNode, GetNode, SamplerCustomAdvanced, VAEDecodeTiled, KSampler, NormalizeAudioLoudness, LTXVPreprocess, PrimitiveInt, LoadImage, LoadAudio, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 643970427179113, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/LTX2.3去字幕无字幕版数字人视频说话唱歌对口型ai数字人视频短剧对话数字人视频_2042076729832906754.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042076729832906754.json`

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
- `PrimitiveInt`
- `LoadImage`
- `LoadAudio`
- `PrimitiveStringMultiline`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `643970427179113`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **64%**（49/76）

**有卡**：`LTXVCropGuides`、`LTXVConcatAVLatent`、`RandomNoise`、`CFGGuider`、`LTXVSeparateAVLatent`、`CheckpointLoaderSimple`、`KSamplerSelect`、`BasicScheduler`、`CLIPTextEncode`、`LTXVImgToVideoInplace`、`SolidMask`、`PrimitiveBoolean`、`ResizeImagesByLongerEdge`、`SimpleMath+`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`Int`、`VHS_VideoCombine`、`LTX2SamplingPreviewOverride`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`MelBandRoFormerSampler`、`LTXAVTextEncoderLoader`、`LTX2_NAG`、`LoraLoaderModelOnly`、`LTXVConditioning`、`LTXVAudioVAELoader`、`LayerUtility: PurgeVRAM`、`JoinStrings`、`DF_Int_to_Float`、`ImageResizeKJv2`、`MelBandRoFormerModelLoader`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`KSampler`、`NormalizeAudioLoudness`、`LTXVPreprocess`、`LoadImage`、`LoadAudio`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
