---
key: 视频生成/图生视频/LTX2.3-音频数字人(双采样高清版)_2050231422836846593.json
name: LTX2.3-音频数字人(双采样高清版)_2050231422836846593.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-音频数字人(双采样高清版)_2050231422836846593.json
hash: 1291f482de1f40d8
coverage: 0.547826
learned_at: 2026-10-15 22:37:17
nodes: [SetNode, VAELoader, VAELoaderKJ, VAELoader, SetNode, SetNode, GetNode, GetNode, Note, Note, ManualSigmas, KSamplerSelect, RandomNoise, CFGGuider, LTXVConcatAVLatent, RandomNoise, LTXVLatentUpsampler, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, VHS_VideoCombine, GetNode, LTXVConcatAVLatent, SetNode, GetNode, SetNode, LTXVSeparateAVLatent, GetNode, SetNode, LatentUpscaleModelLoader, SetNode, GetNode, GetNode, GetNode, LTXVImgToVideoConditionOnly, ComfySwitchNode, GetNode, LTXVAudioVAEEncode, SolidMask, SetLatentNoiseMask, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, GetNode, LTXVPreprocess, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, SimpleCalculatorKJ, SetNode, Note, Note, INTConstant, Display Any (rgthree), GetNode, MelBandRoFormerSampler, SetNode, Note, CR Text, AudioCrop, INTConstant, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSpatioTemporalTiledVAEDecode, GetNode, LTXVAudioVAEDecode, PreviewAudio, LTXVSpatioTemporalTiledVAEDecode, CFGGuider, PrimitiveFloat, GetNode, LTX2SamplingPreviewOverride, KSamplerSelect, GetNode, LTXVConditioning, LTX2_NAG, SetNode, GetNode, GetNode, SetNode, CLIPTextEncode, CLIPTextEncode, PrimitiveStringMultiline, CR Prompt Text, SamplerCustomAdvanced, GetNode, PrimitiveBoolean, SetNode, Note, Note, GetNode, llama_cpp_instruct_adv, llama_cpp_parameters, llama_cpp_model_loader, LayerUtility: PurgeVRAM V2, ShowText|pysssss, SetNode, LoadImage, LoraLoaderModelOnly, DualCLIPLoader, LoraLoaderModelOnly, MelBandRoFormerModelLoader, LoraLoaderModelOnly, UNETLoader, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), RH_LLMAPI_Pro_Node, LoadAudio, ManualSigmas, SigmasPreview, Fast Groups Bypasser (rgthree), MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3-音频数字人(双采样高清版)_2050231422836846593.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2050231422836846593.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（115 个）：
- `SetNode`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Note`
- `Note`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `GetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoConditionOnly`
- `ComfySwitchNode`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVImgToVideoInplace`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `LTXVPreprocess`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `SetNode`
- `Note`
- `Note`
- `INTConstant`
- `Display Any (rgthree)`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `Note`
- `CR Text`
- `AudioCrop`
- `INTConstant`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `PreviewAudio`
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `CFGGuider`
- `PrimitiveFloat`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `KSamplerSelect` ★核心
- `GetNode`
- `LTXVConditioning`
- `LTX2_NAG`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `CR Prompt Text`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `PrimitiveBoolean`
- `SetNode`
- `Note`
- `Note`
- `GetNode`
- `llama_cpp_instruct_adv`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `LayerUtility: PurgeVRAM V2`
- `ShowText|pysssss`
- `SetNode`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `MelBandRoFormerModelLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `RH_LLMAPI_Pro_Node`
- `LoadAudio`
- `ManualSigmas`
- `SigmasPreview`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`

## 知识

覆盖率 **55%**（63/115）

**有卡**：`VAELoader`、`VAELoaderKJ`、`ManualSigmas`、`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`VHS_VideoCombine`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`LTXVImgToVideoConditionOnly`、`LTXVAudioVAEEncode`、`SolidMask`、`SetLatentNoiseMask`、`LTXVImgToVideoInplace`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleCalculatorKJ`、`INTConstant`、`Display Any (rgthree)`、`MelBandRoFormerSampler`、`CR Text`、`AudioCrop`、`SamplerCustomAdvanced`、`LTXVSpatioTemporalTiledVAEDecode`、`LTXVAudioVAEDecode`、`PreviewAudio`、`LTX2SamplingPreviewOverride`、`LTXVConditioning`、`LTX2_NAG`、`CLIPTextEncode`、`CR Prompt Text`、`PrimitiveBoolean`、`llama_cpp_instruct_adv`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`LayerUtility: PurgeVRAM V2`、`LoadImage`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`MelBandRoFormerModelLoader`、`UNETLoader`、`Mute / Bypass Relay (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`RH_LLMAPI_Pro_Node`、`LoadAudio`、`SigmasPreview`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
