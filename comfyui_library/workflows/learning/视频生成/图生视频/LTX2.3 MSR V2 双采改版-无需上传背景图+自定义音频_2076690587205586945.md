---
key: 视频生成/图生视频/LTX2.3 MSR V2 双采改版-无需上传背景图+自定义音频_2076690587205586945.json
name: LTX2.3 MSR V2 双采改版-无需上传背景图+自定义音频_2076690587205586945.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2076690587205586945.json
hash: 4e8edf64c233b877
coverage: 0.903614
learned_at: 2026-10-15 22:41:33
nodes: [RandomNoise, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), CFGGuider, ComfyMathExpression, LTXVAudioVAEDecode, SamplerCustomAdvanced, LayerUtility: PurgeVRAM, Reroute, ComfyMathExpression, PathchSageAttentionKJ, CLIPTextEncode, PromptRelayEncode, PrimitiveInt, KSamplerSelect, ManualSigmas, EmptyLTXVLatentVideo, LTXVConcatAVLatent, ComfyMathExpression, LayerUtility: PurgeVRAM, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, LoadImage, Label (rgthree), LoadImage, RepeatImageBatch, PrimitiveInt, RepeatImageBatch, RepeatImageBatch, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, LoadImage, RepeatImageBatch, RandomNoise, CFGGuider, PrimitiveInt, PrimitiveInt, ComfyMathExpression, RepeatImageBatch, ComfyMathExpression, LTXVSeparateAVLatent, LTXVConditioning, BatchImagesNode, LTX2_NAG, KSamplerSelect, LTXTiledSampler, LTXVSeparateAVLatent, LTXVCropGuides, LatentUpscaleModelLoader, LTXVLatentUpsampler, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXAddVideoICLoRAGuide, LTXVCropGuides, LTXAddVideoICLoRAGuide, LTXVConcatAVLatent, PrimitiveStringMultiline, PrimitiveStringMultiline, ComfyMathExpression, VHS_VideoCombine, ManualSigmas, Note, TrimAudioDuration, ComfyMathExpression, MelBandRoFormerSampler, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, LoraLoaderModelOnly, UNETLoader, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, LTXICLoRALoaderModelOnly, MelBandRoFormerModelLoader, LoadAudio, LoadImage, RTXVideoSuperResolution, VAEDecodeTiled, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3 MSR V2 双采改版-无需上传背景图+自定义音频_2076690587205586945.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2076690587205586945.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（83 个）：
- `RandomNoise`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `CFGGuider`
- `ComfyMathExpression`
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `Reroute`
- `ComfyMathExpression`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `PromptRelayEncode`
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `LayerUtility: PurgeVRAM`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `Label (rgthree)`
- `LoadImage`
- `RepeatImageBatch`
- `PrimitiveInt`
- `RepeatImageBatch`
- `RepeatImageBatch`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `RepeatImageBatch`
- `RandomNoise`
- `CFGGuider`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `RepeatImageBatch`
- `ComfyMathExpression`
- `LTXVSeparateAVLatent`
- `LTXVConditioning`
- `BatchImagesNode`
- `LTX2_NAG`
- `KSamplerSelect` ★核心
- `LTXTiledSampler` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTXVCropGuides`
- `LTXAddVideoICLoRAGuide`
- `LTXVConcatAVLatent`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `ManualSigmas`
- `Note`
- `TrimAudioDuration`
- `ComfyMathExpression`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTXICLoRALoaderModelOnly` ★核心
- `MelBandRoFormerModelLoader`
- `LoadAudio`
- `LoadImage`
- `RTXVideoSuperResolution`
- `VAEDecodeTiled` ★核心
- `LoadImage`

## 知识

覆盖率 **90%**（75/83）

**有卡**：`RandomNoise`、`Label (rgthree)`、`CFGGuider`、`ComfyMathExpression`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`LayerUtility: PurgeVRAM`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`PromptRelayEncode`、`KSamplerSelect`、`ManualSigmas`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`ResizeImagesByLongerEdge`、`LoadImage`、`RepeatImageBatch`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`BatchImagesNode`、`LTX2_NAG`、`LTXTiledSampler`、`LTXVCropGuides`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXAddVideoICLoRAGuide`、`VHS_VideoCombine`、`TrimAudioDuration`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`LoraLoaderModelOnly`、`UNETLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`LTXICLoRALoaderModelOnly`、`MelBandRoFormerModelLoader`、`LoadAudio`、`RTXVideoSuperResolution`、`VAEDecodeTiled`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
