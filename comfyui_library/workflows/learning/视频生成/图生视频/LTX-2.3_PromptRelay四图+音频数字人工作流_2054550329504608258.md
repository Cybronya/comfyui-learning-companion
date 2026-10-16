---
key: 视频生成/图生视频/LTX-2.3_PromptRelay四图+音频数字人工作流_2054550329504608258.json
name: LTX-2.3_PromptRelay四图+音频数字人工作流_2054550329504608258.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2054550329504608258.json
hash: 4f308bd544d398d3
coverage: 0.411765
learned_at: 2026-10-15 22:37:49
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, ManualSigmas, ManualSigmas, GetNode, LTX2MemoryEfficientSageAttentionPatch, LTXVChunkFeedForward, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, RandomNoise, LTXVLatentUpsampler, GetNode, GetNode, VAEDecodeTiled, GetNode, GetNode, LTXVCropGuides, LTXVSeparateAVLatent, PathchSageAttentionKJ, GetNode, LTX2AttentionTunerPatch, SetNode, SetNode, GetNode, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, LTXVSeparateAVLatent, RandomNoise, LTXVScheduler, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, GetNode, CFGGuider, LTXVCropGuides, CFGGuider, GetNode, CLIPTextEncode, ConditioningZeroOut, SetNode, SetNode, GetNode, GetNode, ComfyMathExpression, ComfyMathExpression, GetNode, GetNode, PrimitiveInt, SimpleCalculatorKJ, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, SetNode, LTXVAudioVAEDecode, VAELoader, SamplerCustomAdvanced, VAELoader, VAELoaderKJ, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, GetNode, GetNode, LTXVAudioVAEEncode, SolidMask, ComfyMathExpression, ComfyMathExpression, GetNode, GetNode, LTXVEmptyLatentAudio, SetLatentNoiseMask, ComfySwitchNode, GetNode, ResizeImagesByLongerEdge, LTXVPreprocess, ResizeImagesByLongerEdge, LTXVPreprocess, ResizeImagesByLongerEdge, LTXVPreprocess, ResizeImagesByLongerEdge, LTXVPreprocess, SetNode, SetNode, SetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, GetNode, SetNode, SimpleCalculatorKJ, VHS_VideoCombine, LTXVAddGuideMulti, SetNode, PrimitiveFloat, UNETLoader, LatentUpscaleModelLoader, DualCLIPLoader, INTConstant, INTConstant, GetNode, LTXVAddGuideMulti, GetNode, SetNode, SetNode, PrimitiveFloat, ComfyMathExpression, ComfyMathExpression, GetNode, GetNode, GetNode, LTXVConditioning, GetNode, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, LTX2SamplingPreviewOverride, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, ComfySwitchNode, MarkdownNote, MarkdownNote, SetNode, GetNode, GetNode, SetNode, SetNode, MelBandRoFormerSampler, MelBandRoFormerModelLoader, PrimitiveFloat, SetNode, EmptyLTXVLatentVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadAudio, TrimAudioDuration, PrimitiveNode, INTConstant, INTConstant, INTConstant, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PromptRelayEncodeTimeline, ResizeImageMaskNode, ResizeImageMaskNode, ResizeImageMaskNode, LoadImage, LoadImage, LoadImage, LoadImage, ResizeImageMaskNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 649}
---

# 视频生成/图生视频/LTX-2.3_PromptRelay四图+音频数字人工作流_2054550329504608258.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054550329504608258.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（204 个）：
- `SetNode`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ManualSigmas`
- `ManualSigmas`
- `GetNode`
- `LTX2MemoryEfficientSageAttentionPatch`
- `LTXVChunkFeedForward`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `PathchSageAttentionKJ`
- `GetNode`
- `LTX2AttentionTunerPatch`
- `SetNode`
- `SetNode`
- `GetNode`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `CFGGuider`
- `LTXVCropGuides`
- `CFGGuider`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `SimpleCalculatorKJ`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `VAELoaderKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `SetLatentNoiseMask`
- `ComfySwitchNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `VHS_VideoCombine`
- `LTXVAddGuideMulti`
- `SetNode`
- `PrimitiveFloat`
- `UNETLoader` ★核心
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `LTXVAddGuideMulti`
- `GetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ComfySwitchNode`
- `MarkdownNote`
- `MarkdownNote`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `PrimitiveFloat`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadAudio`
- `TrimAudioDuration`
- `PrimitiveNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PromptRelayEncodeTimeline`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResizeImageMaskNode`

## 关键参数

- `width` = `649`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **41%**（84/204）

**有卡**：`ManualSigmas`、`LTX2MemoryEfficientSageAttentionPatch`、`LTXVChunkFeedForward`、`KSamplerSelect`、`RandomNoise`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`PathchSageAttentionKJ`、`LTX2AttentionTunerPatch`、`LTXVScheduler`、`SamplerCustomAdvanced`、`CFGGuider`、`CLIPTextEncode`、`ConditioningZeroOut`、`ComfyMathExpression`、`SimpleCalculatorKJ`、`LTXVAudioVAEDecode`、`VAELoader`、`VAELoaderKJ`、`LTXVAudioVAEEncode`、`SolidMask`、`LTXVEmptyLatentAudio`、`SetLatentNoiseMask`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXVConcatAVLatent`、`VHS_VideoCombine`、`LTXVAddGuideMulti`、`UNETLoader`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`INTConstant`、`LTXVConditioning`、`LTX2SamplingPreviewOverride`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`EmptyLTXVLatentVideo`、`LoraLoaderModelOnly`、`LoadAudio`、`TrimAudioDuration`、`PromptRelayEncodeTimeline`、`ResizeImageMaskNode`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
