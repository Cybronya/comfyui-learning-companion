---
key: 图片生成/图生图/四宫格-LTX-2.3 图生视频（全面优化版）_2039716029768671234.json
name: 四宫格-LTX-2.3 图生视频（全面优化版）_2039716029768671234
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/四宫格-LTX-2.3 图生视频（全面优化版）_2039716029768671234.json
hash: 15f0bc51ebc24907
coverage: 0.581081
learned_at: 2026-10-23 12:37:22
nodes: [SetNode, SetNode, SimpleMath+, SetNode, INTConstant, GetNode, PrimitiveFloat, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, SetNode, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, CR Float To Integer, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LatentUpscaleModelLoader, VAELoaderKJ, DualCLIPLoader, SetNode, SetNode, SetNode, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, LTXVCropGuides, LTXVAddGuideMulti, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConditioning, GetNode, easy cleanGpuUsed, VAEDecodeTiled, ImageFromBatch+, VHS_VideoCombine, ImageResizeKJv2, TTResolutionSelector, SetNode, VAELoader, SetNode, RHHiddenNodes, UNETLoader, Fast Groups Bypasser (rgthree), easy cleanGpuUsed, PreviewImage, llama_cpp_model_loader, ImageResizeKJv2, llama_cpp_parameters, easy showAnything, CLIPTextEncode, GuHaiAutoImageSplit, llama_cpp_instruct_adv, LoadImage, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 图片生成/图生图/四宫格-LTX-2.3 图生视频（全面优化版）_2039716029768671234.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/四宫格-LTX-2.3 图生视频（全面优化版）_2039716029768671234.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `INTConstant`
- `GetNode`
- `PrimitiveFloat`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SetNode`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Float To Integer`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `DualCLIPLoader`
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
- `LTXVAddGuideMulti`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConditioning`
- `GetNode`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `TTResolutionSelector`
- `SetNode`
- `VAELoader`
- `SetNode`
- `RHHiddenNodes`
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `easy cleanGpuUsed`
- `PreviewImage`
- `llama_cpp_model_loader`
- `ImageResizeKJv2`
- `llama_cpp_parameters`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `GuHaiAutoImageSplit`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **58%**（43/74）

**有卡**：`SimpleMath+`、`INTConstant`、`LTXVAudioVAEDecode`、`ImageResizeKJv2`、`ImageFromBatch+`、`CR Float To Integer`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVCropGuides`、`LTXVAddGuideMulti`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`VHS_VideoCombine`、`TTResolutionSelector`、`VAELoader`、`RHHiddenNodes`、`UNETLoader`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`GuHaiAutoImageSplit`、`llama_cpp_instruct_adv`、`LoadImage`、`Text`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
