---
key: 视频生成/图生视频/LTX2.3 MSR V2 双采+ Customer Audio_2076574537289920514.json
name: LTX2.3 MSR V2 双采+ Customer Audio_2076574537289920514.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 MSR V2 双采+ Customer Audio_2076574537289920514.json
hash: c43283d39e8cefe6
coverage: 0.701923
learned_at: 2026-10-15 22:41:31
nodes: [KSamplerSelect, PrimitiveInt, ResizeImagesByLongerEdge, SetNode, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, Label (rgthree), LoadImage, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SetNode, ResizeImagesByLongerEdge, LTX2_NAG, GetNode, GetNode, CLIPTextEncode, LTXVConcatAVLatent, GetNode, ManualSigmas, LoadImage, LTXVSeparateAVLatent, Reroute, LayerUtility: PurgeVRAM, VAEDecodeTiled, ComfyMathExpression, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, GetNode, ResizeImagesByLongerEdge, SetNode, PrimitiveInt, PrimitiveInt, PrimitiveInt, SetNode, SetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, GetNode, GetNode, LiconMSR, GetNode, SetNode, PathchSageAttentionKJ, LTXAddVideoICLoRAGuide, SamplerCustomAdvanced, RandomNoise, CFGGuider, LTXVConditioning, VHS_VideoCombine, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVCropGuides, PrimitiveStringMultiline, SetLatentNoiseMask, LTXVAudioVAEEncode, SolidMask, PreviewAudio, MelBandRoFormerSampler, TrimAudioDuration, ComfyMathExpression, CLIPTextEncode, CFGGuider, RandomNoise, LTXVLatentUpsampler, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, GetNode, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVSeparateAVLatent, FrameInterpolate, FrameInterpolationModelLoader, LayerUtility: PurgeVRAM, LTXVCropGuides, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LTXICLoRALoaderModelOnly, TrimAudioDuration, LoadAudio, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, UNETLoader, MelBandRoFormerModelLoader, ComfyMathExpression, RTXVideoSuperResolution, LatentUpscaleModelLoader, LTXVAddGuideMulti, LTXVAddGuideMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3 MSR V2 双采+ Customer Audio_2076574537289920514.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2076574537289920514.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（104 个）：
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `Label (rgthree)`
- `LoadImage`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `LTX2_NAG`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `GetNode`
- `ManualSigmas`
- `LoadImage`
- `LTXVSeparateAVLatent`
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `VAEDecodeTiled` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `GetNode`
- `GetNode`
- `LiconMSR`
- `GetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `LTXAddVideoICLoRAGuide`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `LTXVConditioning`
- `VHS_VideoCombine`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `LTXVCropGuides`
- `PrimitiveStringMultiline`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `PreviewAudio`
- `MelBandRoFormerSampler` ★核心
- `TrimAudioDuration`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `RandomNoise`
- `LTXVLatentUpsampler` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVSeparateAVLatent`
- `FrameInterpolate`
- `FrameInterpolationModelLoader`
- `LayerUtility: PurgeVRAM`
- `LTXVCropGuides`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `TrimAudioDuration`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `MelBandRoFormerModelLoader`
- `ComfyMathExpression`
- `RTXVideoSuperResolution`
- `LatentUpscaleModelLoader`
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`

## 知识

覆盖率 **70%**（73/104）

**有卡**：`KSamplerSelect`、`ResizeImagesByLongerEdge`、`Label (rgthree)`、`LoadImage`、`LTX2_NAG`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LayerUtility: PurgeVRAM`、`VAEDecodeTiled`、`ComfyMathExpression`、`LiconMSR`、`PathchSageAttentionKJ`、`LTXAddVideoICLoRAGuide`、`SamplerCustomAdvanced`、`RandomNoise`、`CFGGuider`、`LTXVConditioning`、`VHS_VideoCombine`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`PreviewAudio`、`MelBandRoFormerSampler`、`TrimAudioDuration`、`LTXVLatentUpsampler`、`FrameInterpolate`、`FrameInterpolationModelLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXICLoRALoaderModelOnly`、`LoadAudio`、`LoraLoaderModelOnly`、`UNETLoader`、`MelBandRoFormerModelLoader`、`RTXVideoSuperResolution`、`LatentUpscaleModelLoader`、`LTXVAddGuideMulti`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
