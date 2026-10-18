---
key: 视频生成/图生视频/双人对唱，不变脸，高清晰，全自动_LTX2.3_2051860484126715906.json
name: 双人对唱，不变脸，高清晰，全自动_LTX2.3_2051860484126715906.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/双人对唱，不变脸，高清晰，全自动_LTX2.3_2051860484126715906.json
hash: c88f03d07ce0a891
coverage: 0.6875
learned_at: 2026-10-15 22:37:24
nodes: [DualCLIPLoader, Note, VAELoaderKJ, KSamplerSelect, CR Text, LTXVSeparateAVLatent, VAELoaderKJ, SolidMask, Reroute, Reroute, LTXVImgToVideoInplaceKJ, LoraLoaderModelOnly, LTXVConcatAVLatent, LTXVAudioVAEEncode, SetLatentNoiseMask, ShowAnything|Mie, MarkdownNote, Float, CLIPTextEncode, CR Text, MarkdownNote, MarkdownNote, Note, MarkdownNote, MarkdownNote, MarkdownNote, Note, easy showAnything, MathExpression|pysssss, MathExpression|pysssss, Float, Qwen3ASRTranscribe, SamplerCustom, LoadAudio, Audio Duration (mtb), Int to String, CR Text Replace, ShowAnything|Mie, Text, PreviewAny, TTResolutionSelector, MarkdownNote, LoadImage, LoadImage, LoadImage, MarkdownNote, PreviewImage, LoraLoaderModelOnly, DiffusionModelLoaderKJ, RH_LLMAPI_Pro_Node, PreviewAny, MelBandRoFormerModelLoader, MelBandRoFormerSampler, Qwen3ASRLoader, ManualSigmas, MarkdownNote, LoadImage, MarkdownNote, AudioCrop, MarkdownNote, ImageResizeKJv2, EmptyLTXVLatentVideo, Reroute, PreviewAny, PreviewAny, Split String, PreviewAny, SomethingToString, RH_Translator, VAEDecodeTiled, PreviewAny, VHS_VideoCombine, PromptRelayEncode, LTXVConditioning, LTX2_NAG, CR Text, CR Text Concatenate, PreviewAudio, RHHiddenNodes, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 视频生成/图生视频/双人对唱，不变脸，高清晰，全自动_LTX2.3_2051860484126715906.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2051860484126715906.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（80 个）：
- `DualCLIPLoader`
- `Note`
- `VAELoaderKJ`
- `KSamplerSelect` ★核心
- `CR Text`
- `LTXVSeparateAVLatent`
- `VAELoaderKJ`
- `SolidMask`
- `Reroute`
- `Reroute`
- `LTXVImgToVideoInplaceKJ`
- `LoraLoaderModelOnly` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `ShowAnything|Mie`
- `MarkdownNote`
- `Float`
- `CLIPTextEncode` ★核心
- `CR Text`
- `MarkdownNote`
- `MarkdownNote`
- `Note`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Note`
- `easy showAnything`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `Float`
- `Qwen3ASRTranscribe`
- `SamplerCustom` ★核心
- `LoadAudio`
- `Audio Duration (mtb)`
- `Int to String`
- `CR Text Replace`
- `ShowAnything|Mie`
- `Text`
- `PreviewAny`
- `TTResolutionSelector`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `RH_LLMAPI_Pro_Node`
- `PreviewAny`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `Qwen3ASRLoader`
- `ManualSigmas`
- `MarkdownNote`
- `LoadImage`
- `MarkdownNote`
- `AudioCrop`
- `MarkdownNote`
- `ImageResizeKJv2`
- `EmptyLTXVLatentVideo`
- `Reroute`
- `PreviewAny`
- `PreviewAny`
- `Split String`
- `PreviewAny`
- `SomethingToString`
- `RH_Translator`
- `VAEDecodeTiled` ★核心
- `PreviewAny`
- `VHS_VideoCombine`
- `PromptRelayEncode`
- `LTXVConditioning`
- `LTX2_NAG`
- `CR Text`
- `CR Text Concatenate`
- `PreviewAudio`
- `RHHiddenNodes`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **69%**（55/80）

**有卡**：`DualCLIPLoader`、`VAELoaderKJ`、`KSamplerSelect`、`CR Text`、`LTXVSeparateAVLatent`、`SolidMask`、`LTXVImgToVideoInplaceKJ`、`LoraLoaderModelOnly`、`LTXVConcatAVLatent`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`ShowAnything|Mie`、`Float`、`CLIPTextEncode`、`MathExpression|pysssss`、`Qwen3ASRTranscribe`、`SamplerCustom`、`LoadAudio`、`Audio Duration (mtb)`、`Int to String`、`CR Text Replace`、`Text`、`TTResolutionSelector`、`LoadImage`、`DiffusionModelLoaderKJ`、`RH_LLMAPI_Pro_Node`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`Qwen3ASRLoader`、`ManualSigmas`、`AudioCrop`、`ImageResizeKJv2`、`EmptyLTXVLatentVideo`、`Split String`、`SomethingToString`、`RH_Translator`、`VAEDecodeTiled`、`VHS_VideoCombine`、`PromptRelayEncode`、`LTXVConditioning`、`LTX2_NAG`、`CR Text Concatenate`、`PreviewAudio`、`RHHiddenNodes`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler、LTXVConcatAVLatent、LTXVSeparateAVLatent
