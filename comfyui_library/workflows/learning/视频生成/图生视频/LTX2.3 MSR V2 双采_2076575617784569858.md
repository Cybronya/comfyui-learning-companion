---
key: 视频生成/图生视频/LTX2.3 MSR V2 双采_2076575617784569858.json
name: LTX2.3 MSR V2 双采_2076575617784569858.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 MSR V2 双采_2076575617784569858.json
hash: 1a7d73c28bb0247d
coverage: 0.677083
learned_at: 2026-10-15 22:41:31
nodes: [LTXVEmptyLatentAudio, Reroute, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, PrimitiveInt, PrimitiveInt, LTX2_NAG, LTXVConditioning, ManualSigmas, ComfyMathExpression, PrimitiveInt, PrimitiveInt, ComfyMathExpression, CLIPTextEncode, ComfyMathExpression, RandomNoise, LayerUtility: PurgeVRAM, SamplerCustomAdvanced, PathchSageAttentionKJ, ResizeImagesByLongerEdge, EmptyLTXVLatentVideo, VAEDecodeTiled, VHS_VideoCombine, SetNode, GetNode, SetNode, SetNode, ResizeImagesByLongerEdge, LoadImage, SetNode, ResizeImagesByLongerEdge, LoadImage, SetNode, ResizeImagesByLongerEdge, GetNode, GetNode, GetNode, GetNode, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), GetNode, GetNode, GetNode, SetNode, GetNode, LiconMSR, GetNode, LTXAddVideoICLoRAGuide, GetNode, CLIPTextEncode, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, RandomNoise, CFGGuider, LTXVSeparateAVLatent, KSamplerSelect, LTXVConcatAVLatent, LatentUpscaleModelLoader, LTXVAudioVAEDecode, LTXVLatentUpsampler, ComfyMathExpression, ComfyMathExpression, LTXVCropGuides, ComfyMathExpression, LayerUtility: PurgeVRAM, LTXVCropGuides, SamplerCustomAdvanced, ManualSigmas, FrameInterpolationModelLoader, FrameInterpolate, LayerUtility: PurgeVRAM, GetNode, GetNode, GetNode, GetNode, GetNode, LoraLoaderModelOnly, UNETLoader, VAELoaderKJ, DualCLIPLoader, LoadImage, LoadImage, LoadImage, ResizeImagesByLongerEdge, RTXVideoSuperResolution, VAELoaderKJ, LTXICLoRALoaderModelOnly, PrimitiveStringMultiline, LTXVAddGuideMulti, LTXVAddGuideMulti]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 44, "width": 97}
---

# 视频生成/图生视频/LTX2.3 MSR V2 双采_2076575617784569858.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2076575617784569858.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（96 个）：
- `LTXVEmptyLatentAudio` ★核心
- `Reroute`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTX2_NAG`
- `LTXVConditioning`
- `ManualSigmas`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `RandomNoise`
- `LayerUtility: PurgeVRAM`
- `SamplerCustomAdvanced` ★核心
- `PathchSageAttentionKJ`
- `ResizeImagesByLongerEdge`
- `EmptyLTXVLatentVideo`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LiconMSR`
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `LTXVAudioVAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVCropGuides`
- `ComfyMathExpression`
- `LayerUtility: PurgeVRAM`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `FrameInterpolationModelLoader`
- `FrameInterpolate`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResizeImagesByLongerEdge`
- `RTXVideoSuperResolution`
- `VAELoaderKJ`
- `LTXICLoRALoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`

## 关键参数

- `width` = `97`
- `height` = `44`
- `batch_size` = `1`

## 知识

覆盖率 **68%**（65/96）

**有卡**：`LTXVEmptyLatentAudio`、`CFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTX2_NAG`、`LTXVConditioning`、`ManualSigmas`、`ComfyMathExpression`、`CLIPTextEncode`、`RandomNoise`、`LayerUtility: PurgeVRAM`、`SamplerCustomAdvanced`、`PathchSageAttentionKJ`、`ResizeImagesByLongerEdge`、`EmptyLTXVLatentVideo`、`VAEDecodeTiled`、`VHS_VideoCombine`、`LoadImage`、`Label (rgthree)`、`LiconMSR`、`LTXAddVideoICLoRAGuide`、`LatentUpscaleModelLoader`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`FrameInterpolationModelLoader`、`FrameInterpolate`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`RTXVideoSuperResolution`、`LTXICLoRALoaderModelOnly`、`LTXVAddGuideMulti`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
