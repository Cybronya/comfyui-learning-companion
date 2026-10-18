---
key: 视频生成/图生视频/LTX2.3-MSR-V2-多图参考-双采版-自动提示词_2078833439343726593.json
name: LTX2.3-MSR-V2-多图参考-双采版-自动提示词_2078833439343726593.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-MSR-V2-多图参考-双采版-自动提示词_2078833439343726593.json
hash: a9cebcf63e749019
coverage: 0.613861
learned_at: 2026-10-15 22:41:56
nodes: [LTXVEmptyLatentAudio, Reroute, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, PrimitiveInt, PrimitiveInt, LTX2_NAG, LTXVConditioning, ManualSigmas, ComfyMathExpression, PrimitiveInt, ComfyMathExpression, CLIPTextEncode, ComfyMathExpression, RandomNoise, LayerUtility: PurgeVRAM, SamplerCustomAdvanced, PathchSageAttentionKJ, ResizeImagesByLongerEdge, EmptyLTXVLatentVideo, SetNode, GetNode, SetNode, SetNode, ResizeImagesByLongerEdge, SetNode, ResizeImagesByLongerEdge, LoadImage, SetNode, ResizeImagesByLongerEdge, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, LiconMSR, GetNode, LTXAddVideoICLoRAGuide, GetNode, CLIPTextEncode, RandomNoise, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, LatentUpscaleModelLoader, LTXVLatentUpsampler, ComfyMathExpression, ComfyMathExpression, LTXVCropGuides, SamplerCustomAdvanced, ManualSigmas, GetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, LTXICLoRALoaderModelOnly, LTXVAddGuideMulti, LTXVAddGuideMulti, ResizeImagesByLongerEdge, LoadImage, PrimitiveInt, PrimitiveStringMultiline, 孤海注释, RTXVideoSuperResolution, FrameInterpolate, LayerUtility: PurgeVRAM, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, FrameInterpolationModelLoader, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVCropGuides, LayerUtility: PurgeVRAM, LTXVAudioVAEDecode, ComfyMathExpression, VHS_VideoCombine, VHS_VideoCombine, MarkdownNote, PrimitiveStringMultiline, MarkdownNote, LoraLoaderModelOnly, MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 44, "width": 97}
---

# 视频生成/图生视频/LTX2.3-MSR-V2-多图参考-双采版-自动提示词_2078833439343726593.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2078833439343726593.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（101 个）：
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
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `RandomNoise`
- `LayerUtility: PurgeVRAM`
- `SamplerCustomAdvanced` ★核心
- `PathchSageAttentionKJ`
- `ResizeImagesByLongerEdge`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
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
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `孤海注释`
- `RTXVideoSuperResolution`
- `FrameInterpolate`
- `LayerUtility: PurgeVRAM`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `FrameInterpolationModelLoader`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LayerUtility: PurgeVRAM`
- `LTXVAudioVAEDecode` ★核心
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `44`
- `batch_size` = `1`

## 知识

覆盖率 **61%**（62/101）

**有卡**：`LTXVEmptyLatentAudio`、`CFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTX2_NAG`、`LTXVConditioning`、`ManualSigmas`、`ComfyMathExpression`、`CLIPTextEncode`、`RandomNoise`、`LayerUtility: PurgeVRAM`、`SamplerCustomAdvanced`、`PathchSageAttentionKJ`、`ResizeImagesByLongerEdge`、`EmptyLTXVLatentVideo`、`LoadImage`、`LiconMSR`、`LTXAddVideoICLoRAGuide`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXICLoRALoaderModelOnly`、`LTXVAddGuideMulti`、`RTXVideoSuperResolution`、`FrameInterpolate`、`LoraLoaderModelOnly`、`FrameInterpolationModelLoader`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
