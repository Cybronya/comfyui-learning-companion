---
key: 音频生成/音频生成/LTX2.3 V2V时间戳控制Prompt Relay视频4D扩展_2047301031557603329.json
name: LTX2.3 V2V时间戳控制Prompt Relay视频4D扩展_2047301031557603329
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/LTX2.3 V2V时间戳控制Prompt Relay视频4D扩展_2047301031557603329.json
hash: 1f3566385e71b8b1
coverage: 0.719008
learned_at: 2026-10-18 03:04:51
nodes: [LTXVSeparateAVLatent, CFGGuider, ManualSigmas, KSamplerSelect, VAEDecodeTiled, LTXVAudioVAEDecode, ResizeImageMaskNode, Switch image [Crystools], RandomNoise, GetImageSize, Color Correct (mtb), LTXVEmptyLatentAudio, NormalizeAudioLoudness, NormalizeAudioLoudness, MarkdownNote, MarkdownNote, SetNode, LoadAudio, MarkdownNote, PreviewAudio, LTXVAudioVideoMask, LTXVAudioVAEEncode, AudioConcat, LTXVAudioVAEDecode, PreviewAudio, SetNode, Reroute, StringConcatenate, GetNode, SamplerCustomAdvanced, LTXVCropGuides, LTXVConditioning, SetNode, ConditioningZeroOut, SetNode, CM_FloatToInt, StringConcatenate, StringConcatenate, EmptyAudio, AudioConcat, SetNode, GetNode, Reroute, Reroute, easy showAnything, easy showAnything, StringConcatenate, LTXVAudioVAEEncode, LTXAddVideoICLoRAGuide, PreviewAny, JWIntegerToString, LTXVConcatAVLatent, MathExpression|pysssss, LTXVAudioVideoMask, JWIntegerToString, StringConcatenate, SimpleCalculatorKJ, SimpleCalculatorKJ, TrimAudioDuration, SimpleCalculatorKJ, SetNode, SimpleCalculatorKJ, SimpleCalculatorKJ, GetNode, GetNode, GetNode, StringConcatenate, JWIntegerToString, JWIntegerToString, ResizeImageMaskNode, CheckpointLoaderSimple, LTXVAudioVAELoader, easy ckptNames, Int, Int, Int, Int, Color Correct (mtb), PrimitiveBoolean, Switch image [Crystools], PrimitiveStringMultiline, GetNode, PromptRelayEncode, GetNode, Reroute, GetNode, CLIPTextEncode, LoraLoaderModelOnly, LTXAVTextEncoderLoader, LTXICLoRALoaderModelOnly, SetNode, Int, Int, MathExpression|pysssss, MathExpression|pysssss, PrimitiveStringMultiline, PrimitiveStringMultiline, VHS_LoadVideo, PrimitiveStringMultiline, ImageConcanate, GetNode, ImageResizeKJv2, ImagePadKJ, VHS_VideoInfo, Note, GetImageRangeFromBatch, Int, Int, MathExpression|pysssss, MathExpression|pysssss, GetNode, SimpleCalculatorKJ, LoraLoaderModelOnly, VHS_VideoCombine, ImageResizeKJv2, SetNode, ImagePadKJ, VHS_VideoCombine, PrimitiveStringMultiline, EmptyLTXVLatentVideo, MathExpression|pysssss]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "LTX-2\\ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 音频生成/音频生成/LTX2.3 V2V时间戳控制Prompt Relay视频4D扩展_2047301031557603329.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/LTX2.3 V2V时间戳控制Prompt Relay视频4D扩展_2047301031557603329.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（121 个）：
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ResizeImageMaskNode`
- `Switch image [Crystools]`
- `RandomNoise`
- `GetImageSize`
- `Color Correct (mtb)`
- `LTXVEmptyLatentAudio` ★核心
- `NormalizeAudioLoudness`
- `NormalizeAudioLoudness`
- `MarkdownNote`
- `MarkdownNote`
- `SetNode`
- `LoadAudio`
- `MarkdownNote`
- `PreviewAudio`
- `LTXVAudioVideoMask`
- `LTXVAudioVAEEncode` ★核心
- `AudioConcat`
- `LTXVAudioVAEDecode` ★核心
- `PreviewAudio`
- `SetNode`
- `Reroute`
- `StringConcatenate`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVConditioning`
- `SetNode`
- `ConditioningZeroOut`
- `SetNode`
- `CM_FloatToInt`
- `StringConcatenate`
- `StringConcatenate`
- `EmptyAudio`
- `AudioConcat`
- `SetNode`
- `GetNode`
- `Reroute`
- `Reroute`
- `easy showAnything`
- `easy showAnything`
- `StringConcatenate`
- `LTXVAudioVAEEncode` ★核心
- `LTXAddVideoICLoRAGuide`
- `PreviewAny`
- `JWIntegerToString`
- `LTXVConcatAVLatent`
- `MathExpression|pysssss`
- `LTXVAudioVideoMask`
- `JWIntegerToString`
- `StringConcatenate`
- `SimpleCalculatorKJ`
- `SimpleCalculatorKJ`
- `TrimAudioDuration`
- `SimpleCalculatorKJ`
- `SetNode`
- `SimpleCalculatorKJ`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `StringConcatenate`
- `JWIntegerToString`
- `JWIntegerToString`
- `ResizeImageMaskNode`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `easy ckptNames`
- `Int`
- `Int`
- `Int`
- `Int`
- `Color Correct (mtb)`
- `PrimitiveBoolean`
- `Switch image [Crystools]`
- `PrimitiveStringMultiline`
- `GetNode`
- `PromptRelayEncode`
- `GetNode`
- `Reroute`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `SetNode`
- `Int`
- `Int`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `VHS_LoadVideo`
- `PrimitiveStringMultiline`
- `ImageConcanate`
- `GetNode`
- `ImageResizeKJv2`
- `ImagePadKJ`
- `VHS_VideoInfo`
- `Note`
- `GetImageRangeFromBatch`
- `Int`
- `Int`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetNode`
- `SimpleCalculatorKJ`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `SetNode`
- `ImagePadKJ`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `EmptyLTXVLatentVideo`
- `MathExpression|pysssss`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `LTX-2\ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **72%**（87/121）

**有卡**：`LTXVSeparateAVLatent`、`CFGGuider`、`ManualSigmas`、`KSamplerSelect`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ResizeImageMaskNode`、`Switch image [Crystools]`、`RandomNoise`、`GetImageSize`、`Color Correct (mtb)`、`LTXVEmptyLatentAudio`、`NormalizeAudioLoudness`、`LoadAudio`、`PreviewAudio`、`LTXVAudioVideoMask`、`LTXVAudioVAEEncode`、`AudioConcat`、`StringConcatenate`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVConditioning`、`ConditioningZeroOut`、`CM_FloatToInt`、`EmptyAudio`、`LTXAddVideoICLoRAGuide`、`JWIntegerToString`、`LTXVConcatAVLatent`、`MathExpression|pysssss`、`SimpleCalculatorKJ`、`TrimAudioDuration`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`easy ckptNames`、`Int`、`PrimitiveBoolean`、`PromptRelayEncode`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`LTXICLoRALoaderModelOnly`、`VHS_LoadVideo`、`ImageConcanate`、`ImageResizeKJv2`、`ImagePadKJ`、`VHS_VideoInfo`、`GetImageRangeFromBatch`、`VHS_VideoCombine`、`EmptyLTXVLatentVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
