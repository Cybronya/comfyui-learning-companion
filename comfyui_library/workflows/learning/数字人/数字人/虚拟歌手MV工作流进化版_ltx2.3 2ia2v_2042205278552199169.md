---
key: 数字人/数字人/虚拟歌手MV工作流进化版_ltx2.3 2ia2v_2042205278552199169.json
name: 虚拟歌手MV工作流进化版_ltx2.3 2ia2v_2042205278552199169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/虚拟歌手MV工作流进化版_ltx2.3 2ia2v_2042205278552199169.json
hash: 593873c091f9a22c
coverage: 0.684615
learned_at: 2026-10-26 02:04:39
nodes: [GetNode, GetNode, EmptyLTXVLatentVideo, FloatConstant, Text Multiline, Text Multiline, Text Multiline, PrimitiveStringMultiline, Text Multiline, Text Multiline, Text Multiline, GetNode, HeartMuLa_Transcribe, LTXVConditioning, Reroute, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, Text Multiline, SetNode, SimpleMath+, KSamplerSelect, Reroute, easy showAnything, GetNode, Reroute, PainterAudioLength, LTXVAudioVAELoader, LTXVCropGuides, CFGGuider, KSamplerSelect, Reroute, LTXVLatentUpsampler, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, Bjornulf_ShowInt, CM_IntToFloat, MathExpression_UTK, Int, ComfyMathExpression, ComfyMathExpression, SetNode, SetNode, Reroute, ManualSigmas, LTXVConcatAVLatent, SetLatentNoiseMask, LTXVAudioVAEEncode, SolidMask, ImageResizeKJv2, LoadImage, MarkdownNote, LoadImage, Text Multiline, MarkdownNote, Text Multiline, LoadImage, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, MelBandRoFormerSampler, MelBandRoFormerModelLoader, ImageResizeKJv2, LoadImage, CR Text Replace, GetNode, GetNode, SetNode, GetNode, SetNode, Bjornulf_ShowInt, Bjornulf_ShowFloat, DualCLIPLoader, CLIPTextEncode, CLIPTextEncode, easy showAnything, TTResolutionSelector, LoadAudio, PreviewAudio, Text Multiline, MarkdownNote, Reroute, SimpleMath+, Reroute, MarkdownNote, AudioCrop, SamplerCustomAdvanced, GetNode, LTXVSeparateAVLatent, VAEDecodeTiled, GetNode, GetImageRangeFromBatch, CM_IntToFloat, ComfyMathExpression, Bjornulf_ShowInt, VHS_VideoCombine, PreviewImage, CheckpointLoaderSimple, SetNode, Reroute, LTX2_NAG, Reroute, RandomNoise, PrimitiveInt, CFGGuider, RandomNoise, LTXVImgToVideoInplaceKJ, Reroute, Reroute, LatentUpscaleModelLoader, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, KSamplerSelect, RHHiddenNodes, LTXVPreprocess, LTXVPreprocess, MarkdownNote, Text Multiline, RHHiddenNodes, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, RHHiddenNodes, MarkdownNote]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
---

# 数字人/数字人/虚拟歌手MV工作流进化版_ltx2.3 2ia2v_2042205278552199169.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/虚拟歌手MV工作流进化版_ltx2.3 2ia2v_2042205278552199169.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（130 个）：
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `FloatConstant`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `PrimitiveStringMultiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `GetNode`
- `HeartMuLa_Transcribe`
- `LTXVConditioning`
- `Reroute`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `Text Multiline`
- `SetNode`
- `SimpleMath+`
- `KSamplerSelect` ★核心
- `Reroute`
- `easy showAnything`
- `GetNode`
- `Reroute`
- `PainterAudioLength`
- `LTXVAudioVAELoader`
- `LTXVCropGuides`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `Bjornulf_ShowInt`
- `CM_IntToFloat`
- `MathExpression_UTK`
- `Int`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `Reroute`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `ImageResizeKJv2`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `Text Multiline`
- `MarkdownNote`
- `Text Multiline`
- `LoadImage`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `CR Text Replace`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowFloat`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `TTResolutionSelector`
- `LoadAudio`
- `PreviewAudio`
- `Text Multiline`
- `MarkdownNote`
- `Reroute`
- `SimpleMath+`
- `Reroute`
- `MarkdownNote`
- `AudioCrop`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetImageRangeFromBatch`
- `CM_IntToFloat`
- `ComfyMathExpression`
- `Bjornulf_ShowInt`
- `VHS_VideoCombine`
- `PreviewImage`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `Reroute`
- `LTX2_NAG`
- `Reroute`
- `RandomNoise`
- `PrimitiveInt`
- `CFGGuider`
- `RandomNoise`
- `LTXVImgToVideoInplaceKJ`
- `Reroute`
- `Reroute`
- `LatentUpscaleModelLoader`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `RHHiddenNodes`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `MarkdownNote`
- `Text Multiline`
- `RHHiddenNodes`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RHHiddenNodes`
- `MarkdownNote`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **68%**（89/130）

**有卡**：`EmptyLTXVLatentVideo`、`FloatConstant`、`Text Multiline`、`HeartMuLa_Transcribe`、`LTXVConditioning`、`SimpleMath+`、`KSamplerSelect`、`PainterAudioLength`、`LTXVAudioVAELoader`、`LTXVCropGuides`、`CFGGuider`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`Bjornulf_ShowInt`、`CM_IntToFloat`、`MathExpression_UTK`、`Int`、`ComfyMathExpression`、`ManualSigmas`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`ImageResizeKJv2`、`LoadImage`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`CR Text Replace`、`Bjornulf_ShowFloat`、`DualCLIPLoader`、`CLIPTextEncode`、`TTResolutionSelector`、`LoadAudio`、`PreviewAudio`、`AudioCrop`、`VAEDecodeTiled`、`GetImageRangeFromBatch`、`VHS_VideoCombine`、`CheckpointLoaderSimple`、`LTX2_NAG`、`RandomNoise`、`LTXVImgToVideoInplaceKJ`、`LatentUpscaleModelLoader`、`easy cleanGpuUsed`、`RHHiddenNodes`、`LTXVPreprocess`、`LoraLoaderModelOnly`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
