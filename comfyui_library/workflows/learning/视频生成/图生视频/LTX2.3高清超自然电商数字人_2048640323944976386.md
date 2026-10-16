---
key: 视频生成/图生视频/LTX2.3高清超自然电商数字人_2048640323944976386.json
name: LTX2.3高清超自然电商数字人_2048640323944976386.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2048640323944976386.json
hash: 48295de6a3ab32d8
coverage: 0.444444
learned_at: 2026-10-15 22:37:10
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, LTXVConcatAVLatent, GetNode, SetNode, GetNode, GetNode, GetNode, MelBandRoFormerModelLoader, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, VAELoaderKJ, VAELoaderKJ, GetNode, SetNode, SetNode, GetNode, LTXVImgToVideoInplaceKJ, GetNode, KSamplerSelect, LTXVSeparateAVLatent, MelBandRoFormerSampler, ManualSigmas, GetNode, MathExpression|pysssss, easy showAnything, SolidMask, VAEDecodeTiled, DiffusionModelLoaderKJ, SetNode, ImageResizeKJv2, PreviewImage, LTXVAudioVAEEncode, SetLatentNoiseMask, MathExpression|pysssss, Audio Duration (mtb), SetNode, SamplerCustom, GetNode, GetNode, LTXVConditioning, SetNode, GetNode, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, DualCLIPLoader, easy cleanGpuUsed, LoadImage, VHS_VideoCombine, Note, LoadAudio, Float, Note, Note, Int, Int, TTResolutionSelector, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, PromptRelayEncode, GetNode, Float, SetNode, GetNode, CLIPTextEncode, Text, Text, Text, AudioCrop]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3高清超自然电商数字人_2048640323944976386.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2048640323944976386.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（90 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MelBandRoFormerModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `MelBandRoFormerSampler` ★核心
- `ManualSigmas`
- `GetNode`
- `MathExpression|pysssss`
- `easy showAnything`
- `SolidMask`
- `VAEDecodeTiled` ★核心
- `DiffusionModelLoaderKJ`
- `SetNode`
- `ImageResizeKJv2`
- `PreviewImage`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `MathExpression|pysssss`
- `Audio Duration (mtb)`
- `SetNode`
- `SamplerCustom` ★核心
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `SetNode`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `easy cleanGpuUsed`
- `LoadImage`
- `VHS_VideoCombine`
- `Note`
- `LoadAudio`
- `Float`
- `Note`
- `Note`
- `Int`
- `Int`
- `TTResolutionSelector`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `PromptRelayEncode`
- `GetNode`
- `Float`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `Text`
- `Text`
- `Text`
- `AudioCrop`

## 知识

覆盖率 **44%**（40/90）

**有卡**：`LTXVConcatAVLatent`、`MelBandRoFormerModelLoader`、`EmptyLTXVLatentVideo`、`VAELoaderKJ`、`LTXVImgToVideoInplaceKJ`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`MelBandRoFormerSampler`、`ManualSigmas`、`MathExpression|pysssss`、`SolidMask`、`VAEDecodeTiled`、`DiffusionModelLoaderKJ`、`ImageResizeKJv2`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`Audio Duration (mtb)`、`SamplerCustom`、`LTXVConditioning`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`easy cleanGpuUsed`、`LoadImage`、`VHS_VideoCombine`、`LoadAudio`、`Float`、`Int`、`TTResolutionSelector`、`PromptRelayEncode`、`CLIPTextEncode`、`Text`、`AudioCrop`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler、LTXVConcatAVLatent、LTXVSeparateAVLatent
