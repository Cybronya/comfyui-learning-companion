---
key: 视频生成/图生视频/LTX2.3-MSR-V2-多图参考-双采版-自动提示词 V2 版_2081280741002006529.json
name: LTX2.3-MSR-V2-多图参考-双采版-自动提示词 V2 版_2081280741002006529.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2081280741002006529.json
hash: 2fe3348890a5c980
coverage: 0.693878
learned_at: 2026-10-15 22:42:21
nodes: [LTXVEmptyLatentAudio, Reroute, CFGGuider, KSamplerSelect, ManualSigmas, ComfyMathExpression, ComfyMathExpression, RandomNoise, SamplerCustomAdvanced, EmptyLTXVLatentVideo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, RandomNoise, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, LatentUpscaleModelLoader, LTXVLatentUpsampler, ManualSigmas, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVAddGuideMulti, 孤海注释, RTXVideoSuperResolution, FrameInterpolate, LayerUtility: PurgeVRAM, LTXVSeparateAVLatent, LoadImage, MarkdownNote, SetNode, ResizeImagesByLongerEdge, LoadImage, SetNode, ResizeImagesByLongerEdge, LoadImage, SetNode, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, SetNode, SetNode, ResizeImagesByLongerEdge, LTX2_NAG, PathchSageAttentionKJ, LTXAddVideoICLoRAGuide, GetNode, LTXVConditioning, CLIPTextEncode, CLIPTextEncode, ComfyMathExpression, ComfyMathExpression, VAELoaderKJ, VAELoaderKJ, UNETLoader, Int, Int, Int, LTXVConcatAVLatent, LayerUtility: PurgeVRAM, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecodeTiled, ComfyMathExpression, LTXVAudioVAEDecode, LTXVCropGuides, LayerUtility: PurgeVRAM, LiconMSR, LTXVAddGuideMulti, ComfyMathExpression, FrameInterpolationModelLoader, LoraLoaderModelOnly, VHS_VideoCombine, LoadImage, LoadImage, LTXICLoRALoaderModelOnly, LTXICLoRALoaderModelOnly, MarkdownNote, DualCLIPLoader, DualCLIPLoader, LTXICLoRALoaderModelOnly, SamplerCustomAdvanced, VHS_VideoCombine, PrimitiveStringMultiline, Int, PrimitiveStringMultiline, MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 44, "width": 97}
---

# 视频生成/图生视频/LTX2.3-MSR-V2-多图参考-双采版-自动提示词 V2 版_2081280741002006529.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2081280741002006529.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（98 个）：
- `LTXVEmptyLatentAudio` ★核心
- `Reroute`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAddGuideMulti`
- `孤海注释`
- `RTXVideoSuperResolution`
- `FrameInterpolate`
- `LayerUtility: PurgeVRAM`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `MarkdownNote`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `LTX2_NAG`
- `PathchSageAttentionKJ`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `Int`
- `Int`
- `Int`
- `LTXVConcatAVLatent`
- `LayerUtility: PurgeVRAM`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `ComfyMathExpression`
- `LTXVAudioVAEDecode` ★核心
- `LTXVCropGuides`
- `LayerUtility: PurgeVRAM`
- `LiconMSR`
- `LTXVAddGuideMulti`
- `ComfyMathExpression`
- `FrameInterpolationModelLoader`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `MarkdownNote`
- `DualCLIPLoader`
- `DualCLIPLoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `Int`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `44`
- `batch_size` = `1`

## 知识

覆盖率 **69%**（68/98）

**有卡**：`LTXVEmptyLatentAudio`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`ComfyMathExpression`、`RandomNoise`、`SamplerCustomAdvanced`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVAddGuideMulti`、`RTXVideoSuperResolution`、`FrameInterpolate`、`LayerUtility: PurgeVRAM`、`LTXVSeparateAVLatent`、`LoadImage`、`ResizeImagesByLongerEdge`、`LTX2_NAG`、`PathchSageAttentionKJ`、`LTXAddVideoICLoRAGuide`、`LTXVConditioning`、`CLIPTextEncode`、`VAELoaderKJ`、`UNETLoader`、`Int`、`LTXVCropGuides`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LiconMSR`、`FrameInterpolationModelLoader`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`LTXICLoRALoaderModelOnly`、`DualCLIPLoader`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
