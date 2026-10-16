---
key: 视频生成/图生视频/LTX2.3 双人角色+音色参考生视频_2042618627672772609.json
name: LTX2.3 双人角色+音色参考生视频_2042618627672772609.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2042618627672772609.json
hash: 2d8d58bc1b56bc32
coverage: 0.495868
learned_at: 2026-10-15 22:36:29
nodes: [SamplerCustomAdvanced, CFGGuider, GetNode, GetNode, CFGGuider, KSamplerSelect, LTXVAudioVAEDecode, GetNode, ManualSigmas, VAEDecodeTiled, GetNode, GetNode, ModelPatchTorchSettings, SetNode, SetNode, Anything Everywhere, SetNode, GetNode, KSamplerSelect, RandomNoise, GetNode, PathchSageAttentionKJ, GetNode, SetNode, SetNode, MathExpression|pysssss, MathExpression|pysssss, SetNode, SetNode, SetNode, SetNode, PrimitiveInt, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, RandomNoise, LTXVPreprocess, SetNode, ManualSigmas, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVCropGuides, GetNode, LTXVImgToVideoInplace, Note, SamplerCustomAdvanced, LTXVSeparateAVLatent, easy cleanGpuUsed, VHS_VideoCombine, LatentUpscaleModelLoader, GetNode, CLIPTextEncode, GetNode, GetNode, LTXVConditioning, ComfyMathExpression, SetNode, PrimitiveInt, LTXVChunkFeedForward, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXAddVideoICLoRAGuideAdvanced, ComfyMathExpression, GetNode, GetNode, GetNode, AudioConcat, DualCLIPLoader, SetNode, MelBandRoFormerModelLoader, PrimitiveInt, PrimitiveInt, LTXVReferenceAudio, TrimVideoLatent, VAELoaderKJ, VAELoaderKJ, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, LTX2_NAG, LoadAudio, LoadAudio, SetNode, SetNode, ImageResizeKJv2, ImageResizeKJv2, easy imageRemBg, GetNode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, Note, MelBandRoFormerSampler, SetNode, Note, AudioCrop, LoraLoaderModelOnly, LoadImage, LoadImage, easy imageRemBg, ImageAddMulti, SetNode, PreviewImage, PrimitiveStringMultiline, PrimitiveInt, Note, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 双人角色+音色参考生视频_2042618627672772609.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042618627672772609.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（121 个）：
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `ManualSigmas`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `ModelPatchTorchSettings`
- `SetNode`
- `SetNode`
- `Anything Everywhere`
- `SetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `GetNode`
- `PathchSageAttentionKJ`
- `GetNode`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `LTXVPreprocess`
- `SetNode`
- `ManualSigmas`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `GetNode`
- `LTXVImgToVideoInplace`
- `Note`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `LatentUpscaleModelLoader`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `ComfyMathExpression`
- `SetNode`
- `PrimitiveInt`
- `LTXVChunkFeedForward`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXAddVideoICLoRAGuideAdvanced`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `AudioConcat`
- `DualCLIPLoader`
- `SetNode`
- `MelBandRoFormerModelLoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVReferenceAudio`
- `TrimVideoLatent`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTXICLoRALoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `LoadAudio`
- `LoadAudio`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `easy imageRemBg`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `Note`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `Note`
- `AudioCrop`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `easy imageRemBg`
- `ImageAddMulti`
- `SetNode`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `Note`
- `UNETLoader` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **50%**（60/121）

**有卡**：`SamplerCustomAdvanced`、`CFGGuider`、`KSamplerSelect`、`LTXVAudioVAEDecode`、`ManualSigmas`、`VAEDecodeTiled`、`ModelPatchTorchSettings`、`RandomNoise`、`PathchSageAttentionKJ`、`MathExpression|pysssss`、`LTXVSeparateAVLatent`、`LTXVPreprocess`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`LTXVImgToVideoInplace`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`LTXVConditioning`、`ComfyMathExpression`、`LTXVChunkFeedForward`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXAddVideoICLoRAGuideAdvanced`、`AudioConcat`、`DualCLIPLoader`、`MelBandRoFormerModelLoader`、`LTXVReferenceAudio`、`TrimVideoLatent`、`VAELoaderKJ`、`LTXICLoRALoaderModelOnly`、`LoraLoaderModelOnly`、`LTX2_NAG`、`LoadAudio`、`ImageResizeKJv2`、`easy imageRemBg`、`LayerUtility: ImageScaleByAspectRatio V2`、`MelBandRoFormerSampler`、`AudioCrop`、`LoadImage`、`ImageAddMulti`、`UNETLoader`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
