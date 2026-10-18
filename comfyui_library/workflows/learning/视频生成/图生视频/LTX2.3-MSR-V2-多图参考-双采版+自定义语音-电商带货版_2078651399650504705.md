---
key: 视频生成/图生视频/LTX2.3-MSR-V2-多图参考-双采版+自定义语音-电商带货版_2078651399650504705.json
name: LTX2.3-MSR-V2-多图参考-双采版+自定义语音-电商带货版_2078651399650504705.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-MSR-V2-多图参考-双采版+自定义语音-电商带货版_2078651399650504705.json
hash: 9a1392952a4e42e1
coverage: 0.648148
learned_at: 2026-10-15 22:41:54
nodes: [KSamplerSelect, ResizeImagesByLongerEdge, SetNode, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, LoadImage, SetNode, ResizeImagesByLongerEdge, LTX2_NAG, GetNode, GetNode, CLIPTextEncode, LTXVConcatAVLatent, GetNode, ManualSigmas, LoadImage, LTXVSeparateAVLatent, Reroute, LayerUtility: PurgeVRAM, ComfyMathExpression, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, PrimitiveInt, PrimitiveInt, PrimitiveInt, SetNode, SetNode, PrimitiveStringMultiline, GetNode, GetNode, LiconMSR, GetNode, SetNode, PathchSageAttentionKJ, LTXAddVideoICLoRAGuide, SamplerCustomAdvanced, RandomNoise, CFGGuider, LTXVConditioning, EmptyLTXVLatentVideo, LTXVCropGuides, SetLatentNoiseMask, LTXVAudioVAEEncode, SolidMask, CLIPTextEncode, CFGGuider, RandomNoise, LTXVLatentUpsampler, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LTXICLoRALoaderModelOnly, TrimAudioDuration, UNETLoader, LatentUpscaleModelLoader, LTXVAddGuideMulti, LTXVAddGuideMulti, LTXVAudioVAEDecode, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, LoraLoaderModelOnly, ComfyMathExpression, TrimAudioDuration, PreviewAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecodeTiled, VHS_VideoCombine, VHS_VideoCombine, ComfyMathExpression, LayerUtility: PurgeVRAM, RTXVideoSuperResolution, LoraLoaderModelOnly, MarkdownNote, LoadImage, LoadImage, ResizeImagesByLongerEdge, LoadAudio, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, FrameInterpolationModelLoader, FrameInterpolate, LoadImage, PrimitiveInt]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3-MSR-V2-多图参考-双采版+自定义语音-电商带货版_2078651399650504705.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2078651399650504705.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（108 个）：
- `KSamplerSelect` ★核心
- `ResizeImagesByLongerEdge`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `LoadImage`
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
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
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
- `EmptyLTXVLatentVideo`
- `LTXVCropGuides`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `RandomNoise`
- `LTXVLatentUpsampler` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `TrimAudioDuration`
- `UNETLoader` ★核心
- `LatentUpscaleModelLoader`
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode` ★核心
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `LoraLoaderModelOnly` ★核心
- `ComfyMathExpression`
- `TrimAudioDuration`
- `PreviewAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ComfyMathExpression`
- `LayerUtility: PurgeVRAM`
- `RTXVideoSuperResolution`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `ResizeImagesByLongerEdge`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `FrameInterpolationModelLoader`
- `FrameInterpolate`
- `LoadImage`
- `PrimitiveInt`

## 知识

覆盖率 **65%**（70/108）

**有卡**：`KSamplerSelect`、`ResizeImagesByLongerEdge`、`LoadImage`、`LTX2_NAG`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LayerUtility: PurgeVRAM`、`ComfyMathExpression`、`LiconMSR`、`PathchSageAttentionKJ`、`LTXAddVideoICLoRAGuide`、`SamplerCustomAdvanced`、`RandomNoise`、`CFGGuider`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVCropGuides`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`LTXVLatentUpsampler`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXICLoRALoaderModelOnly`、`TrimAudioDuration`、`UNETLoader`、`LatentUpscaleModelLoader`、`LTXVAddGuideMulti`、`LTXVAudioVAEDecode`、`LoraLoaderModelOnly`、`PreviewAudio`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`VAEDecodeTiled`、`VHS_VideoCombine`、`RTXVideoSuperResolution`、`LoadAudio`、`FrameInterpolationModelLoader`、`FrameInterpolate`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
