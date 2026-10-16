---
key: 视频生成/图生视频/opsv-LTX2.3-4帧合一剧情_2050847417603502081.json
name: opsv-LTX2.3-4帧合一剧情_2050847417603502081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2050847417603502081.json
hash: 3d7ec594cf87f345
coverage: 0.646018
learned_at: 2026-10-15 22:37:20
nodes: [GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, MultiTextConcatenate, RH_Utils, GetNode, Text, CR Text Replace, PrimitiveFloat, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, easy showAnything, GuHaiAutoImageSplit, Reroute, CLIPTextEncode, GetNode, LTXVConditioning, CFGGuider, KSamplerSelect, ManualSigmas, GetNode, KSamplerSelect, ManualSigmas, RandomNoise, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, ImageScaleBy, GetNode, GetNode, LTXVLatentUpsampler, GetNode, ImageResizeKJv2, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, LTXAVTextEncoderLoader, CLIPTextEncode, GetNode, GetNode, ComfyMathExpression, CM_FloatToInt, FloatConstant, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVEmptyLatentAudio, LTXVAudioVAELoader, CheckpointLoaderSimple, LoraLoaderModelOnly, SetNode, SetNode, SetNode, LatentUpscaleModelLoader, SetNode, EmptyLTXVLatentVideo, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, LoadImage, LoadImage, LoadImage, RH_LLMAPI_Pro_Node, CR Text, SaveImage, RH_Nano_Banana2_Image2Image, CR Text, easy showAnything, Fast Groups Bypasser (rgthree), PreviewImage, Fast Groups Bypasser (rgthree), Label (rgthree), SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SimpleMath+, GetNode, GetNode, VAEDecodeTiled, VHS_VideoCombine, Label (rgthree), TTResolutionSelector, LoadImage, Int, LoadImage, LoadImage, LoadImage, LoadImage, ImageStitch, ImageStitch, ImageStitch, LTXVAudioVAEDecode, VHS_VideoCombine, CustomAddLabel, RH_LLMAPI_Pro_Node, Text, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/opsv-LTX2.3-4帧合一剧情_2050847417603502081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2050847417603502081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（113 个）：
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `MultiTextConcatenate`
- `RH_Utils`
- `GetNode`
- `Text`
- `CR Text Replace`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `easy showAnything`
- `GuHaiAutoImageSplit`
- `Reroute`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LTXVConditioning`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `ImageScaleBy`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `ImageResizeKJv2`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `CM_FloatToInt`
- `FloatConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `CR Text`
- `SaveImage`
- `RH_Nano_Banana2_Image2Image`
- `CR Text`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `Label (rgthree)`
- `TTResolutionSelector`
- `LoadImage`
- `Int`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageStitch`
- `ImageStitch`
- `ImageStitch`
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `CustomAddLabel`
- `RH_LLMAPI_Pro_Node`
- `Text`
- `Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **65%**（73/113）

**有卡**：`ImageResizeKJv2`、`MultiTextConcatenate`、`RH_Utils`、`Text`、`CR Text Replace`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`GuHaiAutoImageSplit`、`CLIPTextEncode`、`LTXVConditioning`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVImgToVideoConditionOnly`、`LTXVConcatAVLatent`、`ImageScaleBy`、`LTXVLatentUpsampler`、`ImageFromBatch+`、`LTXAVTextEncoderLoader`、`ComfyMathExpression`、`CM_FloatToInt`、`FloatConstant`、`LTXVEmptyLatentAudio`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplaceKJ`、`LoadImage`、`RH_LLMAPI_Pro_Node`、`CR Text`、`SaveImage`、`RH_Nano_Banana2_Image2Image`、`Label (rgthree)`、`SimpleMath+`、`VAEDecodeTiled`、`VHS_VideoCombine`、`TTResolutionSelector`、`Int`、`ImageStitch`、`LTXVAudioVAEDecode`、`CustomAddLabel`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
