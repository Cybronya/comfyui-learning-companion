---
key: 视频生成/图生视频/LTX-2.3 20宫格(2.0升级版)无限时长可调整_2051228355147644930.json
name: LTX-2.3 20宫格(2.0升级版)无限时长可调整_2051228355147644930.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2051228355147644930.json
hash: f84bb01b99724441
coverage: 0.696429
learned_at: 2026-10-15 22:37:21
nodes: [SetNode, SetNode, SimpleMath+, SetNode, INTConstant, GetNode, SetNode, GetNode, GetNode, GetNode, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, CR Float To Integer, RandomNoise, KSamplerSelect, GetNode, GetNode, SamplerCustomAdvanced, LTXVSeparateAVLatent, SetNode, easy indexAnything, GetNode, easy lengthAnything, SetNode, SetNode, SetNode, PreviewImage, easy batchAnything, easy isNone, If ANY execute A else B, EmptyAudio, AudioConcat, easy forLoopStart, VAELoader, SetNode, VAELoaderKJ, SetNode, DualCLIPLoader, PrimitiveFloat, easy promptList, LTXVConcatAVLatent, EmptyLTXVLatentVideo, SetNode, GetObjectFromJson, GetNode, GetNode, ManualSigmas, GetObjectFromJson, GetObjectFromJson, LatentUpscaleModelLoader, SetNode, easy indexAnything, ShowText|pysssss, GetNode, easy forLoopEnd, GetNode, Reroute, Reroute, Reroute, Reroute, LTXVEmptyLatentAudio, CFGGuider, LTXVCropGuides, LTXVConditioning, Light-Tool: DeserializeJsonString, SDVM Image List Repeat, PreviewImage, GuHaiAutoImageSplit, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, CLIPTextEncode, VAEDecodeTiled, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, GetTextFromJson, GetTextFromJson, GetTextFromJson, easy cleanGpuUsed, UNETLoader, UNETLoader, VHS_VideoCombine, Text, Text, Text, Text, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, PromptRelayEncode, LTXVAddGuideMulti, TTResolutionSelector, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Int, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.3 20宫格(2.0升级版)无限时长可调整_2051228355147644930.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2051228355147644930.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（112 个）：
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `INTConstant`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `CR Float To Integer`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `SetNode`
- `easy indexAnything`
- `GetNode`
- `easy lengthAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `easy batchAnything`
- `easy isNone`
- `If ANY execute A else B`
- `EmptyAudio`
- `AudioConcat`
- `easy forLoopStart`
- `VAELoader`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `DualCLIPLoader`
- `PrimitiveFloat`
- `easy promptList`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `GetObjectFromJson`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `GetObjectFromJson`
- `GetObjectFromJson`
- `LatentUpscaleModelLoader`
- `SetNode`
- `easy indexAnything`
- `ShowText|pysssss`
- `GetNode`
- `easy forLoopEnd`
- `GetNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVEmptyLatentAudio` ★核心
- `CFGGuider`
- `LTXVCropGuides`
- `LTXVConditioning`
- `Light-Tool: DeserializeJsonString`
- `SDVM Image List Repeat`
- `PreviewImage`
- `GuHaiAutoImageSplit`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `GetTextFromJson`
- `GetTextFromJson`
- `GetTextFromJson`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `Text`
- `Text`
- `Text`
- `Text`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PromptRelayEncode`
- `LTXVAddGuideMulti`
- `TTResolutionSelector`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Int`
- `Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **70%**（78/112）

**有卡**：`SimpleMath+`、`INTConstant`、`ImageFromBatch+`、`CR Float To Integer`、`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`easy indexAnything`、`easy lengthAnything`、`easy batchAnything`、`easy isNone`、`If ANY execute A else B`、`EmptyAudio`、`AudioConcat`、`easy forLoopStart`、`VAELoader`、`VAELoaderKJ`、`DualCLIPLoader`、`easy promptList`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`GetObjectFromJson`、`ManualSigmas`、`LatentUpscaleModelLoader`、`easy forLoopEnd`、`LTXVEmptyLatentAudio`、`CFGGuider`、`LTXVCropGuides`、`LTXVConditioning`、`Light-Tool: DeserializeJsonString`、`SDVM Image List Repeat`、`GuHaiAutoImageSplit`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`VAEDecodeTiled`、`ImageResizeKJv2`、`GetTextFromJson`、`easy cleanGpuUsed`、`UNETLoader`、`VHS_VideoCombine`、`Text`、`LoraLoaderModelOnly`、`PromptRelayEncode`、`LTXVAddGuideMulti`、`TTResolutionSelector`、`LoadImage`、`Int`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
