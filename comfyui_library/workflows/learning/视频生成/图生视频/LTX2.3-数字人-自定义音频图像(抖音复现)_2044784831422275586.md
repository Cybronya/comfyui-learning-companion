---
key: 视频生成/图生视频/LTX2.3-数字人-自定义音频图像(抖音复现)_2044784831422275586.json
name: LTX2.3-数字人-自定义音频图像(抖音复现)_2044784831422275586.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-数字人-自定义音频图像(抖音复现)_2044784831422275586.json
hash: b3b3127f7b0a6394
coverage: 0.594937
learned_at: 2026-10-15 22:36:41
nodes: [SetNode, SolidMask, SetLatentNoiseMask, VAELoaderKJ, GetNode, GetNode, VAELoader, GetNode, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, GetNode, LTXVConcatAVLatent, LTXVSpatioTemporalTiledVAEDecode, SetNode, SetNode, LTXVConditioning, LTXVPreprocess, LayerUtility: ImageScaleByAspectRatio V2, GetNode, SetNode, SetNode, GetNode, GetNode, Note, Note, Note, Note, Note, INTConstant, Label (rgthree), LoadAudio, DualCLIPLoader, VAELoader, MelBandRoFormerModelLoader, VHS_VideoCombine, CLIPTextEncode, llama_cpp_parameters, LoadImage, CLIPTextEncode, LayerUtility: PurgeVRAM V2, PreviewTextNode, llama_cpp_model_loader, PreviewAudio, LTXVAudioVAEDecode, GetNode, PrimitiveFloat, Note, Note, SetNode, SetNode, SetNode, Float, SimpleCalculatorKJ, TrimAudioDuration, MelBandRoFormerSampler, LTXVAudioVAEEncode, CR Text, llama_cpp_instruct_adv, GetNode, LTXVSeparateAVLatent, GetNode, ManualSigmas, SamplerCustomAdvanced, KSamplerSelect, RandomNoise, CFGGuider, LTX2SamplingPreviewOverride, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, SetNode, LTX2_NAG, SetNode, GetNode, GetNode, SigmasPreview, GetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3-数字人-自定义音频图像(抖音复现)_2044784831422275586.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044784831422275586.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（79 个）：
- `SetNode`
- `SolidMask`
- `SetLatentNoiseMask`
- `VAELoaderKJ`
- `GetNode`
- `GetNode`
- `VAELoader`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `SetNode`
- `SetNode`
- `LTXVConditioning`
- `LTXVPreprocess`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `INTConstant`
- `Label (rgthree)`
- `LoadAudio`
- `DualCLIPLoader`
- `VAELoader`
- `MelBandRoFormerModelLoader`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `llama_cpp_parameters`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `PreviewTextNode`
- `llama_cpp_model_loader`
- `PreviewAudio`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `PrimitiveFloat`
- `Note`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `Float`
- `SimpleCalculatorKJ`
- `TrimAudioDuration`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `CR Text`
- `llama_cpp_instruct_adv`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `LTX2SamplingPreviewOverride`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `LTX2_NAG`
- `SetNode`
- `GetNode`
- `GetNode`
- `SigmasPreview`
- `GetNode`

## 知识

覆盖率 **59%**（47/79）

**有卡**：`SolidMask`、`SetLatentNoiseMask`、`VAELoaderKJ`、`VAELoader`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`LTXVSpatioTemporalTiledVAEDecode`、`LTXVConditioning`、`LTXVPreprocess`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`Label (rgthree)`、`LoadAudio`、`DualCLIPLoader`、`MelBandRoFormerModelLoader`、`VHS_VideoCombine`、`CLIPTextEncode`、`llama_cpp_parameters`、`LoadImage`、`LayerUtility: PurgeVRAM V2`、`PreviewTextNode`、`llama_cpp_model_loader`、`PreviewAudio`、`LTXVAudioVAEDecode`、`Float`、`SimpleCalculatorKJ`、`TrimAudioDuration`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`CR Text`、`llama_cpp_instruct_adv`、`LTXVSeparateAVLatent`、`ManualSigmas`、`SamplerCustomAdvanced`、`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`LTX2SamplingPreviewOverride`、`UNETLoader`、`LoraLoaderModelOnly`、`LTX2_NAG`、`SigmasPreview`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
