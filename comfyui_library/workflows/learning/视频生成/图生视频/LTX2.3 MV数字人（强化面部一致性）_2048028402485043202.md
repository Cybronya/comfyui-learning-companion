---
key: 视频生成/图生视频/LTX2.3 MV数字人（强化面部一致性）_2048028402485043202.json
name: LTX2.3 MV数字人（强化面部一致性）_2048028402485043202.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2048028402485043202.json
hash: 89dcf8b8b0819a74
coverage: 0.746479
learned_at: 2026-10-15 22:37:08
nodes: [Reroute, GetNode, GetNode, LTXVImgToVideoInplace, LTXVAudioVAEEncode, EmptyLTXVLatentVideo, GetNode, CheckpointLoaderSimple, LTXVAudioVAELoader, LoraLoaderModelOnly, SetNode, MelBandRoFormerSampler, PainterAudioLength, Bjornulf_ShowFloat, ImageResizeKJv2, ComfyMathExpression, ComfyMathExpression, LoadImage, DualCLIPLoader, CLIPTextEncode, CLIPTextEncode, SetNode, GetNode, MelBandRoFormerModelLoader, LTXVConditioning, CFGGuider, LTXVSeparateAVLatent, LTXVImgToVideoInplace, LTXVConcatAVLatent, GetNode, Reroute, VAEDecodeTiled, Reroute, Reroute, SimpleCalculatorKJ, Note, MathExpression_UTK, Bjornulf_ShowInt, PreviewImage, Reroute, LTXVCropGuides, CFGGuider, GetNode, KSamplerSelect, Reroute, RandomNoise, SeedGenerator, RandomNoise, LTXVSeparateAVLatent, LTXVLatentUpsampler, LatentUpscaleModelLoader, Bjornulf_ShowInt, Note, CR Text, SolidMask, SetLatentNoiseMask, ManualSigmas, VHS_VideoCombine, LoadAudio, AudioCrop, TTResolutionSelector, SimpleMath+, PrimitiveFloat, LTX2_NAG, BasicScheduler, KSamplerSelect, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVConcatAVLatent, LTXVReferenceAudio, Label (rgthree)]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
---

# 视频生成/图生视频/LTX2.3 MV数字人（强化面部一致性）_2048028402485043202.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2048028402485043202.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `Reroute`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEEncode` ★核心
- `EmptyLTXVLatentVideo`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `PainterAudioLength`
- `Bjornulf_ShowFloat`
- `ImageResizeKJv2`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LoadImage`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `MelBandRoFormerModelLoader`
- `LTXVConditioning`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `GetNode`
- `Reroute`
- `VAEDecodeTiled` ★核心
- `Reroute`
- `Reroute`
- `SimpleCalculatorKJ`
- `Note`
- `MathExpression_UTK`
- `Bjornulf_ShowInt`
- `PreviewImage`
- `Reroute`
- `LTXVCropGuides`
- `CFGGuider`
- `GetNode`
- `KSamplerSelect` ★核心
- `Reroute`
- `RandomNoise`
- `SeedGenerator`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `Bjornulf_ShowInt`
- `Note`
- `CR Text`
- `SolidMask`
- `SetLatentNoiseMask`
- `ManualSigmas`
- `VHS_VideoCombine`
- `LoadAudio`
- `AudioCrop`
- `TTResolutionSelector`
- `SimpleMath+`
- `PrimitiveFloat`
- `LTX2_NAG`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `LTXVReferenceAudio`
- `Label (rgthree)`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **75%**（53/71）

**有卡**：`LTXVImgToVideoInplace`、`LTXVAudioVAEEncode`、`EmptyLTXVLatentVideo`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`MelBandRoFormerSampler`、`PainterAudioLength`、`Bjornulf_ShowFloat`、`ImageResizeKJv2`、`ComfyMathExpression`、`LoadImage`、`DualCLIPLoader`、`CLIPTextEncode`、`MelBandRoFormerModelLoader`、`LTXVConditioning`、`CFGGuider`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`VAEDecodeTiled`、`SimpleCalculatorKJ`、`MathExpression_UTK`、`Bjornulf_ShowInt`、`LTXVCropGuides`、`KSamplerSelect`、`RandomNoise`、`SeedGenerator`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`CR Text`、`SolidMask`、`SetLatentNoiseMask`、`ManualSigmas`、`VHS_VideoCombine`、`LoadAudio`、`AudioCrop`、`TTResolutionSelector`、`SimpleMath+`、`LTX2_NAG`、`BasicScheduler`、`SamplerCustomAdvanced`、`LTXVReferenceAudio`、`Label (rgthree)`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
