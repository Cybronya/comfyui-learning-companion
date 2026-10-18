---
key: 视频生成/图生视频/LTX-2.3 20宫格无限时长可 - for 循环 ComfyUI工作流_2058423071744282626.json
name: LTX-2.3 20宫格无限时长可 - for 循环 ComfyUI工作流_2058423071744282626.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3 20宫格无限时长可 - for 循环 ComfyUI工作流_2058423071744282626.json
hash: 8d2e3f4441f93167
coverage: 0.696429
learned_at: 2026-10-15 22:38:22
nodes: [SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, CR Float To Integer, KSamplerSelect, GetNode, GetNode, SamplerCustomAdvanced, LTXVSeparateAVLatent, SetNode, easy indexAnything, GetNode, easy lengthAnything, SetNode, SetNode, SetNode, PreviewImage, easy isNone, If ANY execute A else B, EmptyAudio, AudioConcat, easy forLoopStart, VAELoader, SetNode, VAELoaderKJ, SetNode, DualCLIPLoader, PrimitiveFloat, easy promptList, LTXVConcatAVLatent, EmptyLTXVLatentVideo, SetNode, GetNode, GetNode, GetObjectFromJson, GetObjectFromJson, LatentUpscaleModelLoader, SetNode, easy indexAnything, ShowText|pysssss, easy forLoopEnd, LTXVEmptyLatentAudio, CFGGuider, LTXVCropGuides, Light-Tool: DeserializeJsonString, SDVM Image List Repeat, PreviewImage, GuHaiAutoImageSplit, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, CLIPTextEncode, VAEDecodeTiled, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, easy cleanGpuUsed, UNETLoader, UNETLoader, VHS_VideoCombine, Text, Text, Text, Text, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, PromptRelayEncode, TTResolutionSelector, LoadImage, Text, LTXVAddGuideMulti, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, LoadImage, GetTextFromJson, GetTextFromJson, GetObjectFromJson, GetTextFromJson, LoadImage, Int, LoadImage, LoadImage, RandomNoise, ManualSigmas, LTXVConditioning, GetNode, INTConstant, SimpleMath+, SetNode, Reroute, Reroute, Reroute, Reroute, GetNode, easy batchAnything]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.3 20宫格无限时长可 - for 循环 ComfyUI工作流_2058423071744282626.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2058423071744282626.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（112 个）：
- `SetNode`
- `SetNode`
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
- `GetNode`
- `GetNode`
- `GetObjectFromJson`
- `GetObjectFromJson`
- `LatentUpscaleModelLoader`
- `SetNode`
- `easy indexAnything`
- `ShowText|pysssss`
- `easy forLoopEnd`
- `LTXVEmptyLatentAudio` ★核心
- `CFGGuider`
- `LTXVCropGuides`
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
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
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
- `TTResolutionSelector`
- `LoadImage`
- `Text`
- `LTXVAddGuideMulti`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `LoadImage`
- `GetTextFromJson`
- `GetTextFromJson`
- `GetObjectFromJson`
- `GetTextFromJson`
- `LoadImage`
- `Int`
- `LoadImage`
- `LoadImage`
- `RandomNoise`
- `ManualSigmas`
- `LTXVConditioning`
- `GetNode`
- `INTConstant`
- `SimpleMath+`
- `SetNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `GetNode`
- `easy batchAnything`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **70%**（78/112）

**有卡**：`ImageFromBatch+`、`CR Float To Integer`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`easy indexAnything`、`easy lengthAnything`、`easy isNone`、`If ANY execute A else B`、`EmptyAudio`、`AudioConcat`、`easy forLoopStart`、`VAELoader`、`VAELoaderKJ`、`DualCLIPLoader`、`easy promptList`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`GetObjectFromJson`、`LatentUpscaleModelLoader`、`easy forLoopEnd`、`LTXVEmptyLatentAudio`、`CFGGuider`、`LTXVCropGuides`、`Light-Tool: DeserializeJsonString`、`SDVM Image List Repeat`、`GuHaiAutoImageSplit`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`VAEDecodeTiled`、`ImageResizeKJv2`、`easy cleanGpuUsed`、`UNETLoader`、`VHS_VideoCombine`、`Text`、`LoraLoaderModelOnly`、`PromptRelayEncode`、`TTResolutionSelector`、`LoadImage`、`LTXVAddGuideMulti`、`GetTextFromJson`、`Int`、`RandomNoise`、`ManualSigmas`、`LTXVConditioning`、`INTConstant`、`SimpleMath+`、`easy batchAnything`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
