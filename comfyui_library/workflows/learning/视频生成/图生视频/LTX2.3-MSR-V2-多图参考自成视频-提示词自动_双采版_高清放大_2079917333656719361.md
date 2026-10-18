---
key: 视频生成/图生视频/LTX2.3-MSR-V2-多图参考自成视频-提示词自动_双采版_高清放大_2079917333656719361.json
name: LTX2.3-MSR-V2-多图参考自成视频-提示词自动_双采版_高清放大_2079917333656719361.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-MSR-V2-多图参考自成视频-提示词自动_双采版_高清放大_2079917333656719361.json
hash: 96c6a18bcaf5f104
coverage: 0.631579
learned_at: 2026-10-15 22:42:07
nodes: [LTXVEmptyLatentAudio, Reroute, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, PrimitiveInt, PrimitiveInt, LTX2_NAG, LTXVConditioning, ManualSigmas, ComfyMathExpression, PrimitiveInt, ComfyMathExpression, CLIPTextEncode, ComfyMathExpression, RandomNoise, LayerUtility: PurgeVRAM, SamplerCustomAdvanced, PathchSageAttentionKJ, ResizeImagesByLongerEdge, EmptyLTXVLatentVideo, SetNode, GetNode, SetNode, SetNode, ResizeImagesByLongerEdge, SetNode, ResizeImagesByLongerEdge, LoadImage, SetNode, ResizeImagesByLongerEdge, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, LiconMSR, GetNode, LTXAddVideoICLoRAGuide, GetNode, CLIPTextEncode, RandomNoise, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, LatentUpscaleModelLoader, LTXVLatentUpsampler, ComfyMathExpression, ComfyMathExpression, LTXVCropGuides, SamplerCustomAdvanced, ManualSigmas, GetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, LTXICLoRALoaderModelOnly, LTXVAddGuideMulti, LTXVAddGuideMulti, ResizeImagesByLongerEdge, LoadImage, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVCropGuides, LayerUtility: PurgeVRAM, MarkdownNote, PrimitiveStringMultiline, LoraLoaderModelOnly, PrimitiveStringMultiline, LTXVAudioVAEDecode, ComfyMathExpression, RTXVideoSuperResolution, PrimitiveInt, VHS_VideoCombine, FrameInterpolationModelLoader, FrameInterpolate]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 44, "width": 97}
---

# 视频生成/图生视频/LTX2.3-MSR-V2-多图参考自成视频-提示词自动_双采版_高清放大_2079917333656719361.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2079917333656719361.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（95 个）：
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
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LayerUtility: PurgeVRAM`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `LTXVAudioVAEDecode` ★核心
- `ComfyMathExpression`
- `RTXVideoSuperResolution`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `FrameInterpolationModelLoader`
- `FrameInterpolate`

## 关键参数

- `width` = `97`
- `height` = `44`
- `batch_size` = `1`

## 知识

覆盖率 **63%**（60/95）

**有卡**：`LTXVEmptyLatentAudio`、`CFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTX2_NAG`、`LTXVConditioning`、`ManualSigmas`、`ComfyMathExpression`、`CLIPTextEncode`、`RandomNoise`、`LayerUtility: PurgeVRAM`、`SamplerCustomAdvanced`、`PathchSageAttentionKJ`、`ResizeImagesByLongerEdge`、`EmptyLTXVLatentVideo`、`LoadImage`、`LiconMSR`、`LTXAddVideoICLoRAGuide`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXICLoRALoaderModelOnly`、`LTXVAddGuideMulti`、`LoraLoaderModelOnly`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`RTXVideoSuperResolution`、`VHS_VideoCombine`、`FrameInterpolationModelLoader`、`FrameInterpolate`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
