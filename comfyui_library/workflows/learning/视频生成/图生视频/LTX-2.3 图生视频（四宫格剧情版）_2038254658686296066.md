---
key: 视频生成/图生视频/LTX-2.3 图生视频（四宫格剧情版）_2038254658686296066.json
name: LTX-2.3 图生视频（四宫格剧情版）_2038254658686296066.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2038254658686296066.json
hash: 3ffec9b2b167cda4
coverage: 0.576471
learned_at: 2026-10-15 22:36:01
nodes: [LTXVAudioVAEDecode, PrimitiveFloat, LTXAVTextEncoderLoader, GetNode, SimpleMath+, SetNode, SetNode, GetNode, GetNode, CheckpointLoaderSimple, SetNode, LTXVAudioVAELoader, SetNode, GetNode, SamplerCustomAdvanced, CFGGuider, KSamplerSelect, GetNode, GetNode, SetNode, LTXVLatentUpsampler, GetNode, GetNode, GetNode, CFGGuider, KSamplerSelect, ManualSigmas, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, LTXVConcatAVLatent, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, LatentUpscaleModelLoader, LTXVConcatAVLatent, LTXVEmptyLatentAudio, ImageScaleBy, RandomNoise, CLIPTextEncode, CLIPTextEncode, ManualSigmas, LoraLoaderModelOnly, SetNode, VAEDecodeTiled, GetNode, FloatConstant, LTXVConditioning, easy showAnything, GetNode, GetNode, GetNode, GetNode, Int, PreviewImage, GuHaiAutoImageSplit, TTResolutionSelector, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageResizeKJv2, ImageFromBatch+, ImageResizeKJv2, ImageResizeKJv2, SetNode, SetNode, SetNode, ImageResizeKJv2, Reroute, Reroute, SetNode, SetNode, SetNode, RH_LLMAPI_Pro_Node, Text, VHS_VideoCombine, LoadImage, CM_FloatToInt, ComfyMathExpression, LTXVImgToVideoInplaceKJ]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.3 图生视频（四宫格剧情版）_2038254658686296066.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038254658686296066.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（85 个）：
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveFloat`
- `LTXAVTextEncoderLoader`
- `GetNode`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `LTXVAudioVAELoader`
- `SetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
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
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LatentUpscaleModelLoader`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `ImageScaleBy`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `FloatConstant`
- `LTXVConditioning`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `PreviewImage`
- `GuHaiAutoImageSplit`
- `TTResolutionSelector`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `Reroute`
- `Reroute`
- `SetNode`
- `SetNode`
- `SetNode`
- `RH_LLMAPI_Pro_Node`
- `Text`
- `VHS_VideoCombine`
- `LoadImage`
- `CM_FloatToInt`
- `ComfyMathExpression`
- `LTXVImgToVideoInplaceKJ`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **58%**（49/85）

**有卡**：`LTXVAudioVAEDecode`、`LTXAVTextEncoderLoader`、`SimpleMath+`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`SamplerCustomAdvanced`、`CFGGuider`、`KSamplerSelect`、`LTXVLatentUpsampler`、`ManualSigmas`、`LTXVImgToVideoConditionOnly`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`RandomNoise`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`LTXVEmptyLatentAudio`、`ImageScaleBy`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`VAEDecodeTiled`、`FloatConstant`、`LTXVConditioning`、`Int`、`GuHaiAutoImageSplit`、`TTResolutionSelector`、`ImageFromBatch+`、`ImageResizeKJv2`、`RH_LLMAPI_Pro_Node`、`Text`、`VHS_VideoCombine`、`LoadImage`、`CM_FloatToInt`、`ComfyMathExpression`、`LTXVImgToVideoInplaceKJ`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
