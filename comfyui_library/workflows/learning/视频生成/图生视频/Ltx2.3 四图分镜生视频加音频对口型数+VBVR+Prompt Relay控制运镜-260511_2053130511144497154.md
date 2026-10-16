---
key: 视频生成/图生视频/Ltx2.3 四图分镜生视频加音频对口型数+VBVR+Prompt Relay控制运镜-260511_2053130511144497154.json
name: Ltx2.3 四图分镜生视频加音频对口型数+VBVR+Prompt Relay控制运镜-260511_2053130511144497154.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2053130511144497154.json
hash: 1070da33a79357d9
coverage: 0.45098
learned_at: 2026-10-15 22:37:36
nodes: [LTXVSeparateAVLatent, GetNode, PathchSageAttentionKJ, LTX2MemoryEfficientSageAttentionPatch, GetNode, GetNode, GetNode, UNETLoader, LatentUpscaleModelLoader, VAELoader, VAELoaderKJ, SetNode, DualCLIPLoader, LTXVCropGuides, GetNode, VAEDecodeTiled, GetNode, SetNode, GetNode, SetNode, SetNode, KSamplerSelect, RandomNoise, LTXVConcatAVLatent, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RandomNoise, GetNode, GetNode, CFGGuider, KSamplerSelect, GetNode, SetNode, LTXVConditioning, GetNode, SetNode, GetNode, EmptyLTXVLatentVideo, ComfyMathExpression, GetNode, ComfyMathExpression, GetNode, GetNode, ComfyMathExpression, GetNode, GetNode, ComfyMathExpression, GetNode, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, SetNode, GetNode, ResizeImagesByLongerEdge, LTXVPreprocess, SetNode, GetNode, ResizeImagesByLongerEdge, LTXVPreprocess, SetNode, GetNode, GetNode, GetNode, ResizeImagesByLongerEdge, LTXVPreprocess, SetNode, GetNode, GetNode, MelBandRoFormerSampler, PrimitiveInt, easy showAnything, GetNode, MelBandRoFormerModelLoader, SetNode, ComfySwitchNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, TrimAudioDuration, SetNode, GetNode, SetNode, SetNode, SetNode, SolidMask, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, CFGGuider, SamplerCustomAdvanced, GetNode, LTXVAudioVAEDecode, LTXVLatentUpsampler, LTXVCropGuides, LTXVAddGuideMulti, LTXVAddGuideMulti, Int, SetNode, SetNode, SetNode, ResizeImageMaskNode, ResizeImageMaskNode, LoadImage, LoadImage, LoadImage, LoadImage, ResizeImageMaskNode, GetNode, SimpleCalculatorKJ, Int, LTX2SamplingPreviewOverride, Int, INTConstant, SetNode, ConditioningZeroOut, SetNode, Note, Note, Note, SetNode, Note, Note, INTConstant, VHS_VideoCombine, Note, PrimitiveNode, LoadAudio, PrimitiveInt, PromptRelayEncodeTimeline, LoraLoaderModelOnly, VAELoader, PrimitiveFloat, SetLatentNoiseMask, LTXVAudioVAEEncode, LTXVConcatAVLatent, SamplerCustomAdvanced, ManualSigmas, ManualSigmas]
patterns: []
missing: []
---

# 视频生成/图生视频/Ltx2.3 四图分镜生视频加音频对口型数+VBVR+Prompt Relay控制运镜-260511_2053130511144497154.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053130511144497154.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（153 个）：
- `LTXVSeparateAVLatent`
- `GetNode`
- `PathchSageAttentionKJ`
- `LTX2MemoryEfficientSageAttentionPatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `LatentUpscaleModelLoader`
- `VAELoader`
- `VAELoaderKJ`
- `SetNode`
- `DualCLIPLoader`
- `LTXVCropGuides`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `GetNode`
- `SetNode`
- `LTXVConditioning`
- `GetNode`
- `SetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `PrimitiveInt`
- `easy showAnything`
- `GetNode`
- `MelBandRoFormerModelLoader`
- `SetNode`
- `ComfySwitchNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `TrimAudioDuration`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SolidMask`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResizeImageMaskNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `Int`
- `LTX2SamplingPreviewOverride`
- `Int`
- `INTConstant`
- `SetNode`
- `ConditioningZeroOut`
- `SetNode`
- `Note`
- `Note`
- `Note`
- `SetNode`
- `Note`
- `Note`
- `INTConstant`
- `VHS_VideoCombine`
- `Note`
- `PrimitiveNode`
- `LoadAudio`
- `PrimitiveInt`
- `PromptRelayEncodeTimeline`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `PrimitiveFloat`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `ManualSigmas`

## 知识

覆盖率 **45%**（69/153）

**有卡**：`LTXVSeparateAVLatent`、`PathchSageAttentionKJ`、`LTX2MemoryEfficientSageAttentionPatch`、`UNETLoader`、`LatentUpscaleModelLoader`、`VAELoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXVCropGuides`、`VAEDecodeTiled`、`KSamplerSelect`、`RandomNoise`、`LTXVConcatAVLatent`、`CFGGuider`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`TrimAudioDuration`、`SolidMask`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`LTXVAddGuideMulti`、`Int`、`LoadImage`、`SimpleCalculatorKJ`、`LTX2SamplingPreviewOverride`、`INTConstant`、`ConditioningZeroOut`、`VHS_VideoCombine`、`LoadAudio`、`PromptRelayEncodeTimeline`、`LoraLoaderModelOnly`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`ManualSigmas`

**用到的条目**：VAELoader、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
