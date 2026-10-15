---
key: 视频生成/文生视频/LTX23_5图生视频Gemini+VBVR+PromptRelay_2054601890872209409.json
name: LTX23_5图生视频Gemini+VBVR+PromptRelay_2054601890872209409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX23_5图生视频Gemini+VBVR+PromptRelay_2054601890872209409.json
hash: 80f88164474150b9
coverage: 0.5
learned_at: 2026-10-15 22:45:18
nodes: [GetNode, GetNode, GetNode, SetNode, GetNode, ManualSigmas, ManualSigmas, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, VAEDecodeTiled, GetNode, GetNode, SamplerCustomAdvanced, GetNode, CFGGuider, CFGGuider, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVPreprocess, SetNode, LTXVPreprocess, SetNode, LTXVPreprocess, SetNode, GetNode, GetNode, GetNode, UNETLoader, LTXVChunkFeedForward, DualCLIPLoader, VAELoader, VAELoaderKJ, VAELoader, SetNode, SetNode, SetNode, SetNode, SetNode, LTX2MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, LTX2AttentionTunerPatch, LatentUpscaleModelLoader, INTConstant, INTConstant, SetNode, SetNode, SetNode, TrimAudioDuration, SetNode, ComfySwitchNode, SetNode, PrimitiveInt, SimpleCalculatorKJ, GetNode, MelBandRoFormerSampler, SetNode, MelBandRoFormerModelLoader, EmptyLTXVLatentVideo, ComfyMathExpression, GetNode, GetNode, ComfyMathExpression, SetNode, ConditioningZeroOut, GetNode, SetNode, ComfyMathExpression, GetNode, ComfyMathExpression, SolidMask, SetLatentNoiseMask, LTXVAudioVAEEncode, GetNode, ComfyMathExpression, LTXVEmptyLatentAudio, GetNode, LTXVConcatAVLatent, RandomNoise, LTXVConditioning, GetNode, SamplerCustomAdvanced, KSamplerSelect, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, LTXVCropGuides, LTXVLatentUpsampler, GetNode, GetNode, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LTXVConcatAVLatent, GetNode, SetNode, SetNode, GetNode, SetNode, SetNode, RandomNoise, GetNode, GetNode, GetNode, LTXVCropGuides, SetNode, SetNode, LTXVAudioVAEDecode, GetNode, PrimitiveFloat, SetNode, SetNode, LTXVPreprocess, SetNode, GetNode, PrimitiveFloat, SetNode, PrimitiveInt, ResizeLongestToNode, ResizeLongestToNode, ResizeLongestToNode, ResizeLongestToNode, LTXVPreprocess, GetNode, GetNode, LTXVScheduler, GetNode, VHS_VideoCombine, PrimitiveInt, PrimitiveInt, PrimitiveInt, ComfySwitchNode, LTXVAddGuideMulti, LTXVAddGuideMulti, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PromptRelaySmartEncode, RH_LLMAPI_Pro_Node, easy showAnything, JjkConcat, JjkConcat, TextBoxMira, RH_Nano_Banana2_Gemini31Flash, PreviewImage, GetNode, GetNode, PreviewImage, PreviewImage, PreviewImage, easy showAnything, easy ifElse, RH_LLMAPI_Pro_Node, 1hew_ImageGridSplit, easy ifElse, PreviewImage, 1hew_ImageGridSplit, easy ifElse, PrimitiveBoolean, ResizeLongestToNode, 1hew_ImageGridSplit, 1hew_ImageGridSplit, LoadAudio, TextBoxMira, SetNode, LTX2SamplingPreviewOverride, GetNode, PrimitiveNode, PrimitiveInt, easy mathInt, easy mathInt, easy mathInt, easy mathInt, easy mathInt, easy mathInt, easy mathInt, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextBoxMira, TextBoxMira, TextBoxMira, TextBoxMira]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 193}
---

# 视频生成/文生视频/LTX23_5图生视频Gemini+VBVR+PromptRelay_2054601890872209409.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX23_5图生视频Gemini+VBVR+PromptRelay_2054601890872209409.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（192 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ManualSigmas`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `CFGGuider`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `SetNode`
- `LTXVPreprocess`
- `SetNode`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `LTXVChunkFeedForward`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTX2MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `LTX2AttentionTunerPatch`
- `LatentUpscaleModelLoader`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SetNode`
- `TrimAudioDuration`
- `SetNode`
- `ComfySwitchNode`
- `SetNode`
- `PrimitiveInt`
- `SimpleCalculatorKJ`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `MelBandRoFormerModelLoader`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `ConditioningZeroOut`
- `GetNode`
- `SetNode`
- `ComfyMathExpression`
- `GetNode`
- `ComfyMathExpression`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `LTXVConditioning`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `SetNode`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `PrimitiveFloat`
- `SetNode`
- `PrimitiveInt`
- `ResizeLongestToNode`
- `ResizeLongestToNode`
- `ResizeLongestToNode`
- `ResizeLongestToNode`
- `LTXVPreprocess`
- `GetNode`
- `GetNode`
- `LTXVScheduler`
- `GetNode`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfySwitchNode`
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PromptRelaySmartEncode`
- `RH_LLMAPI_Pro_Node`
- `easy showAnything`
- `JjkConcat`
- `JjkConcat`
- `TextBoxMira`
- `RH_Nano_Banana2_Gemini31Flash`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `easy showAnything`
- `easy ifElse`
- `RH_LLMAPI_Pro_Node`
- `1hew_ImageGridSplit`
- `easy ifElse`
- `PreviewImage`
- `1hew_ImageGridSplit`
- `easy ifElse`
- `PrimitiveBoolean`
- `ResizeLongestToNode`
- `1hew_ImageGridSplit`
- `1hew_ImageGridSplit`
- `LoadAudio`
- `TextBoxMira`
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `PrimitiveNode`
- `PrimitiveInt`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextBoxMira`
- `TextBoxMira`
- `TextBoxMira`
- `TextBoxMira`

## 关键参数

- `width` = `193`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **50%**（96/192）

**有卡**：`ManualSigmas`、`KSamplerSelect`、`VAEDecodeTiled`、`SamplerCustomAdvanced`、`CFGGuider`、`LTXVPreprocess`、`UNETLoader`、`LTXVChunkFeedForward`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`LTX2MemoryEfficientSageAttentionPatch`、`PathchSageAttentionKJ`、`LTX2AttentionTunerPatch`、`LatentUpscaleModelLoader`、`INTConstant`、`TrimAudioDuration`、`SimpleCalculatorKJ`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`ConditioningZeroOut`、`SolidMask`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`RandomNoise`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`ResizeLongestToNode`、`LTXVScheduler`、`VHS_VideoCombine`、`LTXVAddGuideMulti`、`LoraLoaderModelOnly`、`PromptRelaySmartEncode`、`RH_LLMAPI_Pro_Node`、`JjkConcat`、`TextBoxMira`、`RH_Nano_Banana2_Gemini31Flash`、`1hew_ImageGridSplit`、`PrimitiveBoolean`、`LoadAudio`、`LTX2SamplingPreviewOverride`、`easy mathInt`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
