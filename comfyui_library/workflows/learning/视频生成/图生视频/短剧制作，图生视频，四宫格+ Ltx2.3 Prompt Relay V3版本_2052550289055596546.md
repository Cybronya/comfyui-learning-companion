---
key: 视频生成/图生视频/短剧制作，图生视频，四宫格+ Ltx2.3 Prompt Relay V3版本_2052550289055596546.json
name: 短剧制作，图生视频，四宫格+ Ltx2.3 Prompt Relay V3版本_2052550289055596546.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2052550289055596546.json
hash: 3f797a8d2294b8c1
coverage: 0.597701
learned_at: 2026-10-15 22:37:30
nodes: [LTXVAudioVAEDecode, GetNode, GetNode, GetNode, GetNode, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ImageFromBatch+, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, VAELoaderKJ, SetNode, LatentUpscaleModelLoader, SetNode, SetNode, ImageFromBatch+, GetNode, GetNode, LTXVCropGuides, GetNode, LTXVSeparateAVLatent, SetNode, LTXVAddGuideMulti, DualCLIPLoader, CLIPTextEncode, CLIPTextEncode, GetNode, VHS_VideoCombine, RH_LLMAPI_Pro_Node, VAEDecodeTiled, easy cleanGpuUsed, easy showAnything, RH_LLMAPI_Pro_Node, PreviewImage, GetNode, GetNode, CR Float To Integer, GetNode, CLIPTextEncode, easy showAnything, ImageFromBatch+, GuHaiAutoImageSplit, PreviewImage, SetNode, SetNode, SetNode, GetNode, SimpleMath+, SetNode, GetNode, SetNode, VHS_VideoCombine, UNETLoader, Note, PrimitiveFloat, SetNode, LTXVConditioning, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SetNode, SetNode, SolidMask, GetNode, LoadImage, INTConstant, INTConstant, ImpactSwitch, Note, PromptRelayEncodeTimeline, Int, Int, Int, Text, LTXICLoRALoaderModelOnly, LTXICLoRALoaderModelOnly, LTXVEmptyLatentAudio, LTXVAudioVAEEncode, SetLatentNoiseMask, LoadAudio, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/短剧制作，图生视频，四宫格+ Ltx2.3 Prompt Relay V3版本_2052550289055596546.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052550289055596546.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（87 个）：
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `VAELoaderKJ`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `SetNode`
- `ImageFromBatch+`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `LTXVAddGuideMulti`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `RH_LLMAPI_Pro_Node`
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `CR Float To Integer`
- `GetNode`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `ImageFromBatch+`
- `GuHaiAutoImageSplit`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `SetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `Note`
- `PrimitiveFloat`
- `SetNode`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `SetNode`
- `SetNode`
- `SolidMask`
- `GetNode`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `ImpactSwitch`
- `Note`
- `PromptRelayEncodeTimeline`
- `Int`
- `Int`
- `Int`
- `Text`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `LoadAudio`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **60%**（52/87）

**有卡**：`LTXVAudioVAEDecode`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageFromBatch+`、`VAELoader`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVAddGuideMulti`、`DualCLIPLoader`、`CLIPTextEncode`、`VHS_VideoCombine`、`RH_LLMAPI_Pro_Node`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`CR Float To Integer`、`GuHaiAutoImageSplit`、`SimpleMath+`、`UNETLoader`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`SolidMask`、`LoadImage`、`INTConstant`、`PromptRelayEncodeTimeline`、`Int`、`Text`、`LTXICLoRALoaderModelOnly`、`LTXVEmptyLatentAudio`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LoadAudio`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
