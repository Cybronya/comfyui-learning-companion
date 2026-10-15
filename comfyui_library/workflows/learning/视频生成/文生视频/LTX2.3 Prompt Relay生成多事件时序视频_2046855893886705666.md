---
key: 视频生成/文生视频/LTX2.3 Prompt Relay生成多事件时序视频_2046855893886705666.json
name: LTX2.3 Prompt Relay生成多事件时序视频_2046855893886705666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 Prompt Relay生成多事件时序视频_2046855893886705666.json
hash: dffe1717cbeb1241
coverage: 0.496689
learned_at: 2026-10-15 22:44:58
nodes: [SimpleCalculatorKJ, GetNode, GetNode, SimpleCalculatorKJ, GetNode, SimpleCalculatorKJ, GetNode, SimpleCalculatorKJ, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, UnetLoaderGGUF, DualCLIPLoaderGGUF, SetNode, SetNode, SetNode, ResizeImagesByLongerEdge, SetNode, INTConstant, INTConstant, INTConstant, SetNode, SimpleCalculatorKJ, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, LTXVSeparateAVLatent, GetNode, SetNode, SetNode, GetNode, KSamplerSelect, ManualSigmas, ManualSigmas, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, MarkdownNote, LTX2MemoryEfficientSageAttentionPatch, LTXVChunkFeedForward, LoraLoaderModelOnly, LTX2AttentionTunerPatch, LTXVPreprocess, ComfyMathExpression, GetNode, ComfyMathExpression, GetNode, GetNode, GetNode, SetNode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, SamplerCustomAdvanced, SamplerCustomAdvanced, GetNode, GetNode, LTXVLatentUpsampler, LTXVScheduler, ManualSigmas, ImageResizeKJv2, PrimitiveFloat, MarkdownNote, Reroute, Reroute, Reroute, Reroute, StringConcatenate, JWIntegerToString, SetNode, GetNode, GetNode, GetNode, KSamplerSelect, GetNode, SetNode, GetNode, LTXVConcatAVLatent, GetNode, GetNode, SetNode, LTX2SamplingPreviewOverride, GetNode, CFGGuider, GetNode, CFGGuider, CLIPTextEncode, LTXVConditioning, ConditioningZeroOut, PathchSageAttentionKJ, PrimitiveStringMultiline, PrimitiveStringMultiline, SetNode, GetNode, GetNode, GetNode, LTXVImgToVideoInplace, RandomNoise, RandomNoise, PrimitiveBoolean, UNETLoader, UNETLoader, LatentUpscaleModelLoader, DualCLIPLoader, VAELoader, VAELoaderKJ, VAELoader, INTConstant, INTConstant, PrimitiveStringMultiline, LoadImage, LoraLoaderModelOnly, easy showAnything, SetNode, JWIntegerToString, JWIntegerToString, JWIntegerToString, StringConcatenate, PrimitiveStringMultiline, LTXVImgToVideoInplace, StringConcatenate, PrimitiveStringMultiline, GetNode, GetNode, GetNode, VHS_VideoCombine, CreateVideo, SaveVideo, StringConcatenate, StringConcatenate, StringConcatenate, GetNode, PromptRelayEncode, easy showAnything, SimpleCalculatorKJ, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.3 Prompt Relay生成多事件时序视频_2046855893886705666.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 Prompt Relay生成多事件时序视频_2046855893886705666.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（151 个）：
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoaderGGUF`
- `SetNode`
- `SetNode`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `ManualSigmas`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `MarkdownNote`
- `LTX2MemoryEfficientSageAttentionPatch`
- `LTXVChunkFeedForward`
- `LoraLoaderModelOnly` ★核心
- `LTX2AttentionTunerPatch`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVScheduler`
- `ManualSigmas`
- `ImageResizeKJv2`
- `PrimitiveFloat`
- `MarkdownNote`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `StringConcatenate`
- `JWIntegerToString`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `ConditioningZeroOut`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `RandomNoise`
- `RandomNoise`
- `PrimitiveBoolean`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `INTConstant`
- `INTConstant`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `SetNode`
- `JWIntegerToString`
- `JWIntegerToString`
- `JWIntegerToString`
- `StringConcatenate`
- `PrimitiveStringMultiline`
- `LTXVImgToVideoInplace`
- `StringConcatenate`
- `PrimitiveStringMultiline`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `CreateVideo`
- `SaveVideo`
- `StringConcatenate`
- `StringConcatenate`
- `StringConcatenate`
- `GetNode`
- `PromptRelayEncode`
- `easy showAnything`
- `SimpleCalculatorKJ`
- `INTConstant`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **50%**（75/151）

**有卡**：`SimpleCalculatorKJ`、`UnetLoaderGGUF`、`DualCLIPLoaderGGUF`、`ResizeImagesByLongerEdge`、`INTConstant`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`KSamplerSelect`、`ManualSigmas`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTX2MemoryEfficientSageAttentionPatch`、`LTXVChunkFeedForward`、`LoraLoaderModelOnly`、`LTX2AttentionTunerPatch`、`LTXVPreprocess`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`LTXVScheduler`、`ImageResizeKJv2`、`StringConcatenate`、`JWIntegerToString`、`LTX2SamplingPreviewOverride`、`CFGGuider`、`CLIPTextEncode`、`LTXVConditioning`、`ConditioningZeroOut`、`PathchSageAttentionKJ`、`LTXVImgToVideoInplace`、`RandomNoise`、`PrimitiveBoolean`、`UNETLoader`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`LoadImage`、`VHS_VideoCombine`、`CreateVideo`、`SaveVideo`、`PromptRelayEncode`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
