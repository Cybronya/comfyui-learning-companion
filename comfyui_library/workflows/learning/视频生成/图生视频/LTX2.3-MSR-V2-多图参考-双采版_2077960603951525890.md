---
key: 视频生成/图生视频/LTX2.3-MSR-V2-多图参考-双采版_2077960603951525890.json
name: LTX2.3-MSR-V2-多图参考-双采版_2077960603951525890.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2077960603951525890.json
hash: 7f3214292222eafe
coverage: 0.659794
learned_at: 2026-10-15 22:41:46
nodes: [LTXVEmptyLatentAudio, Reroute, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, PrimitiveInt, PrimitiveInt, LTX2_NAG, LTXVConditioning, ManualSigmas, ComfyMathExpression, PrimitiveInt, ComfyMathExpression, CLIPTextEncode, ComfyMathExpression, RandomNoise, LayerUtility: PurgeVRAM, SamplerCustomAdvanced, PathchSageAttentionKJ, ResizeImagesByLongerEdge, EmptyLTXVLatentVideo, SetNode, GetNode, SetNode, SetNode, ResizeImagesByLongerEdge, SetNode, ResizeImagesByLongerEdge, LoadImage, SetNode, ResizeImagesByLongerEdge, GetNode, GetNode, GetNode, GetNode, Label (rgthree), Label (rgthree), Label (rgthree), GetNode, GetNode, GetNode, SetNode, GetNode, LiconMSR, GetNode, LTXAddVideoICLoRAGuide, GetNode, CLIPTextEncode, RandomNoise, CFGGuider, LTXVSeparateAVLatent, KSamplerSelect, LTXVConcatAVLatent, LatentUpscaleModelLoader, LTXVLatentUpsampler, ComfyMathExpression, ComfyMathExpression, LTXVCropGuides, SamplerCustomAdvanced, ManualSigmas, GetNode, GetNode, GetNode, GetNode, GetNode, LoraLoaderModelOnly, UNETLoader, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, LTXICLoRALoaderModelOnly, LTXVAddGuideMulti, LTXVAddGuideMulti, ResizeImagesByLongerEdge, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveInt, MarkdownNote, VHS_VideoCombine, VHS_VideoCombine, PrimitiveStringMultiline, 孤海注释, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, RTXVideoSuperResolution, FrameInterpolationModelLoader, ComfyMathExpression, LTXVAudioVAEDecode, VAEDecodeTiled, FrameInterpolate, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LTXVCropGuides]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 44, "width": 97}
---

# 视频生成/图生视频/LTX2.3-MSR-V2-多图参考-双采版_2077960603951525890.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2077960603951525890.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（97 个）：
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
- `RandomNoise`
- `CFGGuider`
- `LTXVSeparateAVLatent`
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
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `MarkdownNote`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `孤海注释`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `RTXVideoSuperResolution`
- `FrameInterpolationModelLoader`
- `ComfyMathExpression`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `FrameInterpolate`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LTXVCropGuides`

## 关键参数

- `width` = `97`
- `height` = `44`
- `batch_size` = `1`

## 知识

覆盖率 **66%**（64/97）

**有卡**：`LTXVEmptyLatentAudio`、`CFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTX2_NAG`、`LTXVConditioning`、`ManualSigmas`、`ComfyMathExpression`、`CLIPTextEncode`、`RandomNoise`、`LayerUtility: PurgeVRAM`、`SamplerCustomAdvanced`、`PathchSageAttentionKJ`、`ResizeImagesByLongerEdge`、`EmptyLTXVLatentVideo`、`LoadImage`、`Label (rgthree)`、`LiconMSR`、`LTXAddVideoICLoRAGuide`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXICLoRALoaderModelOnly`、`LTXVAddGuideMulti`、`VHS_VideoCombine`、`RTXVideoSuperResolution`、`FrameInterpolationModelLoader`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`FrameInterpolate`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
