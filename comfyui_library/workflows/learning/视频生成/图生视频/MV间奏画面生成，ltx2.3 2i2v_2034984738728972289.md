---
key: 视频生成/图生视频/MV间奏画面生成，ltx2.3 2i2v_2034984738728972289.json
name: MV间奏画面生成，ltx2.3 2i2v_2034984738728972289.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MV间奏画面生成，ltx2.3 2i2v_2034984738728972289.json
hash: d6c34e25d543f9ce
coverage: 0.626168
learned_at: 2026-10-15 22:35:47
nodes: [SamplerCustomAdvanced, SamplerCustomAdvanced, CFGGuider, LTXVCropGuides, Reroute, Reroute, KSamplerSelect, RandomNoise, LTXVSeparateAVLatent, SetLatentNoiseMask, LTXVAudioVAEEncode, SolidMask, LatentUpscaleModelLoader, Reroute, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, LTXVImgToVideoInplace, LTXVConcatAVLatent, Reroute, Reroute, LTXVLatentUpsampler, KSamplerSelect, RandomNoise, GetNode, GetNode, GetNode, VAEDecodeTiled, CM_IntToFloat, GetNode, GetNode, Reroute, Reroute, CFGGuider, Reroute, LTXVImgToVideoInplaceKJ, GetNode, LTXVConcatAVLatent, Reroute, easy showAnything, LTXVConditioning, ImageAndMaskResizeNode, ImageResizeKJv2, ComfyMathExpression, GetNode, EmptyLTXVLatentVideo, Reroute, ComfyMathExpression, GetNode, MathExpression|pysssss, Bjornulf_ShowFloat, SetNode, Reroute, Reroute, CheckpointLoaderSimple, CLIPTextEncode, LoadImage, CLIPTextEncode, ManualSigmas, PreviewAudio, ComfyMathExpression, SetNode, SetNode, LTXVPreprocess, SetNode, PainterAudioLength, Reroute, ManualSigmas, LTXVPreprocess, ImageAndMaskResizeNode, ImageResizeKJv2, LTXAVTextEncoderLoader, LTXVAudioVAELoader, SetNode, CM_IntToFloat, LoadImage, Int, LoadImage, Text, SaveImage, MarkdownNote, FloatConstant, VHS_VideoCombine, AudioCrop, LoadAudio, MarkdownNote, PrimitiveInt, SetNode, MarkdownNote, MarkdownNote, RH_Nano_Banana2_Gemini31Flash, LoadImage, MarkdownNote, MarkdownNote, Bjornulf_ShowInt, SimpleMath+, SetNode, CR Text, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVChunkFeedForward, ModelPatchTorchSettings, PathchSageAttentionKJ, CR Text]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
---

# 视频生成/图生视频/MV间奏画面生成，ltx2.3 2i2v_2034984738728972289.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2034984738728972289.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（107 个）：
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `LTXVCropGuides`
- `Reroute`
- `Reroute`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `LatentUpscaleModelLoader`
- `Reroute`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `Reroute`
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `CM_IntToFloat`
- `GetNode`
- `GetNode`
- `Reroute`
- `Reroute`
- `CFGGuider`
- `Reroute`
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `LTXVConcatAVLatent`
- `Reroute`
- `easy showAnything`
- `LTXVConditioning`
- `ImageAndMaskResizeNode`
- `ImageResizeKJv2`
- `ComfyMathExpression`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `Reroute`
- `ComfyMathExpression`
- `GetNode`
- `MathExpression|pysssss`
- `Bjornulf_ShowFloat`
- `SetNode`
- `Reroute`
- `Reroute`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ManualSigmas`
- `PreviewAudio`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `LTXVPreprocess`
- `SetNode`
- `PainterAudioLength`
- `Reroute`
- `ManualSigmas`
- `LTXVPreprocess`
- `ImageAndMaskResizeNode`
- `ImageResizeKJv2`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `SetNode`
- `CM_IntToFloat`
- `LoadImage`
- `Int`
- `LoadImage`
- `Text`
- `SaveImage`
- `MarkdownNote`
- `FloatConstant`
- `VHS_VideoCombine`
- `AudioCrop`
- `LoadAudio`
- `MarkdownNote`
- `PrimitiveInt`
- `SetNode`
- `MarkdownNote`
- `MarkdownNote`
- `RH_Nano_Banana2_Gemini31Flash`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `Bjornulf_ShowInt`
- `SimpleMath+`
- `SetNode`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CR Text`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **63%**（67/107）

**有卡**：`SamplerCustomAdvanced`、`CFGGuider`、`LTXVCropGuides`、`KSamplerSelect`、`RandomNoise`、`LTXVSeparateAVLatent`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`LatentUpscaleModelLoader`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`CM_IntToFloat`、`LTXVImgToVideoInplaceKJ`、`LTXVConditioning`、`ImageAndMaskResizeNode`、`ImageResizeKJv2`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`MathExpression|pysssss`、`Bjornulf_ShowFloat`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`LoadImage`、`ManualSigmas`、`PreviewAudio`、`LTXVPreprocess`、`PainterAudioLength`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`Int`、`Text`、`SaveImage`、`FloatConstant`、`VHS_VideoCombine`、`AudioCrop`、`LoadAudio`、`RH_Nano_Banana2_Gemini31Flash`、`Bjornulf_ShowInt`、`SimpleMath+`、`CR Text`、`LoraLoaderModelOnly`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
