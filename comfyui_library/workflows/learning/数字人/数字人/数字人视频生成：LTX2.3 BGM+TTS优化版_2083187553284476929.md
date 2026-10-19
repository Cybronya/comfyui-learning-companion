---
key: 数字人/数字人/数字人视频生成：LTX2.3 BGM+TTS优化版_2083187553284476929.json
name: 数字人视频生成：LTX2.3 BGM+TTS优化版_2083187553284476929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/数字人视频生成：LTX2.3 BGM+TTS优化版_2083187553284476929.json
hash: b02bcf8d51753d80
coverage: 0.512195
learned_at: 2026-10-18 19:07:51
nodes: [BasicScheduler, MelBandRoFormerSampler, CLIPTextEncode, GetNode, GetNode, ImageResizeKJv2, SetNode, SetNode, GetNode, GetNode, ImageResizeKJv2, ResizeImageMaskNode, GetImageSize, SetNode, SetNode, SetNode, Compare, InversionDemoLazySwitch, easy showAnything, SetNode, UNETLoader, LayerUtility: PurgeVRAM, LatentUpscaleModelLoader, DualCLIPLoader, SetNode, VAELoader, VAELoaderKJ, SetNode, SetNode, SetNode, PathchSageAttentionKJ, LTXVChunkFeedForward, LTX2AttentionTunerPatch, LTXVConditioning, GetNode, EmptyLTXVLatentVideo, LTXVImgToVideoInplaceKJ, GetNode, GetNode, VAELoader, SetNode, GetNode, GetNode, SimpleMath+, LTXVPreprocess, SimpleMath+, SetNode, INTConstant, SetNode, SetNode, SetLatentNoiseMask, SolidMask, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, SetNode, PrimitiveFloat, LTXVAudioVAEEncode, GetNode, TrimAudioDuration, ComfySwitchNode, MelBandRoFormerModelLoader, SetNode, GetNode, PrimitiveStringMultiline, JoinStrings, CLIPTextEncode, LTX2_NAG, SetNode, SetNode, GetNode, LTX2SamplingPreviewOverride, SetNode, CFGGuider, RandomNoise, GetNode, LTXVConcatAVLatent, KSamplerSelect, ModelSamplingSD3, SamplerCustomAdvanced, SetNode, SetNode, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecode, GetNode, SetNode, LayerUtility: PurgeVRAM, INTConstant, GetNode, INTConstant, SetNode, SetNode, SimpleCalculatorKJ, SetNode, INTConstant, SetNode, PrimitiveFloat, INTConstant, SimpleMath+, Int, RH_GetAudioDuration, easy showAnything, LoadImage, IndexTTS2_Basic, easy showAnything, LoraLoaderModelOnly, GetNode, GetNode, TrimAudioDuration, VHS_VideoCombine, GetNode, LoadAudio, JjkText, GetNode, LoadAudio, SaveAudio, PrimitiveStringMultiline, SoundFlow_Mixer, RH_LLMAPI_NODE]
patterns: []
missing: []
---

# 数字人/数字人/数字人视频生成：LTX2.3 BGM+TTS优化版_2083187553284476929.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/数字人视频生成：LTX2.3 BGM+TTS优化版_2083187553284476929.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（123 个）：
- `BasicScheduler`
- `MelBandRoFormerSampler` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ResizeImageMaskNode`
- `GetImageSize`
- `SetNode`
- `SetNode`
- `SetNode`
- `Compare`
- `InversionDemoLazySwitch`
- `easy showAnything`
- `SetNode`
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `SetNode`
- `VAELoader`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `LTX2AttentionTunerPatch`
- `LTXVConditioning`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `GetNode`
- `VAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `LTXVPreprocess`
- `SimpleMath+`
- `SetNode`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SetLatentNoiseMask`
- `SolidMask`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `PrimitiveFloat`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `TrimAudioDuration`
- `ComfySwitchNode`
- `MelBandRoFormerModelLoader`
- `SetNode`
- `GetNode`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `SetNode`
- `CFGGuider`
- `RandomNoise`
- `GetNode`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ModelSamplingSD3`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `INTConstant`
- `GetNode`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `SetNode`
- `INTConstant`
- `SetNode`
- `PrimitiveFloat`
- `INTConstant`
- `SimpleMath+`
- `Int`
- `RH_GetAudioDuration`
- `easy showAnything`
- `LoadImage`
- `IndexTTS2_Basic`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `TrimAudioDuration`
- `VHS_VideoCombine`
- `GetNode`
- `LoadAudio`
- `JjkText`
- `GetNode`
- `LoadAudio`
- `SaveAudio`
- `PrimitiveStringMultiline`
- `SoundFlow_Mixer`
- `RH_LLMAPI_NODE`

## 知识

覆盖率 **51%**（63/123）

**有卡**：`BasicScheduler`、`MelBandRoFormerSampler`、`CLIPTextEncode`、`ImageResizeKJv2`、`ResizeImageMaskNode`、`GetImageSize`、`Compare`、`InversionDemoLazySwitch`、`UNETLoader`、`LayerUtility: PurgeVRAM`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LTX2AttentionTunerPatch`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplaceKJ`、`SimpleMath+`、`LTXVPreprocess`、`INTConstant`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEEncode`、`TrimAudioDuration`、`MelBandRoFormerModelLoader`、`JoinStrings`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`CFGGuider`、`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ModelSamplingSD3`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecode`、`SimpleCalculatorKJ`、`Int`、`RH_GetAudioDuration`、`LoadImage`、`IndexTTS2_Basic`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`LoadAudio`、`SaveAudio`、`SoundFlow_Mixer`、`RH_LLMAPI_NODE`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
