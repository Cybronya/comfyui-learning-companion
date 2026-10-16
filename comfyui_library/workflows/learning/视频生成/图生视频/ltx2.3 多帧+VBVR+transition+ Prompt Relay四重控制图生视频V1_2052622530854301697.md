---
key: 视频生成/图生视频/ltx2.3 多帧+VBVR+transition+ Prompt Relay四重控制图生视频V1_2052622530854301697.json
name: ltx2.3 多帧+VBVR+transition+ Prompt Relay四重控制图生视频V1_2052622530854301697.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2052622530854301697.json
hash: ab2b96d08ffa3043
coverage: 0.460227
learned_at: 2026-10-15 22:37:30
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, ManualSigmas, ManualSigmas, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, RandomNoise, GetNode, GetNode, VAEDecodeTiled, GetNode, GetNode, LTXVCropGuides, LTXVSeparateAVLatent, LatentUpscaleModelLoader, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, GetNode, SetNode, SetNode, SetNode, LTXVSeparateAVLatent, SetNode, GetNode, SetNode, KSamplerSelect, SamplerCustomAdvanced, GetNode, CFGGuider, LTXVCropGuides, CFGGuider, GetNode, CLIPTextEncode, ConditioningZeroOut, SetNode, MelBandRoFormerSampler, SetNode, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, PrimitiveFloat, GetNode, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, GetNode, ComfyMathExpression, ComfyMathExpression, GetNode, GetNode, GetNode, VAELoader, GetNode, GetNode, INTConstant, INTConstant, DualCLIPLoader, VAELoader, VAELoaderKJ, MelBandRoFormerModelLoader, EmptyLTXVLatentVideo, PrimitiveFloat, LTX2SamplingPreviewOverride, ResizeImagesByLongerEdge, LTXVLatentUpsampler, LTXVConcatAVLatent, LTXVConditioning, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, LTXVScheduler, ResizeImageMaskNode, GetNode, GetNode, GetNode, GetNode, ManualSigmas, SamplerCustomAdvanced, LTX2MemoryEfficientSageAttentionPatch, LTXVChunkFeedForward, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveInt, ResizeImageMaskNode, LTXVPreprocess, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, SolidMask, LTXVAudioVAEEncode, PrimitiveNode, INTConstant, INTConstant, PrimitiveFloat, LTXVEmptyLatentAudio, RandomNoise, LTXVConcatAVLatent, SetLatentNoiseMask, GetNode, ComfySwitchNode, INTConstant, GetNode, LTXVPreprocess, GetNode, SetNode, LTXVPreprocess, ResizeImageMaskNode, GetNode, LTX2AttentionTunerPatch, SetNode, ComfySwitchNode, SetNode, GetNode, SimpleCalculatorKJ, SetNode, TrimAudioDuration, GetNode, SetNode, LTXVPreprocess, GetNode, GetNode, GetNode, ComfyMathExpression, ComfyMathExpression, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVAddGuideMulti, LTXVAddGuideMulti, GetNode, Int, Int, Int, PrimitiveInt, SetNode, VHS_VideoCombine, LoadAudio, PromptRelayEncodeTimeline, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 385}
---

# 视频生成/图生视频/ltx2.3 多帧+VBVR+transition+ Prompt Relay四重控制图生视频V1_2052622530854301697.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052622530854301697.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（176 个）：
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
- `SetNode`
- `SetNode`
- `GetNode`
- `ManualSigmas`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `GetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `CFGGuider`
- `LTXVCropGuides`
- `CFGGuider`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `MelBandRoFormerModelLoader`
- `EmptyLTXVLatentVideo`
- `PrimitiveFloat`
- `LTX2SamplingPreviewOverride`
- `ResizeImagesByLongerEdge`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVScheduler`
- `ResizeImageMaskNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTX2MemoryEfficientSageAttentionPatch`
- `LTXVChunkFeedForward`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `PrimitiveNode`
- `INTConstant`
- `INTConstant`
- `PrimitiveFloat`
- `LTXVEmptyLatentAudio` ★核心
- `RandomNoise`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `GetNode`
- `ComfySwitchNode`
- `INTConstant`
- `GetNode`
- `LTXVPreprocess`
- `GetNode`
- `SetNode`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `GetNode`
- `LTX2AttentionTunerPatch`
- `SetNode`
- `ComfySwitchNode`
- `SetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `SetNode`
- `TrimAudioDuration`
- `GetNode`
- `SetNode`
- `LTXVPreprocess`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`
- `GetNode`
- `Int`
- `Int`
- `Int`
- `PrimitiveInt`
- `SetNode`
- `VHS_VideoCombine`
- `LoadAudio`
- `PromptRelayEncodeTimeline`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心

## 关键参数

- `width` = `385`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **46%**（81/176）

**有卡**：`ManualSigmas`、`KSamplerSelect`、`RandomNoise`、`VAEDecodeTiled`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`CFGGuider`、`CLIPTextEncode`、`ConditioningZeroOut`、`MelBandRoFormerSampler`、`LTXVAudioVAEDecode`、`ComfyMathExpression`、`VAELoader`、`INTConstant`、`DualCLIPLoader`、`VAELoaderKJ`、`MelBandRoFormerModelLoader`、`EmptyLTXVLatentVideo`、`LTX2SamplingPreviewOverride`、`ResizeImagesByLongerEdge`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`LTXVConditioning`、`LTXVScheduler`、`ResizeImageMaskNode`、`LTX2MemoryEfficientSageAttentionPatch`、`LTXVChunkFeedForward`、`LoadImage`、`LTXVPreprocess`、`SolidMask`、`LTXVAudioVAEEncode`、`LTXVEmptyLatentAudio`、`SetLatentNoiseMask`、`LTX2AttentionTunerPatch`、`SimpleCalculatorKJ`、`TrimAudioDuration`、`LTXVAddGuideMulti`、`Int`、`VHS_VideoCombine`、`LoadAudio`、`PromptRelayEncodeTimeline`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
