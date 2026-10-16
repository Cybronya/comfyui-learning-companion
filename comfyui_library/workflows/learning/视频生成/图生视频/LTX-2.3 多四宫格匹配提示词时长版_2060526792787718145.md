---
key: 视频生成/图生视频/LTX-2.3 多四宫格匹配提示词时长版_2060526792787718145.json
name: LTX-2.3 多四宫格匹配提示词时长版_2060526792787718145.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2060526792787718145.json
hash: 88c07e5eff918932
coverage: 0.716049
learned_at: 2026-10-15 22:38:48
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, CR Float To Integer, RandomNoise, KSamplerSelect, GetNode, GetNode, SamplerCustomAdvanced, LTXVSeparateAVLatent, SetNode, GetNode, VAELoader, SetNode, VAELoaderKJ, SetNode, DualCLIPLoader, LTXVConcatAVLatent, EmptyLTXVLatentVideo, SetNode, GetNode, GetNode, ManualSigmas, GetObjectFromJson, LatentUpscaleModelLoader, SetNode, GetNode, Reroute, LTXVEmptyLatentAudio, CFGGuider, LTXVCropGuides, LTXVConditioning, PreviewImage, GuHaiAutoImageSplit, LTXVAudioVAEDecode, GetNode, CLIPTextEncode, VAEDecodeTiled, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, GetTextFromJson, GetTextFromJson, easy cleanGpuUsed, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PromptRelayEncode, LTXVAddGuideMulti, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, TTResolutionSelector, GetObjectFromJson, Light-Tool: DeserializeJsonString, VHS_VideoCombine, GetObjectFromJson, SetNode, PrimitiveFloat, GetTextFromJson, easy indexAnything, easy indexAnything, easy indexAnything, SimpleMath+, LoadImage, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.3 多四宫格匹配提示词时长版_2060526792787718145.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2060526792787718145.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（81 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
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
- `GetNode`
- `VAELoader`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `DualCLIPLoader`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `GetObjectFromJson`
- `LatentUpscaleModelLoader`
- `SetNode`
- `GetNode`
- `Reroute`
- `LTXVEmptyLatentAudio` ★核心
- `CFGGuider`
- `LTXVCropGuides`
- `LTXVConditioning`
- `PreviewImage`
- `GuHaiAutoImageSplit`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `GetTextFromJson`
- `GetTextFromJson`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PromptRelayEncode`
- `LTXVAddGuideMulti`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `TTResolutionSelector`
- `GetObjectFromJson`
- `Light-Tool: DeserializeJsonString`
- `VHS_VideoCombine`
- `GetObjectFromJson`
- `SetNode`
- `PrimitiveFloat`
- `GetTextFromJson`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `SimpleMath+`
- `LoadImage`
- `Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **72%**（58/81）

**有卡**：`ImageFromBatch+`、`CR Float To Integer`、`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAELoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`ManualSigmas`、`GetObjectFromJson`、`LatentUpscaleModelLoader`、`LTXVEmptyLatentAudio`、`CFGGuider`、`LTXVCropGuides`、`LTXVConditioning`、`GuHaiAutoImageSplit`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`VAEDecodeTiled`、`ImageResizeKJv2`、`GetTextFromJson`、`easy cleanGpuUsed`、`UNETLoader`、`LoraLoaderModelOnly`、`PromptRelayEncode`、`LTXVAddGuideMulti`、`easy indexAnything`、`TTResolutionSelector`、`Light-Tool: DeserializeJsonString`、`VHS_VideoCombine`、`SimpleMath+`、`LoadImage`、`Text`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
