---
key: 数字人/数字人/LTX-2.3 自动四宫格播客一致性工作流 V2.3_2038470088306728961.json
name: LTX-2.3 自动四宫格播客一致性工作流 V2.3_2038470088306728961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX-2.3 自动四宫格播客一致性工作流 V2.3_2038470088306728961.json
hash: 25fa226d57b4a041
coverage: 0.563107
learned_at: 2026-10-26 01:55:43
nodes: [LTXVAudioVAEDecode, PrimitiveFloat, LTXAVTextEncoderLoader, SetNode, SetNode, GetNode, CheckpointLoaderSimple, SetNode, LTXVAudioVAELoader, SetNode, GetNode, SamplerCustomAdvanced, CFGGuider, KSamplerSelect, GetNode, GetNode, LTXVLatentUpsampler, GetNode, GetNode, CFGGuider, KSamplerSelect, ManualSigmas, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, LTXVConcatAVLatent, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, LTXVConcatAVLatent, LTXVEmptyLatentAudio, ImageScaleBy, RandomNoise, CLIPTextEncode, ManualSigmas, VAEDecodeTiled, FloatConstant, LTXVConditioning, GetNode, GetNode, GetNode, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageResizeKJv2, ImageFromBatch+, ImageResizeKJv2, SetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, SetNode, SetNode, CM_FloatToInt, ComfyMathExpression, CLIPTextEncode, SimpleMath+, easy showAnything, SimpleMath+, SetNode, SimpleMath+, GetNode, GetNode, LTXVImgToVideoInplaceKJ, GetNode, SimpleMath+, SetNode, LatentUpscaleModelLoader, GetNode, GetNode, VHS_VideoCombine, GetNode, easy showAnything, easy showAnything, easy showAnything, TTResolutionSelector, Text, LoadImage, LoadImage, LoadImage, GuHaiAutoImageSplit, PreviewImage, GetNode, GetNode, GetNode, SetNode, GetNode, RH_LLMAPI_Pro_Node, TTResolutionSelector, GetNode, Int, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage, PrimitiveStringMultiline, RH_Nano_Banana2_Gemini31Flash, SetNode, ImageResizeKJv2]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 数字人/数字人/LTX-2.3 自动四宫格播客一致性工作流 V2.3_2038470088306728961.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX-2.3 自动四宫格播客一致性工作流 V2.3_2038470088306728961.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（103 个）：
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveFloat`
- `LTXAVTextEncoderLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `LTXVAudioVAELoader`
- `SetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVImgToVideoConditionOnly`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `ImageScaleBy`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `ManualSigmas`
- `VAEDecodeTiled` ★核心
- `FloatConstant`
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `CM_FloatToInt`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `easy showAnything`
- `SimpleMath+`
- `SetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `SimpleMath+`
- `SetNode`
- `LatentUpscaleModelLoader`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `TTResolutionSelector`
- `Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GuHaiAutoImageSplit`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `RH_LLMAPI_Pro_Node`
- `TTResolutionSelector`
- `GetNode`
- `Int`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `PrimitiveStringMultiline`
- `RH_Nano_Banana2_Gemini31Flash`
- `SetNode`
- `ImageResizeKJv2`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **56%**（58/103）

**有卡**：`LTXVAudioVAEDecode`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`SamplerCustomAdvanced`、`CFGGuider`、`KSamplerSelect`、`LTXVLatentUpsampler`、`ManualSigmas`、`LTXVImgToVideoConditionOnly`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`RandomNoise`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`ImageScaleBy`、`CLIPTextEncode`、`VAEDecodeTiled`、`FloatConstant`、`LTXVConditioning`、`ImageFromBatch+`、`ImageResizeKJv2`、`CM_FloatToInt`、`ComfyMathExpression`、`SimpleMath+`、`LTXVImgToVideoInplaceKJ`、`LatentUpscaleModelLoader`、`VHS_VideoCombine`、`TTResolutionSelector`、`Text`、`LoadImage`、`GuHaiAutoImageSplit`、`RH_LLMAPI_Pro_Node`、`Int`、`LoraLoaderModelOnly`、`SaveImage`、`RH_Nano_Banana2_Gemini31Flash`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
