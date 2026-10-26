---
key: 数字人/数字人/Ltx2.3数字人说话-极速参数优化-202606_2068623008067051522.json
name: Ltx2.3数字人说话-极速参数优化-202606_2068623008067051522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Ltx2.3数字人说话-极速参数优化-202606_2068623008067051522.json
hash: 7f98b0426fded6e2
coverage: 0.5
learned_at: 2026-10-26 01:56:28
nodes: [SetNode, SetNode, SetNode, GetNode, INTConstant, INTConstant, CFGGuider, SetNode, GetNode, DualCLIPLoader, VAELoader, VAELoaderKJ, VAELoader, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, LTXVChunkFeedForward, LTX2AttentionTunerPatch, GetNode, easy showAnything, GetNode, InversionDemoLazySwitch, 1hew_AudioDuration, Compare, TrimAudioDuration, GetNode, SamplerCustomAdvanced, SetNode, SetNode, SimpleMath+, easy showAnything, SimpleMath+, TrimAudioDuration, SetNode, PrimitiveStringMultiline, JoinStrings, GetNode, GetNode, LayerUtility: PurgeVRAM, VAEDecode, SetNode, easy showAnything, SetNode, SetNode, SetNode, KSamplerSelect, INTConstant, INTConstant, SetNode, GetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, GetNode, GetNode, SolidMask, LTXVConcatAVLatent, GetNode, GetNode, ColorMatchV2, GetNode, LTX2SamplingPreviewOverride, ModelSamplingSD3, LTX2_NAG, RandomNoise, BasicScheduler, CLIPTextEncode, CLIPTextEncode, LTXVPreprocess, PreviewAudio, LatentUpscaleModelLoader, LTXVSeparateAVLatent, GetNode, SetLatentNoiseMask, LTXVAudioVAEEncode, ImageResizeKJv2, LTXVConditioning, GetNode, LoadAudio, SimpleMath+, GetNode, SetNode, PreviewImage, LTXVImgToVideoInplaceKJ, GetNode, GetNode, GetNode, PrimitiveFloat, SetNode, SetNode, PrimitiveFloat, INTConstant, Qwen3_VQA, LoadImage, SetNode, PrimitiveFloat, PrimitiveStringMultiline, easy showAnything, VHS_VideoCombine, GetNode, GetNode, GetNode, MarkdownNote]
patterns: []
missing: []
---

# 数字人/数字人/Ltx2.3数字人说话-极速参数优化-202606_2068623008067051522.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Ltx2.3数字人说话-极速参数优化-202606_2068623008067051522.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（104 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `CFGGuider`
- `SetNode`
- `GetNode`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `LTX2AttentionTunerPatch`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `InversionDemoLazySwitch`
- `1hew_AudioDuration`
- `Compare`
- `TrimAudioDuration`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `easy showAnything`
- `SimpleMath+`
- `TrimAudioDuration`
- `SetNode`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `SetNode`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `INTConstant`
- `INTConstant`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `SolidMask`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `ColorMatchV2`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `ModelSamplingSD3`
- `LTX2_NAG`
- `RandomNoise`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `PreviewAudio`
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `ImageResizeKJv2`
- `LTXVConditioning`
- `GetNode`
- `LoadAudio`
- `SimpleMath+`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `INTConstant`
- `Qwen3_VQA`
- `LoadImage`
- `SetNode`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `MarkdownNote`

## 知识

覆盖率 **50%**（52/104）

**有卡**：`INTConstant`、`CFGGuider`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LTX2AttentionTunerPatch`、`InversionDemoLazySwitch`、`1hew_AudioDuration`、`Compare`、`TrimAudioDuration`、`SamplerCustomAdvanced`、`SimpleMath+`、`JoinStrings`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`KSamplerSelect`、`EmptyLTXVLatentVideo`、`SolidMask`、`LTXVConcatAVLatent`、`ColorMatchV2`、`LTX2SamplingPreviewOverride`、`ModelSamplingSD3`、`LTX2_NAG`、`RandomNoise`、`BasicScheduler`、`CLIPTextEncode`、`LTXVPreprocess`、`PreviewAudio`、`LatentUpscaleModelLoader`、`LTXVSeparateAVLatent`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`ImageResizeKJv2`、`LTXVConditioning`、`LoadAudio`、`LTXVImgToVideoInplaceKJ`、`Qwen3_VQA`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
