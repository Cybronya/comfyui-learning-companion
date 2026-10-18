---
key: 音频生成/音频生成/LTX2.3 MV数字人（moss长音频加强面部一致性）_2049272954013360129.json
name: LTX2.3 MV数字人（moss长音频加强面部一致性）_2049272954013360129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/LTX2.3 MV数字人（moss长音频加强面部一致性）_2049272954013360129.json
hash: 2f3c16a370e190ad
coverage: 0.76
learned_at: 2026-10-18 03:04:51
nodes: [Reroute, GetNode, GetNode, LTXVImgToVideoInplace, LTXVAudioVAEEncode, EmptyLTXVLatentVideo, GetNode, CheckpointLoaderSimple, LTXVAudioVAELoader, SetNode, MelBandRoFormerSampler, PainterAudioLength, Bjornulf_ShowFloat, ImageResizeKJv2, ComfyMathExpression, ComfyMathExpression, DualCLIPLoader, CLIPTextEncode, CLIPTextEncode, SetNode, GetNode, MelBandRoFormerModelLoader, LTXVSeparateAVLatent, LTXVConcatAVLatent, GetNode, Reroute, VAEDecodeTiled, Reroute, Reroute, SimpleCalculatorKJ, Note, MathExpression_UTK, Bjornulf_ShowInt, PreviewImage, Reroute, LTXVCropGuides, CFGGuider, GetNode, KSamplerSelect, Reroute, RandomNoise, SeedGenerator, RandomNoise, LTXVSeparateAVLatent, LTXVLatentUpsampler, Bjornulf_ShowInt, SolidMask, SetLatentNoiseMask, ManualSigmas, VHS_VideoCombine, TTResolutionSelector, SimpleMath+, PrimitiveFloat, BasicScheduler, KSamplerSelect, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVConcatAVLatent, Label (rgthree), Note, AudioCrop, LoadImage, CR Text, LoraLoaderModelOnly, LTXVConditioning, LTXVReferenceAudio, LTX2_NAG, CFGGuider, MossTTSModelLoader, MossTTSVoiceDesign, LayerUtility: PurgeVRAM V2, PreviewAudio, LatentUpscaleModelLoader, LTXVImgToVideoInplace, LoadAudio]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
---

# 音频生成/音频生成/LTX2.3 MV数字人（moss长音频加强面部一致性）_2049272954013360129.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/LTX2.3 MV数字人（moss长音频加强面部一致性）_2049272954013360129.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `Reroute`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEEncode` ★核心
- `EmptyLTXVLatentVideo`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `PainterAudioLength`
- `Bjornulf_ShowFloat`
- `ImageResizeKJv2`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `MelBandRoFormerModelLoader`
- `LTXVSeparateAVLatent`
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
- `Bjornulf_ShowInt`
- `SolidMask`
- `SetLatentNoiseMask`
- `ManualSigmas`
- `VHS_VideoCombine`
- `TTResolutionSelector`
- `SimpleMath+`
- `PrimitiveFloat`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `Label (rgthree)`
- `Note`
- `AudioCrop`
- `LoadImage`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `LTXVReferenceAudio`
- `LTX2_NAG`
- `CFGGuider`
- `MossTTSModelLoader`
- `MossTTSVoiceDesign`
- `LayerUtility: PurgeVRAM V2`
- `PreviewAudio`
- `LatentUpscaleModelLoader`
- `LTXVImgToVideoInplace`
- `LoadAudio`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **76%**（57/75）

**有卡**：`LTXVImgToVideoInplace`、`LTXVAudioVAEEncode`、`EmptyLTXVLatentVideo`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`MelBandRoFormerSampler`、`PainterAudioLength`、`Bjornulf_ShowFloat`、`ImageResizeKJv2`、`ComfyMathExpression`、`DualCLIPLoader`、`CLIPTextEncode`、`MelBandRoFormerModelLoader`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`VAEDecodeTiled`、`SimpleCalculatorKJ`、`MathExpression_UTK`、`Bjornulf_ShowInt`、`LTXVCropGuides`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`SeedGenerator`、`LTXVLatentUpsampler`、`SolidMask`、`SetLatentNoiseMask`、`ManualSigmas`、`VHS_VideoCombine`、`TTResolutionSelector`、`SimpleMath+`、`BasicScheduler`、`SamplerCustomAdvanced`、`Label (rgthree)`、`AudioCrop`、`LoadImage`、`CR Text`、`LoraLoaderModelOnly`、`LTXVConditioning`、`LTXVReferenceAudio`、`LTX2_NAG`、`MossTTSModelLoader`、`MossTTSVoiceDesign`、`LayerUtility: PurgeVRAM V2`、`PreviewAudio`、`LatentUpscaleModelLoader`、`LoadAudio`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
