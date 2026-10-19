---
key: 数字人/数字人/kplei_scail.json_2109885347109883905.json
name: kplei_scail.json_2109885347109883905
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/kplei_scail.json_2109885347109883905.json
hash: d4ca40232a8e8116
coverage: 0.679245
learned_at: 2026-10-19 00:41:06
nodes: [VAELoader, CLIPLoader, PrimitiveFloat, GetNode, GetNode, SetNode, DF_Int_to_Float, ModelAttentionBackend, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, KSamplerSelect, SolidMask, LTXVSeparateAVLatent, LTXVAudioVAEEncode, SetNode, Compare, PreviewImage, ComfyMathExpression, SoundFlow_GetLength, AudioSeparation, Int, InversionDemoLazySwitch, PrimitiveFloat, LTXVConcatAVLatent, SetLatentNoiseMask, LTXVSeparateAVLatent, SetNode, VAEDecode, SelfLiftAvatarH3Sampler, PrimitiveInt, PrimitiveInt, LayerUtility: TextJoin, PrimitiveFloat, BasicScheduler, ConditioningZeroOut, GetNode, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, PrimitiveStringMultiline, UNETLoader, SetNode, VAELoader, MiniMaxH3ReferenceToVideo, LoraLoaderModelOnly, ModelPreviewOverrideKJ, ImageResizeKJv2, LoadImage, VHS_LoadAudioUpload, PrimitiveFloat, JjkText]
patterns: []
missing: []
---

# 数字人/数字人/kplei_scail.json_2109885347109883905.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/kplei_scail.json_2109885347109883905.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `VAELoader`
- `CLIPLoader`
- `PrimitiveFloat`
- `GetNode`
- `GetNode`
- `SetNode`
- `DF_Int_to_Float`
- `ModelAttentionBackend`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `KSamplerSelect` ★核心
- `SolidMask`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEEncode` ★核心
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
- `PrimitiveInt`
- `PrimitiveInt`
- `LayerUtility: TextJoin`
- `PrimitiveFloat`
- `BasicScheduler`
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `SetNode`
- `VAELoader`
- `MiniMaxH3ReferenceToVideo`
- `LoraLoaderModelOnly` ★核心
- `ModelPreviewOverrideKJ`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_LoadAudioUpload`
- `PrimitiveFloat`
- `JjkText`

## 知识

覆盖率 **68%**（36/53）

**有卡**：`VAELoader`、`CLIPLoader`、`DF_Int_to_Float`、`ModelAttentionBackend`、`MiniMaxChunkFeedForward`、`MiniMaxLowVRAMAttention`、`KSamplerSelect`、`SolidMask`、`LTXVSeparateAVLatent`、`LTXVAudioVAEEncode`、`Compare`、`ComfyMathExpression`、`SoundFlow_GetLength`、`AudioSeparation`、`Int`、`InversionDemoLazySwitch`、`LTXVConcatAVLatent`、`SetLatentNoiseMask`、`VAEDecode`、`SelfLiftAvatarH3Sampler`、`LayerUtility: TextJoin`、`BasicScheduler`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`UNETLoader`、`MiniMaxH3ReferenceToVideo`、`ModelPreviewOverrideKJ`、`ImageResizeKJv2`、`LoadImage`、`VHS_LoadAudioUpload`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect
