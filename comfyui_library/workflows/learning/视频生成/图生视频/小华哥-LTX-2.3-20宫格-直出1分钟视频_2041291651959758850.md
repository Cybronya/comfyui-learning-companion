---
key: 视频生成/图生视频/小华哥-LTX-2.3-20宫格-直出1分钟视频_2041291651959758850.json
name: 小华哥-LTX-2.3-20宫格-直出1分钟视频_2041291651959758850.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/小华哥-LTX-2.3-20宫格-直出1分钟视频_2041291651959758850.json
hash: 127a92ceb2d15f3d
coverage: 0.584906
learned_at: 2026-10-15 22:36:18
nodes: [SetNode, SetNode, SimpleMath+, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, SetNode, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, SetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, GetNode, CR Float To Integer, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, VAELoader, LatentUpscaleModelLoader, SetNode, VAELoaderKJ, SetNode, SetNode, SetNode, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, LTXVCropGuides, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, GetNode, RH_LLMAPI_Pro_Node, easy cleanGpuUsed, DualCLIPLoader, SetNode, GetNode, GetNode, TTResolutionSelector, easy indexAnything, easy indexAnything, LTXVAudioVAEDecode, easy cleanGpuUsed, GetNode, SDVM Image List Repeat, easy lengthAnything, SetNode, SetNode, SetNode, GuHaiAutoImageSplit, LTXVAddGuideMulti, ShowText|pysssss, easy showAnything, PreviewImage, Reroute, Reroute, Reroute, Reroute, Reroute, VAEDecodeTiled, easy batchAnything, easy isNone, If ANY execute A else B, EmptyAudio, AudioConcat, Text, easy forLoopEnd, VHS_VideoCombine, easy promptList, UNETLoader, UNETLoader, Text, Text, Text, Text, Text, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PreviewImage, GetNode, INTConstant, PrimitiveFloat, easy forLoopStart, LTXVConditioning]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/小华哥-LTX-2.3-20宫格-直出1分钟视频_2041291651959758850.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041291651959758850.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（106 个）：
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SetNode`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Float To Integer`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `VAELoader`
- `LatentUpscaleModelLoader`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `GetNode`
- `RH_LLMAPI_Pro_Node`
- `easy cleanGpuUsed`
- `DualCLIPLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `TTResolutionSelector`
- `easy indexAnything`
- `easy indexAnything`
- `LTXVAudioVAEDecode` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `SDVM Image List Repeat`
- `easy lengthAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `GuHaiAutoImageSplit`
- `LTXVAddGuideMulti`
- `ShowText|pysssss`
- `easy showAnything`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAEDecodeTiled` ★核心
- `easy batchAnything`
- `easy isNone`
- `If ANY execute A else B`
- `EmptyAudio`
- `AudioConcat`
- `Text`
- `easy forLoopEnd`
- `VHS_VideoCombine`
- `easy promptList`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Text`
- `Text`
- `Text`
- `Text`
- `Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `GetNode`
- `INTConstant`
- `PrimitiveFloat`
- `easy forLoopStart`
- `LTXVConditioning`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **58%**（62/106）

**有卡**：`SimpleMath+`、`ImageResizeKJv2`、`ImageFromBatch+`、`CR Float To Integer`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`VAELoader`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`RH_LLMAPI_Pro_Node`、`easy cleanGpuUsed`、`DualCLIPLoader`、`TTResolutionSelector`、`easy indexAnything`、`LTXVAudioVAEDecode`、`SDVM Image List Repeat`、`easy lengthAnything`、`GuHaiAutoImageSplit`、`LTXVAddGuideMulti`、`VAEDecodeTiled`、`easy batchAnything`、`easy isNone`、`If ANY execute A else B`、`EmptyAudio`、`AudioConcat`、`Text`、`easy forLoopEnd`、`VHS_VideoCombine`、`easy promptList`、`UNETLoader`、`LoadImage`、`INTConstant`、`easy forLoopStart`、`LTXVConditioning`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
