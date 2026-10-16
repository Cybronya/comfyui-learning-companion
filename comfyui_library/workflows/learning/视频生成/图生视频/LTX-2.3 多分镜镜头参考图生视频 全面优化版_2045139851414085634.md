---
key: 视频生成/图生视频/LTX-2.3 多分镜镜头参考图生视频 全面优化版_2045139851414085634.json
name: LTX-2.3 多分镜镜头参考图生视频 全面优化版_2045139851414085634.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2045139851414085634.json
hash: 592d7a0acd60e336
coverage: 0.58427
learned_at: 2026-10-15 22:36:46
nodes: [SetNode, SetNode, SimpleMath+, SetNode, INTConstant, GetNode, PrimitiveFloat, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, SetNode, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, SetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, GetNode, CR Float To Integer, LTXVEmptyLatentAudio, LatentUpscaleModelLoader, VAELoaderKJ, DualCLIPLoader, SetNode, SetNode, SetNode, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, LTXVCropGuides, LTXVSeparateAVLatent, CLIPTextEncode, LTXVConditioning, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, ImageFromBatch+, ImageResizeKJv2, TTResolutionSelector, SetNode, easy showAnything, PreviewImage, LoadImage, RH_LLMAPI_Pro_Node, easy showAnything, Fast Groups Bypasser (rgthree), VAELoader, SetNode, RHHiddenNodes, PrimitiveNode, LoadImage, LoadImage, LoadImage, LoadImage, RH_Nano_Banana2_Gemini31Flash, SaveImage, UNETLoader, Fast Groups Bypasser (rgthree), CR Text, Fast Groups Bypasser (rgthree), VAELoader, Wan22ImageToVideoLatent, easy showAnything, CRT_UpscaleModelAdv, VAEDecodeTiled, GuHaiAutoImageSplit, LTXVAddGuideMulti, VHS_VideoCombine, Note, Text, EmptyLTXVLatentVideo, RH_LLMAPI_Pro_Node, SamplerCustomAdvanced, RandomNoise]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.3 多分镜镜头参考图生视频 全面优化版_2045139851414085634.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2045139851414085634.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（89 个）：
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
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Float To Integer`
- `LTXVEmptyLatentAudio` ★核心
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `CFGGuider`
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
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `TTResolutionSelector`
- `SetNode`
- `easy showAnything`
- `PreviewImage`
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
- `LoadImage`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `VAELoader`
- `Wan22ImageToVideoLatent`
- `easy showAnything`
- `CRT_UpscaleModelAdv`
- `VAEDecodeTiled` ★核心
- `GuHaiAutoImageSplit`
- `LTXVAddGuideMulti`
- `VHS_VideoCombine`
- `Note`
- `Text`
- `EmptyLTXVLatentVideo`
- `RH_LLMAPI_Pro_Node`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **58%**（52/89）

**有卡**：`SimpleMath+`、`INTConstant`、`LTXVAudioVAEDecode`、`ImageResizeKJv2`、`ImageFromBatch+`、`CR Float To Integer`、`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`easy cleanGpuUsed`、`TTResolutionSelector`、`LoadImage`、`RH_LLMAPI_Pro_Node`、`VAELoader`、`RHHiddenNodes`、`RH_Nano_Banana2_Gemini31Flash`、`SaveImage`、`UNETLoader`、`CR Text`、`Wan22ImageToVideoLatent`、`CRT_UpscaleModelAdv`、`VAEDecodeTiled`、`GuHaiAutoImageSplit`、`LTXVAddGuideMulti`、`VHS_VideoCombine`、`Text`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`RandomNoise`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
