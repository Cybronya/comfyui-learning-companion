---
key: 视频生成/图生视频/LTX2.3 单图mv ID-LoRA （增强人脸一致、口型准确、动态协调）_2046304725880016898.json
name: LTX2.3 单图mv ID-LoRA （增强人脸一致、口型准确、动态协调）_2046304725880016898.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 单图mv ID-LoRA （增强人脸一致、口型准确、动态协调）_2046304725880016898.json
hash: 3e6cd3f0ef3b9c17
coverage: 0.756757
learned_at: 2026-10-15 22:36:56
nodes: [LTXVLatentUpsampler, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetNode, LTXVSeparateAVLatent, MelBandRoFormerModelLoader, SamplerCustomAdvanced, PainterAudioLength, MathExpression_UTK, Bjornulf_ShowFloat, Bjornulf_ShowInt, Reroute, Reroute, LatentUpscaleModelLoader, GetNode, Reroute, PreviewImage, KSamplerSelect, Bjornulf_ShowInt, PrimitiveFloat, LTXVConcatAVLatent, GetNode, DualCLIPLoader, SeedGenerator, CFGGuider, LTX2_NAG, GetNode, LTXVCropGuides, CFGGuider, Reroute, KSamplerSelect, VAEDecodeTiled, GetNode, SimpleMath+, LTXVAudioVAEEncode, ComfyMathExpression, ComfyMathExpression, GetNode, SolidMask, SetLatentNoiseMask, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVReferenceAudio, Note, LTXVAudioVAELoader, SetNode, LTXVImgToVideoInplace, Note, MelBandRoFormerSampler, ManualSigmas, RandomNoise, LoadImage, SimpleCalculatorKJ, ImageResizeKJv2, SetNode, LoadAudio, LTXVPreprocess, EmptyLTXVLatentVideo, TTResolutionSelector, Reroute, ManualSigmas, CheckpointLoaderSimple, LoadImage, VHS_VideoCombine, AudioCrop, CR Text, RHHiddenNodes, LoraLoaderModelOnly, Reroute, LTXVConditioning, CLIPTextEncode, CLIPTextEncode, RandomNoise, RHHiddenNodes]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
---

# 视频生成/图生视频/LTX2.3 单图mv ID-LoRA （增强人脸一致、口型准确、动态协调）_2046304725880016898.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046304725880016898.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVSeparateAVLatent`
- `MelBandRoFormerModelLoader`
- `SamplerCustomAdvanced` ★核心
- `PainterAudioLength`
- `MathExpression_UTK`
- `Bjornulf_ShowFloat`
- `Bjornulf_ShowInt`
- `Reroute`
- `Reroute`
- `LatentUpscaleModelLoader`
- `GetNode`
- `Reroute`
- `PreviewImage`
- `KSamplerSelect` ★核心
- `Bjornulf_ShowInt`
- `PrimitiveFloat`
- `LTXVConcatAVLatent`
- `GetNode`
- `DualCLIPLoader`
- `SeedGenerator`
- `CFGGuider`
- `LTX2_NAG`
- `GetNode`
- `LTXVCropGuides`
- `CFGGuider`
- `Reroute`
- `KSamplerSelect` ★核心
- `VAEDecodeTiled` ★核心
- `GetNode`
- `SimpleMath+`
- `LTXVAudioVAEEncode` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVReferenceAudio`
- `Note`
- `LTXVAudioVAELoader`
- `SetNode`
- `LTXVImgToVideoInplace`
- `Note`
- `MelBandRoFormerSampler` ★核心
- `ManualSigmas`
- `RandomNoise`
- `LoadImage`
- `SimpleCalculatorKJ`
- `ImageResizeKJv2`
- `SetNode`
- `LoadAudio`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `TTResolutionSelector`
- `Reroute`
- `ManualSigmas`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `AudioCrop`
- `CR Text`
- `RHHiddenNodes`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `RHHiddenNodes`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **76%**（56/74）

**有卡**：`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`MelBandRoFormerModelLoader`、`PainterAudioLength`、`MathExpression_UTK`、`Bjornulf_ShowFloat`、`Bjornulf_ShowInt`、`LatentUpscaleModelLoader`、`KSamplerSelect`、`LTXVConcatAVLatent`、`DualCLIPLoader`、`SeedGenerator`、`CFGGuider`、`LTX2_NAG`、`LTXVCropGuides`、`VAEDecodeTiled`、`SimpleMath+`、`LTXVAudioVAEEncode`、`ComfyMathExpression`、`SolidMask`、`SetLatentNoiseMask`、`LTXVImgToVideoInplace`、`LTXVReferenceAudio`、`LTXVAudioVAELoader`、`MelBandRoFormerSampler`、`ManualSigmas`、`RandomNoise`、`LoadImage`、`SimpleCalculatorKJ`、`ImageResizeKJv2`、`LoadAudio`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`TTResolutionSelector`、`CheckpointLoaderSimple`、`VHS_VideoCombine`、`AudioCrop`、`CR Text`、`RHHiddenNodes`、`LoraLoaderModelOnly`、`LTXVConditioning`、`CLIPTextEncode`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
