---
key: 视频生成/图生视频/四宫格-LTX-2.3 图生视频（全面优化版）_2037715284160684033.json
name: 四宫格-LTX-2.3 图生视频（全面优化版）_2037715284160684033.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2037715284160684033.json
hash: 128108967f26ec2f
coverage: 0.583333
learned_at: 2026-10-15 22:35:58
nodes: [SetNode, SetNode, SimpleMath+, SetNode, INTConstant, GetNode, PrimitiveFloat, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, SetNode, GuHaiAutoImageSplit, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, SetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, GetNode, CR Float To Integer, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LatentUpscaleModelLoader, VAELoaderKJ, DualCLIPLoader, SetNode, SetNode, SetNode, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, LTXVCropGuides, LTXVAddGuideMulti, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, LTXVConditioning, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, VAEDecodeTiled, ImageFromBatch+, VHS_VideoCombine, ImageResizeKJv2, TTResolutionSelector, SetNode, easy showAnything, PreviewImage, RH_LLMAPI_Pro_Node, Text, LoadImage, RH_LLMAPI_Pro_Node, easy showAnything, Fast Groups Bypasser (rgthree), VAELoader, SetNode, RHHiddenNodes, PrimitiveNode, LoadImage, LoadImage, LoadImage, CR Text, LoadImage, RH_Nano_Banana2_Gemini31Flash, SaveImage, Fast Groups Bypasser (rgthree), UNETLoader, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/四宫格-LTX-2.3 图生视频（全面优化版）_2037715284160684033.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037715284160684033.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（84 个）：
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
- `GuHaiAutoImageSplit`
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
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `TTResolutionSelector`
- `SetNode`
- `easy showAnything`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `Text`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `VAELoader`
- `SetNode`
- `RHHiddenNodes`
- `PrimitiveNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `LoadImage`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **58%**（49/84）

**有卡**：`SimpleMath+`、`INTConstant`、`LTXVAudioVAEDecode`、`ImageResizeKJv2`、`GuHaiAutoImageSplit`、`ImageFromBatch+`、`CR Float To Integer`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVCropGuides`、`LTXVAddGuideMulti`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`VHS_VideoCombine`、`TTResolutionSelector`、`RH_LLMAPI_Pro_Node`、`Text`、`LoadImage`、`VAELoader`、`RHHiddenNodes`、`CR Text`、`RH_Nano_Banana2_Gemini31Flash`、`SaveImage`、`UNETLoader`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
