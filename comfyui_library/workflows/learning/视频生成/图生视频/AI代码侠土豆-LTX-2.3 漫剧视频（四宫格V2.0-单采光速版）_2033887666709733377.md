---
key: 视频生成/图生视频/AI代码侠土豆-LTX-2.3 漫剧视频（四宫格V2.0-单采光速版）_2033887666709733377.json
name: AI代码侠土豆-LTX-2.3 漫剧视频（四宫格V2.0-单采光速版）_2033887666709733377.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AI代码侠土豆-LTX-2.3 漫剧视频（四宫格V2.0-单采光速版）_2033887666709733377.json
hash: 6c7fad11840f082f
coverage: 0.561644
learned_at: 2026-10-15 22:35:42
nodes: [SetNode, SetNode, SimpleMath+, SetNode, INTConstant, GetNode, PrimitiveFloat, SetNode, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, SetNode, GuHaiAutoImageSplit, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, SetNode, SetNode, ImageResizeKJv2, SetNode, CR Float To Integer, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, VAELoader, LatentUpscaleModelLoader, SetNode, VAELoaderKJ, SetNode, DualCLIPLoader, SetNode, SetNode, SetNode, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, LTXVCropGuides, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, LTXVConditioning, GetNode, easy showAnything, VHS_VideoCombine, PreviewImage, TTResolutionSelector, RH_LLMAPI_Pro_Node, easy cleanGpuUsed, easy cleanGpuUsed, VAEDecodeTiled, LoadImage, Text, UNETLoader, RHHiddenNodes, GetNode, GetNode, GetNode, GetNode, LTXVAddGuideMulti]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/AI代码侠土豆-LTX-2.3 漫剧视频（四宫格V2.0-单采光速版）_2033887666709733377.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033887666709733377.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `INTConstant`
- `GetNode`
- `PrimitiveFloat`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SetNode`
- `GuHaiAutoImageSplit`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `CR Float To Integer`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `VAELoader`
- `LatentUpscaleModelLoader`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
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
- `easy showAnything`
- `VHS_VideoCombine`
- `PreviewImage`
- `TTResolutionSelector`
- `RH_LLMAPI_Pro_Node`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `LoadImage`
- `Text`
- `UNETLoader` ★核心
- `RHHiddenNodes`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAddGuideMulti`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **56%**（41/73）

**有卡**：`SimpleMath+`、`INTConstant`、`LTXVAudioVAEDecode`、`ImageResizeKJv2`、`GuHaiAutoImageSplit`、`ImageFromBatch+`、`CR Float To Integer`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`VAELoader`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`VHS_VideoCombine`、`TTResolutionSelector`、`RH_LLMAPI_Pro_Node`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`LoadImage`、`Text`、`UNETLoader`、`RHHiddenNodes`、`LTXVAddGuideMulti`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
