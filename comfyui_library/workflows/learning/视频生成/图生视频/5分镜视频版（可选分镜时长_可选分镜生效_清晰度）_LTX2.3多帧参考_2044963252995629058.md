---
key: 视频生成/图生视频/5分镜视频版（可选分镜时长_可选分镜生效_清晰度）_LTX2.3多帧参考_2044963252995629058.json
name: 5分镜视频版（可选分镜时长_可选分镜生效_清晰度）_LTX2.3多帧参考_2044963252995629058.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/5分镜视频版（可选分镜时长_可选分镜生效_清晰度）_LTX2.3多帧参考_2044963252995629058.json
hash: 25250f91ae7edf95
coverage: 0.791411
learned_at: 2026-10-15 22:36:43
nodes: [easy showAnything, CR Text, easy showAnything, easy showAnything, easy showAnything, CR Text, easy showAnything, easy float, easy float, easy float, PrimitiveInt, easy float, easy float, PrimitiveInt, Bjornulf_IfElse, Bjornulf_IfElse, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, MathExpression|pysssss, LazySwitch1way, LazySwitch1way, LazySwitch2way, LazySwitch1way, MathExpression|pysssss, CR Text Concatenate, CR Text, CR Text Concatenate, CR Text, CR Text Concatenate, CR Text Concatenate, CR Text, CR Text Concatenate, CR Text Concatenate, CR Text, CR Text, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy float, PrimitiveInt, Bjornulf_IfElse, CR Text, easy float, MathExpression|pysssss, LazySwitch2way, MathExpression|pysssss, LazySwitch2way, PrimitiveInt, MathExpression|pysssss, LazySwitch1way, easy float, PrimitiveInt, LazySwitch2way, CFGGuider, CLIPTextEncode, CLIPTextEncode, MathExpression|pysssss, MathExpression|pysssss, Bjornulf_IfElse, PrimitiveInt, PrimitiveInt, LoadImage, LoadImage, PrimitiveInt, PrimitiveInt, PrimitiveInt, LoadImage, LoadImage, PrimitiveInt, LazySwitch1way, LazySwitch1way, MathExpression|pysssss, LazySwitch1way, LazySwitch1way, LoadImage, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, RandomNoise, RH_Translator, VAEDecodeTiled, VHS_VideoCombine, PreviewAny, PreviewAny, GetNode, GetNode, GetNode, LTXVLatentUpsampler, ManualSigmas, KSamplerSelect, SamplerCustomAdvanced, RandomNoise, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVSeparateAVLatent, GetImageRangeFromBatch, LTXVAudioVAEDecode, easy convertAnything, SetNode, SetNode, SetNode, LTX2_NAG, CFGNorm, LayerUtility: PurgeVRAM V2, CFGGuider, ManualSigmas, LTXVConcatAVLatent, KSamplerSelect, SamplerCustomAdvanced, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVAddGuideMulti, easy convertAnything, CR Text, CR Text Concatenate, RHHiddenNodes, PrimitiveInt, JWInteger, easy boolean, easy boolean, easy boolean, easy boolean, MarkdownNote, LTXVAudioVAELoader, CR Text Concatenate, CR Text, RH_LLMAPI_Pro_Node, CR Text Concatenate, CR Text, MarkdownNote, VAELoaderKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXVChunkFeedForward, DualCLIPLoader, easy boolean, LazySwitch1way, LoraLoaderModelOnly, LTXVConditioning, CR Text, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CheckpointLoaderSimple, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 20, "width": 93}
---

# 视频生成/图生视频/5分镜视频版（可选分镜时长_可选分镜生效_清晰度）_LTX2.3多帧参考_2044963252995629058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044963252995629058.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（163 个）：
- `easy showAnything`
- `CR Text`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `CR Text`
- `easy showAnything`
- `easy float`
- `easy float`
- `easy float`
- `PrimitiveInt`
- `easy float`
- `easy float`
- `PrimitiveInt`
- `Bjornulf_IfElse`
- `Bjornulf_IfElse`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `MathExpression|pysssss`
- `LazySwitch1way`
- `LazySwitch1way`
- `LazySwitch2way`
- `LazySwitch1way`
- `MathExpression|pysssss`
- `CR Text Concatenate`
- `CR Text`
- `CR Text Concatenate`
- `CR Text`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text`
- `CR Text`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy float`
- `PrimitiveInt`
- `Bjornulf_IfElse`
- `CR Text`
- `easy float`
- `MathExpression|pysssss`
- `LazySwitch2way`
- `MathExpression|pysssss`
- `LazySwitch2way`
- `PrimitiveInt`
- `MathExpression|pysssss`
- `LazySwitch1way`
- `easy float`
- `PrimitiveInt`
- `LazySwitch2way`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `Bjornulf_IfElse`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `LazySwitch1way`
- `LazySwitch1way`
- `MathExpression|pysssss`
- `LazySwitch1way`
- `LazySwitch1way`
- `LoadImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RandomNoise`
- `RH_Translator`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `PreviewAny`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `GetImageRangeFromBatch`
- `LTXVAudioVAEDecode` ★核心
- `easy convertAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTX2_NAG`
- `CFGNorm`
- `LayerUtility: PurgeVRAM V2`
- `CFGGuider`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVAddGuideMulti`
- `easy convertAnything`
- `CR Text`
- `CR Text Concatenate`
- `RHHiddenNodes`
- `PrimitiveInt`
- `JWInteger`
- `easy boolean`
- `easy boolean`
- `easy boolean`
- `easy boolean`
- `MarkdownNote`
- `LTXVAudioVAELoader`
- `CR Text Concatenate`
- `CR Text`
- `RH_LLMAPI_Pro_Node`
- `CR Text Concatenate`
- `CR Text`
- `MarkdownNote`
- `VAELoaderKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXVChunkFeedForward`
- `DualCLIPLoader`
- `easy boolean`
- `LazySwitch1way`
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `93`
- `height` = `20`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **79%**（129/163）

**有卡**：`CR Text`、`easy float`、`Bjornulf_IfElse`、`MathExpression|pysssss`、`LazySwitch1way`、`LazySwitch2way`、`CR Text Concatenate`、`CFGGuider`、`CLIPTextEncode`、`LoadImage`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`RandomNoise`、`RH_Translator`、`VAEDecodeTiled`、`VHS_VideoCombine`、`LTXVLatentUpsampler`、`ManualSigmas`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`GetImageRangeFromBatch`、`LTXVAudioVAEDecode`、`easy convertAnything`、`LTX2_NAG`、`CFGNorm`、`LayerUtility: PurgeVRAM V2`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVAddGuideMulti`、`RHHiddenNodes`、`JWInteger`、`easy boolean`、`LTXVAudioVAELoader`、`RH_LLMAPI_Pro_Node`、`VAELoaderKJ`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LTXVChunkFeedForward`、`DualCLIPLoader`、`LTXVConditioning`、`CheckpointLoaderSimple`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、CFGNorm、KSamplerSelect
