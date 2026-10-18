---
key: 视频生成/图生视频/Ltx2.3-Prompt Relay+Sulphur+VBVR-人物表情更丰富-四图分镜生视频加音频对口型_2057471351287537666.json
name: Ltx2.3-Prompt Relay+Sulphur+VBVR-人物表情更丰富-四图分镜生视频加音频对口型_2057471351287537666.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3-Prompt Relay+Sulphur+VBVR-人物表情更丰富-四图分镜生视频加音频对口型_2057471351287537666.json
hash: 78d1f75c61bab650
coverage: 0.465116
learned_at: 2026-10-15 22:38:13
nodes: [LTXVSeparateAVLatent, GetNode, VAELoader, SetNode, DualCLIPLoader, LTXVCropGuides, GetNode, VAEDecodeTiled, GetNode, SetNode, GetNode, SetNode, SetNode, KSamplerSelect, LTXVConcatAVLatent, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RandomNoise, GetNode, GetNode, CFGGuider, KSamplerSelect, GetNode, SetNode, LTXVConditioning, GetNode, SetNode, ComfyMathExpression, GetNode, GetNode, GetNode, ResizeImagesByLongerEdge, GetNode, GetNode, GetNode, GetNode, easy showAnything, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SolidMask, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, CFGGuider, SamplerCustomAdvanced, LTXVAudioVAEDecode, LTXVLatentUpsampler, LTXVCropGuides, LTXVAddGuideMulti, SetNode, SetNode, SetNode, SimpleCalculatorKJ, LTX2SamplingPreviewOverride, SetNode, ConditioningZeroOut, SetNode, Note, Note, Note, SetNode, INTConstant, Note, SetLatentNoiseMask, LTXVAudioVAEEncode, LTXVConcatAVLatent, SamplerCustomAdvanced, ManualSigmas, ManualSigmas, GetNode, SetNode, GetNode, LTXVAddGuideMulti, PrimitiveFloat, GetNode, GetNode, GetNode, ImageResizeKJv2, ResizeImagesByLongerEdge, LTXVPreprocess, SetNode, GetNode, GetNode, LTXVPreprocess, SetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, ResizeImagesByLongerEdge, LTXVPreprocess, SetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, ResizeImagesByLongerEdge, SetNode, LTXVPreprocess, PrimitiveInt, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, ComfyMathExpression, INTConstant, Note, TrimAudioDuration, MelBandRoFormerModelLoader, MelBandRoFormerSampler, SetNode, SetNode, ComfySwitchNode, Int, LoadImage, LoadImage, LoadImage, LoadImage, Int, Note, Int, SimpleMath+, SimpleMath+, PrimitiveInt, LoadAudio, PrimitiveNode, PromptRelayEncodeTimeline, Int, Int, Int, Int, VHS_VideoCombine, VHS_VideoCombine, SetNode, VAELoader, ComfyMathExpression, SetNode, EmptyLTXVLatentVideo, PathchSageAttentionKJ, LoraLoaderModelOnly, VAELoaderKJ, LatentUpscaleModelLoader, UNETLoader, LTX2MemoryEfficientSageAttentionPatch, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, RandomNoise, UNETLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/Ltx2.3-Prompt Relay+Sulphur+VBVR-人物表情更丰富-四图分镜生视频加音频对口型_2057471351287537666.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2057471351287537666.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（172 个）：
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAELoader`
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
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SolidMask`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `LTXVAddGuideMulti`
- `SetNode`
- `SetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `LTX2SamplingPreviewOverride`
- `SetNode`
- `ConditioningZeroOut`
- `SetNode`
- `Note`
- `Note`
- `Note`
- `SetNode`
- `INTConstant`
- `Note`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `ManualSigmas`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVAddGuideMulti`
- `PrimitiveFloat`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `LTXVPreprocess`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `INTConstant`
- `Note`
- `TrimAudioDuration`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `SetNode`
- `ComfySwitchNode`
- `Int`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Int`
- `Note`
- `Int`
- `SimpleMath+`
- `SimpleMath+`
- `PrimitiveInt`
- `LoadAudio`
- `PrimitiveNode`
- `PromptRelayEncodeTimeline`
- `Int`
- `Int`
- `Int`
- `Int`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `VAELoader`
- `ComfyMathExpression`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `LTX2MemoryEfficientSageAttentionPatch`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `UNETLoader` ★核心

## 知识

覆盖率 **47%**（80/172）

**有卡**：`LTXVSeparateAVLatent`、`VAELoader`、`DualCLIPLoader`、`LTXVCropGuides`、`VAEDecodeTiled`、`KSamplerSelect`、`LTXVConcatAVLatent`、`RandomNoise`、`CFGGuider`、`LTXVConditioning`、`ComfyMathExpression`、`ResizeImagesByLongerEdge`、`SolidMask`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`LTXVAddGuideMulti`、`SimpleCalculatorKJ`、`LTX2SamplingPreviewOverride`、`ConditioningZeroOut`、`INTConstant`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`ManualSigmas`、`ImageResizeKJv2`、`LTXVPreprocess`、`TrimAudioDuration`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`Int`、`LoadImage`、`SimpleMath+`、`LoadAudio`、`PromptRelayEncodeTimeline`、`VHS_VideoCombine`、`EmptyLTXVLatentVideo`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`UNETLoader`、`LTX2MemoryEfficientSageAttentionPatch`

**用到的条目**：VAELoader、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
