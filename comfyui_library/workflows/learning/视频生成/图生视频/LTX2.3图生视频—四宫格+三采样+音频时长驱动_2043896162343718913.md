---
key: 视频生成/图生视频/LTX2.3图生视频—四宫格+三采样+音频时长驱动_2043896162343718913.json
name: LTX2.3图生视频—四宫格+三采样+音频时长驱动_2043896162343718913.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3图生视频—四宫格+三采样+音频时长驱动_2043896162343718913.json
hash: 7e6504846835b56d
coverage: 0.623853
learned_at: 2026-10-15 22:36:34
nodes: [LTXAVTextEncoderLoader, GetNode, CheckpointLoaderSimple, SetNode, LTXVAudioVAELoader, SetNode, GetNode, GetNode, GetNode, LatentUpscaleModelLoader, LTXVEmptyLatentAudio, SetNode, GetNode, GetNode, GetNode, PreviewImage, GuHaiAutoImageSplit, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, SetNode, SetNode, Reroute, Reroute, CM_FloatToInt, LTXVImgToVideoInplaceKJ, CFGGuider, RandomNoise, VAEDecodeTiled, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, ManualSigmas, KSamplerSelect, LTXVConcatAVLatent, SetNode, LTXVLatentUpsampler, GetNode, GetNode, GetNode, LTXVAudioVAEDecode, SaveAudio, RandomNoise, CFGGuider, ManualSigmas, LTXVConcatAVLatent, GetNode, LTXVAudioVAEDecode, SaveAudio, VHS_VideoCombine, GetNode, LTXVImgToVideoConditionOnly, GetNode, GetNode, GetNode, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, GetNode, GetNode, EmptyLTXVLatentVideo, LoadAudio, SetNode, Audio Duration (mtb), SetNode, SimpleCalculatorKJ, easy showAnything, RH_LLMAPI_Pro_Node, ShowAnything|Mie, PrimitiveInt, SamplerCustomAdvanced, LoadImage, SetReserveVRAM, SamplerCustomAdvanced, SamplerCustomAdvanced, CFGGuider, ManualSigmas, LTXVConcatAVLatent, RandomNoise, PurgeVRAM_UTK, LoraLoaderModelOnly, LTXVSeparateAVLatent, PurgeVRAM_UTK, PurgeVRAM_UTK, LTXVSeparateAVLatent, LTXVSeparateAVLatent, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, TTResolutionSelector, GetNode, SetNode, SetNode, easy mathInt, easy mathInt, ImageResizeKJv2, SetNode, SetNode, Text, PrimitiveFloat, CLIPTextEncode, GetNode, GetNode, LTX2_NAG, LTXVConditioning, CLIPTextEncode, KSamplerSelect, KSamplerSelect]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3图生视频—四宫格+三采样+音频时长驱动_2043896162343718913.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2043896162343718913.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（109 个）：
- `LTXAVTextEncoderLoader`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `LTXVAudioVAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LatentUpscaleModelLoader`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `GuHaiAutoImageSplit`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `SetNode`
- `SetNode`
- `Reroute`
- `Reroute`
- `CM_FloatToInt`
- `LTXVImgToVideoInplaceKJ`
- `CFGGuider`
- `RandomNoise`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `SaveAudio`
- `RandomNoise`
- `CFGGuider`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `SaveAudio`
- `VHS_VideoCombine`
- `GetNode`
- `LTXVImgToVideoConditionOnly`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoConditionOnly`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LoadAudio`
- `SetNode`
- `Audio Duration (mtb)`
- `SetNode`
- `SimpleCalculatorKJ`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `ShowAnything|Mie`
- `PrimitiveInt`
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `SetReserveVRAM`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `PurgeVRAM_UTK`
- `LoraLoaderModelOnly` ★核心
- `LTXVSeparateAVLatent`
- `PurgeVRAM_UTK`
- `PurgeVRAM_UTK`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `TTResolutionSelector`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy mathInt`
- `easy mathInt`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `Text`
- `PrimitiveFloat`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `LTX2_NAG`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **62%**（68/109）

**有卡**：`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`LTXVEmptyLatentAudio`、`GuHaiAutoImageSplit`、`ImageFromBatch+`、`CM_FloatToInt`、`LTXVImgToVideoInplaceKJ`、`CFGGuider`、`RandomNoise`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ManualSigmas`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`SaveAudio`、`VHS_VideoCombine`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`LoadAudio`、`Audio Duration (mtb)`、`SimpleCalculatorKJ`、`RH_LLMAPI_Pro_Node`、`ShowAnything|Mie`、`SamplerCustomAdvanced`、`LoadImage`、`SetReserveVRAM`、`PurgeVRAM_UTK`、`LoraLoaderModelOnly`、`LTXVSeparateAVLatent`、`ImageResizeKJv2`、`TTResolutionSelector`、`easy mathInt`、`Text`、`CLIPTextEncode`、`LTX2_NAG`、`LTXVConditioning`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
