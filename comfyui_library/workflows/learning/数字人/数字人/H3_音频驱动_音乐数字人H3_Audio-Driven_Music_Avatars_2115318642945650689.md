---
key: 数字人/数字人/H3_音频驱动_音乐数字人H3_Audio-Driven_Music_Avatars_2115318642945650689.json
name: H3_音频驱动_音乐数字人H3_Audio-Driven_Music_Avatars_2115318642945650689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/H3_音频驱动_音乐数字人H3_Audio-Driven_Music_Avatars_2115318642945650689.json
hash: 115c05ca90b366ef
coverage: 0.673469
learned_at: 2026-10-30 17:56:30
nodes: [VAELoader, VAELoader, VAEDecode, CLIPLoader, PrimitiveFloat, ImageResizeKJv2, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, DF_Int_to_Float, ModelAttentionBackend, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, MiniMaxH3ReferenceToVideo, KSamplerSelect, ConditioningZeroOut, LTXVSeparateAVLatent, SolidMask, SetLatentNoiseMask, LTXVSeparateAVLatent, LTXVAudioVAEEncode, LTXVConcatAVLatent, GetNode, ModelPreviewOverrideKJ, UNETLoader, LoraLoaderModelOnly, BasicScheduler, SetNode, Compare, PreviewImage, SelfLiftAvatarH3Sampler, ComfyMathExpression, SoundFlow_GetLength, AudioSeparation, Int, InversionDemoLazySwitch, PrimitiveFloat, LoadImage, PrimitiveStringMultiline, PrimitiveFloat, PrimitiveInt, PrimitiveInt, VHS_LoadAudioUpload, PreviewAudio, PrimitiveFloat, VHS_VideoCombine]
patterns: []
missing: []
---

# 数字人/数字人/H3_音频驱动_音乐数字人H3_Audio-Driven_Music_Avatars_2115318642945650689.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/H3_音频驱动_音乐数字人H3_Audio-Driven_Music_Avatars_2115318642945650689.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `VAELoader`
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPLoader`
- `PrimitiveFloat`
- `ImageResizeKJv2`
- `SetNode`
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
- `LTXVSeparateAVLatent`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEEncode` ★核心
- `LTXVConcatAVLatent`
- `GetNode`
- `ModelPreviewOverrideKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `SetNode`
- `Compare`
- `PreviewImage`
- `SelfLiftAvatarH3Sampler` ★核心
- `ComfyMathExpression`
- `SoundFlow_GetLength`
- `AudioSeparation`
- `Int`
- `InversionDemoLazySwitch`
- `PrimitiveFloat`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_LoadAudioUpload`
- `PreviewAudio`
- `PrimitiveFloat`
- `VHS_VideoCombine`

## 知识

覆盖率 **67%**（33/49）

**有卡**：`VAELoader`、`VAEDecode`、`CLIPLoader`、`ImageResizeKJv2`、`DF_Int_to_Float`、`ModelAttentionBackend`、`MiniMaxChunkFeedForward`、`MiniMaxLowVRAMAttention`、`MiniMaxH3ReferenceToVideo`、`KSamplerSelect`、`ConditioningZeroOut`、`LTXVSeparateAVLatent`、`SolidMask`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`LTXVConcatAVLatent`、`ModelPreviewOverrideKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`BasicScheduler`、`Compare`、`SelfLiftAvatarH3Sampler`、`ComfyMathExpression`、`SoundFlow_GetLength`、`AudioSeparation`、`Int`、`InversionDemoLazySwitch`、`LoadImage`、`VHS_LoadAudioUpload`、`PreviewAudio`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect
