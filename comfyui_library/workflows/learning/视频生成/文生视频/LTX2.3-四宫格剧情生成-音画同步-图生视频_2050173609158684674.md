---
key: 视频生成/文生视频/LTX2.3-四宫格剧情生成-音画同步-图生视频_2050173609158684674.json
name: LTX2.3-四宫格剧情生成-音画同步-图生视频_2050173609158684674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-四宫格剧情生成-音画同步-图生视频_2050173609158684674.json
hash: fcb3db6a83893ebe
coverage: 0.528302
learned_at: 2026-10-11 19:49:37
nodes: [GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, MultiTextConcatenate, RH_Utils, GetNode, Text, CR Text Replace, PrimitiveFloat, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, easy showAnything, Text, GuHaiAutoImageSplit, Reroute, CLIPTextEncode, GetNode, LTXVConditioning, CFGGuider, KSamplerSelect, ManualSigmas, GetNode, KSamplerSelect, ManualSigmas, RandomNoise, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, ImageScaleBy, GetNode, GetNode, LTXVLatentUpsampler, GetNode, ImageResizeKJv2, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, LTXAVTextEncoderLoader, CLIPTextEncode, GetNode, RH_LLMAPI_Pro_Node, GetNode, ComfyMathExpression, CM_FloatToInt, FloatConstant, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVEmptyLatentAudio, LTXVAudioVAELoader, CheckpointLoaderSimple, LoraLoaderModelOnly, SetNode, SetNode, SetNode, LatentUpscaleModelLoader, SetNode, EmptyLTXVLatentVideo, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, LoadImage, LoadImage, LoadImage, RH_LLMAPI_Pro_Node, CR Text, SaveImage, RH_Nano_Banana2_Image2Image, CR Text, easy showAnything, Fast Groups Bypasser (rgthree), Text, LoadImage, PreviewImage, Fast Groups Bypasser (rgthree), Label (rgthree), SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SimpleMath+, GetNode, GetNode, VAEDecodeTiled, LTXVAudioVAEDecode, VHS_VideoCombine, VHS_VideoCombine, CustomAddLabel, Label (rgthree), Int, TTResolutionSelector]
patterns: []
missing: [CR Text, CR Text, CR Text Replace, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, Label (rgthree), Label (rgthree), SimpleMath+]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3-四宫格剧情生成-音画同步-图生视频_2050173609158684674.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-四宫格剧情生成-音画同步-图生视频_2050173609158684674.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（106 个）：
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
- `Text`
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
- `RH_LLMAPI_Pro_Node`
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
- `Text`
- `LoadImage`
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
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CustomAddLabel`
- `Label (rgthree)`
- `Int`
- `TTResolutionSelector`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **53%**（56/106）

**有卡**：`ImageResizeKJv2`、`MultiTextConcatenate`、`RH_Utils`、`Text`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`GuHaiAutoImageSplit`、`CLIPTextEncode`、`LTXVConditioning`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVImgToVideoConditionOnly`、`LTXVConcatAVLatent`、`ImageScaleBy`、`LTXVLatentUpsampler`、`LTXAVTextEncoderLoader`、`RH_LLMAPI_Pro_Node`、`ComfyMathExpression`、`CM_FloatToInt`、`FloatConstant`、`LTXVEmptyLatentAudio`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplaceKJ`、`LoadImage`、`SaveImage`、`RH_Nano_Banana2_Image2Image`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`CustomAddLabel`、`Int`、`TTResolutionSelector`

**缺卡**（10）：`CR Text`、`CR Text`、`CR Text Replace`、`ImageFromBatch+`、`ImageFromBatch+`、`ImageFromBatch+`、`ImageFromBatch+`、`Label (rgthree)`、`Label (rgthree)`、`SimpleMath+`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
