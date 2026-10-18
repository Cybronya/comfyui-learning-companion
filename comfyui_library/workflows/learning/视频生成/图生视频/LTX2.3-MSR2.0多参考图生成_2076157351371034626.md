---
key: 视频生成/图生视频/LTX2.3-MSR2.0多参考图生成_2076157351371034626.json
name: LTX2.3-MSR2.0多参考图生成_2076157351371034626.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-MSR2.0多参考图生成_2076157351371034626.json
hash: d14ce9b816ec5f7d
coverage: 0.465116
learned_at: 2026-10-15 22:41:29
nodes: [SetNode, LTXAVTextEncoderLoader, LTXVAudioVAELoader, SetNode, CFGGuider, KSamplerSelect, ManualSigmas, CheckpointLoaderSimple, SetNode, SetNode, GetNode, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, SetNode, SetNode, SetNode, SetNode, SimpleMath+, GetNode, GetNode, GetNode, GetNode, CM_FloatToInt, GetNode, GetNode, SetNode, SetNode, GetNode, CLIPTextEncode, SetNode, SetNode, RandomNoise, LTXVCropGuides, GetNode, GetNode, GetNode, SetNode, VAEDecode, easy cleanGpuUsed, GetNode, GetNode, LTXVConditioning, PrimitiveFloat, LoadImage, SetNode, LoadImage, SetNode, GetNode, GetNode, Label (rgthree), Label (rgthree), CLIPTextEncode, ImageResizeKJv2, ImageResizeKJv2, SetNode, ImageResizeKJv2, ImageResizeKJv2, SetNode, ImageResizeKJv2, SetNode, GetNode, LoadImage, TTResolutionSelector, Text, VHS_VideoCombine, INTConstant, LoadImage, LoadImage, LiconMSR, GetNode, GetNode, GetNode, PreviewImage, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 24, "width": 121}
---

# 视频生成/图生视频/LTX2.3-MSR2.0多参考图生成_2076157351371034626.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2076157351371034626.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（86 个）：
- `SetNode`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `SetNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CM_FloatToInt`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `RandomNoise`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `PrimitiveFloat`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `LoadImage`
- `TTResolutionSelector`
- `Text`
- `VHS_VideoCombine`
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `LiconMSR`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`
- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **47%**（40/86）

**有卡**：`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`CheckpointLoaderSimple`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`SimpleMath+`、`CM_FloatToInt`、`CLIPTextEncode`、`RandomNoise`、`LTXVCropGuides`、`VAEDecode`、`easy cleanGpuUsed`、`LTXVConditioning`、`LoadImage`、`Label (rgthree)`、`ImageResizeKJv2`、`TTResolutionSelector`、`Text`、`VHS_VideoCombine`、`INTConstant`、`LiconMSR`、`LTXAddVideoICLoRAGuide`、`LTXICLoRALoaderModelOnly`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
