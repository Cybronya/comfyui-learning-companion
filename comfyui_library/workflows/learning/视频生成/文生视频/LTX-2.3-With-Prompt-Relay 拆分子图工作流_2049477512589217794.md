---
key: 视频生成/文生视频/LTX-2.3-With-Prompt-Relay 拆分子图工作流_2049477512589217794.json
name: LTX-2.3-With-Prompt-Relay 拆分子图工作流_2049477512589217794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3-With-Prompt-Relay 拆分子图工作流_2049477512589217794.json
hash: f161321f925b4b13
coverage: 0.413462
learned_at: 2026-10-10 23:00:12
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, VAEDecodeTiled, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, LTXVAudioVAEDecode, SetNode, SetLatentNoiseMask, LoadAudio, SetNode, TrimAudioDuration, PreviewAudio, LTXVAudioVAEEncode, GetNode, SetNode, PrimitiveFloat, SimpleCalculatorKJ, SimpleCalculatorKJ, SetNode, PrimitiveBoolean, INTConstant, INTConstant, INTConstant, INTConstant, Fast Groups Bypasser (rgthree), INTConstant, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, UnetLoaderGGUF, VAELoaderKJ, Any Switch (rgthree), SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVImgToVideoConditionOnly, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, RandomNoise, LTXVSeparateAVLatent, SetNode, LoraLoaderModelOnly, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, SamplerCustomAdvanced, LTXVSeparateAVLatent, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, CFGGuider, RandomNoise, GetNode, GetNode, GetNode, GetNode, GetNode, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, LTXVPreprocess, CM_FloatToInt, LTXVEmptyLatentAudio, Any Switch (rgthree), LTXVConcatAVLatent, Fast Groups Bypasser (rgthree), Any Switch (rgthree), GetNode, Any Switch (rgthree), SimpleCalculatorKJ, Note, Fast Groups Bypasser (rgthree), StringConcatenate, StringConcatenate, StringConcatenate, Note, PrimitiveStringMultiline, GetNode, easy showAnything, JWIntegerToString, JWIntegerToString, JWIntegerToString, StringConcatenate, JWIntegerToString, StringConcatenate, StringConcatenate, PrimitiveStringMultiline, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, GetNode, Fast Groups Bypasser (rgthree), GetNode, SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LatentUpscaleModelLoader, SetNode, SimpleCalculatorKJ, SimpleCalculatorKJ, SimpleCalculatorKJ, Any Switch (rgthree), Any Switch (rgthree), SimpleCalculatorKJ, SolidMask, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, SetNode, GetNode, GetNode, SetNode, VAEDecodeTiled, VHS_VideoCombine, Any Switch (rgthree), GetNode, CLIPTextEncode, GetNode, GetNode, ConditioningZeroOut, SetNode, GetNode, PromptRelayEncode, PrimitiveStringMultiline, PrimitiveStringMultiline, GetNode, GetNode, SimpleCalculatorKJ, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, VAEDecodeTiled, VHS_VideoCombine, GetNode, GetNode, LTXVLatentUpsampler, GetNode, LTXVConcatAVLatent, SetNode, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, ResizeImageMaskNode, SetNode, LoadImage, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 24, "width": 97}
---

# 视频生成/文生视频/LTX-2.3-With-Prompt-Relay 拆分子图工作流_2049477512589217794.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3-With-Prompt-Relay 拆分子图工作流_2049477512589217794.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Other

**节点**（208 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `SetLatentNoiseMask`
- `LoadAudio`
- `SetNode`
- `TrimAudioDuration`
- `PreviewAudio`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SetNode`
- `PrimitiveFloat`
- `SimpleCalculatorKJ`
- `SimpleCalculatorKJ`
- `SetNode`
- `PrimitiveBoolean`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `UnetLoaderGGUF` ★核心
- `VAELoaderKJ`
- `Any Switch (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoConditionOnly`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoConditionOnly`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoConditionOnly`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `CM_FloatToInt`
- `LTXVEmptyLatentAudio` ★核心
- `Any Switch (rgthree)`
- `LTXVConcatAVLatent`
- `Fast Groups Bypasser (rgthree)`
- `Any Switch (rgthree)`
- `GetNode`
- `Any Switch (rgthree)`
- `SimpleCalculatorKJ`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `StringConcatenate`
- `StringConcatenate`
- `StringConcatenate`
- `Note`
- `PrimitiveStringMultiline`
- `GetNode`
- `easy showAnything`
- `JWIntegerToString`
- `JWIntegerToString`
- `JWIntegerToString`
- `StringConcatenate`
- `JWIntegerToString`
- `StringConcatenate`
- `StringConcatenate`
- `PrimitiveStringMultiline`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `SetNode`
- `SimpleCalculatorKJ`
- `SimpleCalculatorKJ`
- `SimpleCalculatorKJ`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `SimpleCalculatorKJ`
- `SolidMask`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `Any Switch (rgthree)`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `SetNode`
- `GetNode`
- `PromptRelayEncode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `GetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `ResizeImageMaskNode`
- `SetNode`
- `LoadImage`
- `Note`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **41%**（86/208）

**有卡**：`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`SetLatentNoiseMask`、`LoadAudio`、`TrimAudioDuration`、`PreviewAudio`、`LTXVAudioVAEEncode`、`SimpleCalculatorKJ`、`PrimitiveBoolean`、`INTConstant`、`VHS_VideoCombine`、`UnetLoaderGGUF`、`VAELoaderKJ`、`LTXVImgToVideoConditionOnly`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVSeparateAVLatent`、`LoraLoaderModelOnly`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`CM_FloatToInt`、`LTXVEmptyLatentAudio`、`StringConcatenate`、`JWIntegerToString`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`SolidMask`、`CLIPTextEncode`、`ConditioningZeroOut`、`PromptRelayEncode`、`ResizeImageMaskNode`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
