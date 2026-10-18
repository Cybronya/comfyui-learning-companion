---
key: 视频生成/图生视频/ltx-2.3-图生视频-多图参考版_2038430942880079873.json
name: ltx-2.3-图生视频-多图参考版_2038430942880079873.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/ltx-2.3-图生视频-多图参考版_2038430942880079873.json
hash: 86e8856469233b67
coverage: 0.821918
learned_at: 2026-10-15 22:36:02
nodes: [CLIPTextEncode, LTXVConditioning, CLIPTextEncode, EmptyLTXVLatentVideo, LTXVConcatAVLatent, CR Text, easy showAnything, CR Text, easy showAnything, easy showAnything, easy showAnything, CR Text, easy showAnything, easy float, easy float, easy float, PrimitiveInt, easy float, easy float, PrimitiveInt, easy float, PrimitiveInt, Bjornulf_IfElse, Bjornulf_IfElse, Bjornulf_IfElse, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, MathExpression|pysssss, LazySwitch1way, LTXVEmptyLatentAudio, PrimitiveInt, PrimitiveInt, LazySwitch1way, MathExpression|pysssss, MathExpression|pysssss, LazySwitch1way, LazySwitch1way, LazySwitch1way, LazySwitch2way, LazySwitch1way, MathExpression|pysssss, CR Text Concatenate, CR Text, CR Text Concatenate, CR Text, CR Text Concatenate, CR Text Concatenate, CR Text, CR Text Concatenate, CR Text Concatenate, CR Text, CR Text, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, MathExpression|pysssss, ImpactSwitch, LazySwitch1way, PrimitiveInt, LoadImage, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, JWInteger, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy float, PrimitiveInt, Bjornulf_IfElse, CR Text, RandomNoise, LazySwitch2way, easy float, MathExpression|pysssss, LazySwitch2way, MathExpression|pysssss, LazySwitch2way, LazySwitch1way, easy boolean, VHS_VideoCombine, easy boolean, LoadImage, easy boolean, LoadImage, easy boolean, LoadImage, easy boolean, LoadImage, LTXVAddGuideMulti, CFGGuider, MathExpression|pysssss, MathExpression|pysssss, LTXVAudioVAELoader, VAELoaderKJ, DualCLIPLoader, PathchSageAttentionKJ, CheckpointLoaderSimple, LoraLoaderModelOnly, KSamplerSelect, LTX2SamplingPreviewOverride, CR Text Concatenate, CR Text Concatenate, LazySwitch1way, LazySwitch1way, easy boolean, CR Text, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ManualSigmas, easy convertAnything, easy convertAnything, PrimitiveInt, LTXVAudioVAEDecode, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, VAEDecodeTiled, SamplerCustomAdvanced, LayerUtility: PurgeVRAM V2, RTXVideoSuperResolution, LTXVSeparateAVLatent, GetImageRangeFromBatch, PreviewAny, CR Text, LoraLoaderModelOnly, RH_LLMAPI_Pro_Node, DapaoGeminiInstructionZhenzhenNode, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 20, "width": 93}
---

# 视频生成/图生视频/ltx-2.3-图生视频-多图参考版_2038430942880079873.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038430942880079873.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（146 个）：
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `CR Text`
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
- `easy float`
- `PrimitiveInt`
- `Bjornulf_IfElse`
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
- `LTXVEmptyLatentAudio` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `LazySwitch1way`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `LazySwitch1way`
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
- `CR Text Concatenate`
- `MathExpression|pysssss`
- `ImpactSwitch`
- `LazySwitch1way`
- `PrimitiveInt`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `JWInteger`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy float`
- `PrimitiveInt`
- `Bjornulf_IfElse`
- `CR Text`
- `RandomNoise`
- `LazySwitch2way`
- `easy float`
- `MathExpression|pysssss`
- `LazySwitch2way`
- `MathExpression|pysssss`
- `LazySwitch2way`
- `LazySwitch1way`
- `easy boolean`
- `VHS_VideoCombine`
- `easy boolean`
- `LoadImage`
- `easy boolean`
- `LoadImage`
- `easy boolean`
- `LoadImage`
- `easy boolean`
- `LoadImage`
- `LTXVAddGuideMulti`
- `CFGGuider`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `LTXVAudioVAELoader`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `PathchSageAttentionKJ`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `LTX2SamplingPreviewOverride`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `LazySwitch1way`
- `LazySwitch1way`
- `easy boolean`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ManualSigmas`
- `easy convertAnything`
- `easy convertAnything`
- `PrimitiveInt`
- `LTXVAudioVAEDecode` ★核心
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecodeTiled` ★核心
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `RTXVideoSuperResolution`
- `LTXVSeparateAVLatent`
- `GetImageRangeFromBatch`
- `PreviewAny`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `RH_LLMAPI_Pro_Node`
- `DapaoGeminiInstructionZhenzhenNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`

## 关键参数

- `width` = `93`
- `height` = `20`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **82%**（120/146）

**有卡**：`CLIPTextEncode`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`CR Text`、`easy float`、`Bjornulf_IfElse`、`MathExpression|pysssss`、`LazySwitch1way`、`LTXVEmptyLatentAudio`、`LazySwitch2way`、`CR Text Concatenate`、`LoadImage`、`JWInteger`、`RandomNoise`、`easy boolean`、`VHS_VideoCombine`、`LTXVAddGuideMulti`、`CFGGuider`、`LTXVAudioVAELoader`、`VAELoaderKJ`、`DualCLIPLoader`、`PathchSageAttentionKJ`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`KSamplerSelect`、`LTX2SamplingPreviewOverride`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`ManualSigmas`、`easy convertAnything`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`SamplerCustomAdvanced`、`LayerUtility: PurgeVRAM V2`、`RTXVideoSuperResolution`、`LTXVSeparateAVLatent`、`GetImageRangeFromBatch`、`RH_LLMAPI_Pro_Node`、`DapaoGeminiInstructionZhenzhenNode`、`VAELoader`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
