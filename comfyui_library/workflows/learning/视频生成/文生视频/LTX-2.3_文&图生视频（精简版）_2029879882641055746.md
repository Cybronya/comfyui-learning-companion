---
key: 视频生成/文生视频/LTX-2.3_文&图生视频（精简版）_2029879882641055746.json
name: LTX-2.3_文&图生视频（精简版）_2029879882641055746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3_文&图生视频（精简版）_2029879882641055746.json
hash: 0a61aa2ccdc6eda2
coverage: 0.55
learned_at: 2026-10-15 22:44:42
nodes: [LTXVAudioVAEDecode, PrimitiveFloat, CLIPTextEncode, GetNode, CLIPTextEncode, SimpleMath+, SetNode, SetNode, GetNode, GetNode, LTXVPreprocess, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, GetNode, GetNode, CM_FloatToInt, GetNode, CheckpointLoaderSimple, SetNode, LTXVAudioVAELoader, SetNode, GetNode, GetNode, easy cleanGpuUsed, GetNode, GetNode, LTXVConditioning, SamplerCustomAdvanced, CFGGuider, RandomNoise, GetNode, KSamplerSelect, ManualSigmas, GetNode, LTXVSeparateAVLatent, GetNode, ImageResizeKJv2, SetNode, SetNode, SetNode, PrimitiveBoolean, SetNode, LoraLoaderModelOnly, SetNode, TTResolutionSelector, VAEDecodeTiled, GetNode, RH_LLMAPI_Pro_Node, easy showAnything, VHS_VideoCombine, LoadImage, Text, Int, LTXAVTextEncoderLoader, TextGenerateLTX2Prompt, PreviewAny, DualCLIPLoader, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX-2.3_文&图生视频（精简版）_2029879882641055746.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3_文&图生视频（精简版）_2029879882641055746.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（60 个）：
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveFloat`
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
- `GetNode`
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
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveBoolean`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `TTResolutionSelector`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `RH_LLMAPI_Pro_Node`
- `easy showAnything`
- `VHS_VideoCombine`
- `LoadImage`
- `Text`
- `Int`
- `LTXAVTextEncoderLoader`
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

覆盖率 **55%**（33/60）

**有卡**：`LTXVAudioVAEDecode`、`CLIPTextEncode`、`SimpleMath+`、`LTXVPreprocess`、`LTXVImgToVideoConditionOnly`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CM_FloatToInt`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`easy cleanGpuUsed`、`LTXVConditioning`、`SamplerCustomAdvanced`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`LTXVSeparateAVLatent`、`ImageResizeKJv2`、`PrimitiveBoolean`、`LoraLoaderModelOnly`、`TTResolutionSelector`、`VAEDecodeTiled`、`RH_LLMAPI_Pro_Node`、`VHS_VideoCombine`、`LoadImage`、`Text`、`Int`、`LTXAVTextEncoderLoader`、`TextGenerateLTX2Prompt`、`DualCLIPLoader`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
