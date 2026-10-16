---
key: 视频生成/图生视频/（官方版-循环）Infinite Talk无限时长加速版双人数字人V1 林耀2.6_2019704865835982849.json
name: （官方版-循环）Infinite Talk无限时长加速版双人数字人V1 林耀2.6_2019704865835982849.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2019704865835982849.json
hash: c02893dfb592a4ff
coverage: 0.828571
learned_at: 2026-10-15 22:35:04
nodes: [VAEDecode, KSamplerSelect, KSamplerSelect, CFGGuider, RandomNoise, BasicScheduler, easy showAnything, ConditioningZeroOut, BasicScheduler, ConditioningZeroOut, RandomNoise, CFGGuider, SamplerCustomAdvanced, CLIPTextEncode, ModelPatchTorchSettings, PathchSageAttentionKJ, MelBandRoFormerModelLoader, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MelBandRoFormerSampler, Audio Duration (mtb), Reroute, AudioConcat, JWInteger, Note, Note, Note, TrimAudioDuration, TrimAudioDuration, JWFloat, JWFloat, JWFloat, JWFloat, Note, Note, Note, Note, SimpleCalculatorKJ, LoraLoaderModelOnly, UNETLoader, Note, ModelPatchLoader, AudioEncoderLoader, CLIPLoader, VAELoader, SimpleMath+, CR Text, Note, Note, LoadAudio, VAEDecode, easy forLoopStart, LayerUtility: ImageScaleByAspectRatio V2, AudioEncoderEncode, AudioEncoderEncode, LoadAudio, PreviewAudio, SamplerCustomAdvanced, ImageFromBatch, GetImageSizeAndCount, ImageBatch, easy forLoopEnd, LoadImage, LoadImage, CLIPTextEncode, WanInfiniteTalkToVideo, WanInfiniteTalkToVideo, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/（官方版-循环）Infinite Talk无限时长加速版双人数字人V1 林耀2.6_2019704865835982849.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2019704865835982849.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（70 个）：
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `BasicScheduler`
- `easy showAnything`
- `ConditioningZeroOut`
- `BasicScheduler`
- `ConditioningZeroOut`
- `RandomNoise`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerSampler` ★核心
- `Audio Duration (mtb)`
- `Reroute`
- `AudioConcat`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `TrimAudioDuration`
- `TrimAudioDuration`
- `JWFloat`
- `JWFloat`
- `JWFloat`
- `JWFloat`
- `Note`
- `Note`
- `Note`
- `Note`
- `SimpleCalculatorKJ`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Note`
- `ModelPatchLoader`
- `AudioEncoderLoader`
- `CLIPLoader`
- `VAELoader`
- `SimpleMath+`
- `CR Text`
- `Note`
- `Note`
- `LoadAudio`
- `VAEDecode` ★核心
- `easy forLoopStart`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AudioEncoderEncode`
- `AudioEncoderEncode`
- `LoadAudio`
- `PreviewAudio`
- `SamplerCustomAdvanced` ★核心
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `ImageBatch`
- `easy forLoopEnd`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `WanInfiniteTalkToVideo`
- `WanInfiniteTalkToVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **83%**（58/70）

**有卡**：`VAEDecode`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`BasicScheduler`、`ConditioningZeroOut`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`Audio Duration (mtb)`、`AudioConcat`、`JWInteger`、`TrimAudioDuration`、`JWFloat`、`SimpleCalculatorKJ`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelPatchLoader`、`AudioEncoderLoader`、`CLIPLoader`、`VAELoader`、`SimpleMath+`、`CR Text`、`LoadAudio`、`easy forLoopStart`、`LayerUtility: ImageScaleByAspectRatio V2`、`AudioEncoderEncode`、`PreviewAudio`、`ImageFromBatch`、`GetImageSizeAndCount`、`ImageBatch`、`easy forLoopEnd`、`LoadImage`、`WanInfiniteTalkToVideo`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
