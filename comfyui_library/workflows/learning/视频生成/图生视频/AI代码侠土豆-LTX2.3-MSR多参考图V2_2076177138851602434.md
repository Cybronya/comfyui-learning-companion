---
key: 视频生成/图生视频/AI代码侠土豆-LTX2.3-MSR多参考图V2_2076177138851602434.json
name: AI代码侠土豆-LTX2.3-MSR多参考图V2_2076177138851602434.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2076177138851602434.json
hash: b81c57303b25cb47
coverage: 0.461538
learned_at: 2026-10-15 22:41:29
nodes: [LTXAVTextEncoderLoader, SetNode, KSamplerSelect, ManualSigmas, SetNode, GetNode, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetNode, SetNode, GetNode, GetNode, LTXVAudioVAEDecode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, SetNode, SetNode, SetNode, SetNode, SimpleMath+, GetNode, GetNode, GetNode, GetNode, CM_FloatToInt, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, LTXVCropGuides, GetNode, GetNode, GetNode, SetNode, GetNode, ImageResizeKJv2, VAEDecode, easy cleanGpuUsed, GetNode, GetNode, GetNode, SetNode, PrimitiveFloat, ImageResizeKJv2, LoadImage, ImageResizeKJv2, SetNode, ImageResizeKJv2, LoadImage, SetNode, GetNode, GetNode, Label (rgthree), CFGGuider, TTResolutionSelector, SetNode, RandomNoise, LowVRAMCheckpointLoader, LiconMSR, LTXVAudioVAELoader, LTXAddVideoICLoRAGuide, SetNode, LTXVConditioning, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, LTX2_NAG, LTXICLoRALoaderModelOnly, Label (rgthree), LoadImage, LoadImage, LoadImage, INTConstant, VHS_VideoCombine, ImageResizeKJv2, SetNode, Text, PromptRelayEncode, SetNode, Text, SetNode, GetNode, GetNode, GetNode, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 24, "width": 121}
---

# 视频生成/图生视频/AI代码侠土豆-LTX2.3-MSR多参考图V2_2076177138851602434.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2076177138851602434.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（91 个）：
- `LTXAVTextEncoderLoader`
- `SetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
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
- `SetNode`
- `SetNode`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveFloat`
- `ImageResizeKJv2`
- `LoadImage`
- `ImageResizeKJv2`
- `SetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `Label (rgthree)`
- `CFGGuider`
- `TTResolutionSelector`
- `SetNode`
- `RandomNoise`
- `LowVRAMCheckpointLoader` ★核心
- `LiconMSR`
- `LTXVAudioVAELoader`
- `LTXAddVideoICLoRAGuide`
- `SetNode`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTX2_NAG`
- `LTXICLoRALoaderModelOnly` ★核心
- `Label (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `INTConstant`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `SetNode`
- `Text`
- `PromptRelayEncode`
- `SetNode`
- `Text`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **46%**（42/91）

**有卡**：`LTXAVTextEncoderLoader`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`SimpleMath+`、`CM_FloatToInt`、`LTXVCropGuides`、`ImageResizeKJv2`、`VAEDecode`、`easy cleanGpuUsed`、`LoadImage`、`Label (rgthree)`、`CFGGuider`、`TTResolutionSelector`、`RandomNoise`、`LowVRAMCheckpointLoader`、`LiconMSR`、`LTXVAudioVAELoader`、`LTXAddVideoICLoRAGuide`、`LTXVConditioning`、`CLIPTextEncode`、`LTX2_NAG`、`LTXICLoRALoaderModelOnly`、`INTConstant`、`VHS_VideoCombine`、`Text`、`PromptRelayEncode`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
