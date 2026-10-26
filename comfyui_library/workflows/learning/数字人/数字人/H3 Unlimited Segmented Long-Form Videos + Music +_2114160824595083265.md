---
key: 数字人/数字人/H3 Unlimited Segmented Long-Form Videos + Music +_2114160824595083265.json
name: H3 Unlimited Segmented Long-Form Videos + Music +_2114160824595083265
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/H3 Unlimited Segmented Long-Form Videos + Music +_2114160824595083265.json
hash: 3670a2cc500aa864
coverage: 0.673469
learned_at: 2026-10-26 22:10:11
nodes: [VAELoader, VAELoader, CLIPLoader, PrimitiveFloat, ImageResizeKJv2, SetNode, GetNode, GetNode, SetNode, GetNode, DF_Int_to_Float, ModelAttentionBackend, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, MiniMaxH3ReferenceToVideo, KSamplerSelect, ConditioningZeroOut, SolidMask, LTXVSeparateAVLatent, LTXVAudioVAEEncode, GetNode, ModelPreviewOverrideKJ, UNETLoader, LoraLoaderModelOnly, BasicScheduler, SetNode, Compare, PreviewImage, ComfyMathExpression, SoundFlow_GetLength, AudioSeparation, Int, InversionDemoLazySwitch, PrimitiveFloat, LTXVConcatAVLatent, SetLatentNoiseMask, LTXVSeparateAVLatent, SetNode, VAEDecode, SelfLiftAvatarH3Sampler, PrimitiveStringMultiline, PrimitiveInt, PrimitiveInt, PrimitiveFloat, PreviewAudio, PrimitiveFloat, VHS_LoadAudioUpload, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 数字人/数字人/H3 Unlimited Segmented Long-Form Videos + Music +_2114160824595083265.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/H3 Unlimited Segmented Long-Form Videos + Music +_2114160824595083265.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `PrimitiveFloat`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `DF_Int_to_Float`
- `ModelAttentionBackend`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `MiniMaxH3ReferenceToVideo`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `SolidMask`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `ModelPreviewOverrideKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `SetNode`
- `Compare`
- `PreviewImage`
- `ComfyMathExpression`
- `SoundFlow_GetLength`
- `AudioSeparation`
- `Int`
- `InversionDemoLazySwitch`
- `PrimitiveFloat`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `LTXVSeparateAVLatent`
- `SetNode`
- `VAEDecode` ★核心
- `SelfLiftAvatarH3Sampler` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PreviewAudio`
- `PrimitiveFloat`
- `VHS_LoadAudioUpload`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **67%**（33/49）

**有卡**：`VAELoader`、`CLIPLoader`、`ImageResizeKJv2`、`DF_Int_to_Float`、`ModelAttentionBackend`、`MiniMaxChunkFeedForward`、`MiniMaxLowVRAMAttention`、`MiniMaxH3ReferenceToVideo`、`KSamplerSelect`、`ConditioningZeroOut`、`SolidMask`、`LTXVSeparateAVLatent`、`LTXVAudioVAEEncode`、`ModelPreviewOverrideKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`BasicScheduler`、`Compare`、`ComfyMathExpression`、`SoundFlow_GetLength`、`AudioSeparation`、`Int`、`InversionDemoLazySwitch`、`LTXVConcatAVLatent`、`SetLatentNoiseMask`、`VAEDecode`、`SelfLiftAvatarH3Sampler`、`PreviewAudio`、`VHS_LoadAudioUpload`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect
