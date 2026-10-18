---
key: 视频生成/图生视频/LTX-2.3 漫剧视频V2.0（四宫格-单采极速版）_2041770093574627329.json
name: LTX-2.3 漫剧视频V2.0（四宫格-单采极速版）_2041770093574627329.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3 漫剧视频V2.0（四宫格-单采极速版）_2041770093574627329.json
hash: fa5460d67df483f1
coverage: 0.561644
learned_at: 2026-10-15 22:36:22
nodes: [SetNode, SetNode, SimpleMath+, SetNode, INTConstant, GetNode, PrimitiveFloat, SetNode, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, SetNode, GuHaiAutoImageSplit, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, SetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, GetNode, CR Float To Integer, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, VAELoader, LatentUpscaleModelLoader, SetNode, VAELoaderKJ, SetNode, DualCLIPLoader, SetNode, SetNode, SetNode, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, LTXVCropGuides, LTXVAddGuideMulti, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, LTXVConditioning, GetNode, easy showAnything, VHS_VideoCombine, PreviewImage, TTResolutionSelector, RH_LLMAPI_Pro_Node, easy cleanGpuUsed, easy cleanGpuUsed, VAEDecodeTiled, UNETLoader, LoadImage, RHHiddenNodes, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.3 漫剧视频V2.0（四宫格-单采极速版）_2041770093574627329.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041770093574627329.json`

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
- `LTXVAddGuideMulti`
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
- `UNETLoader` ★核心
- `LoadImage`
- `RHHiddenNodes`
- `Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **56%**（41/73）

**有卡**：`SimpleMath+`、`INTConstant`、`LTXVAudioVAEDecode`、`ImageResizeKJv2`、`GuHaiAutoImageSplit`、`ImageFromBatch+`、`CR Float To Integer`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`VAELoader`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVCropGuides`、`LTXVAddGuideMulti`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`VHS_VideoCombine`、`TTResolutionSelector`、`RH_LLMAPI_Pro_Node`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`UNETLoader`、`LoadImage`、`RHHiddenNodes`、`Text`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
