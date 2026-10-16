---
key: 视频生成/图生视频/LTX-2.3首尾帧（双采高动态版）_2042066721300815873.json
name: LTX-2.3首尾帧（双采高动态版）_2042066721300815873.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2042066721300815873.json
hash: 177210830ac16f5d
coverage: 0.573333
learned_at: 2026-10-15 22:36:24
nodes: [LTXVAudioVAEDecode, PrimitiveFloat, LTXAVTextEncoderLoader, CLIPTextEncode, GetNode, CLIPTextEncode, SimpleMath+, SetNode, GetNode, GetNode, GetNode, CM_FloatToInt, CheckpointLoaderSimple, SetNode, LTXVAudioVAELoader, SetNode, GetNode, LTXVConditioning, SamplerCustomAdvanced, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, GetNode, LoraLoaderModelOnly, SetNode, LatentUpscaleModelLoader, SetNode, GetNode, CFGGuider, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, Int, EmptyLTXVLatentVideo, GetNode, GetNode, LTXVEmptyLatentAudio, GetNode, LTXVLatentUpsampler, GetNode, GetNode, LTXVImgToVideoInplaceKJ, VAEDecodeTiled, ImageResizeKJv2, SetNode, ImageConcatMulti, GetNode, GetNode, LTXVPreprocess, ImageResizeKJv2, SetNode, RandomNoise, GetNode, VHS_VideoCombine, LTXVConcatAVLatent, LTXVPreprocess, RH_LLMAPI_Pro_Node, easy showAnything, GetNode, GetNode, LTXVImgToVideoInplaceKJ, TTResolutionSelector, LoadImage, LoadImage, Text, SetNode, SetNode, SetNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.3首尾帧（双采高动态版）_2042066721300815873.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042066721300815873.json`

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
- `GetNode`
- `GetNode`
- `GetNode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `LTXVAudioVAELoader`
- `SetNode`
- `GetNode`
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `GetNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `VAEDecodeTiled` ★核心
- `ImageResizeKJv2`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `SetNode`
- `RandomNoise`
- `GetNode`
- `VHS_VideoCombine`
- `LTXVConcatAVLatent`
- `LTXVPreprocess`
- `RH_LLMAPI_Pro_Node`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `TTResolutionSelector`
- `LoadImage`
- `LoadImage`
- `Text`
- `SetNode`
- `SetNode`
- `SetNode`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **57%**（43/75）

**有卡**：`LTXVAudioVAEDecode`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`SimpleMath+`、`CM_FloatToInt`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXVConditioning`、`SamplerCustomAdvanced`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`Int`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplaceKJ`、`VAEDecodeTiled`、`ImageResizeKJv2`、`ImageConcatMulti`、`LTXVPreprocess`、`VHS_VideoCombine`、`RH_LLMAPI_Pro_Node`、`TTResolutionSelector`、`LoadImage`、`Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
