---
key: 视频生成/文生视频/LTX-2.3 文&图生视频（高清放大版）_2029905437574828033.json
name: LTX-2.3 文&图生视频（高清放大版）_2029905437574828033
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3 文&图生视频（高清放大版）_2029905437574828033.json
hash: 4b43d1c212c9d542
coverage: 0.56
learned_at: 2026-10-11 03:16:45
nodes: [LTXVAudioVAEDecode, PrimitiveFloat, LTXAVTextEncoderLoader, CLIPTextEncode, GetNode, CLIPTextEncode, SimpleMath+, SetNode, SetNode, GetNode, GetNode, LTXVPreprocess, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, GetNode, GetNode, CM_FloatToInt, CheckpointLoaderSimple, SetNode, LTXVAudioVAELoader, SetNode, GetNode, GetNode, easy cleanGpuUsed, GetNode, GetNode, LTXVConditioning, SamplerCustomAdvanced, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, GetNode, GetNode, ImageResizeKJv2, SetNode, SetNode, PrimitiveBoolean, SetNode, LoraLoaderModelOnly, SetNode, LatentUpscaleModelLoader, SetNode, LTXVLatentUpsampler, GetNode, SetNode, GetNode, ImageScaleBy, VAEDecodeTiled, TTResolutionSelector, GetNode, CFGGuider, KSamplerSelect, ManualSigmas, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, LTXVConcatAVLatent, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, easy showAnything, RH_LLMAPI_Pro_Node, Int, VHS_VideoCombine, Text, LoadImage, TextGenerateLTX2Prompt, PreviewAny, DualCLIPLoader, Note]
patterns: []
missing: [SimpleMath+, easy cleanGpuUsed]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX-2.3 文&图生视频（高清放大版）_2029905437574828033.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3 文&图生视频（高清放大版）_2029905437574828033.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（75 个）：
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveFloat`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `LTXVAudioVAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `PrimitiveBoolean`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `ImageScaleBy`
- `VAEDecodeTiled` ★核心
- `TTResolutionSelector`
- `GetNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVImgToVideoConditionOnly`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `Int`
- `VHS_VideoCombine`
- `Text`
- `LoadImage`
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `DualCLIPLoader`
- `Note`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **56%**（42/75）

**有卡**：`LTXVAudioVAEDecode`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`LTXVPreprocess`、`LTXVImgToVideoConditionOnly`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CM_FloatToInt`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXVConditioning`、`SamplerCustomAdvanced`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`ImageResizeKJv2`、`PrimitiveBoolean`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`ImageScaleBy`、`VAEDecodeTiled`、`TTResolutionSelector`、`LTXVSeparateAVLatent`、`RH_LLMAPI_Pro_Node`、`Int`、`VHS_VideoCombine`、`Text`、`LoadImage`、`TextGenerateLTX2Prompt`、`DualCLIPLoader`

**缺卡**（2）：`SimpleMath+`、`easy cleanGpuUsed`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
