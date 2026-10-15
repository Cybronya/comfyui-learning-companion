---
key: 视频生成/文生视频/LTX-2.3 批量化漫剧 20宫格 直出1分钟视频_2046021811200069633.json
name: LTX-2.3 批量化漫剧 20宫格 直出1分钟视频_2046021811200069633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3 批量化漫剧 20宫格 直出1分钟视频_2046021811200069633.json
hash: 2cf51f8a3ab74eed
coverage: 0.588785
learned_at: 2026-10-15 22:44:39
nodes: [SetNode, SetNode, SimpleMath+, SetNode, INTConstant, GetNode, PrimitiveFloat, SetNode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, SetNode, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, SetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, GetNode, CR Float To Integer, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, VAELoader, LatentUpscaleModelLoader, SetNode, VAELoaderKJ, SetNode, SetNode, SetNode, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, LTXVCropGuides, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, LTXVConditioning, GetNode, easy cleanGpuUsed, DualCLIPLoader, SetNode, GetNode, GetNode, TTResolutionSelector, easy indexAnything, easy indexAnything, LTXVAudioVAEDecode, easy cleanGpuUsed, GetNode, SDVM Image List Repeat, easy lengthAnything, SetNode, SetNode, SetNode, GuHaiAutoImageSplit, PreviewImage, LTXVAddGuideMulti, ShowText|pysssss, easy showAnything, PreviewImage, Reroute, Reroute, Reroute, Reroute, Reroute, VAEDecodeTiled, easy batchAnything, easy isNone, EmptyAudio, AudioConcat, easy forLoopStart, easy forLoopEnd, VHS_VideoCombine, easy promptList, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Text, Text, Text, Text, Text, UNETLoader, UNETLoader, If ANY execute A else B, RH_LLMAPI_Pro_Node, Text, ImageFromBatch+, Int]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX-2.3 批量化漫剧 20宫格 直出1分钟视频_2046021811200069633.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3 批量化漫剧 20宫格 直出1分钟视频_2046021811200069633.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（107 个）：
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `INTConstant`
- `GetNode`
- `PrimitiveFloat`
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
- `GetNode`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `GetNode`
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
- `PreviewImage`
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
- `EmptyAudio`
- `AudioConcat`
- `easy forLoopStart`
- `easy forLoopEnd`
- `VHS_VideoCombine`
- `easy promptList`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Text`
- `Text`
- `Text`
- `Text`
- `Text`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `If ANY execute A else B`
- `RH_LLMAPI_Pro_Node`
- `Text`
- `ImageFromBatch+`
- `Int`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **59%**（63/107）

**有卡**：`SimpleMath+`、`INTConstant`、`ImageResizeKJv2`、`ImageFromBatch+`、`CR Float To Integer`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`VAELoader`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`easy cleanGpuUsed`、`DualCLIPLoader`、`TTResolutionSelector`、`easy indexAnything`、`LTXVAudioVAEDecode`、`SDVM Image List Repeat`、`easy lengthAnything`、`GuHaiAutoImageSplit`、`LTXVAddGuideMulti`、`VAEDecodeTiled`、`easy batchAnything`、`easy isNone`、`EmptyAudio`、`AudioConcat`、`easy forLoopStart`、`easy forLoopEnd`、`VHS_VideoCombine`、`easy promptList`、`LoadImage`、`Text`、`UNETLoader`、`If ANY execute A else B`、`RH_LLMAPI_Pro_Node`、`Int`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
