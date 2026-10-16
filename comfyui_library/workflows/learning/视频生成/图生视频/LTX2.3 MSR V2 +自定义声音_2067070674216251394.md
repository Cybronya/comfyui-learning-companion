---
key: 视频生成/图生视频/LTX2.3 MSR V2 +自定义声音_2067070674216251394.json
name: LTX2.3 MSR V2 +自定义声音_2067070674216251394.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2067070674216251394.json
hash: 3b2f3a9e9f0f3058
coverage: 0.679012
learned_at: 2026-10-15 22:39:56
nodes: [KSamplerSelect, PrimitiveInt, ResizeImagesByLongerEdge, SetNode, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, Label (rgthree), LoadImage, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SetNode, ResizeImagesByLongerEdge, LTX2_NAG, GetNode, GetNode, CLIPTextEncode, LTXVConcatAVLatent, GetNode, ManualSigmas, LoadImage, LTXVSeparateAVLatent, Reroute, LayerUtility: PurgeVRAM, ComfyMathExpression, VAEDecodeTiled, ComfyMathExpression, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, GetNode, ResizeImagesByLongerEdge, SetNode, PrimitiveInt, PrimitiveInt, PrimitiveInt, SetNode, SetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, GetNode, GetNode, LiconMSR, GetNode, SetNode, PathchSageAttentionKJ, LTXAddVideoICLoRAGuide, SamplerCustomAdvanced, RandomNoise, CFGGuider, LTXVConditioning, VHS_VideoCombine, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVCropGuides, PrimitiveStringMultiline, TrimAudioDuration, SetLatentNoiseMask, LTXVAudioVAEEncode, SolidMask, PreviewAudio, MelBandRoFormerSampler, TrimAudioDuration, CLIPTextEncode, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, LoadImage, LoadImage, LoadImage, LTXVAddGuideMulti, MelBandRoFormerModelLoader, LoadAudio, ComfyMathExpression, UNETLoader, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3 MSR V2 +自定义声音_2067070674216251394.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067070674216251394.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（81 个）：
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
- `ComfyMathExpression`
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
- `TrimAudioDuration`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `PreviewAudio`
- `MelBandRoFormerSampler` ★核心
- `TrimAudioDuration`
- `CLIPTextEncode` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LTXVAddGuideMulti`
- `MelBandRoFormerModelLoader`
- `LoadAudio`
- `ComfyMathExpression`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心

## 知识

覆盖率 **68%**（55/81）

**有卡**：`KSamplerSelect`、`ResizeImagesByLongerEdge`、`Label (rgthree)`、`LoadImage`、`LTX2_NAG`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LayerUtility: PurgeVRAM`、`ComfyMathExpression`、`VAEDecodeTiled`、`LiconMSR`、`PathchSageAttentionKJ`、`LTXAddVideoICLoRAGuide`、`SamplerCustomAdvanced`、`RandomNoise`、`CFGGuider`、`LTXVConditioning`、`VHS_VideoCombine`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`TrimAudioDuration`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`PreviewAudio`、`MelBandRoFormerSampler`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXVAddGuideMulti`、`MelBandRoFormerModelLoader`、`LoadAudio`、`UNETLoader`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
