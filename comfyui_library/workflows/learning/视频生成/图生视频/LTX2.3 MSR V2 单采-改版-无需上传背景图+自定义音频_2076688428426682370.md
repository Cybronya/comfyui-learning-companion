---
key: 视频生成/图生视频/LTX2.3 MSR V2 单采-改版-无需上传背景图+自定义音频_2076688428426682370.json
name: LTX2.3 MSR V2 单采-改版-无需上传背景图+自定义音频_2076688428426682370.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 MSR V2 单采-改版-无需上传背景图+自定义音频_2076688428426682370.json
hash: cf41b87a866dcd27
coverage: 0.873239
learned_at: 2026-10-15 22:41:33
nodes: [RandomNoise, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), PrimitiveStringMultiline, PrimitiveStringMultiline, CFGGuider, ComfyMathExpression, LTXVAudioVAEDecode, VAEDecodeTiled, PrimitiveInt, PrimitiveInt, LTXVCropGuides, SamplerCustomAdvanced, LayerUtility: PurgeVRAM, Reroute, PathchSageAttentionKJ, CLIPTextEncode, PromptRelayEncode, PrimitiveInt, LTXAddVideoICLoRAGuide, KSamplerSelect, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, LTX2_NAG, EmptyLTXVLatentVideo, LTXVConcatAVLatent, ComfyMathExpression, FrameInterpolationModelLoader, LayerUtility: PurgeVRAM, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, LoadImage, Label (rgthree), BatchImagesNode, LoadImage, RepeatImageBatch, PrimitiveInt, RepeatImageBatch, RepeatImageBatch, ResizeImagesByLongerEdge, RepeatImageBatch, ResizeImagesByLongerEdge, LoadImage, RepeatImageBatch, ComfyMathExpression, ComfyMathExpression, PrimitiveStringMultiline, PrimitiveStringMultiline, VHS_VideoCombine, LTXVAudioVAEEncode, SolidMask, TrimAudioDuration, MelBandRoFormerSampler, ComfyMathExpression, SetLatentNoiseMask, LoraLoaderModelOnly, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, LTXICLoRALoaderModelOnly, MelBandRoFormerModelLoader, LoadAudio, LoadImage, LoadImage, UNETLoader, RTXVideoSuperResolution, FrameInterpolate]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3 MSR V2 单采-改版-无需上传背景图+自定义音频_2076688428426682370.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2076688428426682370.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（71 个）：
- `RandomNoise`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `CFGGuider`
- `ComfyMathExpression`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `Reroute`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `PromptRelayEncode`
- `PrimitiveInt`
- `LTXAddVideoICLoRAGuide`
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `LTX2_NAG`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `FrameInterpolationModelLoader`
- `LayerUtility: PurgeVRAM`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `Label (rgthree)`
- `BatchImagesNode`
- `LoadImage`
- `RepeatImageBatch`
- `PrimitiveInt`
- `RepeatImageBatch`
- `RepeatImageBatch`
- `ResizeImagesByLongerEdge`
- `RepeatImageBatch`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `RepeatImageBatch`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `TrimAudioDuration`
- `MelBandRoFormerSampler` ★核心
- `ComfyMathExpression`
- `SetLatentNoiseMask`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTXICLoRALoaderModelOnly` ★核心
- `MelBandRoFormerModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `RTXVideoSuperResolution`
- `FrameInterpolate`

## 知识

覆盖率 **87%**（62/71）

**有卡**：`RandomNoise`、`Label (rgthree)`、`CFGGuider`、`ComfyMathExpression`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`LayerUtility: PurgeVRAM`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`PromptRelayEncode`、`LTXAddVideoICLoRAGuide`、`KSamplerSelect`、`LTXVConditioning`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTX2_NAG`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`FrameInterpolationModelLoader`、`ResizeImagesByLongerEdge`、`LoadImage`、`BatchImagesNode`、`RepeatImageBatch`、`VHS_VideoCombine`、`LTXVAudioVAEEncode`、`SolidMask`、`TrimAudioDuration`、`MelBandRoFormerSampler`、`SetLatentNoiseMask`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoaderKJ`、`LTXICLoRALoaderModelOnly`、`MelBandRoFormerModelLoader`、`LoadAudio`、`UNETLoader`、`RTXVideoSuperResolution`、`FrameInterpolate`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
