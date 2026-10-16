---
key: 视频生成/图生视频/LTX2.3数字人-极速版_2044577721174462465.json
name: LTX2.3数字人-极速版_2044577721174462465.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2044577721174462465.json
hash: 6eea8ba2badddd78
coverage: 0.607595
learned_at: 2026-10-15 22:36:38
nodes: [SetNode, VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, SetNode, EmptyLTXVLatentVideo, GetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, LTXVImgToVideoInplace, SetNode, GetNode, GetNode, LTXVConcatAVLatent, SamplerCustomAdvanced, GetNode, LTXVSeparateAVLatent, GetNode, CLIPTextEncode, LTXVSpatioTemporalTiledVAEDecode, GetNode, MelBandRoFormerModelLoader, GetNode, MelBandRoFormerSampler, GetNode, GetNode, SetNode, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, LTXVAudioVAEDecode, MathExpression|pysssss, Float, MathExpression|pysssss, SetNode, SetNode, GetNode, GetNode, GetNode, LTXVConditioning, LTX2_NAG, GetNode, Note, VHS_VideoCombine, Audio Duration (mtb), Reroute, SetNode, GetNode, GetNode, CLIPTextEncode, AudioCrop, DualCLIPLoader, RH_LLMAPI_Pro_Node, CR Prompt Text, ConcatTextOfUtils, LoadImage, CR Text, CR Text, LoadAudio, UNETLoader, LoraLoaderModelOnly, LTX2AttentionTunerPatch, PathchSageAttentionKJ, ModelPatchTorchSettings, LoraLoaderModelOnly, LTXVChunkFeedForward, Int, Int, TTResolutionSelector, Bool]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3数字人-极速版_2044577721174462465.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044577721174462465.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（79 个）：
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVImgToVideoInplace`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `GetNode`
- `MelBandRoFormerModelLoader`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `LTXVAudioVAEDecode` ★核心
- `MathExpression|pysssss`
- `Float`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `LTX2_NAG`
- `GetNode`
- `Note`
- `VHS_VideoCombine`
- `Audio Duration (mtb)`
- `Reroute`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `AudioCrop`
- `DualCLIPLoader`
- `RH_LLMAPI_Pro_Node`
- `CR Prompt Text`
- `ConcatTextOfUtils`
- `LoadImage`
- `CR Text`
- `CR Text`
- `LoadAudio`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2AttentionTunerPatch`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `LTXVChunkFeedForward`
- `Int`
- `Int`
- `TTResolutionSelector`
- `Bool`

## 知识

覆盖率 **61%**（48/79）

**有卡**：`VAELoaderKJ`、`EmptyLTXVLatentVideo`、`ImageResizeKJv2`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CLIPTextEncode`、`LTXVSpatioTemporalTiledVAEDecode`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEDecode`、`MathExpression|pysssss`、`Float`、`LTXVConditioning`、`LTX2_NAG`、`VHS_VideoCombine`、`Audio Duration (mtb)`、`AudioCrop`、`DualCLIPLoader`、`RH_LLMAPI_Pro_Node`、`CR Prompt Text`、`ConcatTextOfUtils`、`LoadImage`、`CR Text`、`LoadAudio`、`UNETLoader`、`LoraLoaderModelOnly`、`LTX2AttentionTunerPatch`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`Int`、`TTResolutionSelector`、`Bool`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
