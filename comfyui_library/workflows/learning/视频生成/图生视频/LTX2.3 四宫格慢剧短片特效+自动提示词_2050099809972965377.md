---
key: 视频生成/图生视频/LTX2.3 四宫格慢剧短片特效+自动提示词_2050099809972965377.json
name: LTX2.3 四宫格慢剧短片特效+自动提示词_2050099809972965377.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2050099809972965377.json
hash: a3a825666cc8d4f7
coverage: 0.560748
learned_at: 2026-10-15 22:37:17
nodes: [SetNode, SetNode, SetNode, Int, Note, TTResolutionSelector, LoadImage, CR Text Replace, ShowText|pysssss, easy showAnything, LTXVAudioVAELoader, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, SimpleMath+, SimpleMath+, SimpleMath+, GetNode, easy showAnything, easy showAnything, SetNode, SetNode, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, SetNode, SetNode, SetNode, GetNode, CLIPTextEncode, SetNode, RandomNoise, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, ImageScaleBy, LTXVImgToVideoConditionOnly, ManualSigmas, LTXVConcatAVLatent, LTXVLatentUpsampler, GetNode, SamplerCustomAdvanced, KSamplerSelect, CFGGuider, ManualSigmas, RandomNoise, LTXVSeparateAVLatent, LTXVAudioVAEDecode, GetNode, GetNode, VHS_VideoCombine, SetNode, easy showAnything, SetNode, PrimitiveFloat, Text, Text, easy convertAnything, SetNode, SetNode, GetNode, GetNode, CM_FloatToInt, FloatConstant, GetNode, ComfyMathExpression, CLIPTextEncode, Text, Text, GetNode, VAEDecodeTiled, GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, SimpleMath+, ImageResizeKJv2, GuHaiAutoImageSplit, PreviewImage, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, SetNode, MarkdownNote, RH_LLMAPI_Pro_Node, MarkdownNote, MarkdownNote, LTXVConditioning, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, GetNode, GetNode, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, LTXVEmptyLatentAudio, CR Text, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 四宫格慢剧短片特效+自动提示词_2050099809972965377.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2050099809972965377.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（107 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `Note`
- `TTResolutionSelector`
- `LoadImage`
- `CR Text Replace`
- `ShowText|pysssss`
- `easy showAnything`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `GetNode`
- `easy showAnything`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `ImageScaleBy`
- `LTXVImgToVideoConditionOnly`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `CFGGuider`
- `ManualSigmas`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `easy showAnything`
- `SetNode`
- `PrimitiveFloat`
- `Text`
- `Text`
- `easy convertAnything`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CM_FloatToInt`
- `FloatConstant`
- `GetNode`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `Text`
- `Text`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SimpleMath+`
- `ImageResizeKJv2`
- `GuHaiAutoImageSplit`
- `PreviewImage`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `SetNode`
- `MarkdownNote`
- `RH_LLMAPI_Pro_Node`
- `MarkdownNote`
- `MarkdownNote`
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `CR Text`
- `CR Text`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **56%**（60/107）

**有卡**：`Int`、`TTResolutionSelector`、`LoadImage`、`CR Text Replace`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`SimpleMath+`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`ImageScaleBy`、`LTXVImgToVideoConditionOnly`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`Text`、`easy convertAnything`、`CM_FloatToInt`、`FloatConstant`、`ComfyMathExpression`、`VAEDecodeTiled`、`ImageResizeKJv2`、`GuHaiAutoImageSplit`、`ImageFromBatch+`、`RH_LLMAPI_Pro_Node`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplaceKJ`、`LTXVEmptyLatentAudio`、`CR Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
