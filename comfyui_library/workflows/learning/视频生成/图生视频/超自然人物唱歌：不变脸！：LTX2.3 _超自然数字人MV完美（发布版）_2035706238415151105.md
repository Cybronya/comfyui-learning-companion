---
key: 视频生成/图生视频/超自然人物唱歌：不变脸！：LTX2.3 _超自然数字人MV完美（发布版）_2035706238415151105.json
name: 超自然人物唱歌：不变脸！：LTX2.3 _超自然数字人MV完美（发布版）_2035706238415151105.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2035706238415151105.json
hash: 3f1f03389a98bb9c
coverage: 0.66055
learned_at: 2026-10-15 22:35:50
nodes: [SamplerCustomAdvanced, LTXVCropGuides, KSamplerSelect, RandomNoise, LTXVSeparateAVLatent, Reroute, SetLatentNoiseMask, LTXVAudioVAEEncode, SolidMask, LatentUpscaleModelLoader, SetNode, SetNode, Reroute, Reroute, GetNode, Reroute, Reroute, LTXVConcatAVLatent, GetNode, LTXVSeparateAVLatent, SamplerCustomAdvanced, CFGGuider, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, LTXVLatentUpsampler, GetNode, CLIPTextEncode, Reroute, Reroute, CM_IntToFloat, LTXAVTextEncoderLoader, SetNode, PrimitiveInt, GetNode, ComfyMathExpression, Bjornulf_ShowInt, LTXVImgToVideoInplaceKJ, CM_IntToFloat, VAEDecodeTiled, GetNode, Reroute, CLIPTextEncode, LTXVImgToVideoInplace, PainterAudioLength, PreviewAudio, Reroute, SimpleMath+, MathExpression_UTK, Reroute, Bjornulf_ShowInt, ManualSigmas, ManualSigmas, easy showAnything, GetNode, KSamplerSelect, RandomNoise, EmptyLTXVLatentVideo, MarkdownNote, CheckpointLoaderSimple, LTXVConditioning, CFGGuider, ImageAndMaskResizeNode, Reroute, ImageAndMaskResizeNode, ImageResizeKJv2, LTXVPreprocess, LTXVPreprocess, ComfyMathExpression, SetNode, ComfyMathExpression, SetNode, ImageResizeKJv2, Int, MarkdownNote, MarkdownNote, LoadImage, LoadImage, FloatConstant, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, Reroute, workflow>1, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, GetNode, CR Text Replace, LTXVAudioVAELoader, VHS_VideoCombine, easy showAnything, Text Multiline, Text Multiline, ShowText|pysssss, HeartMuLa_Transcribe, AudioCrop, SetNode, LoadAudio]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
---

# 视频生成/图生视频/超自然人物唱歌：不变脸！：LTX2.3 _超自然数字人MV完美（发布版）_2035706238415151105.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2035706238415151105.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（109 个）：
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `Reroute`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `LatentUpscaleModelLoader`
- `SetNode`
- `SetNode`
- `Reroute`
- `Reroute`
- `GetNode`
- `Reroute`
- `Reroute`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `CM_IntToFloat`
- `LTXAVTextEncoderLoader`
- `SetNode`
- `PrimitiveInt`
- `GetNode`
- `ComfyMathExpression`
- `Bjornulf_ShowInt`
- `LTXVImgToVideoInplaceKJ`
- `CM_IntToFloat`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `Reroute`
- `CLIPTextEncode` ★核心
- `LTXVImgToVideoInplace`
- `PainterAudioLength`
- `PreviewAudio`
- `Reroute`
- `SimpleMath+`
- `MathExpression_UTK`
- `Reroute`
- `Bjornulf_ShowInt`
- `ManualSigmas`
- `ManualSigmas`
- `easy showAnything`
- `GetNode`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `EmptyLTXVLatentVideo`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `ImageAndMaskResizeNode`
- `Reroute`
- `ImageAndMaskResizeNode`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `ImageResizeKJv2`
- `Int`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `FloatConstant`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `Reroute`
- `workflow>1`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `GetNode`
- `CR Text Replace`
- `LTXVAudioVAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `Text Multiline`
- `Text Multiline`
- `ShowText|pysssss`
- `HeartMuLa_Transcribe`
- `AudioCrop`
- `SetNode`
- `LoadAudio`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **66%**（72/109）

**有卡**：`SamplerCustomAdvanced`、`LTXVCropGuides`、`KSamplerSelect`、`RandomNoise`、`LTXVSeparateAVLatent`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`LatentUpscaleModelLoader`、`LTXVConcatAVLatent`、`CFGGuider`、`LTXVLatentUpsampler`、`CLIPTextEncode`、`CM_IntToFloat`、`LTXAVTextEncoderLoader`、`ComfyMathExpression`、`Bjornulf_ShowInt`、`LTXVImgToVideoInplaceKJ`、`VAEDecodeTiled`、`LTXVImgToVideoInplace`、`PainterAudioLength`、`PreviewAudio`、`SimpleMath+`、`MathExpression_UTK`、`ManualSigmas`、`EmptyLTXVLatentVideo`、`CheckpointLoaderSimple`、`LTXVConditioning`、`ImageAndMaskResizeNode`、`ImageResizeKJv2`、`LTXVPreprocess`、`Int`、`LoadImage`、`FloatConstant`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`workflow>1`、`Text Multiline`、`CR Text Replace`、`LTXVAudioVAELoader`、`VHS_VideoCombine`、`HeartMuLa_Transcribe`、`AudioCrop`、`LoadAudio`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
