---
key: 视频生成/图生视频/小Seedance， 连环画视频，短视频 Ltx2.3 自带音效_2037892741253832706.json
name: 小Seedance， 连环画视频，短视频 Ltx2.3 自带音效_2037892741253832706.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/小Seedance， 连环画视频，短视频 Ltx2.3 自带音效_2037892741253832706.json
hash: 6b10e2b830364666
coverage: 0.567568
learned_at: 2026-10-15 22:35:59
nodes: [GetNode, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CR Float To Integer, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, CLIPTextEncode, GetNode, GetNode, GetNode, SamplerCustomAdvanced, CLIPTextEncode, LTXVConditioning, easy cleanGpuUsed, easy cleanGpuUsed, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ImageFromBatch+, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, INTConstant, RH_LLMAPI_Pro_Node, RH_LLMAPI_Pro_Node, DualCLIPLoader, SetNode, VAELoader, VAELoaderKJ, SetNode, LatentUpscaleModelLoader, SetNode, UNETLoader, SetNode, GuHaiAutoImageSplit, ImageFromBatch+, ImageFromBatch+, SetNode, SetNode, SetNode, SetNode, PreviewImage, SimpleMath+, SetNode, GetNode, VHS_VideoCombine, LoadImage, Text, easy showAnything, TwoWaySwitch, LTXVAddGuideMulti, VAEDecodeTiled, PrimitiveFloat, SetNode, GetNode, LTXVCropGuides, GetNode, LTXVSeparateAVLatent, GetNode, easy showAnything, SetNode, PreviewImage, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/小Seedance， 连环画视频，短视频 Ltx2.3 自带音效_2037892741253832706.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037892741253832706.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Float To Integer`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `INTConstant`
- `RH_LLMAPI_Pro_Node`
- `RH_LLMAPI_Pro_Node`
- `DualCLIPLoader`
- `SetNode`
- `VAELoader`
- `VAELoaderKJ`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `UNETLoader` ★核心
- `SetNode`
- `GuHaiAutoImageSplit`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `SimpleMath+`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `LoadImage`
- `Text`
- `easy showAnything`
- `TwoWaySwitch`
- `LTXVAddGuideMulti`
- `VAEDecodeTiled` ★核心
- `PrimitiveFloat`
- `SetNode`
- `GetNode`
- `LTXVCropGuides`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `easy showAnything`
- `SetNode`
- `PreviewImage`
- `Note`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **57%**（42/74）

**有卡**：`LTXVAudioVAEDecode`、`CR Float To Integer`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`LTXVConditioning`、`easy cleanGpuUsed`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageFromBatch+`、`INTConstant`、`RH_LLMAPI_Pro_Node`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`UNETLoader`、`GuHaiAutoImageSplit`、`SimpleMath+`、`VHS_VideoCombine`、`LoadImage`、`Text`、`TwoWaySwitch`、`LTXVAddGuideMulti`、`VAEDecodeTiled`、`LTXVCropGuides`、`LTXVSeparateAVLatent`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
